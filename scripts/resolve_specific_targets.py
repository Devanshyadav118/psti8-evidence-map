#!/usr/bin/env python3
"""
scripts/resolve_specific_targets.py
Investigate remaining Thread 6 targets via PubMed, Europe PMC, and Crossref.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

queries = [
    ("beery2018", "Beery AK[Author] AND (behavioral OR neuroscience OR sex)"),
    ("booth2020", "Booth A[Author] AND (PROSPERO OR animal OR preclinical)"),
    ("vandervaart2020", "van der Vaart[Author] OR PreclinicalTrials.eu[Title/Abstract]"),
    ("richedwards2023", "Rich-Edwards[Author] OR (Maney DL[Author] AND sex)"),
    ("soliman2023", "Soliman[Author] AND systematic[Title]"),
    ("vandernaald2024", "van der Naald[Author]"),
    ("rich2024", "Rich[Author] AND Diabetes[Journal] AND sex"),
    ("gartlehner_check", "Gartlehner G[Author] AND (extraction OR \"language model\" OR \"artificial intelligence\")"),
    ("guo_check", "Guo[Author] AND (\"GPT-4\" OR \"language model\") AND (screening OR \"systematic review\")"),
    ("yun_check", "Yun[Author] AND (\"systematic reviews\" OR \"continuous\") AND (\"JAMIA\" OR \"language model\")"),
    ("delgadochaves_check", "\"Delgado-Chaves\" OR \"Delgado Chaves\""),
    ("lieberum_check", "Lieberum[Author] OR \"living systematic review\"[Title] AND (LLM OR LLMs OR \"large language\")")
]

for tag, q in queries:
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(q)}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        ids = data.get("esearchresult", {}).get("idlist", [])
        print(f"\n[{tag}] Query: {q} -> Hits: {ids}")
        for pmid in ids[:3]:
            sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
            req_sum = urllib.request.Request(sum_url, headers=HEADERS)
            with urllib.request.urlopen(req_sum, timeout=10) as r2:
                sdata = json.loads(r2.read().decode())
            summary = sdata.get("result", {}).get(pmid, {})
            doi = ""
            for aid in summary.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value")
            print(f"   PMID {pmid} | DOI: {doi} | {summary.get('sortfirstauthor')} | {summary.get('title')} ({summary.get('source')}, {summary.get('pubdate')})")
    except Exception as e:
        print(f"Error on {tag}: {e}")
