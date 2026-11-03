# Sex-Coverage Audit Report: Published PSTi8 Literature

**Audit Date:** 2026-11-02 (Updated with Thread 3 Primary Studies)  
**Scope:** 20 published preclinical studies investigating PSTi8 (pancreastatin inhibitor peptide, PEGKGEQEHSQQKEEEEEMAV-NH₂) catalogued in [data/evidence_table.csv](../data/evidence_table.csv).  
**Underlying Staging Source:** [docs/staging_new_studies.md](staging_new_studies.md) and [docs/thread3_verification.md](thread3_verification.md).  

---

## 1. Study Coverage Matrix

The matrix below classifies the 20 catalogued primary preclinical studies by disease model / biological indication against the biological sex of animal subjects utilized, incorporating the evidentiary source of sex determination (`sex_source`):

| Disease Model / Indication | Male Only | Female Only | Both Sexes | Sex Unreported / NOT_READ | Total Studies | Evidentiary Basis (`sex_source`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Type 2 Diabetes & Insulin Resistance** | 2 (`valicherla2018`, `singh2020_fetuina`) | 0 | 0 | 4 (`gupta2020_skeletal`, `gupta2019_dex`, `garg2023_ejp`, `garg2023_aminoacids`) | **6** | `valicherla2018`, `singh2020_fetuina`: `full_text`; others: `NOT_READ` |
| **Hyperinsulinemia & Obesity (DIO)** | 1 (`gupta2019_obesity`) | 0 | 0 | 2 (`goand2023_peptides`, `goand2023_lifesci`) | **3** | `gupta2019_obesity`: `inferred_from_model`; others: `NOT_READ` |
| **Hepatic Steatosis, NASH & Mitochondrial/Oxidative Stress** | 0 | 0 | 0 | 3 (`reza2021_mito`, `reza2022_lfs`, `dadge2023_nash`) | **3** | `NOT_READ` (abstracts do not disclose sex; paywalled full text not read) |
| **Perimenopausal Metabolic Dysfunction** | 0 | 2 (`singh2019_menopause`, `singh2020_heliyon`) | 0 | 0 | **2** | `singh2019_menopause`: `inferred_from_model`; `singh2020_heliyon`: `full_text` |
| **Polycystic Ovary Syndrome (PCOS)** | 0 | 2 (`yadav2024_pcos_let`, `yadav2025_pcos_dhea`) | 0 | 0 | **2** | `inferred_from_model` (female-only endocrine models; abstracts do not state sex) |
| **Pharmacokinetics (PK) & Assay Validation** | 0 | 0 | 1 (`valicherla2022_pk`) | 1 (`valicherla2020_jpba`) | **2** | `valicherla2022_pk`: `full_text`; `valicherla2020_jpba`: `NOT_READ` |
| **Colitis & Colonic Epithelial Maintenance** | 0 | 0 | 2 (`tshikudi2024_colitis`, `tshikudi2024_jcag`) | 0 | **2** | `tshikudi2024_colitis`: `full_text`; `tshikudi2024_jcag`: `abstract` |
| **TOTAL** | **3 (15.0%)** | **4 (20.0%)** | **3 (15.0%)** | **10 (50.0%)** | **20** | **5 `full_text`, 4 `inferred_from_model`, 1 `abstract`, 10 `NOT_READ`** |

### Summary of Sex Coverage Across the 20 Studies
- **Total Denominator:** **20 primary preclinical studies** (19 peer-reviewed journal papers + 1 conference abstract supplement).
- **Both Sexes Evaluated:** **3 studies (15.0%)** (`valicherla2022_pk`, `tshikudi2024_colitis`, `tshikudi2024_jcag`).
- **Single-Sex Studies:** **7 studies (35.0%)** (3 male-only, 4 female-only).
- **Unreported / `NOT_READ` Due to Paywalls:** **10 studies (50.0%)** (all 10 are paywalled; sex is not stated in published abstracts).
- **Evidentiary Provenance:** Only **5 studies (25.0%)** have animal sex verified directly from open-access full-text methods. In **4 studies (20.0%)**, sex is inferred from female-specific reproductive surgical/endocrine models. In **1 study (5.0%)**, sex is verified from a published conference abstract. In the remaining **10 studies (50.0%)**, sex is unstated in the abstract and coded strictly as `NOT_READ`.

---

## 2. Detailed Breakdown of Studies Including Both Sexes

Exactly **three studies** (15.0% of the corpus) evaluated both male and female animals:

### A. Valicherla et al., 2022 (*Molecules*, DOI: [10.3390/molecules27020339](https://doi.org/10.3390/molecules27020339))
- **Objective:** Pharmacokinetic characterization in healthy Sprague Dawley rats across intravenous, intraperitoneal, and subcutaneous routes.
- **Sample size:** $n = 3\text{--}6$ per sex per route.
- **Sex analyzed as a variable?** **Yes (`sex_analyzed_as_variable: yes`).** Pharmacokinetic parameters (Cmax, AUC, t1/2, CL, Vd) were calculated and tabulated separately for males and females (Tables 4 and 5).
- **Sex × Treatment interaction tested?** **No (`interaction_tested: no`).** The study evaluated single doses in healthy animals. Male and female PK parameters were compared pairwise/descriptively, with the authors reporting no statistically significant sex differences. No factorial interaction test was conducted.
- **Estrous control:** Neither baseline estrous staging nor longitudinal cycle monitoring is reported in the Methods (`estrous_monitored_outcome: no`, `estrous_baseline_staged: no`; locator: Section 4.5).
- **Evidentiary status:** Verified from open-access full text.

### B. Tshikudi et al., 2024 (*Int J Mol Sci*, DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))
- **Objective:** Therapeutic evaluation of intrarectal PSTi8 in dextran sodium sulfate (DSS)-induced colitis and steady-state epithelial maintenance in C57BL/6 mice.
- **Sample size:** $n = 5\text{--}6$ per sex per arm for tissue/cellular assays; $n = 12\text{--}15$ per sex for Disease Activity Index (DAI) cohorts.
- **Reported Phenotype (exact reporting):**
  - In colitic mice, daily Disease Activity Index (DAI) scores were higher in females treated with intrarectal PSTi8 compared to female vehicle controls at 72 h and 96 h ($p < 0.05$).
  - However, when evaluating the **cumulative Disease Activity Index (sum of DAI)** and **macroscopic damage scores (macro-scores)** encompassing diarrhea, rectal bleeding, and rectal prolapse, cumulative DAI and macroscopic scores were **not significantly different** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice.
  - In colitic males, PSTi8 delayed the onset of DAI elevation (from 24 h to 48 h) and preserved colonic stem cells and differentiated colonic epithelial cells (CECs).
  - The authors explicitly describe these experimental findings as **descriptive**. The phenotype is documented as observed, without characterization as generalized male protection versus female exacerbation.
- **Sex analyzed as a variable?** **Yes (`sex_analyzed_as_variable: yes`).** Endpoints were stratified by sex throughout the Results section.
- **Sex × Treatment interaction tested?** **Confirmed absent (`interaction_tested: no`).** Section 4.11 specifies ordinary one-way ANOVA with Bonferroni or Tukey post-hoc tests; ordinary one-way ANOVA was applied across Figures 1–8. Two-way ANOVA is mentioned only in Figure 1 and 7 captions for longitudinal timecourses and marker arrays, but no two-way ANOVA evaluating a Sex x Treatment interaction was performed anywhere in the paper.
- **Estrous control:** Neither baseline estrous staging nor longitudinal cycle monitoring is reported in the Methods (`estrous_monitored_outcome: no`, `estrous_baseline_staged: no`; locator: Section 4.1, 4.11).
- **Evidentiary status:** Verified from open-access full text.

### C. Tshikudi et al., 2024 (*J Can Assoc Gastroenterol*, DOI: [10.1093/jcag/gwad061.269](https://doi.org/10.1093/jcag/gwad061.269))
- **Objective:** Investigation of colonic mucosal regeneration and epithelium maintenance in male and female C57BL/6 mice under homeostatic (non-colitic) conditions.
- **Sample size:** Unstated in published abstract supplement (`n_per_group: not_reported (abstract-only)`).
- **Treatment:** Intrarectal PSTi8 (2.5 mg/kg daily) or PBS for 6 days.
- **Reported Phenotype:**
  - Epithelial cell proliferation (Ki67) decreased following PSTi8 treatment in both sexes.
  - PSTi8 reduced epithelial differentiation (CK-20, Muc2) and increased tuft cell gene expression (Dclk1) selectively in females, but not in males.
  - Downregulated BMP4 in females without altering expression in males.
  - Enhanced gene expression of ER stress markers ATF6 and CHOP in females, whereas CHOP was unaltered in males.
- **Sex analyzed as a variable?** **Yes (`sex_analyzed_as_variable: yes (abstract-only)`).** Outcomes are explicitly disaggregated and contrasted between sexes throughout the abstract.
- **Sex × Treatment interaction tested?** **Not reported (`interaction_tested: not_reported (abstract-only)`).** Statistical methods and omnibus interaction test statistics ($F$ and p-values) are not disclosed in the conference abstract.
- **Estrous control:** Staging and monitoring are not reported (`estrous_monitored_outcome: no (abstract-only)`, `estrous_baseline_staged: not_reported (abstract-only)`).
- **Evidentiary status:** Verified from open-access published conference abstract.

---

## 3. Methodological Evidence Gaps Categorized by Evidentiary Status

Every gap is categorized strictly into:
- **(a) Confirmed absent in papers read:** Verified by examining full-text methods and results.
- **(b) Unreported in papers read:** The analytical model was utilized, but specific terms or metrics were omitted (`not_reported`).
- **(c) Cannot assess because NOT_READ:** The manuscript is paywalled and details are not disclosed in the abstract.

### Gap 1: Evaluation of Female Animals in General Cardiometabolic & Diabetic Indications
*Scope:* 12 studies modeling Type 2 diabetes, insulin resistance, obesity, or hepatic steatosis (`valicherla2018`, `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, `dadge2023_nash`, `gupta2019_dex`, `singh2020_fetuina`, `reza2021_mito`, `goand2023_peptides`, `goand2023_lifesci`, `garg2023_ejp`, `garg2023_aminoacids`).
- **(a) Confirmed absent in papers read (2 studies):** In `valicherla2018` and `singh2020_fetuina`, methods explicitly state that male rodents were used exclusively across all diabetic and dietary cohorts.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (10 studies):** `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, `dadge2023_nash`, `gupta2019_dex`, `reza2021_mito`, `goand2023_peptides`, `goand2023_lifesci`, `garg2023_ejp`, and `garg2023_aminoacids` are paywalled. Abstracts do not explicitly confirm whether female animals were included.

### Gap 2: Formal Factorial Sex × Treatment Interaction Testing ($p_{\text{sex} \times \text{treatment}}$)
*Scope:* 3 studies including both sexes (`valicherla2022_pk`, `tshikudi2024_colitis`, `tshikudi2024_jcag`).
- **(a) Confirmed absent in papers read (2 studies):** Both `valicherla2022_pk` and `tshikudi2024_colitis` were examined in open full text; neither performed a factorial interaction test (`interaction_tested: no` in both). In `valicherla2022_pk`, sex differences were analyzed via pairwise t-tests/descriptive summaries. In `tshikudi2024_colitis`, Section 4.11 and figure legends specify ordinary one-way ANOVA with Tukey's post-hoc tests between individual group averages; no two-way ANOVA evaluating a Sex x Treatment interaction was performed.
- **(b) Unreported in papers read (0 studies):** Zero fully read studies utilized a factorial model while omitting the interaction statistic.
- **(c) Abstract-only reporting (1 study):** In `tshikudi2024_jcag`, sex-dependent outcomes are reported, but statistical models and interaction statistics are not disclosed (`interaction_tested: not_reported (abstract-only)`).
- **Summary:** **Zero of the 3 studies (0.0%)** testing both sexes published the omnibus interaction test statistic. In both fully read dual-sex studies (100%), factorial interaction testing is confirmed absent.

### Gap 3: Baseline Estrous Cycle Staging vs. Longitudinal Outcome Monitoring
*Scope:* 7 studies using female animals (`singh2019_menopause`, `singh2020_heliyon`, `valicherla2022_pk`, `yadav2024_pcos_let`, `yadav2025_pcos_dhea`, `tshikudi2024_colitis`, `tshikudi2024_jcag`).
- **(a) Confirmed absent in papers read (2 studies):** Neither `valicherla2022_pk` nor `tshikudi2024_colitis` describe baseline estrous staging or longitudinal phase monitoring in female rodents (`estrous_monitored_outcome: no`, `estrous_baseline_staged: no`).
- **(b) Full-text longitudinal monitoring without baseline staging (1 study):** In `singh2020_heliyon`, estrous monitoring is confirmed present (`estrous_monitored_outcome: yes`) via daily vaginal cytology (Section 2.3) as a longitudinal recovery endpoint; baseline staging prior to treatment assignment was not conducted (`estrous_baseline_staged: no`).
- **(c) Abstract-only reporting in paywalled / abstract studies (4 studies):** In `yadav2024_pcos_let` and `yadav2025_pcos_dhea`, abstracts report longitudinal estrous cycle improvement (`estrous_monitored_outcome: yes (abstract-only)`), but baseline pre-treatment staging is not reported (`estrous_baseline_staged: not_reported (abstract-only)`). In `singh2019_menopause`, both fields are `not_reported (abstract-only)`. In `tshikudi2024_jcag`, estrous monitoring is unmentioned (`estrous_monitored_outcome: no (abstract-only)`, `estrous_baseline_staged: not_reported (abstract-only)`).

### Gap 4: Independent Replication of Colonic Epithelial Findings
*Scope:* Colitis and mucosal barrier maintenance (`tshikudi2024_colitis`, `tshikudi2024_jcag`).
- **(a) Confirmed absent in papers read (2 studies):** Both studies originate from a single research team (Jean-Eric Ghia laboratory, University of Manitoba). Independent replication in an external laboratory is absent across all read papers.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (0 studies):** Both studies have accessible text.

### Gap 5: Pharmacokinetics in Diseased or Chronically Dosed States Across Sexes
*Scope:* Pharmacokinetic profiling (`valicherla2020_jpba`, `valicherla2022_pk`).
- **(a) Confirmed absent in papers read (1 study):** In `valicherla2022_pk`, PK comparisons across sexes were evaluated exclusively in healthy, young Sprague Dawley rats following single doses; evaluation in diseased or chronically treated animals is confirmed absent.
- **(b) Unreported in papers read (0 studies).**
- **(c) Cannot assess because NOT_READ (1 study):** In `valicherla2020_jpba`, single-dose mouse PK was performed, but animal sex is paywalled.

---

## 4. What the Evidence Table Supports and What It Does Not

### What the Table Supports
1. **Reporting Practices Across Available Literature:** In the 5 fully read papers, sex was reported clearly in methods. In 2 studies (`valicherla2018`, `singh2020_fetuina`), females were confirmed absent. In 1 study (`singh2020_heliyon`), males were confirmed absent due to the female-specific perimenopause model. In 2 studies (`valicherla2022_pk`, `tshikudi2024_colitis`), both sexes were included. In 1 published abstract supplement (`tshikudi2024_jcag`), both sexes were included.
2. **Documented Findings in Colitis and Mucosal Homeostasis:** In the two studies testing both sexes (`tshikudi2024_colitis`, `tshikudi2024_jcag`), sex differences were observed descriptively in epithelial markers and daily disease activity, alongside non-significant differences on cumulative DAI sum and macroscopic damage scores.
3. **Pervasive Paywall Uncertainty:** Exactly 10 of 20 studies (50.0%) omit sex from their abstracts, demonstrating that literature syntheses cannot determine preclinical sex inclusion without full-text access.

### What the Table Does NOT Support
1. **No Conclusions Regarding PSTi8 Efficacy or Safety:** The evidence table documents methodological and reporting characteristics; it does not evaluate, confirm, or dispute the clinical safety, efficacy, or therapeutic index of PSTi8.
2. **No Generalization Across Paywalled Literature:** Missing data fields labeled `NOT_READ` represent access restrictions, not confirmed absence of data in original manuscripts.
3. **No Characterization of Colitis Findings as Divergent Protection vs Exacerbation:** Because cumulative and macroscopic endpoints were not significantly different and interaction statistics were not reported, the data do not support claims of polarized male-protective versus female-harmful systemic drug actions.
