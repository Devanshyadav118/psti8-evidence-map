# Thread 3 Verification Report: Preclinical PSTi8 Evidence (2018–2026)

**Date of Audit:** 2026-10-31  
**Auditor:** Literature Extraction Agent (AGY pair-programming session)  
**Input Staging Source:** [data/staging/thread3_argon_raw.md](../data/staging/thread3_argon_raw.md) (Gemini 4 Argon unverified search)  
**Output Registries & Tables:**
- [data/staging/thread3_registry_unverified.csv](../data/staging/thread3_registry_unverified.csv) (Updated with verified status, notes, and corrected bibliometrics)
- [docs/staging_new_studies.md](staging_new_studies.md) (Verified new primary studies with sex reporting)

---

## 1. Executive Summary & Verification Counts

All 26 candidate entries from the staging registry were queried directly against **PubMed (NCBI E-utilities)**, **PMC**, and **Crossref API**. No search snippets were accepted as proof; every verification is anchored in authenticated bibliometric API records and article text.

| Status | Count | Description |
|:---|:---:|:---|
| **Verified (`yes`)** | **25** | DOI resolved; title, authors, journal, year matched or corrected; confirmed to be a PSTi8 preclinical study or review citing PSTi8. |
| **Partial (`partial`)** | **1** | Paper exists and was verified, but PSTi8 relevance cannot be confirmed (`singla2026_jri`: review on PCOS/IR by Gayen lab, but PSTi8 is absent from title and abstract; paywalled). |
| **Not Verified (`no`)** | **0** | No fabricated records were found in the 26 candidate entries. |
| **Could Not Open (`could_not_open`)** | **0** | 100% of DOIs/records successfully opened via PubMed or Crossref. |
| **Total Processed** | **26** | Processed and committed across 3 batches (Rows 1–9, Rows 10–18, Rows 19–26). |

---

## 2. Priority Investigation: Five Suspected Repo & Staging Errors

Per user instructions, the five specific suspected discrepancies were audited first against PubMed. The findings resolve critical errors in both our repository's existing files and the staging text:

### (a) First Author of `10.1016/j.lfs.2021.120221` (Garg vs. Reza)
* **PubMed Verification (PMID: 34902437):**
  - **Title:** *Pancreastatin inhibitor PSTi8 prevents free fatty acid-induced oxidative stress and insulin resistance by modulating JNK pathway: In vitro and in vivo findings.*
  - **Authors:** Garg R, Gupta AP, Katekar R, Verma S, Goand UK, Dadge S, Gayen JR.
  - **Journal & Date:** *Life Sci.* 2022 Jan 15; 289: 120221.
  - **Finding:** The first author is **Richa Garg (`Garg R`)**, NOT Reza. In fact, Mohammad Irshad Reza is not an author on this manuscript at all.
  - **Root Cause in Repo:** Our repository previously catalogued this study as `reza2022_lfs`. Reza MI is the first author of a *different*, uncatalogued PSTi8 paper in the same journal: *Reza MI, Syed AA, Singh P, Husain A, Gayen JR. Life Sci. 2021 Nov 1; 284: 119905* (DOI: `10.1016/j.lfs.2021.119905`). The two papers were conflated.

### (b) First Author of `10.1016/j.cyto.2023.156354` (Goand vs. Dadge)
* **PubMed Verification (PMID: 37690261):**
  - **Title:** *Immunometabolic impact of pancreastatin inhibitor PSTi8 in MCD induced mouse model of oxidative stress and steatohepatitis.*
  - **Authors:** Goand UK, Patel I, Verma S, Yadav S, Maity D, Singh N, Vishwakarma S, Rathaur S, Garg R, Gayen JR.
  - **Journal & Date:** *Cytokine.* 2023 Nov; 171: 156354.
  - **Finding:** The first author is **Umesh Kumar Goand (`Goand UK`)**, NOT Dadge. "Dadge S" does not appear anywhere in the author list.
  - **Root Cause in Repo:** Our repository previously named this note `dadge2023_nash` and cited Dadge et al. (though STATE.md noted the discrepancy). The correct citation is *Goand et al., Cytokine, 2023*.

