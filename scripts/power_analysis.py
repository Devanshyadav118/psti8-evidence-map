#!/usr/bin/env python3
"""
scripts/power_analysis.py

Power analysis for detecting Sex x Treatment interaction in preclinical PSTi8 studies.
Calibrated to the 2x2 factorial colitis model in Tshikudi et al., IJMS 2024 (doi: 10.3390/ijms252312757).

This script explicitly models:
1. Error bar interpretation:
   - Interpretation A (Direct SD per Section 4.9: "mean ± S.D."): sigma in [0.8, 1.0]
   - Interpretation B (Converted SEM to SD, assuming n=5-6, SD = SEM * sqrt(n)): sigma in [1.4, 1.8]
2. Range of baseline interaction contrast L:
   - L in [0.5, 5.0] DAI units (from subtle non-significant cumulative differences to peak daily crossover)
3. Sample size requirements for Interaction Test vs. Simple Main Effect test.

Author: Antigravity Vault Agent
Date: 2026-10-28 (Updated)
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
    z_alpha = 1.959963984540054  # two-sided alpha = 0.05
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
    
    n_approx = (4.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2)) / (delta_interaction ** 2)
    n = max(2, math.ceil(n_approx))
    while calculate_interaction_power(delta_interaction, sigma, n, alpha) < target_power:
        n += 1
    return n

def required_n_for_main_effect(delta_main, sigma, target_power=0.80, alpha=0.05):
    """
    Compute required n per group for a two-sample main effect (e.g. within one sex).
    SE = sigma * sqrt(2 / n)
    """
    if delta_main <= 0 or sigma <= 0:
        return 0
    z_alpha = 1.959963984540054
    z_beta = 0.8416212335729143
    n_approx = (2.0 * (sigma ** 2) * ((z_alpha + z_beta) ** 2)) / (delta_main ** 2)
    n = max(2, math.ceil(n_approx))
    return n

def main():
    # Grid of scenarios across:
    # 1. Error bar regimes:
    #    - sigma = 0.8 (low SD, direct reading from Figure 1)
    #    - sigma = 1.0 (central SD, direct reading from Figure 1)
    #    - sigma = 1.4 (converted SEM-to-SD with n=6: 0.57 * sqrt(6) ~ 1.4)
    #    - sigma = 1.8 (high converted SEM-to-SD: 0.75 * sqrt(6) ~ 1.8)
    # 2. Interaction contrast ranges:
    #    - L = 4.5 (High crossover estimate: female +2.0, male -2.5)
    #    - L = 3.5 (Central crossover estimate: female +1.5, male -2.0)
    #    - L = 2.5 (Conservative crossover estimate: female +1.0, male -1.5)
    #    - L = 1.5 (Moderate / attenuated interaction, e.g. cumulative score trend)
    #    - L = 1.0 (Subtle interaction / non-significant cumulative difference)
    #    - L = 0.5 (Small non-significant trend)

    scenarios = [
        # Direct SD regime (Section 4.9: mean +/- SD)
        ("Direct SD (sigma=0.8) | High crossover estimate (L=4.5)", 4.5, 0.8, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=0.8) | Central crossover estimate (L=3.5)", 3.5, 0.8, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=0.8) | Conservative crossover (L=2.5)", 2.5, 0.8, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | High crossover estimate (L=4.5)", 4.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | Central crossover estimate (L=3.5)", 3.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | Conservative crossover (L=2.5)", 2.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | Moderate interaction (L=1.5)", 1.5, 1.0, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | Subtle non-sig trend (L=1.0)", 1.0, 1.0, "Direct SD (Sec 4.9)"),
        ("Direct SD (sigma=1.0) | Small non-sig trend (L=0.5)", 0.5, 1.0, "Direct SD (Sec 4.9)"),
        
        # Converted SEM-to-SD regime (if error bars were SEM * sqrt(6))
        ("Converted SEM-to-SD (sigma=1.4) | High crossover estimate (L=4.5)", 4.5, 1.4, "Converted SEM (n=6)"),
        ("Converted SEM-to-SD (sigma=1.4) | Central crossover estimate (L=3.5)", 3.5, 1.4, "Converted SEM (n=6)"),
        ("Converted SEM-to-SD (sigma=1.4) | Conservative crossover (L=2.5)", 2.5, 1.4, "Converted SEM (n=6)"),
        ("Converted SEM-to-SD (sigma=1.4) | Moderate interaction (L=1.5)", 1.5, 1.4, "Converted SEM (n=6)"),
        ("Converted SEM-to-SD (sigma=1.4) | Subtle non-sig trend (L=1.0)", 1.0, 1.4, "Converted SEM (n=6)"),
        ("Converted SEM-to-SD (sigma=1.8) | High crossover estimate (L=4.5)", 4.5, 1.8, "High Converted SEM"),
        ("Converted SEM-to-SD (sigma=1.8) | Central crossover estimate (L=3.5)", 3.5, 1.8, "High Converted SEM"),
        ("Converted SEM-to-SD (sigma=1.8) | Conservative crossover (L=2.5)", 2.5, 1.8, "High Converted SEM"),
        ("Converted SEM-to-SD (sigma=1.8) | Subtle non-sig trend (L=1.0)", 1.0, 1.8, "High Converted SEM"),
    ]

    results = []

    for name, delta, sigma, regime in scenarios:
        n_per_group = required_n_for_interaction(delta, sigma, target_power=0.80)
        total_animals = n_per_group * 4  # 4 groups in 2x2 design
        std_effect = delta / sigma
        power_at_n = calculate_interaction_power(delta, sigma, n_per_group)
        
        # Compare to simple main effect of size delta/2 (e.g. single-sex effect)
        main_delta = delta / 2.0
        n_main = required_n_for_main_effect(main_delta, sigma, target_power=0.80)
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

    # Save to data/power_results.csv
    output_path = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/power_results.csv"
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

    print(f"Saved {len(results)} power scenarios to {output_path}")

if __name__ == "__main__":
    main()
