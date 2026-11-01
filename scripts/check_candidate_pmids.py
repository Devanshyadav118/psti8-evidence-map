#!/usr/bin/env python3
"""
scripts/check_candidate_pmids.py
Inspect candidate PMIDs for Delgado-Chaves, van der Naald, Beery 2018, Gartlehner, Konet, Yun, etc.
"""

import urllib.request
import urllib.parse
import json

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

pmids_to_check = [
    # Delgado-Chaves
    "39843580", "39761403", "40419963",
    # van der Naald
    "39965905", "39900404", "39829325", "38278428", "38218461",
    # Gartlehner
    "38432227", "41183336",
    # Beery
    "34726153", "34649925", "30414016", "30191477",
    # Booth 2020
    "32005283",
    # Arnegard
    "31971851",
    # Phillips 2023
    "37289836",
    # Levy 2023
    "36889318", "37121495", "37094740",
    # Rich 2024
    "38394289",
    # Guo 2024
    "38367658", "38428540",
    # Konet 2024
    "38895747", "39327610", "38783327",
    # Yun 2024
    "38934289",
    # Lieberum 2025
    "40313300",
    # Soliman 2023
    "37080649", # let's check
    # Rich-Edwards 2023
    "37723561"
]

url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={','.join(pmids_to_check)}&retmode=json"
req = urllib.request.Request(url, headers=HEADERS)
with urllib.request.urlopen(req, timeout=15) as r:
    data = json.loads(r.read().decode())

results = data.get("result", {})
for pmid in pmids_to_check:
    info = results.get(pmid)
    if not info:
        print(f"PMID {pmid}: Not found")
        continue
    doi = ""
    for aid in info.get("articleids", []):
        if aid.get("idtype") == "doi":
            doi = aid.get("value")
    print(f"PMID {pmid}:")
    print(f"  Title:   {info.get('title')}")
    print(f"  Author:  {info.get('sortfirstauthor')}")
    print(f"  Source:  {info.get('source')} ({info.get('pubdate')})")
    print(f"  DOI:     {doi}")