### (c) First Author & Existence of Foundational Paper DOI `10.1038/s41598-018-27018-8`
* **PubMed Verification (PMID: 29880906, PMCID: PMC5992141):**
  - **Title:** *Discovery of pancreastatin inhibitor PSTi8 for the treatment of insulin resistance and diabetes: studies in rodent models of diabetes mellitus.*
  - **Authors:** Hossain Z, Valicherla GR, Gupta AP, Syed AA, Riyazuddin M, Chandra S, Siddiqi MI, Gayen JR.
  - **Journal & Date:** *Sci Rep.* 2018 Jun 7; 8(1): 8715.
  - **Finding:** The paper exists. The first author is **Zakir Hossain (`Hossain Z`)**. Gopal R. Valicherla is the second author.
  - **Critical Repo DOI Error Uncovered:** Our repository previously recorded this foundational study as `valicherla2018` with DOI `10.1038/s41598-018-22528-z`. Querying `10.1038/s41598-018-22528-z` on Crossref returns an HTTP 404 (Not Found), and it does not exist in PubMed. The real, authenticated DOI is **`10.1038/s41598-018-27018-8`**.

### (d) Existence and PSTi8 Content of `10.1016/j.jri.2026.104943`
* **PubMed Verification (PMID: 42531755):**
  - **Title:** *Polycystic ovary syndrome and insulin resistance: A focus on pathogenesis, risk factors, and therapeutic strategies.*
  - **Authors:** Singla J, Yadav S, Gayen JR.
  - **Journal & Date:** *J Reprod Immunol.* 2026 Aug; 170: 104943.
  - **Finding:** The paper **exists** and was published online early by the Gayen lab. However, **PSTi8 is not mentioned in either the title or the abstract**. The abstract reviews conventional therapies (metformin, oral contraceptives) and emerging treatments (GLP-1RAs, microRNA, IL-22, microbiome/FMT).
  - **Status:** Marked as **`partial`**. Because the full text is behind an Elsevier paywall, we cannot confirm whether PSTi8 is discussed in the body text or if Gemini 4 Argon hallucinated its relevance based purely on author affiliation.

### (e) Journal and DOI of the Streptozotocin Glucose Production Paper
* **PubMed Verification (PMID: 36764353):**
  - **Title:** *Pancreastatin inhibitor PSTi8 ameliorates streptozotocin-induced diabetes by suppressing hepatic glucose production.*
  - **Authors:** Garg R, Katekar R, Parwez S, Agarwal A, Sahu S, Dadge S, Verma S, Goand UK, Siddiqi MI, Gayen JR.
  - **Journal & Date:** *Eur J Pharmacol.* 2023 Apr 5; 944: 175559.
  - **DOI:** **`10.1016/j.ejphar.2023.175559`**.
  - **First Author:** **Garg R** (Richa Garg).
  - **Finding:** Confirmed in full. This is a bona fide primary preclinical PSTi8 study published in *European Journal of Pharmacology*.

---

## 3. Detailed Audit of Repository DOIs: Major Pre-existing Errors Discovered

During the verification of Argon's staging records against our repository's existing catalog, four major pre-existing DOI errors in our repository were discovered:

| Repository Paper ID | Repository DOI | Verified PubMed DOI | Actual Article at Repo's DOI |
|:---|:---|:---|:---|
| `valicherla2018` | `10.1038/s41598-018-22528-z` | **`10.1038/s41598-018-27018-8`** | **404 Not Found** on Crossref / absent in PubMed |
| `singh2020_heliyon` | `10.1016/j.heliyon.2020.e05500` | **`10.1016/j.heliyon.2020.e05826`** | *"Woody species composition in agroforestry systems in Ethiopia"* (PMID 33426318) |
| `valicherla2022_pk` | `10.3390/molecules27134153` | **`10.3390/molecules27020339`** | *"Free Amino Acids in Milk, Colostrum and Plasma of Swine"* (PMID 35807399) |
| `tshikudi2024_colitis` | `10.3390/ijms25189949` | **`10.3390/ijms252312757`** | *"Lipopeptide Iturin W against Staphylococcus aureus"* (PMID 39337437) |

*Note: Per user instructions ("Do not edit data/evidence_table.csv or any notes/papers file in this task"), these repository files were NOT modified in this task. They must be corrected in a future session.*

---

## 4. Item-by-Item Corrections in `thread3_registry_unverified.csv`

The staging CSV [data/staging/thread3_registry_unverified.csv](../data/staging/thread3_registry_unverified.csv) was updated with verified data across 3 batches:

