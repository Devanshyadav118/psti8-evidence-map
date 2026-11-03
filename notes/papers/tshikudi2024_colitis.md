---
paper_id: tshikudi2024_colitis
doi: 10.3390/ijms252312757
access: full
last_updated: 2026-10-28
status: complete
---

# Tshikudi et al. 2024 — Colitis, Sex-Dependent CEC Profile

**Citation:** Tshikudi, Hutchison & Ghia, Int J Mol Sci, 2024  
**DOI:** [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757)  
**Access:** Full (MDPI open access)

## Study Design

- **Species/strain:** Mouse / C57BL/6 (Section 4.1, "Animals")
- **Sex:** Both male and female (Section 4.1)
- **n per group:** n=5–6 per sex per condition for tissue/cellular assays; n=12–15 per sex for DAI and body weight cohorts (Section 4.1, 4.11; figure legends)
- **Disease model:** DSS-induced acute colitis (5% DSS, 5 days) + steady-state homeostasis (Section 4.2)
- **Route:** Intrarectal (Section 4.3)
- **Dose:** 10 µg per mouse (~2.5 mg/kg), daily (Section 4.3)
- **Duration:** 7 days, Day 0–6 (Section 4.2–4.3; Fig 1A)

## Sex & Estrous

- **Estrous controlled:** NOT_READ — not described in Methods
- **Sex analyzed as variable:** yes — all data presented separately by sex with within-sex comparisons (Sections 2.1–2.5; Figs 1–8)
- **Interaction tested:** no (confirmed absent) — Section 4.11 specifies one-way ANOVA; no factorial Sex x Treatment interaction test was performed or reported anywhere in the paper

## Statistics

- Section 4.11 ("Statistical Analysis"): *"One-way ANOVA followed by Bonferroni or Tukey-post hoc analysis was performed"* to calculate significance.
- Figures 1–8: Ordinary one-way ANOVA with Tukey's post-hoc tests between individual group averages. Two-way ANOVA is mentioned only in Figure 1 and 7 captions for longitudinal time-courses (DAI/weight loss across days) and gene marker arrays. No two-way ANOVA evaluating a Sex x Treatment interaction was performed. Data reported as mean ± SD.

## Key Findings

- **Endpoints:** Daily DAI score, cumulative sum of DAI, macroscopic damage score (macro-score: diarrhea, bleeding, prolapse), colon length, histology score, colonic epithelial cell (CEC) differentiation/stem markers (Lgr5, Muc2, ChgA, lysozyme), cytokines (TNF-α, IL-6, IL-1β, IFN-γ, IL-17A, IL-10, IL-22), Ki67, cleaved caspase-3 (Figs 1–8)
- **Result:** In colitic female mice, PSTi8 elevated daily DAI scores at 72 h and 96 h (p < 0.05), altered CEC lineage allocation, and increased apoptosis. However, cumulative sum of DAI and macroscopic damage scores showed a **non-significant difference** between PSTi8-treated females and PBS controls, and between PSTi8-treated males and females. In colitic male mice, PSTi8 delayed colitis onset (DAI elevation shifted from 24 h to 48 h) and preserved stem cells and differentiated CECs (Abstract, Section 2.1, Section 3).

## DAI Data (Figure Estimates for Power Analysis)

> **WARNING:** Values below are visual estimates from Figure 1 plots. No numerical tables of means and SDs are provided in the main text or supplement.

- **Error bar definition:** Section 4.11 explicitly states *"Data were expressed as the mean ± standard deviation (S.D.)."* Therefore, graphical error bars reflect sample SD directly (residual $\sigma \approx 0.8\text{--}1.0$). If error bars are alternatively assumed to be SEM with $n=6$, $\sigma \approx \text{SEM} \times \sqrt{6} \approx 1.2\text{--}1.8$.
- **Estimated Group Levels (DSS condition, peak/cumulative):**
  - Male + Vehicle: Mean DAI $\approx 7.0\text{--}7.5$
  - Male + PSTi8: Mean DAI $\approx 5.0\text{--}5.5$ ($\Delta_M \approx -1.5\text{ to } -2.5$)
  - Female + Vehicle: Mean DAI $\approx 5.5\text{--}6.5$
  - Female + PSTi8: Mean DAI $\approx 7.5\text{--}8.5$ ($\Delta_F \approx +1.0\text{ to } +2.0$)
- **Estimated Interaction Contrast Range:** $L = \Delta_F - \Delta_M \in [2.5, 4.5]\text{ DAI units}$ (down to $L \in [0.5, 1.5]$ for cumulative sum / macro-scores where differences were non-significant).

## Notes

Only known primary PSTi8 study to include both sexes in an in vivo disease model. The authors performed separate analyses within each sex by ordinary one-way ANOVA rather than an omnibus factorial interaction test. Estrous staging was not reported. Cumulative macroscopic damage scores did not reach statistical significance between sexes.

See [evidence table](../data/evidence_table.csv) | [schema](../docs/schema.md)
