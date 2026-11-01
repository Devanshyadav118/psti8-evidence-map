#!/usr/bin/env python3
"""
scripts/find_real_papers.py
Search PubMed directly for each of the target papers by author and key terms.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

targets = [
    ("beery2011", "Beery", "Sex bias in neuroscience and biomedical research", "2011"),
    ("prendergast2014", "Prendergast", "Female mice liberated for inclusion in neuroscience", "2014"),
    ("hooijmans2014", "Hooijmans", "SYRCLE's risk of bias tool for animal studies", "2014"),
    ("devries2014", "de Vries", "usefulness of systematic reviews of animal experiments", "2014"),
    ("yoon2014", "Yoon", "Sex bias exists in basic science and translational surgical", "2014"),
    ("beery2018", "Beery", "inclusion in preclinical behavioral neuroscience factorial design", "2018"),
    ("booth2020", "Booth", "PROSPERO preclinical animal systematic review", "2020"),
    ("perciedusert2020", "Percie du Sert", "ARRIVE guidelines 2.0", "2020"),
    ("perciedusert2020_ee", "Percie du Sert", "Reporting animal research: Explanation and elaboration", "2020"),
    ("arnegard2020", "Arnegard", "Sex as a Biological Variable SABV", "2020"),
    ("woitowich2020", "Woitowich", "10-year follow-up study of sex inclusion", "2020"),
    ("vandervaart2020", "van der Vaart", "PreclinicalTrials.eu", "2020"),
    ("page2021", "Page", "PRISMA 2020 statement", "2021"),
    ("rethlefsen2021", "Rethlefsen", "PRISMA-S", "2021"),
    ("garciasifuentes2021", "Garcia-Sifuentes", "Reporting and misreporting of sex differences", "2021"),
    ("richedwards2023", "Rich-Edwards", "Maney sex interaction factorial", "2023"),
    ("soliman2023", "Soliman", "methodological guidance preclinical systematic reviews", "2023"),
    ("phillips2023", "Phillips", "factorial design power sex sample size", "2023"),
    ("levy2023", "Levy", "variability female mice exploratory behavior", "2023"),
    ("vandernaald2024", "van der Naald", "PreclinicalTrials.eu PROSPERO", "2024"),
    ("rich2024", "Rich", "sex reporting Diabetes nonhuman animal", "2024"),
    ("gartlehner2024", "Gartlehner", "Claude data extraction systematic review", "2024"),
    ("guo2024", "Guo", "GPT-4 screening systematic review", "2024"),
    ("konet2024", "Konet", "GPT-4 Claude data extraction systematic reviews", "2024"),
    ("yun2024", "Yun", "systematic reviews data extraction LLM", "2024"),
    ("delgadochaves2025", "Delgado-Chaves", "LLMs biomedical systematic reviews", "2025"),
    ("lieberum2025", "Lieberum", "living systematic review LLMs", "2025")
]

for tag, author, kw, yr in targets:
    # search term
    term = f"{author}[Author] AND ({kw})"
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term)}&retmode=json"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read().decode())
        ids = data.get("esearchresult", {}).get("idlist", [])
        if not ids:
            # fallback without author field tag
            term2 = f"{author} {kw}"
            url2 = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(term2)}&retmode=json"
            req2 = urllib.request.Request(url2, headers=HEADERS)
            with urllib.request.urlopen(req2, timeout=10) as r2:
                data2 = json.loads(r2.read().decode())
            ids = data2.get("esearchresult", {}).get("idlist", [])

        print(f"\nTarget: {tag} ({author}, {yr}) -> hits: {ids}")
        if ids:
            pmid = ids[0]
            sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
            req_sum = urllib.request.Request(sum_url, headers=HEADERS)
            with urllib.request.urlopen(req_sum, timeout=10) as r3:
                sdata = json.loads(r3.read().decode())
            summary = sdata.get("result", {}).get(pmid, {})
            doi = ""
            for aid in summary.get("articleids", []):
                if aid.get("idtype") == "doi":
                    doi = aid.get("value")
            print(f"  Top PMID: {pmid} | DOI: {doi}")
            print(f"  Title:    {summary.get('title')}")
            print(f"  Source:   {summary.get('source')} ({summary.get('pubdate')})")
            print(f"  Authors:  {summary.get('sortfirstauthor')}")
    except Exception as e:
        print(f"  Error on {tag}: {e}")
