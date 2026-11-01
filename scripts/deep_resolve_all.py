#!/usr/bin/env python3
"""
scripts/deep_resolve_all.py

Check PMC IDs, OUP URLs, Crossref titles, Europe PMC, and PubMed to pinpoint
the exact truth for each of the 27 rows in Thread 6.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET
import re

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

def check_pmc(pmcid):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pmc&id={pmcid.replace('PMC','')}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        return data.get("result", {}).get(pmcid.replace('PMC',''), {})
    except Exception as e:
        return {"error": str(e)}

def search_europe_pmc(query):
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(query)}&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        return data.get("resultList", {}).get("result", [])
    except Exception as e:
        return []

def search_crossref(query):
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(query)}&rows=3"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
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

# Check PMC10124267 for Soliman
print("--- Soliman PMC10124267 ---")
pmc_sol = check_pmc("PMC10124267")
print(pmc_sol.get("title"), pmc_sol.get("doi"), pmc_sol.get("authors"))

# Check specific searches in Europe PMC
epmc_targets = [
    ("beery2018", 'AUTH:"Beery" AND "Current Topics in Behavioral Neurosciences"'),
    ("beery2018_2", 'TITLE:"Inclusion of sex" AND AUTH:"Beery"'),
    ("booth2020", 'AUTH:"Booth" AND "PROSPERO" AND "preclinical"'),
    ("booth2020_2", 'TITLE:"PROSPERO" AND "preclinical"'),
    ("vandervaart2020", 'AUTH:"van der Vaart" AND "PreclinicalTrials.eu"'),
    ("vandervaart2020_2", 'TITLE:"PreclinicalTrials.eu"'),
    ("richedwards2023", 'AUTH:"Rich-Edwards" AND AUTH:"Maney"'),
    ("richedwards2023_2", '"subgroup" AND "interaction" AND AUTH:"Maney"'),
    ("soliman2023", 'AUTH:"Soliman" AND "BMJ Open Science"'),
    ("vandernaald2024", 'AUTH:"van der Naald" AND ("PreclinicalTrials.eu" OR "preregistration")'),
    ("rich2024", 'AUTH:"Rich" AND "Diabetes" AND ("nonhuman" OR "animal")'),
    ("rich2024_2", 'TITLE:"sex" AND "Diabetes" AND AUTH:"Rich"'),
    ("gartlehner2024", 'AUTH:"Gartlehner" AND "Claude"'),
    ("guo2024", 'AUTH:"Guo" AND "GPT-4" AND ("screening" OR "systematic review")'),
    ("konet2024", 'AUTH:"Konet" AND "Claude"'),
    ("yun2024", 'AUTH:"Yun" AND "JAMIA"'),
    ("yun2024_2", 'TITLE:"7698207" OR "10.1093/jamia" AND "systematic reviews"'),
    ("delgadochaves2025", 'AUTH:"Delgado-Chaves" AND ("systematic review" OR "screening" OR "LLMs")'),
    ("lieberum2025", 'AUTH:"Lieberum" AND "living systematic review"')
]

for tag, q in epmc_targets:
    res = search_europe_pmc(q)
    print(f"\n[{tag}] Query: {q} -> {len(res)} hits")
    for r in res[:2]:
        print(f"  Title:  {r.get('title')}")
        print(f"  Author: {r.get('authorString')}")
        print(f"  Source: {r.get('journalTitle')} ({r.get('pubYear')})")
        print(f"  DOI:    {r.get('doi')}")
        print(f"  PMID:   {r.get('pmid')} | PMCID: {r.get('pmcid')}")
