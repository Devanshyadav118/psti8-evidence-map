#!/usr/bin/env python3
"""
Update data/staging/thread3_registry_unverified.csv in 3 distinct batches,
saving the file after each batch.
"""

import csv
import json

CSV_PATH = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/thread3_registry_unverified.csv"
RAW_JSON = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/all_26_verified_raw.json"

with open(RAW_JSON, "r") as f:
    raw_data = json.load(f)

# Define verification status, notes, and corrections for each row
verification_info = {
    "valicherla2018": {
        "verified": "yes",
        "citation": "Hossain et al. (Valicherla et al.), Sci Rep, 2018",
        "doi": "10.1038/s41598-018-27018-8",
        "year": "2018",
        "note": "Verified in PubMed (PMID 29880906, PMC5992141). First author is Hossain Z (Valicherla GR is 2nd author). Foundational PSTi8 discovery study. Note: repo previously cited wrong DOI 10.1038/s41598-018-22528-z."
    },
    "gupta2019_dex": {
        "verified": "yes",
        "citation": "Gupta et al., Biomed Pharmacother, 2019",
        "doi": "10.1016/j.biopha.2019.108959",
        "year": "2019",
        "note": "Verified in PubMed (PMID 31108350). First author Gupta AP, journal Biomed Pharmacother 2019 Aug;116:108959. NEW primary study in dexamethasone-induced fatty liver/T2D in mice and HepG2."
    },
    "gupta2019_obesity": {
        "verified": "yes",
        "citation": "Gupta et al., Eur J Pharmacol, 2019",
        "doi": "10.1016/j.ejphar.2019.172723",
        "year": "2019",
        "note": "Verified in PubMed (PMID 31580848). First author Gupta AP, Eur J Pharmacol 2019 Dec 1;864:172723. Catalogued primary study."
    },
    "singh2019_menopause": {
        "verified": "yes",
        "citation": "Valicherla et al., Peptides, 2019",
        "doi": "10.1016/j.peptides.2019.170147",
        "year": "2019",
        "note": "Verified in PubMed (PMID 31618661). First author is Valicherla GR (Singh is not first author), Peptides 2019 Oct;120:170147. Catalogued primary study in menopausal female rats."
    },
    "valicherla2020_jpba": {
        "verified": "yes",
        "citation": "Valicherla et al., J Pharm Biomed Anal, 2020",
        "doi": "10.1016/j.jpba.2019.113074",
        "year": "2020",
        "note": "Verified in PubMed (PMID 31891874). First author Valicherla GR, J Pharm Biomed Anal 2020 Feb 20;180:113074. NEW primary PK/bioanalytical assay study in mice."
    },
    "gupta2020_skeletal": {
        "verified": "yes",
        "citation": "Gupta et al., Eur J Pharmacol, 2020",
        "doi": "10.1016/j.ejphar.2020.173204",
        "year": "2020",
        "note": "Verified in PubMed (PMID 32439261). First author Gupta AP, Eur J Pharmacol 2020 Aug 15;881:173204. Catalogued primary study."
    },
    "singh2020_fetuina": {
        "verified": "yes",
        "citation": "Singh et al., Heliyon, 2020",
        "doi": "10.1016/j.heliyon.2020.e05133",
        "year": "2020",
        "note": "Verified in PubMed (PMID 33033766, PMC7533370). First author Singh P, Heliyon 2020 Oct;6(10):e05133. Open-access NEW primary study in male C57BL/6 mice."
    },
    "singh2020_heliyon": {
        "verified": "yes",
        "citation": "Singh et al., Heliyon, 2020",
        "doi": "10.1016/j.heliyon.2020.e05826",
        "year": "2020",
        "note": "Verified in PubMed (PMID 33426334, PMC7779780). First author Singh P, Heliyon 2020 Dec;6(12):e05826. Open-access catalogued primary study. Note: repo previously had DOI typo e05500."
    },
    "reza2021_mito": {
        "verified": "yes",
        "citation": "Reza et al., Life Sci, 2021",
        "doi": "10.1016/j.lfs.2021.119905",
        "year": "2021",
        "note": "Verified in PubMed (PMID 34453940). First author Reza MI, Life Sci 2021 Nov 1;284:119905. NEW primary study on PST-induced mitochondrial dysfunction and PSTi8 protection."
    },
    "valicherla2022_pk": {
        "verified": "yes",
        "citation": "Valicherla et al., Molecules, 2022",
        "doi": "10.3390/molecules27020339",
        "year": "2022",
        "note": "Verified in PubMed (PMID 35056654, PMC8781445). First author Valicherla GR, Molecules 2022 Jan 6;27(2):339. Open-access catalogued PK study. Note: repo previously had DOI 10.3390/molecules27134153."
    },
    "reza2022_lfs": {
        "verified": "yes",
        "citation": "Garg et al., Life Sci, 2022",
        "doi": "10.1016/j.lfs.2021.120221",
        "year": "2022",
        "note": "Verified in PubMed (PMID 34902437). First author is Garg R (Richa Garg), NOT Reza MI; Reza is not an author on this paper. Corrected citation to Garg et al., Life Sci 2022 Jan 15;289:120221."
    },
    "goand2022_ssrn": {
        "verified": "yes",
        "citation": "Goand et al., SSRN Electronic Journal, 2022",
        "doi": "10.2139/ssrn.4153464",
        "year": "2022",
        "note": "Verified via Crossref. Title: Pancreastatin Inhibitor PSTi8 Balances Energy Homeostasis... First author Umesh K. Goand. Preprint of goand2023_peptides."
    },
    "goand2023_peptides": {
        "verified": "yes",
        "citation": "Goand et al., Peptides, 2023",
        "doi": "10.1016/j.peptides.2022.170902",
        "year": "2023",
        "note": "Verified in PubMed (PMID 36375661). First author Goand UK, Peptides 2023 Jan;159:170902. NEW primary study on eWAT mitochondrial function, macrophages, and Tregs in DIO mice."
    },
    "goand2023_lifesci": {
        "verified": "yes",
        "citation": "Goand et al., Life Sci, 2023",
        "doi": "10.1016/j.lfs.2023.121415",
        "year": "2023",
        "note": "Verified in PubMed (PMID 36690282). First author Goand UK, Life Sci 2023 Mar 1;316:121415. NEW primary study using osmotic minipump delivery of PSTi8 in HFD mice."
    },
    "garg2023_ejp": {
        "verified": "yes",
        "citation": "Garg et al., Eur J Pharmacol, 2023",
        "doi": "10.1016/j.ejphar.2023.175559",
        "year": "2023",
        "note": "Verified in PubMed (PMID 36764353). First author Garg R, Eur J Pharmacol 2023 Apr 5;944:175559. NEW primary study on streptozotocin-induced diabetes and hepatic glucose production."
    },
    "garg2023_review": {
        "verified": "yes",
        "citation": "Garg et al., Amino Acids, 2023",
        "doi": "10.1007/s00726-023-03252-x",
        "year": "2023",
        "note": "Verified in PubMed (PMID 36914766) and Springer full text (21 mentions of PSTi8). First author Garg R, Amino Acids 2023 May;55(5):555-573. Review of CHGA peptides and PSTi8 in diabetes."
    },
    "dadge2023_nash": {
        "verified": "yes",
        "citation": "Goand et al., Cytokine, 2023",
        "doi": "10.1016/j.cyto.2023.156354",
        "year": "2023",
        "note": "Verified in PubMed (PMID 37690261). First author is Goand UK (Umesh Kumar Goand), NOT Dadge; Dadge is not an author on this paper. Corrected citation to Goand et al., Cytokine 2023 Nov;171:156354."
    },
    "garg2023_aminoacids": {
        "verified": "yes",
        "citation": "Garg et al., Amino Acids, 2023",
        "doi": "10.1007/s00726-023-03332-y",
        "year": "2023",
        "note": "Verified in PubMed (PMID 37715808). First author Garg R, Amino Acids 2023 Nov;55(11):1621-1634. NEW primary study on lipolysis and insulin resistance in HFD mice and 3T3-L1/L6 cells."
    },
    "tshikudi2024_jcag": {
        "verified": "yes",
        "citation": "Tshikudi et al., J Can Assoc Gastroenterol, 2024",
        "doi": "10.1093/jcag/gwad061.269",
        "year": "2024",
        "note": "Verified via Crossref and JCAG (Vol 7, Suppl 1, pp. 110-111). First author Tshikudi DM. NEW primary conference abstract testing male and female C57BL/6 mice under homeostatic conditions."
    },
    "tshikudi2024_colitis": {
        "verified": "yes",
        "citation": "Tshikudi et al., Int J Mol Sci, 2024",
        "doi": "10.3390/ijms252312757",
        "year": "2024",
        "note": "Verified in PubMed (PMID 39684467, PMC11641973). First author Tshikudi DM, Int J Mol Sci 2024 Nov 27;25(23):12757. Catalogued primary study. Note: repo previously had DOI 10.3390/ijms25189949."
    },
    "yadav2024_pcos_let": {
        "verified": "yes",
        "citation": "Yadav et al., Steroids, 2024",
        "doi": "10.1016/j.steroids.2024.109558",
        "year": "2024",
        "note": "Verified in PubMed (PMID 39742935). First author Yadav S, Steroids 2025 Feb (online Dec 2024);214:109558. Catalogued primary study in letrozole-HFD PCOS female rats."
    },
    "lu2025_fimmu": {
        "verified": "yes",
        "citation": "Lu et al., Front Immunol, 2025",
        "doi": "10.3389/fimmu.2025.1536020",
        "year": "2025",
        "note": "Verified in PubMed (PMID 39912061, PMC11798928). First author Lu Y, Front Immunol 2025;16:1536020. Review of Treg immunometabolism citing PSTi8 in metabolic disease."
    },
    "maj2025_fimmu": {
        "verified": "yes",
        "citation": "Maj et al., Front Immunol, 2025",
        "doi": "10.3389/fimmu.2025.1567874",
        "year": "2025",
        "note": "Verified in PubMed (PMID 40370467, PMC12074958). First author Maj M, Front Immunol 2025;16:1567874. Review of CHGA peptides explicitly discussing PSTi8 efficacy in T2DM."
    },
    "yadav2025_pcos_dhea": {
        "verified": "yes",
        "citation": "Yadav et al., J Pharmacol Exp Ther, 2025",
        "doi": "10.1016/j.jpet.2025.103765",
        "year": "2025",
        "note": "Verified in PubMed (PMID 41259826). First author Yadav S, J Pharmacol Exp Ther 2025 Dec;JPET-AR-2025-103765. Catalogued primary study in DHEA-HFD PCOS female rats."
    },
    "christoffersson2026_fcdhc": {
        "verified": "yes",
        "citation": "Christoffersson & Muntjewerff, Front Clin Diabetes Healthc, 2026",
        "doi": "10.3389/fcdhc.2026.1812936",
        "year": "2026",
        "note": "Verified in PubMed (PMID 41810427, PMC13110968). First author Christoffersson G, Front Clin Diabetes Healthc 2026;7:1812936. Review citing PSTi8 as a promising drug to block PST."
    },
    "singla2026_jri": {
        "verified": "partial",
        "citation": "Singla et al., J Reprod Immunol, 2026",
        "doi": "10.1016/j.jri.2026.104943",
        "year": "2026",
        "note": "Verified existence in PubMed (PMID 42531755). First author Singla J, J Reprod Immunol 2026 Aug;170:104943. PCOS/IR review by Gayen lab. However, PSTi8 is NOT mentioned in title or abstract; paywalled, full text unverified for PSTi8 mention. Status set to partial."
    }
}

