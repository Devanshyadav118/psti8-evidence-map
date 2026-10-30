#!/usr/bin/env python3
import urllib.request
import json
import xml.etree.ElementTree as ET

headers = {"User-Agent": "PSTi8-Literature-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

def get_paper_data(doi):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={urllib.parse.quote(doi)}[doi]&retmode=json"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        idlist = data.get("esearchresult", {}).get("idlist", [])
        if idlist:
            pmid = idlist[0]
            sum_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id={pmid}&retmode=json"
            with urllib.request.urlopen(urllib.request.Request(sum_url, headers=headers), timeout=15) as r2:
                sdata = json.loads(r2.read().decode()).get("result", {}).get(pmid, {})
            fetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
            with urllib.request.urlopen(urllib.request.Request(fetch_url, headers=headers), timeout=15) as r3:
                xml_str = r3.read().decode()
            root = ET.fromstring(xml_str)
            abstract = " ".join([node.text for node in root.findall(".//AbstractText") if node.text])
            mesh = [node.text for node in root.findall(".//MeshHeading/DescriptorName") if node.text]
            return {
                "source": "pubmed",
                "pmid": pmid,
                "title": sdata.get("title", "").strip(),
                "first_author": sdata.get("sortfirstauthor", ""),
                "authors": [a.get("name") for a in sdata.get("authors", [])],
                "journal": sdata.get("source", ""),
                "pubdate": sdata.get("pubdate", ""),
                "abstract": abstract,
                "mesh": mesh
            }
    except Exception as e:
        print(f"PubMed lookup error for {doi}: {e}")
        
    # try crossref
    url2 = f"https://api.crossref.org/works/{urllib.parse.quote(doi)}"
    try:
        with urllib.request.urlopen(urllib.request.Request(url2, headers=headers), timeout=15) as resp2:
            cdata = json.loads(resp2.read().decode()).get("message", {})
        title = cdata.get("title", [""])[0] if cdata.get("title") else ""
        authors = cdata.get("author", [])
        fa = ""
        if authors:
            family = authors[0].get('family', '')
            given = authors[0].get('given', '')
            fa = f"{family} {given}".strip()
        j = cdata.get("container-title", [""])[0] if cdata.get("container-title") else ""
        y = ""
        for k in ["published-print", "published-online", "created"]:
            if k in cdata and "date-parts" in cdata[k]:
                y = str(cdata[k]["date-parts"][0][0])
                break
        return {
            "source": "crossref",
            "title": title,
            "first_author": fa,
            "authors": [f"{a.get('family', '')} {a.get('given', '')}".strip() for a in authors],
            "journal": j,
            "pubdate": y,
            "abstract": cdata.get("abstract", "")
        }
    except Exception as e:
        return {"error": str(e)}

dois = [
    ("valicherla2018", "10.1038/s41598-018-27018-8"),
    ("gupta2019_dex", "10.1016/j.biopha.2019.108959"),
    ("gupta2019_obesity", "10.1016/j.ejphar.2019.172723"),
    ("singh2019_menopause", "10.1016/j.peptides.2019.170147"),
    ("valicherla2020_jpba", "10.1016/j.jpba.2019.113074"),
    ("gupta2020_skeletal", "10.1016/j.ejphar.2020.173204"),
    ("singh2020_fetuina", "10.1016/j.heliyon.2020.e05133"),
    ("singh2020_heliyon", "10.1016/j.heliyon.2020.e05826"),
    ("reza2021_mito", "10.1016/j.lfs.2021.119905"),
    ("valicherla2022_pk", "10.3390/molecules27020339"),
    ("reza2022_lfs", "10.1016/j.lfs.2021.120221"),
    ("goand2022_ssrn", "10.2139/ssrn.4153464"),
    ("goand2023_peptides", "10.1016/j.peptides.2022.170902"),
    ("goand2023_lifesci", "10.1016/j.lfs.2023.121415"),
    ("garg2023_ejp", "10.1016/j.ejphar.2023.175559"),
    ("garg2023_review", "10.1007/s00726-023-03252-x"),
    ("dadge2023_nash", "10.1016/j.cyto.2023.156354"),
    ("garg2023_aminoacids", "10.1007/s00726-023-03332-y"),
    ("tshikudi2024_jcag", "10.1093/jcag/gwad061.269"),
    ("tshikudi2024_colitis", "10.3390/ijms252312757"),
    ("yadav2024_pcos_let", "10.1016/j.steroids.2024.109558"),
    ("lu2025_fimmu", "10.3389/fimmu.2025.1536020"),
    ("maj2025_fimmu", "10.3389/fimmu.2025.1567874"),
    ("yadav2025_pcos_dhea", "10.1016/j.jpet.2025.103765"),
    ("christoffersson2026_fcdhc", "10.3389/fcdhc.2026.1812936"),
    ("singla2026_jri", "10.1016/j.jri.2026.104943")
]

results = {}
for pid, doi in dois:
    print(f"Fetching {pid} ({doi})...")
    d = get_paper_data(doi)
    results[pid] = d

with open("/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/all_26_verified_raw.json", "w") as out:
    json.dump(results, out, indent=2)

print("Saved all 26 verified records to all_26_verified_raw.json")
