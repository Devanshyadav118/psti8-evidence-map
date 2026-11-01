#!/usr/bin/env python3
"""
scripts/resolve_all_thread6.py

Systematic investigation of all 27 Thread 6 papers.
Queries PubMed by DOI, by title/author, and by topic keywords to resolve
exact metadata, real DOIs, real PMIDs, abstracts, and preprint publication status.
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

def esearch(term):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            data = json.loads(r.read().decode())
        return data.get("esearchresult", {}).get("idlist", [])
    except Exception as e:
        return []

def get_pubmed_details(pmid):
    if not pmid:
        return None
    sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
    req_sum = urllib.request.Request(sum_url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req_sum, timeout=15) as r:
            sdata = json.loads(r.read().decode())
        summary = sdata.get("result", {}).get(str(pmid), {})
        
        doi = ""
        for aid in summary.get("articleids", []):
            if aid.get("idtype") == "doi":
                doi = aid.get("value")
                
        fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
        req_fetch = urllib.request.Request(fetch_url, headers=HEADERS)
        with urllib.request.urlopen(req_fetch, timeout=15) as r2:
            xml_str = r2.read().decode()
            
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
            "pmid": str(pmid),
            "doi": doi,
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

def search_crossref_works(query):
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&rows=3"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        items = data.get("message", {}).get("items", [])
        res = []
        for it in items:
            t = it.get("title", [""])[0] if it.get("title") else ""
            d = it.get("DOI", "")
            j = it.get("container-title", [""])[0] if it.get("container-title") else ""
            fa = ""
            if it.get("author"):
                fa = f"{it['author'][0].get('family', '')} {it['author'][0].get('given', '')}".strip()
            y = ""
            if "published-print" in it:
                dp = it["published-print"].get("date-parts", [[]])[0]
                if dp: y = str(dp[0])
            elif "published-online" in it:
                dp = it["published-online"].get("date-parts", [[]])[0]
                if dp: y = str(dp[0])
            res.append({"doi": d, "title": t, "first_author": fa, "journal": j, "year": y})
        return res
    except Exception as e:
        return []

def main():
    rows = extract_raw_csv_rows()
    print(f"Total rows to resolve: {len(rows)}")

    resolutions = {}

    for i, r in enumerate(rows):
        rid = r["id"]
        doi = r["doi"].strip()
        cit = r["citation"].strip()
        one_liner = r["one_line_relevance"].strip()
        s_url = r["source_url"].strip()

        print(f"\n[{i+1}/{len(rows)}] Resolving {rid}...")
        
        # 1. Search by DOI in PubMed
        pmids = esearch(f"{doi}[doi]")
        time.sleep(0.2)
        pm_data = None
        if pmids:
            pm_data = get_pubmed_details(pmids[0])
            time.sleep(0.2)

        # 2. If DOI didn't find in PubMed, search by citation/author/title
        if not pm_data or "error" in pm_data:
            # try author + keywords
            m_auth = re.match(r"^([A-Za-z\-]+)", cit)
            first_word_author = m_auth.group(1) if m_auth else ""
            # take first 4 words of one_liner
            words = [w for w in re.findall(r"[A-Za-z]{4,}", one_liner)][:4]
            search_query = f"{first_word_author}[author] AND {' '.join(words)}"
            pmids2 = esearch(search_query)
            time.sleep(0.2)
            if pmids2:
                pm_data = get_pubmed_details(pmids2[0])
                time.sleep(0.2)

        # 3. If still nothing or title mismatch, query Crossref
        cr_hits = search_crossref_works(f"{cit} {one_liner[:60]}")
        time.sleep(0.2)

        resolutions[rid] = {
            "row": r,
            "pubmed_match": pm_data,
            "crossref_hits": cr_hits
        }

        print(f"   Row citation: {cit}")
        print(f"   Row DOI:      {doi}")
        if pm_data and "error" not in pm_data:
            print(f"   PubMed match: PMID {pm_data['pmid']} | DOI: {pm_data['doi']} | {pm_data['first_author']} | {pm_data['title'][:60]}... ({pm_data['journal']})")
        else:
            print(f"   PubMed match: None")
        if cr_hits:
            print(f"   Crossref top hit: DOI {cr_hits[0]['doi']} | {cr_hits[0]['first_author']} | {cr_hits[0]['title'][:60]}... ({cr_hits[0]['journal']})")

    out_file = os.path.join(REPO_ROOT, "data", "staging", "thread6_deep_audit_temp.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(resolutions, f, indent=2)
    print(f"\nSaved all deep audit resolutions to {out_file}")

if __name__ == "__main__":
    main()
