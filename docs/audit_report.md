# Sex-Coverage Audit Report: Published PSTi8 Literature

**Audit Date:** 2026-10-28 (Updated)  
**Scope:** 11 published preclinical studies investigating PSTi8 (pancreastatin inhibitor peptide, PEGKGEQEHSQQKEEEEEMAV-NH₂) catalogued in [data/evidence_table.csv](../data/evidence_table.csv).

---

## 1. Study Coverage Matrix

The matrix below classifies the 11 catalogued studies by disease model / biological indication against the biological sex of animal subjects utilized:

| Disease Model / Indication | Male Only | Female Only | Both Sexes | Sex Unreported / NOT_READ | Total Studies |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Type 2 Diabetes & Insulin Resistance** | 1 (`valicherla2018`) | 0 | 0 | 1 (`gupta2020_skeletal`) | **2** |
| **Hyperinsulinemia & Obesity** | 1 (`gupta2019_obesity`) | 0 | 0 | 0 | **1** |
| **Hepatic Steatosis, NASH & Oxidative Stress** | 0 | 0 | 0 | 2 (`reza2022_lfs`, `dadge2023_nash`) | **2** |
| **Perimenopausal Metabolic Dysfunction** | 0 | 2 (`singh2019_menopause`, `singh2020_heliyon`) | 0 | 0 | **2** |
| **Polycystic Ovary Syndrome (PCOS)** | 0 | 2 (`yadav2024_pcos_let`, `yadav2025_pcos_dhea`) | 0 | 0 | **2** |
| **Healthy Pharmacokinetics (PK)** | 0 | 0 | 1 (`valicherla2022_pk`) | 0 | **1** |
| **Colitis & Colonic Epithelial Maintenance** | 0 | 0 | 1 (`tshikudi2024_colitis`) | 0 | **1** |
| **TOTAL** | **2** | **4** | **2** | **3** | **11** |

*Note on counts:* `gupta2019_obesity` is classified under "Male Only" based on consistent reporting across secondary index summaries, but primary full text remains paywalled (`access: abstract`). In `gupta2020_skeletal`, `reza2022_lfs`, and `dadge2023_nash`, animal sex is not reported in abstracts and full text has not been read.

---

## 2. Detailed Breakdown of Studies Including Both Sexes

Only **two studies** (18.2% of the corpus) evaluated both male and female animals:

### A. Valicherla et al., 2022 (*Molecules*, DOI: [10.3390/molecules27020339](https://doi.org/10.3390/molecules27020339))
- **Objective:** Pharmacokinetic characterization in healthy Sprague Dawley rats across IV, IP, and SC routes.
- **Sample size:** $n = 3\text{--}6$ per sex per route.
- **Sex analyzed as a variable?** **Yes.** PK parameters (Cmax, AUC, t1/2, CL, Vd) were calculated and tabulated separately for males and females (Tables 4 and 5).
- **Sex × Treatment interaction tested?** **No (confirmed absent).** The study evaluated single doses in healthy animals. Male and female PK parameters were compared pairwise/descriptively, with the authors reporting no statistically significant sex differences. No factorial interaction test was conducted.

### B. Tshikudi et al., 2024 (*Int J Mol Sci*, DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))
- **Objective:** Therapeutic evaluation of intrarectal PSTi8 in dextran sodium sulfate (DSS)-induced colitis and steady-state epithelial maintenance in C57BL/6 mice.
- **Sample size:** $n = 5\text{--}6$ per sex per arm for tissue/cellular assays; $n = 12\text{--}15$ per sex for Disease Activity Index (DAI) cohorts.
- **Reported Phenotype (exact reporting):**
  - In colitic female mice, intrarectal PSTi8 treatment elevated daily Disease Activity Index (DAI) scores compared to vehicle controls at specific timepoints (72 h and 96 h, $p < 0.05$).
  - However, when evaluating the **cumulative Disease Activity Index (sum of DAI)** and **macroscopic damage scores (macro-scores)** encompassing diarrhea, rectal bleeding, and rectal prolapse, the paper explicitly reports a **non-significant difference** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice.
  - In colitic male mice, PSTi8 delayed the onset of DAI elevation (shifted from 24 h to 48 h) and preserved colonic stem cells and differentiated colonic epithelial cells (CECs).
- **Sex analyzed as a variable?** **Yes.** Endpoints were stratified by sex throughout the Results section.
- **Sex × Treatment interaction tested?** **Unreported.** Section 4.9 specifies two-way ANOVA, but the manuscript does not publish the omnibus interaction test statistic (F-statistic, degrees of freedom, or interaction p-value). Results are presented as within-sex pairwise post-hoc tests.

---

## 3. Methodological Evidence Gaps Categorized by Evidentiary Status

Per project standards, every gap is explicitly categorized into:
- **(a) Confirmed absent in papers read:** Verified by examining the full-text methods and results.
- **(b) Unreported in papers read:** The method or analytical model was utilized, but specific statistical terms or outcomes were not published.
- **(c) Cannot assess because NOT_READ:** The manuscript is paywalled and details are not disclosed in the abstract.

