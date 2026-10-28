# STATE.md — Project Status

**Last Updated:** 2026-10-28  
**Vault:** `psti8-sex-bias-review`

---

## 1. Project Phase & Execution Status

All primary phases (Scaffold, Step 2 extraction, and Tasks A, B, C) are **complete**.

- [x] **Step 1 — Vault Scaffold:** Directory hierarchy, `AGENTS.md`, `CLAUDE.md`, `docs/schema.md`, `sources/study_guide.md`, `docs/decisions/`.
- [x] **Step 2 — Data Extraction & Note Authoring:**
  - [x] Populated [data/evidence_table.csv](data/evidence_table.csv) with all 11 published PSTi8 studies across 20 standardized schema columns.
  - [x] Created all 11 individual markdown files in [notes/papers/](notes/papers/) with YAML frontmatter, locators, and access tags.
- [x] **Task A — Sex-Coverage Audit:** Authored [docs/audit_report.md](docs/audit_report.md) with disease-by-sex matrix, two-sex study breakdown, list of unreported/`NOT_READ` studies, and explicit scope boundaries.
- [x] **Task B — Statistical Power Analysis:**
  - [x] Extracted/estimated DAI parameters from Tshikudi et al. 2024 (labeled as figure-derived estimates).
  - [x] Implemented standalone simulation script [scripts/power_analysis.py](scripts/power_analysis.py).
  - [x] Exported sensitivity matrix to [data/power_results.csv](data/power_results.csv).
  - [x] Authored synthesis report [docs/power_analysis.md](docs/power_analysis.md) highlighting the variance expansion of interaction tests.
- [x] **Task C — Verification Protocol & Handoff:**
  - [x] Generated [docs/spot_check_list.md](docs/spot_check_list.md) with 10 randomly sampled table rows for audit.
  - [x] Updated [INDEX.md](INDEX.md) and [STATE.md](STATE.md).
  - [x] Documented the 3 weakest points of the analysis and top 5 evidence gaps below.

---

## 2. Five Biggest Gaps in the Published PSTi8 Literature

1. **Systematic Exclusion of Female Subjects in Cardiometabolic & Diabetic Efficacy:**
   Every published study evaluating PSTi8 for its primary indication (Type 2 diabetes, insulin resistance, diet-induced obesity) was conducted exclusively in male rodents or did not report animal sex. There is zero published preclinical evidence assessing whether PSTi8 restores glucose homeostasis or insulin sensitivity in female models of general T2D.
2. **Absence of Formal Interaction Testing ($p_{\text{sex} \times \text{treatment}}$):**
   Even in the two studies that included both sexes (`valicherla2022_pk` and `tshikudi2024_colitis`), neither paper published the omnibus interaction F-statistic, degrees of freedom, or interaction p-value. Preclinical studies treat biological sex as an isolated subgrouping filter rather than evaluating moderation within a factorial model.
3. **Omission of Baseline Estrous Cycle Staging and Hormonal Control:**
   In intact female cohorts, estrous cyclicity was either monitored purely as an end-of-study outcome (e.g., confirming perimenopause or PCOS induction) or completely omitted (`tshikudi2024_colitis`, `valicherla2022_pk`). No study staged female animals at baseline to control for cycling estrous phases during drug administration.
4. **Unreplicated Sex-Divergent Toxicity / Liability in Inflammatory Models:**
   The finding that intrarectal PSTi8 aggravated colitis in females while protecting males (`tshikudi2024_colitis`) demonstrates a profound sex-dependent divergence. This adverse vulnerability has never been independently replicated, investigated for underlying hormonal mechanisms (e.g., estrogen receptor interaction), or evaluated in systemic inflammatory states.
5. **No Evaluation of Pharmacokinetics Under Diseased or Chronic Conditions Across Sexes:**
   Sex-comparative PK was assessed solely after a single dose in healthy, young Sprague Dawley rats (`valicherla2022_pk`). Whether chronic dosing, metabolic endotoxemia, altered liver enzyme function, or altered plasma protein binding in disease states leads to sex-differentiated clearance or accumulation is unknown.

---

## 3. Three Weakest Points of this Analysis

1. **Information Incompleteness Driven by Paywalled Literature (`NOT_READ` Prevalence):**
   Six of the 11 catalogued papers (54.5%) are paywalled (Elsevier/ASPET). In accordance with AGENTS.md Rule 1 ("never fill from memory or guess"), critical parameters—such as exact group sizes ($n$), dosing regimens, and explicit confirmation of animal sex—had to be recorded as `NOT_READ`, limiting inferential coverage for these studies.
2. **Reliance on Visual Estimation for Key Quantitative Parameters in Task B:**
   In `tshikudi2024_colitis`, DAI values and variability measures are published solely as graphical bar and line charts in Figure 1, with no numerical tables or effect sizes reported. The baseline interaction contrast ($L = 4.5$) and variance ($\sigma \approx 1.4$) used for power calculations are visual approximations.
3. **Unavailability of Raw Omnibus Interaction Statistics:**
   Because primary studies did not publish the ANOVA interaction F-statistics or mean square error (MSE) terms, the power analysis had to reconstruct the interaction contrast using estimated group means rather than empirically verified error terms from the published statistical models.

---

## 4. Next Steps & Recommended Actions

- [ ] Run user audit using [docs/spot_check_list.md](docs/spot_check_list.md) against primary PDFs.
- [ ] If institutional full-text access for the 6 paywalled papers is provided into `sources/`, update `notes/papers/*.md` and replace `NOT_READ` cells in `data/evidence_table.csv`.
