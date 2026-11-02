---
topic_id: "05"
title: "Factorial Interaction Power, The Subgroup Fallacy, and Preclinical Reporting Standards"
date: "2026-11-02"
author: "Antigravity (Gemini 3.8 Flash High)"
status: "verified"
tags:
  - "statistical_power"
  - "factorial_interaction"
  - "arrive_20"
  - "syrcle_risk_of_bias"
  - "topic_5_synthesis"
---

# Topic 05: Factorial Interaction Power, The Subgroup Fallacy, and Preclinical Reporting Standards

## 1. Executive Overview

Rigorous evaluation of therapeutic candidates requires adherence to established methodological reporting guidelines—specifically the **ARRIVE 2.0 Essential 10** guidelines and the **SYRCLE Risk of Bias** tool—alongside adequate statistical power to detect treatment effects. When evaluating biological sex as an experimental variable, researchers frequently commit the "subgroup fallacy": testing both sexes by splitting standard sample cohorts into male and female arms without increasing sample sizes, followed by separate within-sex significance testing.

This document synthesizes the methodological quality appraisal across the 20 primary PSTi8 studies and presents the formal statistical power modeling derived from the non-central t-distribution (detailed in [`docs/power_analysis.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/power_analysis.md) and [`data/power_results.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/power_results.csv)).

---

## 2. Methodological Quality Appraisal (ARRIVE 2.0 & SYRCLE)

A comprehensive audit of the 20 primary in vivo studies reveals widespread reporting deficiencies across core ARRIVE 2.0 domains:

```
+----------------------------------------------------------------------------------------------------+
|                                    ARRIVE 2.0 REPORTING COMPLIANCE                                  |
+------------------------------+---------------------------+-----------------------------------------+
| Quality Domain               | Reporting Compliance (%)  | Common Evidentiary Finding              |
+------------------------------+---------------------------+-----------------------------------------+
| Random Allocation Method     | 25.0% (5 of 20 studies)   | Generic phrase ("randomly divided")     |
| Allocation Concealment       | 0.0% (0 of 20 studies)    | Completely absent across all studies    |
| Blinding of Experimenters    | 0.0% (0 of 20 studies)    | Not reported in any study               |
| Blinding of Outcome Assessors| 5.0% (1 of 20 studies)    | Reported only in tshikudi2024_colitis   |
| Sample Size Calculation      | 0.0% (0 of 20 studies)    | Zero a priori power calculations        |
| Defined Primary Endpoint     | 30.0% (6 of 20 studies)   | Multiple testing without multiplicity   |
+------------------------------+---------------------------+-----------------------------------------+
```

### Critical Reporting Omissions
1. **Selection Bias (SYRCLE Domain 1 & 2):** While several papers state that animals were "randomly assigned," none described the randomization method (e.g., computer-generated numbers, block randomization) or whether allocation was concealed from handlers.
2. **Detection & Performance Bias (SYRCLE Domain 3 & 4):** Blinding during drug administration and routine care was entirely unreported. Only `tshikudi2024_colitis` explicitly noted that histological damage was "scored in a blinded manner."
3. **Multiplicity and Multiple Comparisons:** Across metabolic studies, dozens of biochemical parameters (glucose, insulin, lipids, cytokines, enzyme activities) were tested using individual Student's t-tests or ANOVA post-hoc tests without formal family-wise error rate (FWER) or false discovery rate (FDR) corrections [Inference].

---

## 3. The Fallacy of Post-Hoc Subgroup Splitting

In preclinical pharmacology, a common error when addressing the NIH SABV mandate is testing both sexes by splitting a planned cohort (e.g., total $N = 12$) into $n = 6$ males and $n = 6$ females. Researchers then run separate statistical tests within each sex:
- If males show $p < 0.05$ and females show $p > 0.05$, authors routinely conclude that the drug "works selectively in males."
- **The Statistical Fallacy:** A difference in significance levels does not establish a significant difference between groups ($p_1 < 0.05$ and $p_2 > 0.05$ does **not** imply that $\text{Effect}_1 \neq \text{Effect}_2$).
- To claim a sex-dependent drug effect, researchers must formally test the **Sex $\times$ Treatment interaction contrast**:
  $$L = (\mu_{\text{Male, Treated}} - \mu_{\text{Male, Vehicle}}) - (\mu_{\text{Female, Treated}} - \mu_{\text{Female, Vehicle}})$$
- Across the entire 20-study PSTi8 corpus, **zero studies (0.0%) published this interaction test statistic**.

---

## 4. Factorial Interaction Power Modeling

To establish the statistical viability of detecting sex differences in preclinical peptide studies, 33 sensitivity scenarios were modeled using the exact non-central Student's t-distribution:
$$t = \frac{\hat{L}}{\text{SE}_L} \sim t(\text{df} = 4(n-1), \delta = \frac{L}{\sigma \sqrt{4/n}})$$

```
+----------------------------------------------------------------------------------------------------+
|                                    FACTORIAL INTERACTION POWER                                      |
+--------------------------+---------------------+-------------------+-------------------------------+
| Standardized Effect Size | Sample Size per Cell| Total Animals (4G)| Statistical Power Achieved    |
| ($L / \sigma$)           | ($n$)               | ($N$)             | (Two-Sided, alpha = 0.05)     |
+--------------------------+---------------------+-------------------+-------------------------------+
| Large (L/sigma = 1.5)    | n = 6               | N = 24            | 41.2% (Underpowered)          |
| Moderate (L/sigma = 1.0) | n = 6               | N = 24            | 18.7% (Severely Underpowered) |
| Subtle (L/sigma = 0.5)   | n = 6               | N = 24            | 7.8% (Near Random Noise)      |
+--------------------------+---------------------+-------------------+-------------------------------+
| Moderate (L/sigma = 1.0) | n = 16              | N = 64            | 50.8%                         |
| Moderate (L/sigma = 1.0) | n = 32              | N = 128           | 81.3% (Adequately Powered)    |
| Subtle (L/sigma = 0.5)   | n = 127             | N = 508           | 80.3% (Adequately Powered)    |
+--------------------------+---------------------+-------------------+-------------------------------+
```

### Essential Takeaways for Phase 2
1. **The Fourfold Sample Multiplier:** Detecting an interaction contrast requires roughly **four times the per-group sample size** ($4 \times$) necessary to detect a main treatment effect of the same magnitude.
2. **High Type II Error in Standard Cohorts:** In conventional preclinical cohorts ($n = 6$ per group), statistical power to detect a genuine moderate interaction is **under 19%**. Over 80% of true sex-specific treatment differences will be missed entirely.
3. **The "Winner's Curse":** Nominally significant interactions discovered in small samples ($n \le 6$) inevitably suffer from massive effect size inflation.
4. **Actionable Recommendation:** Future preclinical studies evaluating sex differences in granin inhibitors must either design factorial interaction cohorts with $n \ge 16\text{--}32$ per cell, or pool data across collaborative multi-center consortia.
