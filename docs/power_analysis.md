# Statistical Power Analysis for Sex × Treatment Interaction in PSTi8 Colitis Models

**Date:** 2026-10-28  
**Reference Study:** Tshikudi et al., *Int J Mol Sci* 2024; 25(23):12757 (DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))  
**Analysis Script:** [scripts/power_analysis.py](../scripts/power_analysis.py)  
**Output Dataset:** [data/power_results.csv](../data/power_results.csv)

---

## 1. Extracted Data & Visual Estimates (Tshikudi et al. 2024)

### Locator
- **Figure 1A:** Disease Activity Index (DAI) daily score progression curves over 6 days of DSS colitis.
- **Figure 1C & 1D:** Cumulative DAI score sum and macroscopic colon damage scores presented as bar charts with error bars (mean ± SD).
- **Methods (Section 4.1 & 4.9):** Animal cohorts of $n = 5\text{--}6$ per group for cellular/tissue endpoints, and larger cohorts ($n = 12\text{--}15$ per group) for daily clinical scoring of DAI and weight loss.

> [!WARNING]
> **Reporting Status — Figure-Derived Estimates:**
> The authors report DAI results exclusively as graphical bar and line plots in Figure 1. No exact numerical table of means, standard deviations (SD), or standard errors (SEM) for daily or cumulative DAI is provided in the main text or supplementary material. The values below are **visual estimates from Figure 1**, not verified numerical facts.

### Visual Estimates (Day 6 / Cumulative DAI)
Under 5% dextran sodium sulfate (DSS) challenge:
- **Male + Vehicle (PBS):** Estimated Mean DAI $\approx 7.5$ (SEM $\approx 0.5$, estimated $\text{SD} \approx 1.2\text{--}1.4$)
- **Male + PSTi8 (10 µg/mouse):** Estimated Mean DAI $\approx 5.0$ (SEM $\approx 0.5$, estimated $\text{SD} \approx 1.2\text{--}1.4$)
  - *Within-male treatment effect:* $\Delta_{\text{male}} = 5.0 - 7.5 = -2.5$ (therapeutic improvement / reduced DAI)
- **Female + Vehicle (PBS):** Estimated Mean DAI $\approx 6.0$ (SEM $\approx 0.5$, estimated $\text{SD} \approx 1.2\text{--}1.4$)
- **Female + PSTi8 (10 µg/mouse):** Estimated Mean DAI $\approx 8.0$ (SEM $\approx 0.8$, estimated $\text{SD} \approx 1.6\text{--}1.8$)
  - *Within-female treatment effect:* $\Delta_{\text{female}} = 8.0 - 6.0 = +2.0$ (disease exacerbation / increased DAI)

### Estimated Interaction Contrast
In a $2 \times 2$ factorial framework (Sex: Male/Female $\times$ Treatment: Vehicle/PSTi8):
$$\Delta_{\text{interaction}} = L = (\mu_{F,\text{PSTi8}} - \mu_{F,\text{Veh}}) - (\mu_{M,\text{PSTi8}} - \mu_{M,\text{Veh}}) = (+2.0) - (-2.5) = +4.5\text{ DAI units}$$
- **Pooled standard deviation ($\sigma$):** $\approx 1.4\text{ DAI units}$ (sensitivity range tested: $1.0\text{--}2.0$).
- **Standardized interaction effect size ($L / \sigma$):** $\approx 3.21$ (representing a profound qualitative crossover interaction).
- **Reported effect sizes:** The original paper does not report Cohen's $d$, partial $\eta^2$, or formal interaction degrees of freedom.

---

## 2. Power Modeling & Sample Size Sensitivity

Statistical power to detect the interaction contrast $L$ at two-tailed $\alpha = 0.05$ with target power $1 - \beta = 0.80$ was modeled using [scripts/power_analysis.py](../scripts/power_analysis.py).

$$\text{SE}_L = \sigma \sqrt{\frac{1}{n} + \frac{1}{n} + \frac{1}{n} + \frac{1}{n}} = \sigma \sqrt{\frac{4}{n}} = \frac{2\sigma}{\sqrt{n}}$$

$$n_{\text{per group}} = \left\lceil \frac{4\sigma^2 (z_{1 - \alpha/2} + z_{1 - \beta})^2}{L^2} \right\rceil$$