def save_csv(rows, fieldnames):
    with open(CSV_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Read current CSV
with open(CSV_PATH, "r") as f:
    rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

if "verification_note" not in fieldnames:
    fieldnames.append("verification_note")

# BATCH 1: Rows 1 to 9 (indices 0 to 8)
print("=== SAVING BATCH 1 (Rows 1-9) ===")
for i in range(0, 9):
    r = rows[i]
    pid = r["id"]
    if pid in verification_info:
        info = verification_info[pid]
        r["verified"] = info["verified"]
        r["citation"] = info["citation"]
        r["doi"] = info["doi"]
        r["year"] = info["year"]
        r["verification_note"] = info["note"]
save_csv(rows, fieldnames)
print("Batch 1 saved successfully.")

# BATCH 2: Rows 10 to 18 (indices 9 to 17)
print("=== SAVING BATCH 2 (Rows 10-18) ===")
for i in range(9, 18):
    r = rows[i]
    pid = r["id"]
    if pid in verification_info:
        info = verification_info[pid]
        r["verified"] = info["verified"]
        r["citation"] = info["citation"]
        r["doi"] = info["doi"]
        r["year"] = info["year"]
        r["verification_note"] = info["note"]
save_csv(rows, fieldnames)
print("Batch 2 saved successfully.")

# BATCH 3: Rows 19 to 26 (indices 18 to 26)
print("=== SAVING BATCH 3 (Rows 19-26) ===")
for i in range(18, len(rows)):
    r = rows[i]
    pid = r["id"]
    if pid in verification_info:
        info = verification_info[pid]
        r["verified"] = info["verified"]
        r["citation"] = info["citation"]
        r["doi"] = info["doi"]
        r["year"] = info["year"]
        r["verification_note"] = info["note"]
save_csv(rows, fieldnames)
print("Batch 3 saved successfully.")

print("All 3 batches saved into data/staging/thread3_registry_unverified.csv!")
