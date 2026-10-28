# Statistical Power Analysis for Sex × Treatment Interaction in PSTi8 Colitis Models

**Date:** 2026-10-28 (Updated)  
**Reference Study:** Tshikudi et al., *Int J Mol Sci* 2024; 25(23):12757 (DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757))  
**Analysis Script:** [scripts/power_analysis.py](../scripts/power_analysis.py)  
**Output Dataset:** [data/power_results.csv](../data/power_results.csv)

---

## 1. Provenance and Derivation of Quantitative Parameters from Figure 1

### A. Graph and Section Locators in Tshikudi et al. (2024)
- **Figure 1A:** Disease Activity Index (DAI) daily score time-course over 6 days of DSS-induced colitis (line plots with error bars).
- **Figure 1C:** Cumulative sum of DAI across the study period (bar charts with error bars).
- **Figure 1D:** Macroscopic damage score (macro-score) assessing diarrhea, rectal bleeding, and rectal prolapse (bar charts with error bars).
- **Methods (Section 4.1 & 4.9):** States $n = 5\text{--}6$ per group for tissue/cellular assays and $n = 12\text{--}15$ per group for daily clinical scoring of DAI and body weight.

### B. Error Bar Definition: SEM vs. SD
In Section 4.9 ("Statistical Analysis"), the authors state:
> *"Data were expressed as the mean ± standard deviation (S.D.)."*

- **Direct Interpretation (Branch A — Stated SD):**  
  Taking the author's methods literally, the error bars in Figure 1 are sample standard deviations ($\text{SD}$). Visual inspection of the bar/line error bars shows error bar half-lengths ranging from approximately $0.6$ to $1.2$ DAI units. Under this direct reading, the within-group residual standard deviation is:
  $$\sigma \in [0.8, 1.0]\text{ DAI units}$$
- **Converted Interpretation (Branch B — Converted SEM):**  
  In preclinical rodent literature, error bars in daily time-course plots are frequently plotted as SEM despite boilerplate methods text. In preliminary extraction rounds, an analyst treated the graphical error bar height ($\approx 0.5\text{--}0.8$) as SEM. Converting SEM to standard deviation with group size $n = 5\text{--}6$ ($\text{SD} = \text{SEM} \times \sqrt{n}$):
  $$\sigma = (0.5\text{--}0.75) \times \sqrt{6} \approx 1.2\text{--}1.84\text{ DAI units (nominal midpoint } \sigma \approx 1.4\text{)}$$
- **Resolution:** To prevent bias from either assumption, the power model was completely re-executed across **both regimes** ($\sigma \in \{0.8, 1.0, 1.4, 1.8\}$).

### C. Baseline Interaction Contrast as an Estimate Range ($L$)
Because Tshikudi et al. provide no numerical tables or published raw data for DAI, all values are **visual estimates from Figure 1 graphs**:
- **Within-Male Response ($\Delta_M = \mu_{M,\text{PSTi8}} - \mu_{M,\text{Veh}}$):** PSTi8 delayed onset and reduced daily DAI scores by an estimated $-1.5$ to $-2.5$ units.
- **Within-Female Response ($\Delta_F = \mu_{F,\text{PSTi8}} - \mu_{F,\text{Veh}}$):** PSTi8 elevated daily DAI scores at 72 h and 96 h by an estimated $+1.0$ to $+2.0$ units ($p < 0.05$).
- **Overall Cumulative Scores:** As explicitly stated in the paper text, when evaluating the cumulative Disease Activity Index (sum of DAI) and macroscopic damage scores (macro-scores), there was a **non-significant difference** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice.
- **Interaction Contrast Range ($L = \Delta_F - \Delta_M$):**
  - *High Crossover Estimate (peak daily divergence):* $L = (+2.0) - (-2.5) = 4.5\text{ DAI units}$
  - *Central Crossover Estimate:* $L = (+1.5) - (-2.0) = 3.5\text{ DAI units}$
  - *Conservative Crossover Estimate:* $L = (+1.0) - (-1.5) = 2.5\text{ DAI units}$
  - *Attenuated / Non-Significant Cumulative Trend:* $L \in [0.5, 1.5]\text{ DAI units}$

---

## 2. Power Modeling Results Across the Estimate Range

Power to detect the interaction contrast $L = (\mu_{F1} - \mu_{F0}) - (\mu_{M1} - \mu_{M0})$ at two-tailed $\alpha = 0.05$ with $80\%$ target power ($1 - \beta = 0.80$) was calculated in a $2 \times 2$ factorial framework using [scripts/power_analysis.py](../scripts/power_analysis.py):

$$\text{SE}_L = \sigma \sqrt{\frac{4}{n}}, \quad n_{\text{per group}} = \left\lceil \frac{4\sigma^2 (z_{1-\alpha/2} + z_{1-\beta})^2}{L^2} \right\rceil$$

### Parameter Matrix (Excerpt from `data/power_results.csv`)