1. **`valicherla2018`:** Verified (`yes`). Citation updated to reflect Hossain Z as first author: `"Hossain et al. (Valicherla et al.), Sci Rep, 2018"`. DOI authenticated as `10.1038/s41598-018-27018-8`.
2. **`gupta2019_dex`:** Verified (`yes`). NEW primary study in *Biomed Pharmacother* (PMID 31108350).
3. **`gupta2019_obesity`:** Verified (`yes`). Catalogued primary study in *Eur J Pharmacol* (PMID 31580848).
4. **`singh2019_menopause`:** Verified (`yes`). Confirmed first author is Valicherla GR (citation: `"Valicherla et al., Peptides, 2019"`).
5. **`valicherla2020_jpba`:** Verified (`yes`). NEW primary study in *J Pharm Biomed Anal* (PMID 31891874).
6. **`gupta2020_skeletal`:** Verified (`yes`). Catalogued primary study in *Eur J Pharmacol* (PMID 32439261).
7. **`singh2020_fetuina`:** Verified (`yes`). NEW primary open-access study in *Heliyon* (PMID 33033766, PMC7533370).
8. **`singh2020_heliyon`:** Verified (`yes`). Authenticated DOI `10.1016/j.heliyon.2020.e05826`.
9. **`reza2021_mito`:** Verified (`yes`). NEW primary study in *Life Sci* (PMID 34453940). First author Reza MI.
10. **`valicherla2022_pk`:** Verified (`yes`). Authenticated DOI `10.3390/molecules27020339`.
11. **`reza2022_lfs`:** Verified (`yes`). Corrected citation from "Reza et al." to `"Garg et al., Life Sci, 2022"`. First author is Garg R.
12. **`goand2022_ssrn`:** Verified (`yes`). Crossref-confirmed preprint of `goand2023_peptides`.
13. **`goand2023_peptides`:** Verified (`yes`). NEW primary study in *Peptides* (PMID 36375661). First author Goand UK.
14. **`goand2023_lifesci`:** Verified (`yes`). NEW primary study in *Life Sci* (PMID 36690282). First author Goand UK.
15. **`garg2023_ejp`:** Verified (`yes`). NEW primary study in *Eur J Pharmacol* (PMID 36764353). First author Garg R.
16. **`garg2023_review`:** Verified (`yes`). Review in *Amino Acids* (PMID 36914766). Verified 21 mentions of PSTi8 in full text HTML.
17. **`dadge2023_nash`:** Verified (`yes`). Corrected citation to `"Goand et al., Cytokine, 2023"`. First author is Goand UK.
18. **`garg2023_aminoacids`:** Verified (`yes`). NEW primary study in *Amino Acids* (PMID 37715808). First author Garg R.
19. **`tshikudi2024_jcag`:** Verified (`yes`). NEW primary conference abstract in *J Can Assoc Gastroenterol* (Vol 7, Suppl 1, pp. 110-111).
20. **`tshikudi2024_colitis`:** Verified (`yes`). Authenticated DOI `10.3390/ijms252312757`.
21. **`yadav2024_pcos_let`:** Verified (`yes`). Catalogued primary study in *Steroids* (PMID 39742935).
22. **`lu2025_fimmu`:** Verified (`yes`). Review in *Front Immunol* (PMID 39912061, PMC11798928). Mentions PSTi8 in PMC full text.
23. **`maj2025_fimmu`:** Verified (`yes`). Review in *Front Immunol* (PMID 40370467, PMC12074958). Mentions PSTi8 in PMC full text.
24. **`yadav2025_pcos_dhea`:** Verified (`yes`). Catalogued primary study in *J Pharmacol Exp Ther* (PMID 41259826).
25. **`christoffersson2026_fcdhc`:** Verified (`yes`). Review in *Front Clin Diabetes Healthc* (PMID 41810427, PMC13110968). Mentions PSTi8 in PMC full text.
26. **`singla2026_jri`:** Verified (`partial`). Paper exists (PMID 42531755), but PSTi8 is not mentioned in abstract; paywalled, full text unverified.

---

## 5. What Could Not Be Verified (Limits)

1. **Paywalled Methods Sections of 7 New Primary Studies:**  
   In `gupta2019_dex`, `valicherla2020_jpba`, `reza2021_mito`, `goand2023_peptides`, `goand2023_lifesci`, `garg2023_ejp`, and `garg2023_aminoacids`, the abstract text does not specify whether male, female, or both animal sexes were tested. Because these journals are behind Elsevier/Springer paywalls, animal sex could not be verified from the Methods sections and was recorded strictly as `NOT_READ`.
2. **Body Text of `singla2026_jri`:**  
   Published in *Journal of Reproductive Immunology* behind an Elsevier paywall. Neither the title nor the abstract mentions PSTi8. Whether the authors mention PSTi8 in the body text or references cannot be assessed without full-text access.
3. **Full PDF of `goand2022_ssrn` Preprint:**  
   SSRN metadata and abstract title were verified via Crossref API, but the standalone SSRN PDF was not downloaded or read.
