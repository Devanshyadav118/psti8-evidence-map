#!/usr/bin/env python3
"""
scripts/power_analysis.py

Power analysis for detecting Sex x Treatment interaction in preclinical PSTi8 studies.
Calibrated to the 2x2 factorial colitis model in Tshikudi et al., IJMS 2024 (doi: 10.3390/ijms252312757).

Key features:
1. Exact Student's t-distribution critical values and non-central t cumulative distribution
   for both 2x2 factorial interaction contrasts and two-sample main effect tests.
2. Direct SD (Section 4.9: "mean ± S.D.") and Converted SEM-to-SD error bar regimes.
3. Realistic daily DAI interaction contrast range: L = 1.0 to 2.5 DAI units (alongside extreme benchmarks L = 3.5, 4.5).
4. Dedicated cumulative-DAI endpoint section (sum of DAI over 7 days, sigma in [2.5, 4.0], L in [1.0, 3.5]).
5. Repo-relative output path (writes directly to data/power_results.csv).

Author: Antigravity Vault Agent
Date: 2026-10-31 (Updated)
"""

import math
import csv
import os

# ---------------------------------------------------------------------------
# Exact t-distribution and non-central t numerical functions (pure Python)
# ---------------------------------------------------------------------------

def betacf(a, b, x, max_iter=200, eps=1e-12):
    """Continued fraction for regularized incomplete beta function (Lentz method)."""
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap
    if abs(d) < 1e-30:
        d = 1e-30
    d = 1.0 / d
    h = d
    for m in range(1, max_iter + 1):
        m2 = 2 * m
        # Even step
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        h *= d * c
        # Odd step
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        if abs(d) < 1e-30:
            d = 1e-30
        c = 1.0 + aa / c
        if abs(c) < 1e-30:
            c = 1e-30
        d = 1.0 / d
        del_h = d * c
        h *= del_h
        if abs(del_h - 1.0) < eps:
            break
    return h

def ibeta(a, b, x):
    """Regularized incomplete beta function I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    lbeta = math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)
    front = math.exp(a * math.log(x) + b * math.log(1.0 - x) - lbeta)
    if x < (a + 1.0) / (a + b + 2.0):
        return front * betacf(a, b, x) / a
    else:
        return 1.0 - front * betacf(b, a, 1.0 - x) / b

def t_crit_2sided(df, alpha=0.05):
    """Two-sided critical value for Student's t distribution with df degrees of freedom."""
    if df < 1:
        raise ValueError("df must be at least 1")
    a = df / 2.0
    b = 0.5
    low, high = 0.0, 1.0
    for _ in range(40):
        mid = (low + high) / 2.0
        val = ibeta(a, b, mid)
        if val < alpha:
            low = mid
        else:
            high = mid
    x = (low + high) / 2.0
    return math.sqrt(df * (1.0 - x) / x)

