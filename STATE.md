# STATE.md — Project Status

**Last Updated:** 2026-10-28 (Updated)  
**Vault:** `psti8-sex-bias-review`

---

## 1. Project Phase & Execution Status

All primary phases (Scaffold, Step 2 extraction, and Tasks A, B, C) are **complete**.

- [x] **Step 1 — Vault Scaffold:** Directory hierarchy, `AGENTS.md`, `CLAUDE.md`, `docs/schema.md`, `sources/study_guide.md`, `docs/decisions/`.
- [x] **Step 2 — Data Extraction & Note Authoring:**
  - [x] Populated [data/evidence_table.csv](data/evidence_table.csv) with all 11 published PSTi8 studies across 20 standardized schema columns.
  - [x] Created all 11 individual markdown files in [notes/papers/](notes/papers/) with YAML frontmatter, locators, and access tags.
- [x] **Task A — Sex-Coverage Audit:**
  - [x] Authored [docs/audit_report.md](docs/audit_report.md) with disease-by-sex matrix, two-sex study breakdown, list of unreported/`NOT_READ` studies, and explicit boundary statements.
  - [x] Classified evidence gaps into (a) confirmed absent, (b) unreported, and (c) cannot assess because NOT_READ, with exact counts.
- [x] **Task B — Statistical Power Analysis:**
  - [x] Documented extraction and derivation of $L$ and $\sigma$ from Figure 1 of Tshikudi et al. (2024).
  - [x] Addressed error bar ambiguity: modeled both direct SD ($\sigma \in [0.8, 1.0]$) and converted SEM-to-SD ($\sigma \in [1.4, 1.8]$).
  - [x] Modeled interaction contrast as an estimate range ($L \in [0.5, 4.5]$) in [scripts/power_analysis.py](scripts/power_analysis.py).
  - [x] Exported 18 sensitivity scenarios to [data/power_results.csv](data/power_results.csv) and authored synthesis in [docs/power_analysis.md](docs/power_analysis.md).
- [x] **Task C — Verification Protocol & Handoff:**
  - [x] Generated [docs/spot_check_list.md](docs/spot_check_list.md) with 10 randomly sampled table rows for audit.
  - [x] Updated [INDEX.md](INDEX.md) and [STATE.md](STATE.md).
  - [x] Added "Papers to Obtain" list resolving paywalled `NOT_READ` fields.

---

## 2. Five Biggest Evidence Gaps in Published PSTi8 Literature

Every evidence-gap statement is categorized by evidentiary status:
*(a) confirmed absent in papers read; (b) unreported in papers read; (c) cannot assess because NOT_READ.*

1. **Female Representation in General Cardiometabolic & Diabetic Studies (Total: 5 studies):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2018`, methods explicitly state only male C57BL/6J, male db/db, and male SD rats were used across all three diabetic models and PK cohorts.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (4 studies):* `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, and `dadge2023_nash` are paywalled; their abstracts do not report whether female animals were included.
2. **Formal Testing of Sex × Treatment Interaction ($p_{\text{sex} \times \text{treatment}}$) (Total: 2 studies with both sexes):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2022_pk`, sex differences were evaluated using descriptive summaries and pairwise t-tests; no factorial interaction test was conducted.
   - *(b) Unreported in papers read (1 study):* In `tshikudi2024_colitis`, two-way ANOVA is specified in Section 4.9, but the omnibus interaction test statistic ($F$, df, $p_{\text{sex} \times \text{treatment}}$) is unreported; only within-sex pairwise post-hocs are presented.
   - *(c) Cannot assess because NOT_READ (0 studies):* Both studies evaluating both sexes were read in full.
3. **Baseline Estrous Cycle Staging and Phase Control (Total: 6 studies using female animals):**
   - *(a) Confirmed absent in papers read (2 studies):* In `valicherla2022_pk` and `tshikudi2024_colitis`, female animals were utilized, but neither methods section describes estrous cycle staging, phase monitoring, or baseline synchronization.
   - *(b) Unreported in papers read (0 studies):* In `singh2020_heliyon`, estrous monitoring is confirmed present via daily vaginal cytology, but was monitored longitudinally as an outcome (confirming perimenopause induction and cycle recovery) rather than used to stage animals prior to treatment.
   - *(c) Cannot assess because NOT_READ (3 studies):* `singh2019_menopause`, `yadav2024_pcos_let`, and `yadav2025_pcos_dhea` are paywalled; baseline staging cannot be determined from abstracts.
4. **Replication of Sex Divergence in Secondary Organ Systems (Total: 1 study):**
   - *(a) Confirmed absent in papers read (1 study):* Independent replication of the sex-divergent colonic epithelial response to PSTi8 is absent across all read papers.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (0 studies):* `tshikudi2024_colitis` was read in full.
   - *Colitis phenotype description:* In `tshikudi2024_colitis`, PSTi8 significantly elevated daily Disease Activity Index (DAI) scores in colitic females compared to vehicle controls at 72 h and 96 h ($p < 0.05$). However, when evaluating the cumulative Disease Activity Index (sum of DAI) and macroscopic damage scores (macro-scores), the paper reports a **non-significant difference** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice. In colitic males, PSTi8 delayed the onset of DAI elevation (from 24 h to 48 h) and preserved stem cells and differentiated colonic epithelial cells.
5. **Sex-Comparative Pharmacokinetics in Diseased or Chronically Treated Animals (Total: 1 study):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2022_pk`, PK parameters were compared across sexes only after single doses in healthy young Sprague Dawley rats; PK profiling under chronic dosing or diseased states is confirmed absent.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (0 studies):* Full text was read.

