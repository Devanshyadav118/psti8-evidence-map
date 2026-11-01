#!/usr/bin/env python3
"""
scripts/test_all_dois.py
Test all 27 DOIs from Argon's Thread 6 staging table for resolution.
"""

import urllib.request
import urllib.parse
import json
import csv

CSV_PATH = "data/staging/thread6_argon_raw.md"
with open(CSV_PATH, "r", encoding="utf-8") as f:
    text = f.read()

lines = text.split("\n")
csv_lines = []
in_csv = False
for l in lines:
    if l.strip() == "```csv":
        in_csv = True
        continue
    if in_csv:
        if l.strip() == "```":
            break
        csv_lines.append(l)

rows = list(csv.DictReader(csv_lines))

print(f"Testing {len(rows)} DOIs directly via https://doi.org/...")

for i, r in enumerate(rows):
    rid = r["id"]
    doi = r["doi"].strip()
    url = f"https://doi.org/{doi}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    status = ""
    resolved_url = ""
    title = ""
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            status = "RESOLVED"
            title = data.get("title", "")
            resolved_url = resp.geturl()
    except urllib.error.HTTPError as e:
        status = f"HTTP {e.code}"
    except Exception as e:
        status = f"ERR: {e}"
        
    print(f"[{i+1}/{len(rows)}] {rid:25} | DOI: {doi:35} | {status} | Title: {title[:50]}")
