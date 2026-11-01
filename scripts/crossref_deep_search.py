#!/usr/bin/env python3
"""
scripts/crossref_deep_search.py
Query Crossref REST API for exact titles, authors, and bibliographic combinations.
"""

import urllib.request
import urllib.parse
import json

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

targets = [
    ("beery2018", "Annaliese Beery inclusion of sex in preclinical behavioral neuroscience Curr Top Behav Neurosci"),
    ("beery2018_title", "Inclusion of sex in preclinical behavioral neuroscience"),
    ("booth2020", "PROSPERO preclinical animal systematic review protocols Booth Syst Rev 2020"),
    ("booth2020_survey", "international survey prospective registration preclinical animal systematic review"),
    ("vandervaart2020", "van der Vaart PreclinicalTrials.eu 2020 Journal of the American Heart Association"),
    ("vandervaart2020_title", "PreclinicalTrials.eu: an international platform to register animal study protocols"),
    ("richedwards2023", "Rich-Edwards Maney sex-by-treatment interactions subgroup Biol Sex Differ 2023"),
    ("richedwards2023_elife", "Rich-Edwards Maney Best practices to promote rigor and reproducibility in the era of sex-inclusive research"),
    ("soliman2023", "Soliman systematic review 42 methodological guidance documents preclinical systematic reviews BMJ Open Science 2023"),
    ("levy2023", "Levy spontaneous behavior estrous state Current Biology 2023"),
    ("levy2023_neubiorev", "Levy meta-analysis 311 rodent exploratory behavior estrous-cycle"),
    ("vandernaald2024", "van der Naald PreclinicalTrials.eu 141 animal study protocols Journal of Clinical Epidemiology 2024"),
    ("vandernaald2024_title", "van der Naald animal study protocols PreclinicalTrials.eu PROSPERO"),
    ("rich2024", "Rich Diabetes 850 nonhuman animal studies 1999-2023 sex specification"),
    ("guo2024", "Guo GPT-4 title abstract screening 24,682 Journal of Clinical Epidemiology 2024"),
    ("yun2024", "Yun 7 LLMs 328 systematic reviews JAMIA 2024 Journal of the American Medical Informatics Association"),
    ("delgadochaves2025", "Delgado-Chaves 18 open- and closed-source LLMs 1,766 abstracts BMC Medical Research Methodology 2025"),
    ("delgadochaves2025_pnas", "Delgado-Chaves Transforming literature screening: The emerging role of large language models in systematic reviews"),
    ("lieberum2025", "Lieberum living systematic review 175 studies LLMs medRxiv 2025")
]

for tag, q in targets:
    url = f"https://api.crossref.org/works?query={urllib.parse.quote(q)}&rows=3"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=12) as r:
            data = json.loads(r.read().decode())
        items = data.get("message", {}).get("items", [])
        print(f"\n==============================")
        print(f"[{tag}] Query: {q}")
        for it in items:
            title = it.get("title", [""])[0] if it.get("title") else ""
            doi = it.get("DOI", "")
            journal = it.get("container-title", [""])[0] if it.get("container-title") else ""
            authors = it.get("author", [])
            fa = ""
            if authors:
                fa = f"{authors[0].get('family', '')} {authors[0].get('given', '')}".strip()
            y = ""
            if "published-print" in it:
                dp = it["published-print"].get("date-parts", [[]])[0]
                if dp: y = str(dp[0])
            elif "published-online" in it:
                dp = it["published-online"].get("date-parts", [[]])[0]
                if dp: y = str(dp[0])
            print(f"  Hit: DOI={doi} | {fa} | {title} | {journal} ({y})")
    except Exception as e:
        print(f"Error on {tag}: {e}")
