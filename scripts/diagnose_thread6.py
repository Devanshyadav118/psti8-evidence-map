#!/usr/bin/env python3
"""
scripts/diagnose_thread6.py
Deep audit of the 27 Thread 6 rows to resolve genuine DOIs, PMIDs, titles, and authors.
"""

import sys
import os
import csv
import json
import time
import re
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
RAW_MD_PATH = os.path.join(REPO_ROOT, "data", "staging", "thread6_argon_raw.md")
HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

def extract_raw_csv_rows():
    with open(RAW_MD_PATH, "r", encoding="utf-8") as f:
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
    return list(csv.DictReader(csv_lines))

def fetch_pubmed_by_pmid(pmid):
    if not pmid:
        return None
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
        summary = data.get("result", {}).get(str(pmid), {})
        
        # also get doi
        doi = ""
        for aid in summary.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value")
                
        # fetch abstract
        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
        req_fetch = urllib.request.Request(fetch_url, headers=HEADERS)
        with urllib.request.urlopen(req_fetch, timeout=15) as r3:
            xml_str = r3.read().decode()
        root = ET.fromstring(xml_str)
        abstract_nodes = root.findall(".//AbstractText")
        abstract = " ".join([node.text for node in abstract_nodes if node.text])

        return {
            "pmid": str(pmid),
            "doi": doi,
            "title": summary.get("title", "").strip(),
            "first_author": summary.get("sortfirstauthor", ""),
            "authors": [a.get("name") for a in summary.get("authors", [])],
            "journal": summary.get("source", ""),
            "pubdate": summary.get("pubdate", ""),
            "abstract": abstract
        }
    except Exception as e:
        return {"error": str(e)}

def search_pubmed_by_title_author(title_words, author):
    term = f"{author}[author] AND {title_words}"
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        idlist = data.get("esearchresult", {}).get("idlist", [])
        return idlist
    except Exception as e:
        return []

def search_crossref_by_query(query):
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&rows=3"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        items = data.get("message", {}).get("items", [])
        results = []
        for it in items:
            title = it.get("title", [""])[0] if it.get("title") else ""
            doi = it.get("DOI", "")
            authors = it.get("author", [])
            fa = ""
            if authors:
                fa = f"{authors[0].get('family', '')} {authors[0].get('given', '')}".strip()
            journal = it.get("container-title", [""])[0] if it.get("container-title") else ""
            results.append({"doi": doi, "title": title, "first_author": fa, "journal": journal})
        return results
    except Exception as e:
        return []

def main():
    rows = extract_raw_csv_rows()
    print(f"Loaded {len(rows)} rows.")

    for i, r in enumerate(rows):
        rid = r["id"]
        doi = r["doi"].strip()
        citation = r["citation"].strip()
        source_url = r["source_url"].strip()
        one_liner = r["one_line_relevance"].strip()

        pmid_match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", source_url)
        url_pmid = pmid_match.group(1) if pmid_match else None

        print(f"\n==========================================")
        print(f"[{i+1}/{len(rows)}] ID: {rid}")
        print(f"  Row citation: {citation}")
        print(f"  Row DOI:      {doi}")
        print(f"  Row URL:      {source_url} (PMID: {url_pmid})")
        print(f"  One-liner:    {one_liner[:80]}...")

        # If URL has PMID, let's see what that PMID actually is!
        if url_pmid:
            pm_res = fetch_pubmed_by_pmid(url_pmid)
            time.sleep(0.3)
            if pm_res and "error" not in pm_res:
                print(f"  PubMed via URL PMID ({url_pmid}):")
                print(f"    Title:        {pm_res.get('title')}")
                print(f"    First Author: {pm_res.get('first_author')}")
                print(f"    Journal:      {pm_res.get('journal')}")
                print(f"    DOI from PM:  {pm_res.get('doi')}")
                if pm_res.get('doi') and pm_res.get('doi').lower() != doi.lower():
                    print(f"    *** DOI MISMATCH! Row DOI={doi} vs PubMed DOI={pm_res.get('doi')} ***")
            else:
                print(f"  PubMed via URL PMID failed: {pm_res}")

        # If DOI was invalid or failed, let's search Crossref by citation/keywords
        if not url_pmid or (pm_res and "error" in pm_res):
            print(f"  Searching Crossref for: {citation}")
            cr_search = search_crossref_by_query(citation)
            time.sleep(0.3)
            for it in cr_search[:2]:
                print(f"    CR Hit: DOI={it['doi']} | {it['first_author']} | {it['title']} ({it['journal']})")

if __name__ == "__main__":
    main()
