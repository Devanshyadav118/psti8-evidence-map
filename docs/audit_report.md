# Sex-Coverage Audit Report: Published PSTi8 Literature

**Audit Date:** 2026-10-28  
**Scope:** 11 published preclinical studies investigating PSTi8 (pancreastatin inhibitor peptide, PEGKGEQEHSQQKEEEEEMAV-NH₂) catalogued in [data/evidence_table.csv](../data/evidence_table.csv).

---

## 1. Study Coverage Matrix

The matrix below groups the 11 catalogued studies by disease model / biological indication against the biological sex of animal subjects utilized:

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

---

## 2. In-Depth Analysis of Studies Including Both Sexes

Only **two studies** (18.2% of the corpus) included both male and female animals:

### A. Valicherla et al., 2022 (*Molecules*, DOI: [10.3390/molecules27020339](https://doi.org/10.3390/molecules27020339))
- **Objective:** Pharmacokinetic characterization in healthy Sprague Dawley rats across IV, IP, and SC routes.
- **Sample size:** n = 3–6 per sex per route.
- **Sex analyzed as a variable?** **Yes.** PK parameters (Cmax, AUC, t1/2, CL, Vd) were calculated and tabulated separately for males and females (Tables 4 and 5).
- **Sex × Treatment interaction tested?** **No.** The study evaluated single doses in healthy animals. Male and female pharmacokinetic parameters were compared pairwise/descriptively, with the authors reporting no statistically significant sex differences. No factorial interaction test was conducted or reported.

### B. Tshikudi et al., 2024 (*Int J Mol Sci*, DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))
- **Objective:** Therapeutic evaluation of intrarectal PSTi8 in dextran sodium sulfate (DSS)-induced colitis and steady-state epithelial maintenance in C57BL/6 mice.
- **Sample size:** n = 5–6 per sex per experimental arm for histology/cellular assays; n = 12–15 per sex for Disease Activity Index (DAI) cohorts.
- **Sex analyzed as a variable?** **Yes.** All primary endpoints (DAI, histology, cytokines, stem-cell and epithelial differentiation markers) were stratified by sex. Strikingly divergent responses were observed: PSTi8 reduced disease severity in males but exacerbated disease activity and altered epithelial lineages in females.
- **Sex × Treatment interaction tested?** **NOT_READ / Ambiguous.** While two-way analysis of variance (ANOVA) was specified in Section 4.9 ("Statistical Analysis"), the paper reports within-sex pairwise post-hoc contrasts (Tukey's tests) rather than providing the omnibus interaction F-statistic, degrees of freedom, or interaction p-value ($p_{\text{sex} \times \text{treatment}}$).

---

## 3. Unreported or NOT_READ Status

Per the project rules, paywalled studies without accessible full-text methods or explicit statements in abstracts are not guessed.

### Studies where Animal Sex is NOT_READ / Unreported
1. **`gupta2020_skeletal`** (Gupta et al., *Eur J Pharmacol*, 2020): Abstract states "mice" without specifying sex. Paywalled.
2. **`reza2022_lfs`** (Reza et al., *Life Sci*, 2022): Abstract states "C57BL/6J mice" without specifying sex. Paywalled.
3. **`dadge2023_nash`** (Goand/Dadge et al., *Cytokine*, 2023): Abstract states "mice" without specifying sex. Paywalled.

### Studies where Estrous Cycle Control is NOT_READ or Unreported
Among the 6 studies utilizing female animals (4 female-only, 2 both sexes):
1. **`singh2019_menopause`**: NOT_READ (abstract does not confirm vaginal cytology or synchronization).
2. **`valicherla2022_pk`**: NOT_READ (no staging or phase synchronization reported in female rats during PK profiling).
3. **`tshikudi2024_colitis`**: NOT_READ (methods describe intact adult females, but make no mention of estrous staging, cytology, or controlling for hormonal fluctuations during DSS colitis induction).
4. *Controlled/monitored subset:* In `singh2020_heliyon`, `yadav2024_pcos_let`, and `yadav2025_pcos_dhea`, estrous cyclicity was tracked via vaginal cytology primarily as a disease-validation or outcome endpoint (cessation/disruption of regular cycles and subsequent restoration), rather than used to stage animals at baseline prior to treatment.

---

## 4. What the Evidence Table Supports and What It Does Not

### What the Table Supports
1. **Pervasive Sex Segregation by Disease Indication:** In preclinical PSTi8 studies, biological sex is strictly compartmentalized:
   - General metabolic and diabetic indications (T2D, obesity, insulin resistance) have historically been evaluated exclusively in male rodents or in cohorts with unreported sex.
   - Female rodents have been investigated exclusively in models of female-specific endocrine conditions (perimenopause, PCOS).
2. **Scarcity of Bidirectional Sex-Comparative Designs:** Only 1 of 10 disease-efficacy studies (`tshikudi2024_colitis`) tested PSTi8 in both sexes within the same experimental framework.
3. **Documented Risk of Unmeasured Sex Divergence:** The only published study comparing both sexes in a non-reproductive disease model (`tshikudi2024_colitis`) revealed diametrically opposed phenotypic outcomes (protection in males vs. exacerbation in females), demonstrating that male-only findings cannot be assumed to extrapolate to females.

### What the Table Does NOT Support
1. **No Conclusions Regarding Efficacy or Safety:** This evidence table does not evaluate, confirm, or disprove the therapeutic efficacy, potency, or clinical safety of PSTi8 in any indication.
2. **No Generalization Across Paywalled Literature:** Missing fields labeled `NOT_READ` reflect access constraints, not verified absence of data in the original full-text manuscripts.
