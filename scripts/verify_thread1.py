#!/usr/bin/env python3
"""
scripts/verify_thread1.py

Systematic verification script for Thread 1 candidate literature against PubMed and Crossref APIs.
Extracts 34 rows from data/staging/thread1_argon_raw.md, audits bibliometrics, PMIDs,
resolves DOIs, extracts abstracts, and saves raw responses.
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
RAW_MD_PATH = os.path.join(REPO_ROOT, "data", "staging", "thread1_argon_raw.md")
RAW_JSON_PATH = os.path.join(REPO_ROOT, "data", "staging", "thread1_raw_api_responses.json")
OUT_CSV_PATH = os.path.join(REPO_ROOT, "data", "staging", "thread1_registry_unverified.csv")

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

    reader = csv.DictReader(csv_lines)
    return list(reader)

def fetch_crossref(doi):
    url = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        msg = data.get("message", {})
        title = msg.get("title", [""])[0] if msg.get("title") else ""
        authors = msg.get("author", [])
        first_author = ""
        if authors:
            fa = authors[0]
            first_author = f"{fa.get('family', '')} {fa.get('given', '')}".strip()
        journal = msg.get("container-title", [""])[0] if msg.get("container-title") else ""
        pub_year = ""
        if "published-print" in msg:
            dp = msg["published-print"].get("date-parts", [[]])[0]
            if dp: pub_year = str(dp[0])
        elif "published-online" in msg:
            dp = msg["published-online"].get("date-parts", [[]])[0]
            if dp: pub_year = str(dp[0])
        elif "created" in msg:
            dp = msg["created"].get("date-parts", [[]])[0]
            if dp: pub_year = str(dp[0])

        return {
            "source": "crossref",
            "title": title,
            "first_author": first_author,
            "authors": [f"{a.get('family', '')} {a.get('given', '')}".strip() for a in authors],
            "journal": journal,
            "year": pub_year,
            "type": msg.get("type", ""),
            "publisher": msg.get("publisher", ""),
            "abstract": msg.get("abstract", "")
        }
    except Exception as e:
        return {"error": str(e)}

def fetch_pubmed(doi=None, pmid=None):
    try:
        if not pmid and doi:
            search_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(doi)}[doi]&retmode=json"
            req_s = urllib.request.Request(search_url, headers=HEADERS)
            with urllib.request.urlopen(req_s, timeout=15) as resp:
                sdata = json.loads(resp.read().decode())
            idlist = sdata.get("esearchresult", {}).get("idlist", [])
            if idlist:
                pmid = idlist[0]

        if not pmid:
            return None

        sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
        req_sum = urllib.request.Request(sum_url, headers=HEADERS)
        with urllib.request.urlopen(req_sum, timeout=15) as r2:
            sdata = json.loads(r2.read().decode())
        summary = sdata.get("result", {}).get(str(pmid), {})

        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
        req_fetch = urllib.request.Request(fetch_url, headers=HEADERS)
        with urllib.request.urlopen(req_fetch, timeout=15) as r3:
            xml_str = r3.read().decode()

        root = ET.fromstring(xml_str)
        abstract_nodes = root.findall(".//AbstractText")
        abstract = " ".join([node.text for node in abstract_nodes if node.text])
        mesh_nodes = root.findall(".//MeshHeading/DescriptorName")
        mesh = [node.text for node in mesh_nodes if node.text]
        pmc_id = ""
        for aid in summary.get("articleids", []):
            if aid.get("idtype") == "pmc":
                pmc_id = aid.get("value")

        return {
            "source": "pubmed",
            "pmid": str(pmid),
            "pmcid": pmc_id,
            "title": summary.get("title", "").strip(),
            "first_author": summary.get("sortfirstauthor", ""),
            "authors": [a.get("name") for a in summary.get("authors", [])],
            "journal": summary.get("source", ""),
            "pubdate": summary.get("pubdate", ""),
            "abstract": abstract,
            "mesh": mesh
        }
    except Exception as e:
        return {"error": str(e)}

def main():
    rows = extract_raw_csv_rows()
    print(f"Extracted {len(rows)} rows from {RAW_MD_PATH}")

    raw_store = {}
    if os.path.exists(RAW_JSON_PATH):
        try:
            with open(RAW_JSON_PATH, "r", encoding="utf-8") as f:
                raw_store = json.load(f)
        except Exception:
            raw_store = {}

    for i, r in enumerate(rows):
        rid = r["id"]
        doi = r["doi"].strip()
        source_url = r["source_url"].strip()

        print(f"\n[{i+1}/{len(rows)}] Auditing {rid} (DOI: {doi})...")

        # extract PMID from source_url if present
        pmid_match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", source_url)
        url_pmid = pmid_match.group(1) if pmid_match else None

        # Fetch Crossref
        cr_data = fetch_crossref(doi)
        time.sleep(0.3)

        # Fetch PubMed by DOI
        pm_data_by_doi = fetch_pubmed(doi=doi)
        time.sleep(0.3)

        # Fetch PubMed by URL PMID if different
        pm_data_by_pmid = None
        if url_pmid and (not pm_data_by_doi or pm_data_by_doi.get("pmid") != url_pmid):
            pm_data_by_pmid = fetch_pubmed(pmid=url_pmid)
            time.sleep(0.3)

        raw_store[rid] = {
            "row": r,
            "crossref": cr_data,
            "pubmed_by_doi": pm_data_by_doi,
            "pubmed_by_url_pmid": pm_data_by_pmid
        }

        # Print quick diagnostic
        cr_ok = "error" not in cr_data and bool(cr_data.get("title"))
        pm_ok = pm_data_by_doi is not None and "error" not in pm_data_by_doi
        print(f"   Crossref: {'OK' if cr_ok else 'FAIL/ERR'}, PubMed (by DOI): {'PMID:'+str(pm_data_by_doi.get('pmid')) if pm_ok else 'None'}")
        if url_pmid:
            match_status = "MATCH" if (pm_ok and str(pm_data_by_doi.get('pmid')) == url_pmid) else f"MISMATCH (url={url_pmid}, doi_pmid={pm_data_by_doi.get('pmid') if pm_ok else 'None'})"
            print(f"   PMID check: {match_status}")

    with open(RAW_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(raw_store, f, indent=2)
    print(f"\nSaved raw responses to {RAW_JSON_PATH}")

if __name__ == "__main__":
    main()
