#!/usr/bin/env python3
"""
scripts/compile_manuscript_docx.py

Compile manuscript/manuscript.md to manuscript/Targeting_GRP78_PSTi8_Manuscript.docx
using python-docx (pandoc is not installed on this host).

Handles: title, headings (##/###), bold/italic/code/links inline, numbered and
bulleted lists, Markdown tables (converted to real Word tables with grid
borders), fenced code blocks (preserved as monospace text, e.g. the ASCII
interface-collapse table in Section 3.7), and horizontal rules.

Known limitation: LaTeX $...$ math is kept as literal text (Word has no
Markdown math import); it renders readably but is not typeset as equations.
"""

import os
import re
import sys

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MD_PATH = os.path.join(REPO_ROOT, "manuscript", "manuscript.md")
DOCX_PATH = os.path.join(REPO_ROOT, "manuscript", "Targeting_GRP78_PSTi8_Manuscript.docx")

try:
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement
except ImportError:
    sys.exit("python-docx is required (pip install python-docx)")

# Inline token regex: code spans first, then links, bold, italic.
INLINE_RE = re.compile(
    r"(?P<code>`[^`]+`)"
    r"|(?P<link>\[[^\]]+\]\([^)]+\))"
    r"|(?P<bold>\*\*[^*]+\*\*)"
    r"|(?P<italic>(?<![\w*])\*[^*\s][^*]*\*)"
    r"|(?P<text>[^`*\[\\]+)"
)


def add_inline(paragraph, text):
    """Add runs for a Markdown-inline string to a python-docx paragraph."""
    for m in INLINE_RE.finditer(text):
        kind = m.lastgroup
        raw = m.group(0)
        if kind == "code":
            run = paragraph.add_run(raw[1:-1])
            run.font.name = "Consolas"
            run.font.size = Pt(9)
        elif kind == "link":
            label = raw[1:raw.index("]")]
            run = paragraph.add_run(label)
        elif kind == "bold":
            run = paragraph.add_run(raw[2:-2])
            run.bold = True
        elif kind == "italic":
            run = paragraph.add_run(raw[1:-1])
            run.italic = True
        else:
            paragraph.add_run(raw)


def set_cell_border(cell, **kwargs):
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    tcBorders = tcPr.first_child_found_in("w:tcBorders")
    if tcBorders is None:
        tcBorders = OxmlElement("w:tcBorders")
        tcPr.append(tcBorders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        tag = f"w:{edge}"
        element = tcBorders.find(qn(tag))
        if element is None:
            element = OxmlElement(tag)
            tcBorders.append(element)
        for key, val in kwargs.items():
            element.set(qn(key), val)


def add_table(doc, rows):
    """rows: list of cell-text lists; first row is the header."""
    table = doc.add_table(rows=0, cols=len(rows[0]))
    table.style = "Table Grid"
    for i, row in enumerate(rows):
        cells = table.add_row().cells
        for j, text in enumerate(row):
            cells[j].text = ""
            para = cells[j].paragraphs[0]
            add_inline(para, text.strip())
            for run in para.runs:
                run.font.size = Pt(9)
                if i == 0:
                    run.bold = True
    return table


def parse_table_block(lines):
    """Parse consecutive '| ... |' lines into rows, skipping the separator."""
    rows = []
    for line in lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if all(re.match(r"^:?-{3,}:?$", c) for c in cells):
            continue
        rows.append(cells)
    return rows


def main():
    with open(MD_PATH, encoding="utf-8") as f:
        lines = f.read().splitlines()

    doc = Document()
    style = doc.styles["Normal"]
    style.font.name = "Calibri"
    style.font.size = Pt(11)

    stats = {"headings": 0, "tables": 0, "code_blocks": 0, "paragraphs": 0}
    i = 0
    in_code = False
    code_lines = []

    def flush_code():
        nonlocal code_lines
        if not code_lines:
            return
        for cl in code_lines:
            p = doc.add_paragraph()
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            run = p.add_run(cl if cl else " ")
            run.font.name = "Consolas"
            run.font.size = Pt(8)
        stats["code_blocks"] += 1
        code_lines = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith("```"):
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            i += 1
            continue
        if in_code:
            code_lines.append(line)
            i += 1
            continue

        if not stripped:
            i += 1
            continue
        if stripped == "---":
            i += 1
            continue

        # Markdown table block
        if stripped.startswith("|"):
            block = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                block.append(lines[i])
                i += 1
            rows = parse_table_block(block)
            if len(rows) >= 2:
                add_table(doc, rows)
                stats["tables"] += 1
            continue

        # Headings
        m = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if m:
            level = len(m.group(1))
            text = m.group(2)
            if level == 1:
                p = doc.add_paragraph()
                p.style = doc.styles["Title"]
                add_inline(p, text)
            else:
                p = doc.add_heading(level=level - 1)
                add_inline(p, text)
            stats["headings"] += 1
            i += 1
            continue

        # Lists (numbered or bulleted), one line per item
        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Number")
            add_inline(p, m.group(3))
            stats["paragraphs"] += 1
            i += 1
            continue
        m = re.match(r"^(\s*)[-*]\s+(.*)$", line)
        if m:
            p = doc.add_paragraph(style="List Bullet")
            add_inline(p, m.group(2))
            stats["paragraphs"] += 1
            i += 1
            continue

        # Plain paragraph (strip a leading blockquote marker if present)
        text = re.sub(r"^>\s?", "", stripped)
        p = doc.add_paragraph()
        add_inline(p, text)
        stats["paragraphs"] += 1
        i += 1

    flush_code()
    doc.save(DOCX_PATH)
    print(f"Saved {DOCX_PATH}")
    print(f"Stats: {stats}")
    print(f"Size: {os.path.getsize(DOCX_PATH)} bytes")


if __name__ == "__main__":
    main()
