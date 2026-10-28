#!/usr/bin/env python3
"""
scripts/power_analysis.py

Power analysis for detecting Sex x Treatment interaction in preclinical PSTi8 studies.
Based on Disease Activity Index (DAI) estimates from Tshikudi et al., IJMS 2024 (doi: 10.3390/ijms252312757).

Author: Antigravity Vault Agent
Date: 2026-10-28
"""

import math
import csv
import os

def normal_cdf(x):
    """Cumulative distribution function for standard normal distribution."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def calculate_interaction_power(delta_interaction, sigma, n_per_group, alpha=0.05):
    """
    Calculate statistical power to detect a 2x2 interaction contrast:
    L = (mu_F,PSTi8 - mu_F,Veh) - (mu_M,PSTi8 - mu_M,Veh)
    SE_L = sigma * sqrt(4 / n)
    """
    if n_per_group < 2 or sigma <= 0 or delta_interaction == 0:
        return 0.0
    se = sigma * math.sqrt(4.0 / n_per_group)
    z_alpha = 1.959963984540054  # for two-sided alpha = 0.05
    effect_ratio = abs(delta_interaction) / se
    power = normal_cdf(effect_ratio - z_alpha) + normal_cdf(-effect_ratio - z_alpha)
    return power

def required_n_for_interaction(delta_interaction, sigma, target_power=0.80, alpha=0.05):
    """
    Compute required animals per group (per sex per treatment) for 80% power.
    4 groups total: Male-Veh, Male-PSTi8, Female-Veh, Female-PSTi8.
    """
    z_alpha = 1.959963984540054  # alpha = 0.05, two-tailed
    z_beta = 0.8416212335729143   # power = 0.80
    
    # Asymptotic normal formula:
    n_approx = (4.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2)) / (delta_interaction ** 2)
    n = max(2, math.ceil(n_approx))
    
    # Iterative refinement to ensure power >= target_power
    while calculate_interaction_power(delta_interaction, sigma, n, alpha) < target_power:
        n += 1
    return n

def required_n_for_main_effect(delta_main, sigma, target_power=0.80, alpha=0.05):
    """
    Compute required n per group for a two-sample main effect (e.g., within one sex).
    SE = sigma * sqrt(2 / n)
    """
    z_alpha = 1.959963984540054
    z_beta = 0.8416212335729143
    n_approx = (2.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2)) / (delta_main ** 2)
    n = max(2, math.ceil(n_approx))
    return n

def main():
    # Base estimates derived from Tshikudi et al. 2024 (Figure 1B/1C estimates for DAI):
    # Male: Vehicle ~7.5, PSTi8 ~5.0 -> delta_male = -2.5
    # Female: Vehicle ~6.0, PSTi8 ~8.0 -> delta_female = +2.0
    # Interaction contrast L = delta_female - delta_male = 2.0 - (-2.5) = 4.5
    # Estimated pooled SD sigma ~ 1.4 (derived from SEM ~0.5-0.8 with n ~ 6)

    base_delta_int = 4.5
    base_sigma = 1.4

    # Scenarios for sensitivity analysis
    scenarios = [
        ("Observed large crossover effect (Tshikudi 2024 estimate)", 4.5, 1.4),
        ("High variability (SD = 2.0)", 4.5, 2.0),
        ("Low variability (SD = 1.0)", 4.5, 1.0),
        ("Moderate interaction (50% reduction in interaction contrast)", 2.25, 1.4),
        ("Modest interaction (contrast = 1.5 DAI units)", 1.5, 1.4),
        ("Subtle interaction (contrast = 1.0 DAI unit)", 1.0, 1.4),
        ("Subtle interaction with high SD (contrast = 1.0, SD = 2.0)", 1.0, 2.0),
        ("Small effect (contrast = 0.75 DAI units, SD = 1.4)", 0.75, 1.4),
        ("Male-only protective effect, zero effect in female (asymmetric)", 2.5, 1.4),
    ]

    results = []

    for name, delta, sigma in scenarios:
        n_per_group = required_n_for_interaction(delta, sigma, target_power=0.80)
        total_animals = n_per_group * 4  # 4 groups in 2x2 design
        std_effect = delta / sigma
        power_at_n = calculate_interaction_power(delta, sigma, n_per_group)
        
        # Compare to simple main effect of size delta/2 (e.g. detecting single-sex effect)
        main_delta = delta / 2.0
        n_main = required_n_for_main_effect(main_delta, sigma, target_power=0.80)
        
        # Ratio of total sample size (4 * n_int vs 2 * n_main)
        ratio = (4 * n_per_group) / (2 * n_main) if n_main > 0 else 0

        results.append({
            "scenario": name,
            "interaction_contrast_L": delta,
            "pooled_sd_sigma": sigma,
            "standardized_effect_L_over_sigma": round(std_effect, 3),
            "n_per_group_per_sex": n_per_group,
            "total_animals_4_groups": total_animals,
            "power_achieved": round(power_at_n, 4),
            "n_main_effect_single_sex": n_main,
            "interaction_vs_main_sample_ratio": round(ratio, 2)
        })

    # Save to data/power_results.csv
    output_path = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/power_results.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    fieldnames = [
        "scenario",
        "interaction_contrast_L",
        "pooled_sd_sigma",
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

    print(f"Saved power results to {output_path}")

    # Print summary to console
    print("\n--- Power Analysis Summary (alpha=0.05, power=0.80) ---")
    for r in results:
        print(f"* {r['scenario']}: n={r['n_per_group_per_sex']}/group (Total N={r['total_animals_4_groups']}) | Std effect={r['standardized_effect_L_over_sigma']}")

if __name__ == "__main__":
    main()
