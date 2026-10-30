#!/usr/bin/env python3
"""
Verify batch of rows from data/staging/thread3_registry_unverified.csv
"""

import sys
import os
import csv
import json
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

CSV_PATH = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/thread3_registry_unverified.csv"
HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

def query_pubmed_by_doi(doi):
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
        
        return {
            "source": "pubmed",
            "pmid": pmid,
            "title": summary.get("title", "").strip(),
            "first_author": summary.get("sortfirstauthor", ""),
            "authors": [a.get("name") for a in summary.get("authors", [])],
            "journal": summary.get("source", ""),
            "pubdate": summary.get("pubdate", ""),
            "abstract": abstract,
            "mesh": mesh,
            "raw_xml": xml_str
        }
    except Exception as e:
        return {"error": str(e)}

def query_crossref_by_doi(doi):
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
            
        abstract = msg.get("abstract", "")
        return {
            "source": "crossref",
            "title": title,
            "first_author": first_author,
            "authors": [f"{a.get('family', '')} {a.get('given', '')}".strip() for a in authors],
            "journal": journal,
            "year": pub_year,
            "abstract": abstract
        }
    except Exception as e:
        return {"error": str(e)}

def verify_doi(doi):
    res = query_pubmed_by_doi(doi)
    if res and "error" not in res:
        return res
    res2 = query_crossref_by_doi(doi)
    if res2 and "error" not in res2:
        return res2
    return {"error": f"PubMed error: {res.get('error') if res else 'not found'}; Crossref error: {res2.get('error') if res2 else 'not found'}"}

def process_batch(start_idx, end_idx):
    with open(CSV_PATH, "r") as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()
        
    if "verification_note" not in fieldnames:
        fieldnames = list(fieldnames) + ["verification_note"]
    else:
        fieldnames = list(fieldnames)

    print(f"Processing rows {start_idx} to {end_idx} (1-based)...")
    for i in range(start_idx - 1, end_idx):
        row = reader[i]
        doi = row["doi"].strip()
        print(f"\n--- Row {i+1}: {row['id']} (DOI: {doi}) ---")
        info = verify_doi(doi)
        
        if "error" in info:
            print(f"COULD NOT OPEN: {info['error']}")
            row["verified"] = "no"
            row["verification_note"] = f"could_not_open: {info['error']}"
            continue
            
        source = info.get("source")
        title = info.get("title", "")
        first_author = info.get("first_author", "")
        authors = info.get("authors", [])
        journal = info.get("journal", "")
        pubdate = info.get("pubdate", "") or info.get("year", "")
        abstract = info.get("abstract", "")
        
        print(f"Source: {source}")
        print(f"Title: {title}")
        print(f"First author: {first_author}")
        print(f"Journal: {journal}")
        print(f"Pubdate/Year: {pubdate}")
        
        # Check PSTi8 presence
        title_lower = title.lower()
        abs_lower = abstract.lower()
        has_psti8 = ("psti8" in title_lower or "psti8" in abs_lower or 
                     "pancreastatin inhibitor" in title_lower or "pancreastatin inhibitor" in abs_lower or
                     "pegkgeqehsqqkeeeeemav" in abs_lower)
        
        print(f"Mentions PSTi8 / pancreastatin inhibitor: {has_psti8}")
        
        # Save raw info for documentation
        row["_verified_info"] = info

    return reader, fieldnames

if __name__ == "__main__":
    b = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if b == 1:
        process_batch(1, 9)
    elif b == 2:
        process_batch(10, 18)
    elif b == 3:
        process_batch(19, 26)
