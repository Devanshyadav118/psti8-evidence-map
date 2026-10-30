#!/usr/bin/env python3
"""
Verification script for Thread 3 registry rows.
Queries PubMed (E-utilities) and Crossref APIs directly.
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
CSV_PATH = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/thread3_registry_unverified.csv"

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
            "articleids": summary.get("articleids", [])
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

def verify_single(doi):
    pb = query_pubmed_by_doi(doi)
    if pb and "error" not in pb:
        return pb
    cr = query_crossref_by_doi(doi)
    if cr and "error" not in cr:
        return cr
    return {"error": f"PubMed: {pb.get('error') if pb else 'not found'}; Crossref: {cr.get('error') if cr else 'not found'}"}

if __name__ == "__main__":
    test_doi = sys.argv[1] if len(sys.argv) > 1 else "10.1016/j.biopha.2019.108959"
    res = verify_single(test_doi)
    print(json.dumps(res, indent=2))
