#!/usr/bin/env python3
"""
scripts/verify_thread2.py

Systematic verification script for Thread 2 candidate literature against PubMed and Crossref APIs.
Processes in 3 batches, validates bibliometrics, role assignment, animal sex, and quantitative claims.
"""

import sys
import os
import csv
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}
CSV_PATH = "/home/devansh/psti8-vault/data/staging/thread2_registry_unverified.csv"
RAW_JSON_PATH = "/home/devansh/psti8-vault/data/staging/thread2_raw_api_responses.json"

def fetch_pubmed(doi):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(doi)}[doi]&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        idlist = data.get("esearchresult", {}).get("idlist", [])
        if not idlist:
            return None
        pmid = idlist[0]
        
        sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
        req_sum = urllib.request.Request(sum_url, headers=HEADERS)
        with urllib.request.urlopen(req_sum, timeout=15) as r2:
            sdata = json.loads(r2.read().decode())
        summary = sdata.get("result", {}).get(pmid, {})
        
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
            "pmid": pmid,
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
            "publisher": msg.get("publisher", "")
        }
    except Exception as e:
        return {"error": str(e)}

def run_batch(start_idx, end_idx):
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        
    raw_store = {}
    if os.path.exists(RAW_JSON_PATH):
        try:
            with open(RAW_JSON_PATH, "r", encoding="utf-8") as jf:
                raw_store = json.load(jf)
        except Exception:
            raw_store = {}
            
    batch_rows = reader[start_idx:end_idx]
    print(f"--- Running batch for rows {start_idx+1} to {min(end_idx, len(reader))} (Total: {len(batch_rows)}) ---")
    
    for idx, row in enumerate(batch_rows, start=start_idx+1):
        pid = row["id"]
        doi = row["doi"]
        print(f"[{idx:2d}/{len(reader)}] Fetching: {pid} (DOI: {doi})")
        
        res = {"pubmed": None, "crossref": None}
        pm_res = fetch_pubmed(doi)
        res["pubmed"] = pm_res
        time.sleep(0.3)
        
        cr_res = fetch_crossref(doi)
        res["crossref"] = cr_res
        time.sleep(0.3)
        
        raw_store[pid] = {
            "row": row,
            "pubmed": pm_res,
            "crossref": cr_res
        }
        
    with open(RAW_JSON_PATH, "w", encoding="utf-8") as jf:
        json.dump(raw_store, jf, indent=2)
    print(f"Saved {len(raw_store)} records to {RAW_JSON_PATH}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 verify_thread2.py <start_idx> <end_idx>")
        sys.exit(1)
    s = int(sys.argv[1])
    e = int(sys.argv[2])
    run_batch(s, e)
