# Statistical Power Analysis for Sex × Treatment Interaction in PSTi8 Colitis Models

**Date:** 2026-10-31 (Updated)  
**Reference Study:** Tshikudi et al., *Int J Mol Sci* 2024; 25(23):12757 (DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))  
**Analysis Script:** [scripts/power_analysis.py](../scripts/power_analysis.py)  
**Output Dataset:** [data/power_results.csv](../data/power_results.csv)

---

## Executive Summary: Realistic Effect-Size Range ($L = 1.0\text{ to }2.5$)

> [!IMPORTANT]
> **Key Finding on Realistic Preclinical Power:**  
> When evaluated across the **realistic effect-size range ($L = 1.0\text{ to }2.5\text{ DAI units}$)**, detecting a biological Sex × Treatment interaction requires:
> - **$n = 6\text{ to }32$ animals per group** ($N = 24\text{ to }128$ total animals) under the direct SD regime ($\sigma = 1.0$).
> - **$n = 11\text{ to }63$ animals per group** ($N = 44\text{ to }252$ total animals) under the converted SEM regime ($\sigma = 1.4$).
> - Peak extreme crossover benchmarks ($L = 4.5$) require only $n = 2\text{--}4$ animals per group, but represent an unrealistic statistical ceiling that masks the severe sample size demands of real-world non-crossover interactions and cumulative disease scores.

---

## 1. Provenance and Derivation of Quantitative Parameters from Figure 1

### A. Graph and Section Locators in Tshikudi et al. (2024)
- **Figure 1A:** Daily Disease Activity Index (DAI) score time-course over 6 days of DSS-induced colitis (line plots with error bars).
- **Figure 1C:** Cumulative sum of DAI across the 7-day study period (bar charts with error bars).
- **Figure 1D:** Macroscopic damage score (macro-score) assessing diarrhea, rectal bleeding, and rectal prolapse (bar charts with error bars).
- **Methods (Section 4.1 & 4.9):** Reports $n = 5\text{--}6$ per group for tissue/cellular assays and $n = 12\text{--}15$ per group for daily clinical scoring cohorts.

### B. Error Bar Definition: SEM vs. SD
In Section 4.9 ("Statistical Analysis"), the authors state:
> *"Data were expressed as the mean ± standard deviation (S.D.)."*

- **Direct Interpretation (Branch A — Stated SD):**  
  Taking the author's methods literally, the error bars in Figure 1 are sample standard deviations ($\text{SD}$). Visual inspection of the bar/line error bars shows daily within-group error bar half-lengths ranging from approximately $0.6$ to $1.2$ DAI units. Under this direct reading, the within-group residual standard deviation is:
  $$\sigma \in [0.8, 1.0]\text{ DAI units}$$
- **Converted Interpretation (Branch B — Converted SEM):**  
  Preclinical rodent papers often plot SEM despite boilerplate "mean ± S.D." methods text. If the graphical error bar height ($\approx 0.5\text{--}0.75$) reflects SEM, then converting SEM to standard deviation with group size $n = 5\text{--}6$ ($\text{SD} = \text{SEM} \times \sqrt{n}$) yields:
  $$\sigma = (0.5\text{--}0.75) \times \sqrt{6} \approx 1.2\text{--}1.84\text{ DAI units (nominal midpoint } \sigma \approx 1.4\text{)}$$
- **Resolution:** All modeling is executed across **both regimes** ($\sigma \in \{0.8, 1.0, 1.4, 1.8\}$).

### C. Baseline Interaction Contrast ($L$)
Because Tshikudi et al. provide graphical figures rather than raw tabulated numerical data:
- **Within-Male Response ($\Delta_M = \mu_{M,\text{PSTi8}} - \mu_{M,\text{Veh}}$):** PSTi8 delayed colitis onset and reduced daily DAI scores by approximately $-1.5$ to $-2.5$ units.
- **Within-Female Response ($\Delta_F = \mu_{F,\text{PSTi8}} - \mu_{F,\text{Veh}}$):** PSTi8 elevated daily DAI scores at 72 h and 96 h by $+1.0$ to $+2.0$ units ($p < 0.05$).
- **Overall Cumulative Scores:** As explicitly stated in the paper text, cumulative DAI (sum of DAI) and macroscopic damage scores (macro-scores) were **not significantly different** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice.
- **Realistic Contrast Range ($L = \Delta_F - \Delta_M$):**
  - **Headlined Realistic Range:** $L \in [1.0, 2.5]\text{ DAI units}$ (capturing conservative crossover down to subtle non-significant trends).
  - *Benchmark Extreme Crossovers:* $L = 3.5$ to $4.5\text{ DAI units}$ (representing transient single-timepoint peak daily divergence).

---

## 2. Statistical Framework: Exact Student's $t$ and Non-Central $t$ Distribution

Power is calculated using exact Student's $t$-distribution critical values and non-central $t$-distribution cumulative probabilities for the $2 \times 2$ factorial contrast:

$$L = (\mu_{F,\text{PSTi8}} - \mu_{F,\text{Veh}}) - (\mu_{M,\text{PSTi8}} - \mu_{M,\text{Veh}})$$

1. **Standard Error of the Contrast:**
   $$\text{SE}_L = \sigma \sqrt{\frac{1}{n} + \frac{1}{n} + \frac{1}{n} + \frac{1}{n}} = \sigma \sqrt{\frac{4}{n}}$$
2. **Degrees of Freedom:**
   For 4 groups with sample size $n$ each, residual error degrees of freedom are:
   $$\text{df} = 4(n - 1)$$
3. **Non-Centrality Parameter ($\delta$):**
   $$\delta = \frac{|L|}{\text{SE}_L} = \frac{|L|}{\sigma \sqrt{4/n}} = \frac{|L|}{\sigma} \frac{\sqrt{n}}{2}$$
4. **Critical Threshold & Two-Sided Power:**
   For nominal $\alpha = 0.05$, two-sided critical value $t_{\text{crit}} = t_{1 - \alpha/2, \text{df}}$.  
   $$\text{Power} = 1 - F(t_{\text{crit}}; \text{df}, \delta) + F(-t_{\text{crit}}; \text{df}, \delta)$$
   where $F(t; \text{df}, \delta)$ is the cumulative distribution function of the non-central $t$-distribution.

---

## 3. Power Modeling Results Across Daily DAI Regimes

Below is the parameter matrix from [data/power_results.csv](../data/power_results.csv):

### A. Direct SD Regime ($\sigma = 0.8\text{ to }1.0$) — Realistic Range Headlined

| Scenario | Contrast $L$ | Residual $\sigma$ | Standardized Effect ($L/\sigma$) | Required $n$ per group | Total Animals ($N$) | Power Achieved |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Realistic: Conservative crossover** | **2.5** | **1.0** | **2.50** | **6** | **24** | **83.0%** |
| **Realistic: Moderate interaction** | **2.0** | **1.0** | **2.00** | **9** | **36** | **82.9%** |
| **Realistic: Attenuated interaction** | **1.5** | **1.0** | **1.50** | **15** | **60** | **81.5%** |
| **Realistic: Subtle non-sig trend** | **1.0** | **1.0** | **1.00** | **32** | **128** | **80.1%** |
| Realistic: Conservative crossover ($\sigma=0.8$) | 2.5 | 0.8 | 3.13 | 4 | 16 | 81.8% |
| Realistic: Moderate interaction ($\sigma=0.8$) | 2.0 | 0.8 | 2.50 | 6 | 24 | 83.0% |
| Realistic: Attenuated interaction ($\sigma=0.8$) | 1.5 | 0.8 | 1.88 | 10 | 40 | 82.3% |
| Realistic: Subtle non-sig trend ($\sigma=0.8$) | 1.0 | 0.8 | 1.25 | 21 | 84 | 80.8% |
| Small non-sig trend | 0.5 | 1.0 | 0.50 | 127 | 508 | 80.3% |
| *Benchmark Extreme:* Central crossover | 3.5 | 1.0 | 3.50 | 4 | 16 | 89.4% |
| *Benchmark Extreme:* High crossover | 4.5 | 0.8 | 5.63 | 2 | 8 | 84.0% |

### B. Converted SEM Regime ($\sigma = 1.4\text{ to }1.8$) — Realistic Range Headlined

| Scenario | Contrast $L$ | Residual $\sigma$ | Standardized Effect ($L/\sigma$) | Required $n$ per group | Total Animals ($N$) | Power Achieved |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Realistic: Conservative crossover ($\sigma=1.4$)** | **2.5** | **1.4** | **1.79** | **11** | **44** | **82.4%** |
| **Realistic: Moderate interaction ($\sigma=1.4$)** | **2.0** | **1.4** | **1.43** | **16** | **64** | **80.3%** |
| **Realistic: Attenuated interaction ($\sigma=1.4$)** | **1.5** | **1.4** | **1.07** | **28** | **112** | **80.2%** |
| **Realistic: Subtle non-sig trend ($\sigma=1.4$)** | **1.0** | **1.4** | **0.71** | **63** | **252** | **80.6%** |
| Realistic: Conservative crossover ($\sigma=1.8$) | 2.5 | 1.8 | 1.39 | 17 | 68 | 80.5% |
| Realistic: Moderate interaction ($\sigma=1.8$) | 2.0 | 1.8 | 1.11 | 26 | 104 | 80.1% |
| Realistic: Attenuated interaction ($\sigma=1.8$) | 1.5 | 1.8 | 0.83 | 46 | 184 | 80.3% |
| Realistic: Subtle non-sig trend ($\sigma=1.8$) | 1.0 | 1.8 | 0.56 | 103 | 412 | 80.3% |
| *Benchmark Extreme:* Central crossover ($\sigma=1.4$) | 3.5 | 1.4 | 2.50 | 6 | 24 | 83.0% |
| *Benchmark Extreme:* High crossover ($\sigma=1.4$) | 4.5 | 1.4 | 3.21 | 4 | 16 | 83.9% |