def normal_cdf(x):
    """Cumulative distribution function for standard normal distribution."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def chi2_pdf(v, df):
    """Probability density function for chi-squared distribution with df degrees of freedom."""
    if v <= 0:
        return 0.0
    half_df = df / 2.0
    log_p = -half_df * math.log(2.0) - math.lgamma(half_df) + (half_df - 1.0) * math.log(v) - v / 2.0
    return math.exp(log_p)

def nct_cdf(t, df, delta, n_steps=120):
    r"""
    Cumulative distribution function for non-central t distribution with df and non-centrality parameter delta.
    P(T <= t) = \int_0^\infty \Phi(t * \sqrt{v/df} - delta) f_{\chi^2}(v; df) dv.
    Evaluated using Simpson's rule over significant probability mass.
    """
    mean = df
    sd = math.sqrt(2.0 * df)
    a = max(1e-5, mean - 5.0 * sd)
    b = mean + 6.0 * sd
    h = (b - a) / n_steps
    total = 0.0
    for i in range(n_steps + 1):
        v = a + i * h
        weight = 2.0 if (i % 2 == 0) else 4.0
        if i == 0 or i == n_steps:
            weight = 1.0
        pdf = chi2_pdf(v, df)
        z = t * math.sqrt(v / df) - delta
        total += weight * normal_cdf(z) * pdf
    return (h / 3.0) * total

# ---------------------------------------------------------------------------
# Power and Sample Size Calculations (t-distribution based)
# ---------------------------------------------------------------------------

def calculate_interaction_power_t(delta_interaction, sigma, n_per_group, alpha=0.05):
    """
    Calculate statistical power to detect a 2x2 interaction contrast:
    L = (mu_F,PSTi8 - mu_F,Veh) - (mu_M,PSTi8 - mu_M,Veh)
    SE_L = sigma * sqrt(4 / n)
    df = 4 * (n - 1)
    Non-centrality parameter: delta = |L| / SE_L = (|L| / sigma) * (sqrt(n) / 2)
    """
    if n_per_group < 2 or sigma <= 0 or delta_interaction == 0:
        return 0.0
    df = 4 * (n_per_group - 1)
    se = sigma * math.sqrt(4.0 / n_per_group)
    ncp = abs(delta_interaction) / se
    tc = t_crit_2sided(df, alpha)
    # Power = 1 - F(tc; df, ncp) + F(-tc; df, ncp)
    power = 1.0 - nct_cdf(tc, df, ncp) + nct_cdf(-tc, df, ncp)
    return max(0.0, min(1.0, power))

def required_n_for_interaction_t(delta_interaction, sigma, target_power=0.80, alpha=0.05):
    """
    Compute required animals per group (per sex per treatment) for target power using t-distribution.
    4 groups total: Male-Veh, Male-PSTi8, Female-Veh, Female-PSTi8.
    """
    if delta_interaction == 0 or sigma <= 0:
        return 0
    z_alpha = 1.959963984540054
    z_beta = 0.8416212335729143
    n_approx = math.ceil(4.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2) / (delta_interaction ** 2))
    n = max(2, n_approx - 2)
    while calculate_interaction_power_t(delta_interaction, sigma, n, alpha) < target_power:
        n += 1
        if n > 2000:
            break
    return n

def calculate_main_effect_power_t(delta_main, sigma, n_per_group, alpha=0.05):
    """
    Calculate power for two-sample t-test (within one sex, 2 groups):
    SE = sigma * sqrt(2 / n)
    df = 2 * (n - 1)
    ncp = delta_main / SE
    """
    if n_per_group < 2 or sigma <= 0 or delta_main == 0:
        return 0.0
    df = 2 * (n_per_group - 1)
    se = sigma * math.sqrt(2.0 / n_per_group)
    ncp = abs(delta_main) / se
    tc = t_crit_2sided(df, alpha)
    power = 1.0 - nct_cdf(tc, df, ncp) + nct_cdf(-tc, df, ncp)
    return max(0.0, min(1.0, power))

def required_n_for_main_effect_t(delta_main, sigma, target_power=0.80, alpha=0.05):
    """
    Compute required n per group for two-sample main effect test using t-distribution.
    """
    if delta_main <= 0 or sigma <= 0:
        return 0
    z_alpha = 1.959963984540054
    z_beta = 0.8416212335729143
    n_approx = math.ceil(2.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2) / (delta_main ** 2))
    n = max(2, n_approx - 2)
    while calculate_main_effect_power_t(delta_main, sigma, n, alpha) < target_power:
        n += 1
        if n > 2000:
            break
    return n

# ---------------------------------------------------------------------------
# Scenario Execution & CSV Output
# ---------------------------------------------------------------------------

def main():
    scenarios = [
        # -------------------------------------------------------------------
        # 1. Daily DAI: Direct SD regime (Section 4.9: "mean ± S.D.")
        #    Headline realistic range: L = 1.0 to 2.5 DAI units
        # -------------------------------------------------------------------
        ("Daily DAI: Direct SD (sigma=1.0) | Conservative crossover (L=2.5)", 2.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=1.0) | Moderate interaction (L=2.0)", 2.0, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=1.0) | Attenuated interaction (L=1.5)", 1.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=1.0) | Subtle non-sig trend (L=1.0)", 1.0, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=0.8) | Conservative crossover (L=2.5)", 2.5, 0.8, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=0.8) | Moderate interaction (L=2.0)", 2.0, 0.8, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=0.8) | Attenuated interaction (L=1.5)", 1.5, 0.8, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=0.8) | Subtle non-sig trend (L=1.0)", 1.0, 0.8, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=1.0) | Small non-sig trend (L=0.5)", 0.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=1.0) | Central crossover benchmark (L=3.5)", 3.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Daily DAI: Direct SD (sigma=0.8) | High crossover benchmark (L=4.5)", 4.5, 0.8, "Direct SD (Sec 4.9)"),

        # -------------------------------------------------------------------
        # 2. Daily DAI: Converted SEM-to-SD regime (if error bars were SEM * sqrt(6))
        #    sigma = 1.4 to 1.8
        # -------------------------------------------------------------------
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | Conservative crossover (L=2.5)", 2.5, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | Moderate interaction (L=2.0)", 2.0, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | Attenuated interaction (L=1.5)", 1.5, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | Subtle non-sig trend (L=1.0)", 1.0, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | Central crossover benchmark (L=3.5)", 3.5, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.4) | High crossover benchmark (L=4.5)", 4.5, 1.4, "Converted SEM (n=6)"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | Conservative crossover (L=2.5)", 2.5, 1.8, "High Converted SEM"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | Moderate interaction (L=2.0)", 2.0, 1.8, "High Converted SEM"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | Attenuated interaction (L=1.5)", 1.5, 1.8, "High Converted SEM"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | Subtle non-sig trend (L=1.0)", 1.0, 1.8, "High Converted SEM"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | Central crossover benchmark (L=3.5)", 3.5, 1.8, "High Converted SEM"),
        ("Daily DAI: Converted SEM-to-SD (sigma=1.8) | High crossover benchmark (L=4.5)", 4.5, 1.8, "High Converted SEM"),

        # -------------------------------------------------------------------
        # 3. Cumulative DAI Endpoint Specifically (Sum of DAI over 7 days, Fig 1C)
        #    sigma_cum in [2.5, 4.0], L_cum in [1.0, 3.5]
        # -------------------------------------------------------------------
        ("Cumulative DAI (sigma=3.0) | High cumulative contrast (L=3.5)", 3.5, 3.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=3.0) | Moderate cumulative contrast (L=2.5)", 2.5, 3.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=3.0) | Realistic subtle contrast (L=1.5)", 1.5, 3.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=3.0) | Small non-sig trend (L=1.0)", 1.0, 3.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=2.5) | Moderate cumulative contrast (L=2.5)", 2.5, 2.5, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=2.5) | Realistic subtle contrast (L=1.5)", 1.5, 2.5, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=2.5) | Small non-sig trend (L=1.0)", 1.0, 2.5, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=4.0) | Moderate cumulative contrast (L=2.5)", 2.5, 4.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=4.0) | Realistic subtle contrast (L=1.5)", 1.5, 4.0, "Cumulative DAI (Fig 1C)"),
        ("Cumulative DAI (sigma=4.0) | Small non-sig trend (L=1.0)", 1.0, 4.0, "Cumulative DAI (Fig 1C)"),
    ]

    results = []

    for name, delta, sigma, regime in scenarios:
        n_per_group = required_n_for_interaction_t(delta, sigma, target_power=0.80)
        total_animals = n_per_group * 4  # 4 groups in 2x2 design
        std_effect = delta / sigma
        power_at_n = calculate_interaction_power_t(delta, sigma, n_per_group)

        # Compare to simple main effect of size delta/2 (e.g. single-sex effect)
        main_delta = delta / 2.0
        n_main = required_n_for_main_effect_t(main_delta, sigma, target_power=0.80)
        ratio = (4 * n_per_group) / (2 * n_main) if n_main > 0 else 0

        results.append({
            "scenario": name,
            "error_bar_regime": regime,
            "interaction_contrast_L": delta,
            "residual_sd_sigma": sigma,
            "standardized_effect_L_over_sigma": round(std_effect, 3),
            "n_per_group_per_sex": n_per_group,
            "total_animals_4_groups": total_animals,
            "power_achieved": round(power_at_n, 4),
            "n_main_effect_single_sex": n_main,
            "interaction_vs_main_sample_ratio": round(ratio, 2)
        })

    # Repo-relative output path
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.dirname(script_dir)
    output_path = os.path.join(repo_root, "data", "power_results.csv")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fieldnames = [
        "scenario",
        "error_bar_regime",
        "interaction_contrast_L",
        "residual_sd_sigma",
        "standardized_effect_L_over_sigma",
        "n_per_group_per_sex",
        "total_animals_4_groups",
        "power_achieved",
        "n_main_effect_single_sex",
        "interaction_vs_main_sample_ratio"
    ]

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(r)

    print(f"Saved {len(results)} t-distribution power scenarios to {output_path}")

if __name__ == "__main__":
    main()