---

## 3. Three Weakest Points of this Analysis

1. **Information Incompleteness Driven by Paywalled Literature (`NOT_READ` Prevalence):**  
   54.5% (6 of 11) of the studies are behind Elsevier/ASPET paywalls. Following AGENTS.md Rule 1 ("never guess or fill from memory"), unverified details (e.g., exact $n$, dose, explicit animal sex) are coded strictly as `NOT_READ`.
2. **Reliance on Visual Estimation for Quantitative Parameters in Task B:**  
   In `tshikudi2024_colitis`, DAI values and variability measures are published solely as graphical bar and line charts in Figure 1, with no numerical tables or reported effect sizes ($d$, $\eta^2$). The baseline interaction contrasts ($L$) are approximations derived from graphs.
3. **Unavailability of Raw Omnibus Interaction Statistics:**  
   Primary literature did not report the $F_{\text{sex} \times \text{treatment}}$ statistic or MSE, requiring the power model to reconstruct contrasts from sample means rather than from empirical model error terms.

---

## 4. Papers to Obtain (Resolving `NOT_READ` Fields)

Obtaining full text for the following paywalled manuscripts will resolve the indicated missing data fields in [data/evidence_table.csv](data/evidence_table.csv):

| # | Paper ID | Citation & DOI | What Obtaining Full Text Resolves |
|---|---|---|---|
| 1 | `gupta2019_obesity` | Gupta et al., *Eur J Pharmacol* 2019<br>DOI: [10.1016/j.ejphar.2019.172723](https://doi.org/10.1016/j.ejphar.2019.172723) | • Confirm whether animals were exclusively male (only reported in secondary summaries)<br>• Extract exact sample size per group ($n$)<br>• Extract PSTi8 dose, administration route, and vehicle |
| 2 | `singh2019_menopause` | Valicherla/Singh et al., *Peptides* 2019<br>DOI: [10.1016/j.peptides.2019.170147](https://doi.org/10.1016/j.peptides.2019.170147) | • Clarify first-author citation attribution (Valicherla GR vs Singh)<br>• Determine whether estrous cycles were staged at baseline before OVX/VCD<br>• Extract sample size per group ($n$), PSTi8 dose, route, and chronic duration |
| 3 | `gupta2020_skeletal` | Gupta et al., *Eur J Pharmacol* 2020<br>DOI: [10.1016/j.ejphar.2020.173204](https://doi.org/10.1016/j.ejphar.2020.173204) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Extract group sample sizes ($n$), PSTi8 dose, and route in HFD+STZ mice<br>• Check whether female mice were included or discussed |
| 4 | `reza2022_lfs` | Reza et al., *Life Sci* 2022<br>DOI: [10.1016/j.lfs.2021.120221](https://doi.org/10.1016/j.lfs.2021.120221) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Extract in vivo group sizes ($n$), route of administration, and treatment schedule<br>• Check whether sex differences were evaluated in hepatic FFA stress |
| 5 | `dadge2023_nash` | Goand et al. (Dadge et al.), *Cytokine* 2023<br>DOI: [10.1016/j.cyto.2023.156354](https://doi.org/10.1016/j.cyto.2023.156354) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Confirm first-author attribution (Goand UK vs Dadge)<br>• Extract sample sizes per group ($n$), route, dose, and duration in MCD diet-induced NASH |
| 6 | `yadav2024_pcos_let` | Yadav et al., *Steroids* 2024<br>DOI: [10.1016/j.steroids.2024.109558](https://doi.org/10.1016/j.steroids.2024.109558) | • Confirm exact rat strain<br>• Extract sample size per group ($n$), PSTi8 dose, and route of administration<br>• Determine whether estrous cycles were staged at baseline prior to letrozole induction |
| * | `yadav2025_pcos_dhea` | Yadav et al., *JPET* 2025<br>DOI: [10.1016/j.jpet.2025.103765](https://doi.org/10.1016/j.jpet.2025.103765) | • Confirm exact rat strain<br>• Extract sample size per group ($n$) and route of administration<br>• Verify baseline estrous staging protocols |
