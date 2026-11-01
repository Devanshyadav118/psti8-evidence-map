#!/usr/bin/env python3
"""
scripts/check_quant_claims.py
Inspect the abstracts of key Thread 6 papers for verbatim presence of quantitative claims.
"""

import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

HEADERS = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

pmids_to_check = {
    "beery2011": "20620164",
    "prendergast2014": "24456941",
    "yoon2014": "25175501",
    "woitowich2020": "32513386",
    "garciasifuentes2021": "34726154",
    "phillips2023": "37289836",
    "gartlehner2024": "38432227",
    "guo2024": "38214966",
    "konet2024": "38895747",
    "delgadochaves2025": "39761403",
    "lieberum2025": "40021099",
    "cherian2024": "38409052"
}

for tag, pmid in pmids_to_check.items():
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            xml_str = r.read().decode()
        root = ET.fromstring(xml_str)
        nodes = root.findall(".//AbstractText")
        abstract = " ".join([n.text for n in nodes if n.text])
        print(f"\n==============================")
        print(f"[{tag}] PMID: {pmid}")
        print(f"Abstract preview: {abstract[:300]}...")
        # check specific terms
        checks = {
            "beery2011": ["5.5", "8 of 10", "60%"],
            "prendergast2014": ["293", "9,932", "variab"],
            "yoon2014": ["1,363", "22%", "80%", "1%"],
            "woitowich2020": ["720", "28%", "49%", "42%"],
            "garciasifuentes2021": ["147", "70%", "interaction"],
            "phillips2023": ["sample size", "both sexes", "two-way"],
            "gartlehner2024": ["96.3%", "1,410", "52"],
            "guo2024": ["24,682", "24,000", "0.91", "76%"],
            "konet2024": ["109", "10", "80%", "95%"],
            "delgadochaves2025": ["18", "1,766", "78", "96.3%"],
            "lieberum2025": ["175", "11,488", "37", "8054"],
            "cherian2024": ["20", "twenty", "87%", "15%"]
        }
        for term in checks.get(tag, []):
            present = term.lower() in abstract.lower()
            print(f"   Term '{term}': {'IN ABSTRACT' if present else 'ABSENT FROM ABSTRACT'}")
    except Exception as e:
        print(f"Error on {tag}: {e}")
