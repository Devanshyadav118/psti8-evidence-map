#!/usr/bin/env python3
"""
scripts/deep_search_titles.py
Search Europe PMC and Crossref for the exact distinctive phrases from Argon's one_line_relevance.
"""

import urllib.request
import urllib.parse
import json

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

phrases = [
    ("beery2018", 'Beery "preclinical behavioral neuroscience" OR "estrous-cycle staging unless required"'),
    ("beery2018_b", 'Beery "Curr Top Behav Neurosci" 2018'),
    ("beery2018_c", 'Beery "factorial" "sample size" sex'),
    ("booth2020", 'Booth "PROSPERO" preclinical animal systematic review'),
    ("booth2020_b", '"PROSPERO" "international survey" "preclinical"'),
    ("vandervaart2020", '"PreclinicalTrials.eu" 2020'),
    ("vandervaart2020_b", '"van der Vaart" PreclinicalTrials.eu'),
    ("richedwards2023", 'Rich-Edwards "subgroup" "interaction"'),
    ("soliman2023", 'Soliman "42 methodological guidance documents"'),
    ("soliman2023_b", 'Soliman "preclinical systematic reviews" 2023'),
    ("levy2023", 'Levy "311 rodent exploratory behavior"'),
    ("levy2023_b", 'Levy "spontaneous behavior" "estrous"'),
    ("vandernaald2024", '"PreclinicalTrials.eu" "141" animal study protocols'),
    ("vandernaald2024_b", '"van der Naald" "PreclinicalTrials.eu" 2024'),
    ("rich2024", '"850 nonhuman animal studies" Diabetes'),
    ("rich2024_b", 'Rich "Diabetes" "1999-2023" OR "25-year"'),
    ("rich2024_c", 'Rich "sex reporting" "Diabetes"'),
    ("gartlehner2024", 'Gartlehner "Claude 2" "1,410" OR "96.3%"'),
    ("gartlehner2024_b", 'Gartlehner "data extraction" "Claude"'),
    ("guo2024", 'Guo "24,682" "GPT-4"'),
    ("guo2024_b", 'Guo "GPT-4" "screening" "J Clin Epidemiol"'),
    ("konet2024", 'Konet "109 studies" "10 systematic reviews"'),
    ("konet2024_b", 'Konet "GPT-4" "Claude" "data extraction"'),
    ("yun2024", 'Yun "328 systematic reviews" "628,434 tokens"'),
    ("yun2024_b", 'Yun "7 LLMs" "continuous outcomes" JAMIA'),
    ("yun2024_c", '"31/9/1912/7698207" OR "7698207"'),
    ("delgadochaves2025", 'Delgado-Chaves "18 open-" "workload reductions"'),
    ("delgadochaves2025_b", 'Delgado-Chaves "1,766 abstracts"'),
    ("delgadochaves2025_c", 'Delgado-Chaves "BMC Med Res Methodol"'),
    ("lieberum2025", '"Lieberum" "175 studies" "11,488"'),
    ("lieberum2025_b", 'Lieberum "living systematic review"')
]

for tag, q in phrases:
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={urllib.parse.quote(q)}&format=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        res = data.get("resultList", {}).get("result", [])
        if res:
            print(f"\n[{tag}] Query: {q} -> FOUND {len(res)} hits!")
            for item in res[:2]:
                print(f"  Title:   {item.get('title')}")
                print(f"  Authors: {item.get('authorString')}")
                print(f"  Journal: {item.get('journalTitle')} ({item.get('pubYear')})")
                print(f"  DOI:     {item.get('doi')}")
                print(f"  PMID:    {item.get('pmid')} | PMCID: {item.get('pmcid')}")
        else:
            print(f"[{tag}] 0 hits.")
    except Exception as e:
        print(f"[{tag}] Error: {e}")