| Scenario & Regime | Contrast $L$ | Residual $\sigma$ | Standardized Effect ($L/\sigma$) | Required $n$ per group | Total Animals ($N$, 4 groups) | Power Achieved |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Direct SD ($\sigma=0.8$)** \| High Crossover ($L=4.5$) | 4.5 | 0.8 | 5.63 | **2** | **8** | 97.8% |
| **Direct SD ($\sigma=0.8$)** \| Central Crossover ($L=3.5$) | 3.5 | 0.8 | 4.38 | **2** | **8** | 87.2% |
| **Direct SD ($\sigma=0.8$)** \| Conservative ($L=2.5$) | 2.5 | 0.8 | 3.13 | **4** | **16** | 87.8% |
| **Direct SD ($\sigma=1.0$)** \| High Crossover ($L=4.5$) | 4.5 | 1.0 | 4.50 | **2** | **8** | 88.9% |
| **Direct SD ($\sigma=1.0$)** \| Central Crossover ($L=3.5$) | 3.5 | 1.0 | 3.50 | **3** | **12** | 85.8% |
| **Direct SD ($\sigma=1.0$)** \| Conservative ($L=2.5$) | 2.5 | 1.0 | 2.50 | **6** | **24** | 86.5% |
| **Direct SD ($\sigma=1.0$)** \| Moderate Trend ($L=1.5$) | 1.5 | 1.0 | 1.50 | **14** | **56** | 80.1% |
| **Direct SD ($\sigma=1.0$)** \| Subtle Non-Sig Trend ($L=1.0$) | 1.0 | 1.0 | 1.00 | **32** | **128** | 80.7% |
| **Direct SD ($\sigma=1.0$)** \| Small Non-Sig Trend ($L=0.5$) | 0.5 | 1.0 | 0.50 | **126** | **504** | 80.1% |
| **Converted SEM ($\sigma=1.4$)** \| High Crossover ($L=4.5$) | 4.5 | 1.4 | 3.21 | **4** | **16** | 89.5% |
| **Converted SEM ($\sigma=1.4$)** \| Central Crossover ($L=3.5$) | 3.5 | 1.4 | 2.50 | **6** | **24** | 86.5% |
| **Converted SEM ($\sigma=1.4$)** \| Conservative ($L=2.5$) | 2.5 | 1.4 | 1.79 | **10** | **40** | 80.6% |
| **Converted SEM ($\sigma=1.4$)** \| Moderate Trend ($L=1.5$) | 1.5 | 1.4 | 1.07 | **28** | **112** | 80.9% |
| **Converted SEM ($\sigma=1.4$)** \| Subtle Non-Sig Trend ($L=1.0$) | 1.0 | 1.4 | 0.71 | **62** | **248** | 80.3% |
| **High Converted SEM ($\sigma=1.8$)** \| High Crossover ($L=4.5$) | 4.5 | 1.8 | 2.50 | **6** | **24** | 86.5% |
| **High Converted SEM ($\sigma=1.8$)** \| Central Crossover ($L=3.5$) | 3.5 | 1.8 | 1.94 | **9** | **36** | 83.1% |
| **High Converted SEM ($\sigma=1.8$)** \| Conservative ($L=2.5$) | 2.5 | 1.8 | 1.39 | **17** | **68** | 81.7% |
| **High Converted SEM ($\sigma=1.8$)** \| Subtle Non-Sig Trend ($L=1.0$) | 1.0 | 1.8 | 0.56 | **102** | **408** | 80.1% |

---

## 3. Methodological Principle: Sample Size Requirements for Interaction Tests vs. Main Effects

> [!IMPORTANT]
> **Factorial interaction tests require substantially larger sample sizes than two-group main-effect tests.**

1. **Variance Doubling of the Contrast:**
   - A two-sample main effect test (e.g., Male Vehicle vs. Male PSTi8) evaluates $\Delta_M = \mu_1 - \mu_2$, with sampling variance $\text{Var}(\Delta_M) = \sigma^2 (1/n + 1/n) = 2\sigma^2 / n$.
   - A $2 \times 2$ interaction test evaluates a four-group linear contrast $L = (\mu_{F1} - \mu_{F0}) - (\mu_{M1} - \mu_{M0})$, with sampling variance $\text{Var}(L) = \sigma^2 (1/n + 1/n + 1/n + 1/n) = 4\sigma^2 / n$—**exactly double the variance of a simple difference**.
2. **Impact of Interaction Morphology (Crossover vs. Quantitative Moderation):**
   - In a pure 180-degree crossover (where treatment improves males by 2 units and worsens females by 2 units), the interaction contrast is doubled ($L = 2 - (-2) = 4$), which counteracts the variance inflation.
   - However, most biological sex interactions are **quantitative attenuations** rather than complete crossovers (e.g., a drug reduces disease by $2.0$ units in males but only by $1.0$ unit in females).
   - In that situation, the interaction contrast is only $L = 2.0 - 1.0 = 1.0$.
   - While detecting the male main effect ($\Delta = 2.0, \sigma = 1.0$) requires only **$n = 4$ per group (total $N = 8$)**, detecting the $L = 1.0$ interaction contrast requires **$n = 32$ per group (total $N = 128$)—a 16-fold expansion in total animal requirements**.
3. **Implications for Preclinical Literature:**
   - Conventional preclinical sample sizes ($n = 5\text{--}6$ per group) are adequately powered ($\ge 80\%$) **only under conditions of massive qualitative crossover** ($L/\sigma \ge 2.5$).
   - For realistic non-crossover interactions or subtle cumulative endpoints (such as the non-significant macro-scores observed in Tshikudi et al.), studies with $n = 5\text{--}6$ are severely underpowered ($< 25\%$ power), providing a statistical explanation for why overall cumulative endpoints often fail to reach significance despite prominent single-timepoint divergence.

---

## 4. Analytical Assumptions

1. **Normality:** Residual errors within each of the 4 groups follow a Gaussian distribution.
2. **Homoscedasticity:** Within-group standard deviation $\sigma$ is assumed uniform across all four conditions.
3. **Balanced Allocation:** Equal sample size $n$ per group across the $2 \times 2$ matrix.
4. **Independent Observations:** Observations between animals are completely independent (no unmodeled cage, rack, or litter clustering).
5. **Two-Tailed Hypothesis:** $H_0: L = 0$ tested at nominal $\alpha = 0.05$.