### Gap 1: Evaluation of Female Animals in General Cardiometabolic & Diabetic Indications
*Scope:* 5 studies modeling Type 2 diabetes, insulin resistance, obesity, or hepatic steatosis (`valicherla2018`, `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, `dadge2023_nash`).
- **(a) Confirmed absent in papers read (1 study):** In `valicherla2018`, methods explicitly state that only male C57BL/6J, male db/db, and male SD rats were used across all three diabetes models and PK experiments.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (4 studies):** `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, and `dadge2023_nash` are paywalled. Abstracts do not explicitly confirm whether female animals were included.

### Gap 2: Formal Factorial Sex × Treatment Interaction Testing ($p_{\text{sex} \times \text{treatment}}$)
*Scope:* 2 studies including both sexes (`valicherla2022_pk`, `tshikudi2024_colitis`).
- **(a) Confirmed absent in papers read (1 study):** In `valicherla2022_pk`, sex differences were analyzed via pairwise t-tests/descriptive summaries; no interaction test was conducted.
- **(b) Unreported in papers read (1 study):** In `tshikudi2024_colitis`, two-way ANOVA was conducted, but the omnibus interaction test statistic ($F_{\text{sex} \times \text{treatment}}$, degrees of freedom, and p-value) is unreported; the paper presents only within-sex pairwise post-hocs.
- **(c) Cannot assess because NOT_READ (0 studies):** Both studies including both sexes were read in full.
*(Note: In the remaining 9 studies, interaction testing was either not applicable due to single-sex design [2 confirmed single-sex in papers read, 3 inferred female-only from abstracts] or cannot be assessed because NOT_READ [3 studies]).*

### Gap 3: Baseline Estrous Cycle Staging and Phase Control
*Scope:* 6 studies using female animals (`singh2019_menopause`, `singh2020_heliyon`, `valicherla2022_pk`, `yadav2024_pcos_let`, `yadav2025_pcos_dhea`, `tshikudi2024_colitis`).
- **(a) Confirmed absent in papers read (2 studies):** Neither `valicherla2022_pk` nor `tshikudi2024_colitis` describe estrous cycle staging, phase monitoring, or synchronization in female rodents prior to or during treatment.
- **(b) Unreported in papers read (0 studies):** In `singh2020_heliyon`, estrous monitoring is confirmed present via daily vaginal cytology, but it was tracked longitudinally to confirm perimenopausal induction and cycle restoration as an outcome, rather than used to stage animals at baseline.
- **(c) Cannot assess because NOT_READ (3 studies):** `singh2019_menopause`, `yadav2024_pcos_let`, and `yadav2025_pcos_dhea` are paywalled. Abstracts mention estrous cyclicity as an outcome, but baseline pre-treatment staging cannot be assessed without full text.

### Gap 4: Independent Replication of Sex Divergence in Secondary Organ Systems
*Scope:* Colitis and mucosal barrier maintenance (`tshikudi2024_colitis`).
- **(a) Confirmed absent in papers read (1 study):** Independent replication of the sex-divergent colonic epithelial response to PSTi8 is absent across all read papers.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (0 studies):** `tshikudi2024_colitis` was read in full.

### Gap 5: Pharmacokinetics in Diseased or Chronically Dosed States Across Sexes
*Scope:* Pharmacokinetic profiling (`valicherla2022_pk`).
- **(a) Confirmed absent in papers read (1 study):** In `valicherla2022_pk`, PK comparisons across sexes were evaluated exclusively in healthy, young Sprague Dawley rats following single doses; evaluation in diseased or chronically treated animals is confirmed absent.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (0 studies):** Full text was read.

---

## 4. What the Evidence Table Supports and What It Does Not

### What the Table Supports
1. **Reporting Practices Across Available Literature:** In the 4 fully read papers, sex was reported clearly in methods. In 1 study (`valicherla2018`), females were confirmed absent. In 1 study (`singh2020_heliyon`), males were confirmed absent due to the female-specific perimenopause model. In 2 studies (`valicherla2022_pk`, `tshikudi2024_colitis`), both sexes were included.
2. **Documented Divergence in Colitis:** In the single fully read study testing both sexes in a non-reproductive disease model (`tshikudi2024_colitis`), sex-differentiated responses were observed on daily DAI scores at 72 h and 96 h, alongside non-significant differences on cumulative DAI sum and macroscopic damage scores.

### What the Table Does NOT Support
1. **No Conclusions Regarding PSTi8 Efficacy or Safety:** The evidence table documents methodological and reporting characteristics; it does not evaluate, confirm, or dispute the clinical safety, efficacy, or therapeutic index of PSTi8.
2. **No Generalization Across Paywalled Literature:** Missing data fields labeled `NOT_READ` represent access restrictions, not confirmed absence of data in original manuscripts.