### Sensitivity Scenarios (from `data/power_results.csv`)

| Scenario | Interaction Contrast ($L$) | Pooled SD ($\sigma$) | Standardized Effect ($L/\sigma$) | Required $n$ per group | Total Animals ($N$, 4 groups) | Power Achieved |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Observed large crossover effect (Tshikudi estimate)** | 4.5 | 1.4 | 3.21 | **4** | **16** | 89.5% |
| **High biological variability** | 4.5 | 2.0 | 2.25 | **7** | **28** | 84.5% |
| **Low biological variability** | 4.5 | 1.0 | 4.50 | **2** | **8** | 88.9% |
| **Moderate crossover interaction** (50% reduction in contrast) | 2.25 | 1.4 | 1.61 | **13** | **52** | 82.6% |
| **Modest interaction** ($L = 1.5$) | 1.50 | 1.4 | 1.07 | **28** | **112** | 80.9% |
| **Subtle interaction** ($L = 1.0$) | 1.00 | 1.4 | 0.71 | **62** | **248** | 80.3% |
| **Subtle interaction with high variability** ($L = 1.0, \sigma = 2.0$) | 1.00 | 2.0 | 0.50 | **126** | **504** | 80.1% |
| **Small effect** ($L = 0.75, \sigma = 1.4$) | 0.75 | 1.4 | 0.54 | **110** | **440** | 80.2% |
| **Asymmetric effect** (benefit in males, zero in females; $L = 2.5$) | 2.50 | 1.4 | 1.79 | **10** | **40** | 80.6% |

---

## 3. Critical Methodological Principle: Sample Size for Interaction Tests vs. Main Effects

> [!IMPORTANT]
> **Statistical interaction tests require substantially larger sample sizes than main-effect tests.**

1. **Variance Inflation of the Interaction Contrast:**
   - A simple main effect comparison between two groups (e.g., Male Vehicle vs. Male PSTi8) has variance $\text{Var}(\Delta_M) = \sigma^2 (1/n + 1/n) = 2\sigma^2 / n$.
   - A $2 \times 2$ interaction contrast involves four independent sample means, yielding $\text{Var}(L) = \sigma^2 (1/n + 1/n + 1/n + 1/n) = 4\sigma^2 / n$—**double the sampling variance**.
2. **Attenuation in Quantitative (Non-Crossover) Interactions:**
   - In most biological studies, a sex difference is not a complete 180-degree crossover (where treatment improves males and worsens females by equal magnitude). Rather, it is typically a quantitative difference (e.g., a drug works moderately in males, but exhibits a weaker or delayed effect in females).
   - If a drug produces an effect of $\Delta = 2.0$ in males and $\Delta = 1.0$ in females (a 50% moderation), the interaction contrast is only $L = 2.0 - 1.0 = 1.0$.
   - While detecting the male main effect ($\Delta = 2.0, \sigma = 1.4$) requires only $n \approx 8$ per group (total $N = 16$), detecting the $L = 1.0$ interaction contrast requires **$n = 62$ per group (total $N = 248$)—over 15 times the total sample size**.
3. **Preclinical Underpowering:**
   - Preclinical rodent experiments typically utilize $n = 5\text{--}8$ animals per group due to ethical and resource constraints.
   - At $n = 6$ per group, an experiment is adequately powered ($\ge 80\%$) **only if the interaction effect size is very large** ($L/\sigma \ge 2.3$), as observed in the extreme crossover of the Tshikudi colitis model.
   - For realistic, moderate, or subtle sex-divergent responses ($L/\sigma \le 1.0$), conventional preclinical sample sizes ($n = 6$) achieve less than 20% statistical power, resulting in high false-negative rates and failure to detect true biological sex differences.

---

## 4. Modeling Assumptions

1. **Normality:** Errors within each group are assumed to follow a Gaussian distribution.
2. **Homoscedasticity:** Residual variance $\sigma^2$ is assumed constant across all four experimental conditions.
3. **Balanced Allocation:** Equal sample size $n$ across all four sex-by-treatment groups.
4. **Independence:** Observations between animals are completely independent (no unmodeled litter effects or cage clustering).
5. **Two-Tailed Null Hypothesis:** $H_0: L = 0$ tested at nominal $\alpha = 0.05$.
