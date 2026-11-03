#!/usr/bin/env python3
"""
scripts/generate_manuscript_figures.py
Generates 5 publication-grade figures in 300 DPI PNG and vector (SVG and PDF) formats
in figures/:
  - fig1_preclinical_sex_audit
  - fig2_factorial_power_and_pk
  - fig3_peptide_biophysics_and_disorder
  - fig4_af3_cofolding_and_contacts
  - fig5_grp78_conservation_and_interactome
"""

import os
import csv
import json
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
from Bio.PDB import PDBParser

def norm_cdf(x):
    """Standard normal cumulative distribution function using math.erf."""
    return 0.5 * (1.0 + np.vectorize(math.erf)(x / np.sqrt(2.0)))


# Set publication style
plt.rcParams['font.sans-serif'] = 'DejaVu Sans'
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['axes.titlesize'] = 11
plt.rcParams['axes.labelsize'] = 10
plt.rcParams['xtick.labelsize'] = 8.5
plt.rcParams['ytick.labelsize'] = 8.5
plt.rcParams['legend.fontsize'] = 8.5
plt.rcParams['lines.linewidth'] = 1.5

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

# -------------------------------------------------------------
# FIGURE 1: Preclinical Sex Audit & ARRIVE 2.0 / SABV Compliance
# -------------------------------------------------------------
def generate_fig1():
    print("Generating Figure 1: Preclinical Sex Audit & Compliance...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Panel A: Disease Model by Sex Category
    categories = [
        "Type 2 Diabetes / IR",
        "Obesity / DIO",
        "NASH / Hepatic Steatosis",
        "Perimenopause IR",
        "PCOS",
        "Pharmacokinetics (PK)",
        "Colitis / Mucosal"
    ]
    male_only = [2, 1, 0, 0, 0, 0, 0]
    female_only = [0, 0, 0, 2, 2, 0, 0]
    both_sexes = [0, 0, 0, 0, 0, 1, 2]
    not_read = [4, 2, 3, 0, 0, 1, 0]

    y = np.arange(len(categories))
    height = 0.65

    c_male = "#2b5c8f"
    c_female = "#d95f02"
    c_both = "#2ca02c"
    c_notread = "#999999"

    ax1.barh(y, male_only, height, label="Male Only", color=c_male, edgecolor="black", linewidth=0.6)
    ax1.barh(y, female_only, height, left=male_only, label="Female Only", color=c_female, edgecolor="black", linewidth=0.6)
    left_both = [i + j for i, j in zip(male_only, female_only)]
    ax1.barh(y, both_sexes, height, left=left_both, label="Both Sexes", color=c_both, edgecolor="black", linewidth=0.6)
    left_nr = [i + j for i, j in zip(left_both, both_sexes)]
    ax1.barh(y, not_read, height, left=left_nr, label="Unstated / NOT_READ", color=c_notread, edgecolor="black", linewidth=0.6)

    ax1.set_yticks(y)
    ax1.set_yticklabels(categories)
    ax1.invert_yaxis()
    ax1.set_xlabel("Number of Primary in vivo Studies (N = 20)")
    ax1.set_title("A. Animal Sex Distribution across Disease Indications", fontweight="bold", loc="left")
    ax1.legend(loc="lower right", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax1.set_xlim(0, 7)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.grid(axis="x", linestyle="--", alpha=0.5)

    # Annotate total counts on bars
    for idx, (m, f, b, nr) in enumerate(zip(male_only, female_only, both_sexes, not_read)):
        total = m + f + b + nr
        ax1.text(total + 0.15, idx, f"n={total}", va="center", fontsize=8.5, fontweight="semibold")

    # Panel B: Methodological Compliance & SABV Quality Metrics
    metrics = [
        "A priori Power / Sample Size Calc",
        "Investigator / Assessor Blinding",
        "Random Sequence Generation Specified",
        "Estrous Baseline Staging in Females",
        "Formal Factorial Interaction Test ($p_{sex \\times rx}$)",
        "Both Sexes Included in Study",
        "Animal Sex Disclosed in Abstract/Methods"
    ]
    # Percentage compliance across N=20 (or relevant denominator)
    pcts = [0.0, 0.0, 0.0, 0.0, 0.0, 15.0, 50.0]
    
    y_m = np.arange(len(metrics))
    colors = ["#e41a1c" if p < 10 else "#ff7f00" if p < 30 else "#377eb8" for p in pcts]
    bars = ax2.barh(y_m, pcts, height=0.6, color=colors, edgecolor="black", linewidth=0.6)

    ax2.set_yticks(y_m)
    ax2.set_yticklabels(metrics)
    ax2.invert_yaxis()
    ax2.set_xlabel("Compliance Rate across Literature (%)")
    ax2.set_title("B. Methodological & SABV Compliance Rates", fontweight="bold", loc="left")
    ax2.set_xlim(0, 100)
    ax2.xaxis.set_major_locator(ticker.MultipleLocator(20))
    ax2.grid(axis="x", linestyle="--", alpha=0.5)

    for bar, pct in zip(bars, pcts):
        ax2.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, f"{pct:.1f}%", va="center", fontsize=8.5, fontweight="bold")

    for fmt in ["png", "svg", "pdf"]:
        outpath = os.path.join(FIG_DIR, f"fig1_preclinical_sex_audit.{fmt}")
        fig.savefig(outpath, dpi=300)
    plt.close(fig)
    print("Saved fig1_preclinical_sex_audit (PNG, SVG, PDF)")

# -------------------------------------------------------------
# FIGURE 2: Factorial Interaction Power & Pharmacokinetics
# -------------------------------------------------------------
def generate_fig2():
    print("Generating Figure 2: Factorial Power & Pharmacokinetics...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Panel A: 2x2 Factorial Interaction Power Curves
    # Calculate power analytically for two-way ANOVA interaction contrast L = (mu11 - mu12) - (mu21 - mu22)
    # Variance of L is 4 * sigma^2 / n. Non-centrality parameter delta = L / (2 * sigma / sqrt(n)) = (L / sigma) * sqrt(n) / 2
    n_vals = np.linspace(3, 30, 200)
    effect_sizes = [
        (0.5, "Small trend ($L/\\sigma = 0.5$)", "#999999", "--"),
        (0.8, "Subtle ($L/\\sigma = 0.8$)", "#377eb8", "-."),
        (1.0, "Moderate ($L/\\sigma = 1.0$)", "#ff7f00", "-"),
        (1.5, "Strong ($L/\\sigma = 1.5$)", "#984ea3", "-"),
        (2.0, "High crossover ($L/\\sigma = 2.0$)", "#e41a1c", "-")
    ]

    alpha = 0.05
    z_alpha = 1.95996398454

    for d_val, label, col, ls in effect_sizes:
        # 4 groups, total N = 4*n, df = 4*(n - 1)
        # Power approximated via non-central normal distribution
        ncp = (d_val / 2.0) * np.sqrt(n_vals)
        power = 1.0 - norm_cdf(z_alpha - ncp) + norm_cdf(-z_alpha - ncp)
        ax1.plot(n_vals, power * 100, label=label, color=col, linestyle=ls, linewidth=2.0)

    # Highlight typical preclinical sample size n=6
    n_typical = 6
    ncp_typ = (1.0 / 2.0) * np.sqrt(n_typical)
    power_typ = (1.0 - norm_cdf(z_alpha - ncp_typ)) * 100
    ax1.axvline(n_typical, color="black", linestyle=":", linewidth=1.2)

    ax1.scatter([n_typical], [power_typ], color="#e41a1c", s=70, zorder=5)
    ax1.annotate(f"Standard $n = 6$/group\nPower = {power_typ:.1f}% for $L/\\sigma = 1.0$\n(Massive False-Negative Deficit)",
                 xy=(n_typical, power_typ), xytext=(n_typical + 3, 20),
                 arrowprops=dict(arrowstyle="->", color="black", lw=1.2),
                 fontsize=8.5, fontweight="semibold", bbox=dict(boxstyle="round,pad=0.3", fc="#fff2f2", ec="#e41a1c", lw=0.8))

    ax1.axhline(80, color="gray", linestyle="--", linewidth=1.0)
    ax1.text(20, 82, "80% Target Statistical Power", fontsize=8.5, color="gray", fontweight="semibold")

    ax1.set_xlabel("Sample Size per Cell ($n$ per sex per treatment group)")
    ax1.set_ylabel("Statistical Power (%)")
    ax1.set_title("A. Statistical Power of $2 \\times 2$ Sex $\\times$ Treatment Factorial Designs", fontweight="bold", loc="left")
    ax1.set_xlim(3, 30)
    ax1.set_ylim(0, 105)
    ax1.legend(loc="lower right", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax1.grid(True, linestyle="--", alpha=0.5)

    # Panel B: Male vs Female PK Comparison (Valicherla et al. 2022)
    routes = ["IV (1 mg/kg)", "IP (1 mg/kg)", "SC (1 mg/kg)"]
    x = np.arange(len(routes))
    width = 0.35

    # Valicherla et al. 2022 Tables 4-5
    # Cmax (ng/mL)
    cmax_male = [1245.3, 342.1, 285.4]
    cmax_male_sd = [156.2, 42.5, 38.1]
    cmax_female = [1198.7, 328.6, 298.2]
    cmax_female_sd = [142.1, 39.8, 41.2]

    # Plot AUC_last (h*ng/mL)
    auc_male = [1580.4, 1502.8, 1234.6]
    auc_male_sd = [185.3, 162.1, 142.5]
    auc_female = [1524.2, 1445.6, 1289.1]
    auc_female_sd = [172.4, 151.8, 138.4]

    rects1 = ax2.bar(x - width/2, auc_male, width, yerr=auc_male_sd, capsize=4,
                     label="Male SD Rats ($n=3$)", color="#2b5c8f", edgecolor="black", linewidth=0.6)
    rects2 = ax2.bar(x + width/2, auc_female, width, yerr=auc_female_sd, capsize=4,
                     label="Female SD Rats ($n=3$)", color="#d95f02", edgecolor="black", linewidth=0.6)

    ax2.set_xticks(x)
    ax2.set_xticklabels(routes)
    ax2.set_ylabel("Systemic Exposure $\\mathrm{AUC}_{0-\\mathrm{last}}$ (h $\\cdot$ ng/mL)")
    ax2.set_title("B. Pharmacokinetic Equivalence across Sexes (Valicherla 2022)", fontweight="bold", loc="left")
    ax2.legend(loc="upper right", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax2.set_ylim(0, 2200)
    ax2.grid(axis="y", linestyle="--", alpha=0.5)

    # Annotate p-values showing lack of formal interaction test
    for idx, (m, f) in enumerate(zip(auc_male, auc_female)):
        ax2.text(idx, max(m, f) + 260, "p > 0.05 (pairwise)\nInteraction: Not Tested",
                 ha="center", fontsize=7.5, color="#555555", style="italic")

    for fmt in ["png", "svg", "pdf"]:
        outpath = os.path.join(FIG_DIR, f"fig2_factorial_power_and_pk.{fmt}")
        fig.savefig(outpath, dpi=300)
    plt.close(fig)
    print("Saved fig2_factorial_power_and_pk (PNG, SVG, PDF)")

# -------------------------------------------------------------
# FIGURE 3: Peptide Biophysics & Intrinsically Disordered Structure
# -------------------------------------------------------------
def generate_fig3():
    print("Generating Figure 3: Peptide Biophysics & Disorder Profile...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5), constrained_layout=True)

    # Panel A: Sliding Window Net Charge & Hydropathy across WT PST-29
    # Read sliding_window_profiles.csv
    csv_path = os.path.join(BASE_DIR, "data", "structures", "1d_sequences", "sliding_window_profiles.csv")
    windows = []
    charges = []
    hydropathies = []
    with open(csv_path) as fp:
        reader = csv.DictReader(fp)
        for row in reader:
            if row["peptide_id"] == "human_wt_pst_29":
                windows.append(int(row["window_start"]))
                charges.append(float(row["net_charge_sidechains_pH74"]))
                hydropathies.append(float(row["kyte_doolittle_hydropathy"]))

    ax1_twin = ax1.twinx()

    l1 = ax1.plot(windows, charges, color="#e41a1c", marker="o", linewidth=2.0, label="Net Charge (pH 7.4)")
    l2 = ax1_twin.plot(windows, hydropathies, color="#2b5c8f", marker="s", linewidth=2.0, label="Kyte-Doolittle Hydropathy")

    # Mark the polyanionic latch vs hydrophobic anchor
    # Window positions start at 1
    # Residues 14-21 are windows starting 14
    ax1.axvspan(14, 18, color="#ffebee", alpha=0.6, label="Acidic Latch (EEEEEMAV)")
    ax1.axvspan(21, 25, color="#e8f5e9", alpha=0.6, label="Hydrophobic Anchor (VPQGLFRG)")

    ax1.axvline(21.5, color="black", linestyle="--", linewidth=1.2)
    ax1.text(21.7, -4.5, "PSTi8\nTruncation\nBoundary", fontsize=8.5, fontweight="bold", color="black")

    ax1.set_xlabel("Sliding Window Center Residue (Window Size = 5, Human WT PST-29)")
    ax1.set_ylabel("Net Charge at pH 7.4 (Elementary Charges)", color="#e41a1c")
    ax1_twin.set_ylabel("Mean Kyte-Doolittle Hydropathy Index", color="#2b5c8f")
    ax1.tick_params(axis='y', labelcolor="#e41a1c")
    ax1_twin.tick_params(axis='y', labelcolor="#2b5c8f")
    ax1.set_title("A. Electrostatic Latch vs. Hydrophobic Anchor Architecture", fontweight="bold", loc="left")
    ax1.set_xlim(1, 26)
    ax1.grid(True, linestyle="--", alpha=0.4)

    # Combined legend
    lines = l1 + l2
    labels = [l.get_label() for l in lines]
    ax1.legend(lines, labels, loc="upper left", frameon=True, edgecolor="none", facecolor="#f0f0f0")

    # Panel B: AlphaFold CHGA Monomer pLDDT Profile (AF-P10645-F1)
    pdb_path = os.path.join(BASE_DIR, "data", "structures", "3d_models", "AF_P10645_F1_model.pdb")
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure("chga", pdb_path)
    res_nums = []
    plddts = []
    for atom in structure.get_atoms():
        if atom.get_name() == "CA":
            res_nums.append(atom.get_parent().id[1])
            plddts.append(atom.get_bfactor())

    res_nums = np.array(res_nums)
    plddts = np.array(plddts)

    ax2.plot(res_nums, plddts, color="#4daf4a", linewidth=1.5, label="Per-Residue pLDDT")
    ax2.axhline(50, color="#e41a1c", linestyle="--", linewidth=1.2, label="IDR Threshold (pLDDT < 50)")
    ax2.axhline(70, color="#ff7f00", linestyle=":", linewidth=1.0, label="Well-folded (pLDDT > 70)")

    # Highlight Pancreastatin domain (human precursor 268-319, PST-29 is 291-319)
    ax2.axvspan(268, 319, color="#ffcdd2", alpha=0.7, label="Pancreastatin Domain (Mean pLDDT = 36.8)")
    ax2.annotate("Pancreastatin IDR\nCoupled folding-and-binding\nrequired with GRP78",
                 xy=(295, 37), xytext=(240, 75),
                 arrowprops=dict(arrowstyle="->", color="#c62828", lw=1.2),
                 fontsize=8.5, fontweight="semibold", bbox=dict(boxstyle="round,pad=0.3", fc="#ffebee", ec="#c62828", lw=0.8))

    ax2.set_xlabel("Amino Acid Coordinate (Human Chromogranin A Precursor, P10645)")
    ax2.set_ylabel("AlphaFold Predicted Local Distance Difference Test (pLDDT)")
    ax2.set_title("B. Intrinsic Disorder Profile of CHGA & Pancreastatin", fontweight="bold", loc="left")
    ax2.set_xlim(1, 457)
    ax2.set_ylim(10, 100)
    ax2.legend(loc="upper right", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax2.grid(True, linestyle="--", alpha=0.5)

    for fmt in ["png", "svg", "pdf"]:
        outpath = os.path.join(FIG_DIR, f"fig3_peptide_biophysics_and_disorder.{fmt}")
        fig.savefig(outpath, dpi=300)
    plt.close(fig)
    print("Saved fig3_peptide_biophysics_and_disorder (PNG, SVG, PDF)")

# -------------------------------------------------------------
# FIGURE 4: AlphaFold 3 Co-Folding Confidence & Interface Contacts
# -------------------------------------------------------------
def generate_fig4():
    print("Generating Figure 4: AF3 Co-Folding & Interface Contacts...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13.5, 5.5), constrained_layout=True)

    # Panel A: Complex Metrics across 4 Complexes (ipTM, pTM, Pairwise ipTM, Min PAE)
    # Read af3_complex_metrics.csv
    csv_path = os.path.join(BASE_DIR, "data", "structures", "3d_models", "af3_complex_metrics.csv")
    data_by_complex = {}
    with open(csv_path) as fp:
        reader = csv.DictReader(fp)
        for r in reader:
            cid = r["peptide_name"]
            if cid not in data_by_complex:
                data_by_complex[cid] = {"iptm": [], "ptm": [], "pair_iptm": [], "min_pae": [], "rank": []}
            data_by_complex[cid]["iptm"].append(float(r["iptm"]))
            data_by_complex[cid]["ptm"].append(float(r["ptm"]))
            data_by_complex[cid]["pair_iptm"].append(float(r["pairwise_chain_iptm_AB"]))
            data_by_complex[cid]["min_pae"].append(float(r["min_pae_AB"]))
            data_by_complex[cid]["rank"].append(float(r["ranking_score"]))

    complex_order = ["PSTi8", "WT_PST29", "E287K_PST29", "G297S_PST29"]
    labels = ["PSTi8 (1-21)\nInhibitor", "WT PST-29\nFull Hormone", "E287K PST-29\nCore Variant", "G297S PST-29\nDiabetogenic"]
    
    x = np.arange(len(complex_order))
    width = 0.2

    iptm_means = [np.mean(data_by_complex[c]["iptm"]) for c in complex_order]
    iptm_stds = [np.std(data_by_complex[c]["iptm"]) for c in complex_order]
    
    ptm_means = [np.mean(data_by_complex[c]["ptm"]) for c in complex_order]
    ptm_stds = [np.std(data_by_complex[c]["ptm"]) for c in complex_order]

    pair_means = [np.mean(data_by_complex[c]["pair_iptm"]) for c in complex_order]
    pair_stds = [np.std(data_by_complex[c]["pair_iptm"]) for c in complex_order]

    rank_means = [np.mean(data_by_complex[c]["rank"]) for c in complex_order]
    rank_stds = [np.std(data_by_complex[c]["rank"]) for c in complex_order]

    ax1.bar(x - 1.5*width, rank_means, width, yerr=rank_stds, capsize=3, label="Model Ranking Score", color="#377eb8", edgecolor="black", lw=0.6)
    ax1.bar(x - 0.5*width, iptm_means, width, yerr=iptm_stds, capsize=3, label="Complex ipTM", color="#4daf4a", edgecolor="black", lw=0.6)
    ax1.bar(x + 0.5*width, ptm_means, width, yerr=ptm_stds, capsize=3, label="Complex pTM", color="#984ea3", edgecolor="black", lw=0.6)
    ax1.bar(x + 1.5*width, pair_means, width, yerr=pair_stds, capsize=3, label="Receptor-Peptide Pairwise ipTM", color="#ff7f00", edgecolor="black", lw=0.6)

    # Annotate minimum inter-chain PAE above bars
    min_pae_seed0 = [2.30, 2.89, 3.71, 5.54]
    for idx, pae in enumerate(min_pae_seed0):
        ax1.text(idx, 0.92, f"Min PAE:\n{pae:.2f} Å", ha="center", fontsize=8.0, fontweight="bold",
                 bbox=dict(boxstyle="round,pad=0.2", fc="#f9f9f9", ec="#cccccc", lw=0.5))

    ax1.set_xticks(x)
    ax1.set_xticklabels(labels)
    ax1.set_ylabel("AlphaFold 3 Confidence Score")
    ax1.set_title("A. Quaternary Co-Folding Confidence (5 Diffusion Samples, modelSeeds [1])", fontweight="bold", loc="left")
    ax1.set_ylim(0, 1.05)
    ax1.legend(loc="lower left", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax1.grid(axis="y", linestyle="--", alpha=0.5)

    # Panel B: Contact Breakdown by Domain (<4.0 A in Model 0)
    # Data from af3_interface_contacts.csv
    # PSTi8: NBD=0, Linker=5, SBDbeta=8
    # WT_PST29: NBD=6, Linker=7, SBDbeta=19
    # E287K: NBD=5, Linker=6, SBDbeta=15
    # G297S: NBD=0, Linker=7, SBDbeta=13
    domain_contacts = {
        "NBD (Residues 1-407)": [0, 6, 5, 0],
        "Interdomain Linker (408-426)": [5, 7, 6, 7],
        "SBD$\\beta$ Cleft (427-537)": [8, 19, 15, 13]
    }

    colors_dom = ["#e41a1c", "#377eb8", "#4daf4a"]
    bottom = np.zeros(len(complex_order))

    for (d_name, counts), col in zip(domain_contacts.items(), colors_dom):
        ax2.bar(x, counts, width=0.5, bottom=bottom, label=d_name, color=col, edgecolor="black", lw=0.6)
        bottom += np.array(counts)

    # Total contact annotations
    total_contacts = [48, 140, 137, 79]
    unique_residues = [13, 32, 26, 20]
    for idx, (tot, res) in enumerate(zip(total_contacts, unique_residues)):
        ax2.text(idx, bottom[idx] + 1.5, f"{tot} atomic contacts\n({res} residues)", ha="center", fontsize=8.0, fontweight="bold")

    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    ax2.set_ylabel("Number of Contacting GRP78 Residues (< 4.0 Å)")
    ax2.set_title("B. GRP78 Domain Contact Footprint: Allosteric Wedge vs. Clamp", fontweight="bold", loc="left")
    ax2.set_ylim(0, 42)
    ax2.legend(loc="upper left", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax2.grid(axis="y", linestyle="--", alpha=0.5)

    # Annotate the mechanistic discoveries
    ax2.text(0, 18, "Steric Wedge\n(0 NBD contacts)", ha="center", fontsize=7.5, fontweight="bold", color="#2b5c8f")
    ax2.text(1, 35, "Tri-Domain\nClamp", ha="center", fontsize=7.5, fontweight="bold", color="#1b7837")
    ax2.text(3, 23, "G297S Collapse:\n0 NBD contacts\n-43.6% atomic contacts", ha="center", fontsize=7.5, fontweight="bold", color="#c62828")

    for fmt in ["png", "svg", "pdf"]:
        outpath = os.path.join(FIG_DIR, f"fig4_af3_cofolding_and_contacts.{fmt}")
        fig.savefig(outpath, dpi=300)
    plt.close(fig)
    print("Saved fig4_af3_cofolding_and_contacts (PNG, SVG, PDF)")

# -------------------------------------------------------------
# FIGURE 5: GRP78 Conservation & Functional Signaling Interactome
# -------------------------------------------------------------
def generate_fig5():
    print("Generating Figure 5: GRP78 Conservation & Functional Interactome...")
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True)

    # Panel A: Cross-Species GRP78 Conservation across Functional Domains
    domains = [
        "Full Mature GRP78\n(19-654)",
        "Nucleotide-Binding (NBD)\n(26-407)",
        "Interdomain Linker\n(408-426)",
        "Substrate Cleft (SBD$\\beta$)\n(427-537)",
        "Substrate Lid (SBD$\\alpha$)\n(538-633)",
        "C-terminal KDEL Tail\n(634-654)"
    ]
    # Human vs Mouse % identity
    h_v_m = [99.53, 99.47, 100.0, 100.00, 99.00, 95.24]
    # Human vs Rat % identity
    h_v_r = [99.37, 99.21, 100.0, 100.00, 99.00, 95.24]

    y = np.arange(len(domains))
    height = 0.35

    rects1 = ax1.barh(y - height/2, h_v_m, height, label="Human vs. Mouse (P11021 vs. P20029)", color="#2b5c8f", edgecolor="black", lw=0.6)
    rects2 = ax1.barh(y + height/2, h_v_r, height, label="Human vs. Rat (P11021 vs. P06761)", color="#e41a1c", edgecolor="black", lw=0.6)

    # Highlight 100% conservation of SBDbeta
    ax1.axvspan(99.95, 100.05, color="#e8f5e9", alpha=0.5)

    ax1.set_yticks(y)
    ax1.set_yticklabels(domains)
    ax1.invert_yaxis()
    ax1.set_xlabel("Sequence Identity (%)")
    ax1.set_title("A. Cross-Species GRP78 Conservation: 100% Cleft Invariance", fontweight="bold", loc="left")
    ax1.set_xlim(92, 101.5)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(2))
    ax1.legend(loc="lower left", frameon=True, edgecolor="none", facecolor="#f0f0f0")
    ax1.grid(axis="x", linestyle="--", alpha=0.5)

    for idx, (vm, vr) in enumerate(zip(h_v_m, h_v_r)):
        ax1.text(vm + 0.3, idx - height/2, f"{vm:.2f}%", va="center", fontsize=8.0, fontweight="bold", color="#2b5c8f")
        ax1.text(vr + 0.3, idx + height/2, f"{vr:.2f}%", va="center", fontsize=8.0, fontweight="bold", color="#e41a1c")

    # Panel B: Functional Signaling Network & Compartmentalization Bridge
    # Schematic network diagram representing ER lumen vs Cell Surface
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis("off")
    ax2.set_title("B. Compartmentalized GRP78 Signaling Network & Insulin Resistance Bridge", fontweight="bold", loc="left")

    # Draw compartment boxes
    # ER Lumen (top half)
    er_box = FancyBboxPatch((0.5, 5.2), 9.0, 4.3, boxstyle="round,pad=0.2",
                            fc="#eef6fb", ec="#2b5c8f", lw=1.5, linestyle="--")
    ax2.add_patch(er_box)
    ax2.text(0.8, 9.1, "ER LUMEN (UPR Chaperone Function)", fontsize=9.0, fontweight="bold", color="#2b5c8f")

    # Plasma Membrane & Cytosol (bottom half)
    cyto_box = FancyBboxPatch((0.5, 0.5), 9.0, 4.3, boxstyle="round,pad=0.2",
                             fc="#fdf7f2", ec="#d95f02", lw=1.5, linestyle="-")
    ax2.add_patch(cyto_box)
    ax2.text(0.8, 4.4, "CYTOSOL & PLASMA MEMBRANE (Pathogenic Signaling)", fontsize=9.0, fontweight="bold", color="#d95f02")

    # Nodes in ER Lumen
    # GRP78, IRE1alpha, PERK, ATF6
    def draw_node(x, y, label, sublabel, color, ec="black"):
        box = FancyBboxPatch((x-1.1, y-0.4), 2.2, 0.8, boxstyle="round,pad=0.1", fc=color, ec=ec, lw=1.0)
        ax2.add_patch(box)
        ax2.text(x, y+0.08, label, ha="center", va="center", fontsize=8.5, fontweight="bold")
        if sublabel:
            ax2.text(x, y-0.2, sublabel, ha="center", va="center", fontsize=7.0, style="italic")

    draw_node(5.0, 7.8, "GRP78 (BiP)", "HSPA5 (0.999)", "#ffffff", "#2b5c8f")
    draw_node(2.0, 6.2, "IRE1α", "ERN1 (Score: 0.999)", "#d0e1f9")
    draw_node(5.0, 6.2, "PERK", "EIF2AK3 (0.999)", "#d0e1f9")
    draw_node(8.0, 6.2, "ATF6", "Sensor (0.999)", "#d0e1f9")

    # Edges in ER
    ax2.annotate("", xy=(2.0, 6.6), xytext=(4.2, 7.5), arrowprops=dict(arrowstyle="-", color="#2b5c8f", lw=1.5))
    ax2.annotate("", xy=(5.0, 6.6), xytext=(5.0, 7.4), arrowprops=dict(arrowstyle="-", color="#2b5c8f", lw=1.5))
    ax2.annotate("", xy=(8.0, 6.6), xytext=(5.8, 7.5), arrowprops=dict(arrowstyle="-", color="#2b5c8f", lw=1.5))

    # Stress Translocation Arrow
    ax2.annotate("ER Stress Translocation\n(Circulating GRP78)",
                 xy=(5.0, 3.8), xytext=(5.0, 5.0),
                 arrowprops=dict(arrowstyle="->", color="#c62828", lw=2.0, linestyle=":"),
                 ha="center", fontsize=8.0, fontweight="bold", color="#c62828")

    # Nodes in Cytosol
    # TRAF2, JNK1, IRS-1 (Ser307), Cell-Surface GRP78, AKT1
    draw_node(2.0, 3.5, "TRAF2", "Adaptor (0.686)", "#fed9a6")
    draw_node(2.0, 2.0, "JNK1 (MAPK8)", "Kinase (0.666)", "#fbb4ae")
    draw_node(2.0, 0.9, "IRS1 (Ser307)", "IR Uncoupling (0.993)", "#e41a1c", ec="black")

    # Cell-Surface GRP78 + PSTi8
    draw_node(7.5, 3.2, "csGRP78", "Cell Surface Receptor", "#ffffff", "#d95f02")
    draw_node(7.5, 1.8, "AKT1", "Insulin Signaling (0.960)", "#b3cde3")
    
    # PSTi8 intervention box
    psti8_box = FancyBboxPatch((6.4, 4.0), 2.2, 0.6, boxstyle="round,pad=0.1", fc="#c8e6c9", ec="#2ca02c", lw=1.2)
    ax2.add_patch(psti8_box)
    ax2.text(7.5, 4.3, "PSTi8 (Inhibitor)", ha="center", va="center", fontsize=8.0, fontweight="bold", color="#1b5e20")
    ax2.annotate("", xy=(7.5, 3.6), xytext=(7.5, 4.0), arrowprops=dict(arrowstyle="-|>", color="#2ca02c", lw=1.8))

    # Signaling edges
    ax2.annotate("", xy=(2.0, 3.1), xytext=(2.0, 2.4), arrowprops=dict(arrowstyle="->", color="#d95f02", lw=1.5))
    ax2.annotate("", xy=(2.0, 1.6), xytext=(2.0, 1.3), arrowprops=dict(arrowstyle="->", color="#c62828", lw=1.8))
    ax2.annotate("Inhibitory Phosphorylation\n(Ser307)", xy=(3.2, 1.2), xytext=(3.5, 1.6),
                 arrowprops=dict(arrowstyle="->", color="#c62828", lw=1.0),
                 fontsize=7.5, color="#c62828", fontweight="bold")

    ax2.annotate("", xy=(7.5, 2.8), xytext=(7.5, 2.2), arrowprops=dict(arrowstyle="<->", color="#2b5c8f", lw=1.5))

    for fmt in ["png", "svg", "pdf"]:
        outpath = os.path.join(FIG_DIR, f"fig5_grp78_conservation_and_interactome.{fmt}")
        fig.savefig(outpath, dpi=300)
    plt.close(fig)
    print("Saved fig5_grp78_conservation_and_interactome (PNG, SVG, PDF)")

def main():
    print("=== Generating 5 Publication-Grade Manuscript Figures ===")
    generate_fig1()
    generate_fig2()
    generate_fig3()
    generate_fig4()
    generate_fig5()
    print("=== All 5 Figures Generated Successfully in figures/ ===")

if __name__ == "__main__":
    main()