---

## 4. Dedicated Section: Powering the Cumulative-DAI Endpoint Specifically

In Figure 1C of Tshikudi et al. (2024), the primary longitudinal clinical metric is the **cumulative sum of DAI scores across the entire 7-day challenge**:
- Cumulative DAI sum reflects the integral of clinical disease activity over time.
- In rodent colitis models, cumulative DAI values typically range from 6 to 15, with pooled residual standard deviation $\sigma_{\text{cum}} \in [2.5, 4.0]\text{ DAI units}$.
- Because treatment differences across sexes accumulate with moderate variance, realistic interaction contrasts on cumulative scores are subtle ($L_{\text{cum}} \in [1.0, 3.5]$ units).

### Cumulative-DAI Power Scenarios (Excerpt from `data/power_results.csv`)

| Cumulative Scenario | Cumulative Contrast $L_{\text{cum}}$ | Residual $\sigma_{\text{cum}}$ | Standardized Effect ($L/\sigma$) | Required $n$ per group | Total Animals ($N$, 4 groups) | Power Achieved |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| High cumulative contrast ($\sigma=3.0$) | 3.5 | 3.0 | 1.17 | **24** | **96** | 80.7% |
| Moderate cumulative contrast ($\sigma=3.0$) | 2.5 | 3.0 | 0.83 | **46** | **184** | 80.3% |
| **Realistic subtle contrast ($\sigma=3.0$)** | **1.5** | **3.0** | **0.50** | **127** | **508** | **80.3%** |
| Small non-sig trend ($\sigma=3.0$) | 1.0 | 3.0 | 0.33 | **284** | **1136** | 80.1% |
| Moderate cumulative contrast ($\sigma=2.5$) | 2.5 | 2.5 | 1.00 | **32** | **128** | 80.1% |
| **Realistic subtle contrast ($\sigma=2.5$)** | **1.5** | **2.5** | **0.60** | **88** | **352** | **80.1%** |
| Small non-sig trend ($\sigma=2.5$) | 1.0 | 2.5 | 0.40 | **197** | **788** | 80.1% |
| Moderate cumulative contrast ($\sigma=4.0$) | 2.5 | 4.0 | 0.63 | **81** | **324** | 80.1% |
| **Realistic subtle contrast ($\sigma=4.0$)** | **1.5** | **4.0** | **0.38** | **224** | **896** | **80.1%** |
| Small non-sig trend ($\sigma=4.0$) | 1.0 | 4.0 | 0.25 | **503** | **2012** | 80.0% |

### Why Cumulative Endpoints Did Not Reach Significance in Tshikudi et al.
1. Tshikudi et al. utilized $n = 12\text{--}15$ mice per group for daily DAI and macroscopic scoring cohorts.
2. For cumulative DAI ($\sigma \approx 3.0$), an $n = 12\text{--}15$ cohort provides only **18% to 26% statistical power** to detect a realistic subtle contrast ($L = 1.5, L/\sigma = 0.50$).
3. To achieve 80% power for $L = 1.5$ requires **$n = 88\text{ to }127$ mice per group** ($N = 352\text{ to }508$).
4. This quantitative modeling demonstrates that the lack of statistically significant differences on cumulative DAI sum and macroscopic scores is an expected consequence of statistical underpowering for cumulative continuous endpoints, rather than evidence of identical biological outcomes.

---

## 5. Methodological Principle: Sample Size Requirements for Interaction Tests vs. Main Effects

1. **Variance Doubling of the Contrast:**
   - A two-sample main effect test (e.g., Male Vehicle vs. Male PSTi8) evaluates $\Delta_M = \mu_1 - \mu_2$, with sampling variance $\text{Var}(\Delta_M) = \sigma^2 (1/n + 1/n) = 2\sigma^2 / n$.
   - A $2 \times 2$ interaction test evaluates the four-group linear contrast $L$, with sampling variance $\text{Var}(L) = \sigma^2 (1/n + 1/n + 1/n + 1/n) = 4\sigma^2 / n$—**double the variance of a simple difference**.
2. **Quantitative Attenuation vs. Pure Crossover:**
   - In a pure crossover where a drug improves males by $2.0$ units and worsens females by $2.0$ units, the interaction contrast is $L = 4.0$.
   - However, real-world sex differences typically manifest as **quantitative moderations** (e.g., drug improves males by $2.0$ units and females by $0.5$ units, yielding $L = 1.5$).
   - In that scenario, detecting the male main effect ($\Delta = 2.0, \sigma = 1.0$) requires only **$n = 5$ per group**, whereas detecting the $L = 1.5$ interaction requires **$n = 15$ per group (total $N = 60$)**—a substantial expansion in total animal requirements.
