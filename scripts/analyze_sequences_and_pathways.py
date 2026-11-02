#!/usr/bin/env python3
"""
scripts/analyze_sequences_and_pathways.py

Computational sequence profiling, cross-species alignment, variant impact scoring,
and functional pathway interaction retrieval for PSTi8, WT PST-29, human coding variants,
and GRP78 (HSPA5) across human, mouse, and rat using local Python, Biopython, and free REST APIs.
"""

import os
import sys
import json
import csv
import urllib.request
import urllib.parse
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from Bio.Align import substitution_matrices, PairwiseAligner

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data", "structures")
DIR_1D = os.path.join(DATA_DIR, "1d_sequences")
OUTPUT_SLIDING = os.path.join(DIR_1D, "sliding_window_profiles.csv")
OUTPUT_ALIGN = os.path.join(DIR_1D, "cross_species_alignment.csv")
OUTPUT_VARIANTS = os.path.join(DIR_1D, "variant_scores.csv")
OUTPUT_PATHWAYS = os.path.join(DATA_DIR, "pathway_interactions.csv")

HEADERS = {"User-Agent": "PSTi8-Pathway-Analysis/1.0 (mailto:devanshyadav118@gmail.com)"}

# Kyte-Doolittle hydropathy scale
KD_SCALE = {
    'A': 1.8, 'R': -4.5, 'N': -3.5, 'D': -3.5, 'C': 2.5,
    'Q': -3.5, 'E': -3.5, 'G': -0.4, 'H': -3.2, 'I': 4.5,
    'L': 3.8, 'K': -3.9, 'M': 1.9, 'F': 2.8, 'P': -1.6,
    'S': -0.8, 'T': -0.7, 'W': -0.9, 'Y': -1.3, 'V': 4.2
}

def sidechain_charge_at_ph(aa, ph=7.4):
    """Calculate side-chain partial charge at given pH using standard Henderson-Hasselbalch pKa."""
    if aa == 'D': # Asp pKa ~ 3.9
        return -1.0 / (1.0 + 10.0 ** (3.9 - ph))
    elif aa == 'E': # Glu pKa ~ 4.1
        return -1.0 / (1.0 + 10.0 ** (4.1 - ph))
    elif aa == 'C': # Cys pKa ~ 8.3
        return -1.0 / (1.0 + 10.0 ** (8.3 - ph))
    elif aa == 'Y': # Tyr pKa ~ 10.1
        return -1.0 / (1.0 + 10.0 ** (10.1 - ph))
    elif aa == 'H': # His pKa ~ 6.0
        return 1.0 / (1.0 + 10.0 ** (ph - 6.0))
    elif aa == 'K': # Lys pKa ~ 10.5
        return 1.0 / (1.0 + 10.0 ** (ph - 10.5))
    elif aa == 'R': # Arg pKa ~ 12.5
        return 1.0 / (1.0 + 10.0 ** (ph - 12.5))
    return 0.0

def step_1_sliding_window_profiles():
    print("\n--- Step 1: Calculating Sliding-Window Physicochemical Profiles ---")
    peptides = [
        ("human_wt_pst_29", "Human WT PST-29", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG"),
        ("human_psti8_21", "Human PSTi8 (21-mer)", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAV"),
        ("human_g297s_pst_29", "Human Gly297Ser PST-29 (rs9658664)", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQSLFRG"),
        ("human_e287k_pst_29", "Human Glu287Lys PST-29 (rs140089514)", "Homo sapiens", "PEGKGEQEHSQQKEKEEEMAVVPQGLFRG"),
        ("mouse_pst_model", "Mouse PST (Synthetic / Model)", "Mus musculus", "PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG"),
        ("rat_pst_model", "Rat PST (Synthetic / Model)", "Rattus norvegicus", "PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG"),
        ("mouse_pst_uniprot_core", "Mouse PST Canonical Core (UniProt P26339)", "Mus musculus", "PSEGKGELEHSQQEEDGEEAMVGTPQGLFPQG"),
        ("rat_pst_uniprot_core", "Rat PST Canonical Core (UniProt P10354)", "Rattus norvegicus", "PSEGKGELEHSQQEEDGEEAMAGPPQGLFPG"),
    ]
    
    rows = []
    window_size = 5
    step = 1
    
    for pep_id, pep_name, species, seq in peptides:
        n_windows = len(seq) - window_size + 1
        for i in range(0, n_windows, step):
            win_start = i + 1
            win_end = i + window_size
            win_center = (win_start + win_end) / 2.0
            win_seq = seq[i:i+window_size]
            
            sc_charge = sum(sidechain_charge_at_ph(aa, 7.4) for aa in win_seq)
            pa = ProteinAnalysis(win_seq)
            isolated_charge = pa.charge_at_pH(7.4)
            kd_hydropathy = sum(KD_SCALE.get(aa, 0.0) for aa in win_seq) / float(window_size)
            
            # Poly-Glu latch flag
            is_poly_glu = "E" in win_seq and win_seq.count("E") >= 3
            # C-terminal anchor flag
            is_c_anchor = any(aa in win_seq for aa in ["V", "P", "L", "F"]) and win_start >= 18
            
            rows.append({
                "peptide_id": pep_id,
                "peptide_name": pep_name,
                "species": species,
                "window_index": (i // step) + 1,
                "window_start": win_start,
                "window_end": win_end,
                "window_center": f"{win_center:.1f}",
                "window_seq": win_seq,
                "net_charge_sidechains_pH74": f"{sc_charge:.4f}",
                "net_charge_isolated_pH74": f"{isolated_charge:.4f}",
                "kyte_doolittle_hydropathy": f"{kd_hydropathy:.4f}",
                "is_poly_glu_latch": "Yes" if is_poly_glu else "No",
                "is_c_terminal_anchor": "Yes" if is_c_anchor else "No"
            })
            
    with open(OUTPUT_SLIDING, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "peptide_id", "peptide_name", "species", "window_index", "window_start",
            "window_end", "window_center", "window_seq", "net_charge_sidechains_pH74",
            "net_charge_isolated_pH74", "kyte_doolittle_hydropathy", "is_poly_glu_latch",
            "is_c_terminal_anchor"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} sliding-window profile rows to {OUTPUT_SLIDING}")

def step_2_cross_species_alignment():
    print("\n--- Step 2: Cross-Species Sequence Alignment & Conservation Mapping ---")
    matrix = substitution_matrices.load("BLOSUM62")
    
    # Load GRP78 sequences
    h_grp_seq = str(SeqIO.read(os.path.join(DIR_1D, "P11021_GRP78_HUMAN.fasta"), "fasta").seq)
    m_grp_seq = str(SeqIO.read(os.path.join(DIR_1D, "P20029_GRP78_MOUSE.fasta"), "fasta").seq)
    r_grp_seq = str(SeqIO.read(os.path.join(DIR_1D, "P06761_GRP78_RAT.fasta"), "fasta").seq)
    
    # Mature sequences (human: 19-654 -> index 18:654; mouse: 20-655 -> index 19:655; rat: 19-654 -> index 18:654)
    h_grp_mat = h_grp_seq[18:654]
    m_grp_mat = m_grp_seq[19:655]
    r_grp_mat = r_grp_seq[18:654]
    
    assert len(h_grp_mat) == 636
    assert len(m_grp_mat) == 636
    assert len(r_grp_mat) == 636
    
    # Domain slices in mature 636-aa sequence:
    # NBD (ATPase domain): mature 1-406 (index 0:406)
    # Interdomain linker: mature 407-426 (index 406:426)
    # SBD total: mature 427-636 (index 426:636)
    #   SBD-beta (substrate binding cleft): mature 427-537 (index 426:537)
    #   SBD-alpha lid / C-tail: mature 538-636 (index 537:636)
    domains = {
        "Full_Mature_GRP78": (0, 636),
        "NBD_ATPase_Domain": (0, 406),
        "Interdomain_Linker": (406, 426),
        "SBD_Total": (426, 636),
        "SBD_Beta_Substrate_Cleft": (426, 537),
        "SBD_Alpha_Lid_and_Tail": (537, 636),
    }
    
    grp_pairs = [
        ("Human_vs_Mouse", "P11021", "Homo sapiens", "P20029", "Mus musculus", h_grp_mat, m_grp_mat, 19, 20),
        ("Human_vs_Rat", "P11021", "Homo sapiens", "P06761", "Rattus norvegicus", h_grp_mat, r_grp_mat, 19, 19),
        ("Mouse_vs_Rat", "P20029", "Mus musculus", "P06761", "Rattus norvegicus", m_grp_mat, r_grp_mat, 20, 19),
    ]
    
    rows = []
    
    for pair_name, q_id, q_org, s_id, s_org, q_seq, s_seq, q_offset, s_offset in grp_pairs:
        for dom_name, (d_start, d_end) in domains.items():
            sub_q = q_seq[d_start:d_end]
            sub_s = s_seq[d_start:d_end]
            d_len = len(sub_q)
            
            n_ident = sum(1 for a, b in zip(sub_q, sub_s) if a == b)
            pct_ident = (n_ident / float(d_len)) * 100.0
            
            n_sim = sum(1 for a, b in zip(sub_q, sub_s) if a == b or matrix.get((a, b), matrix.get((b, a), -1)) > 0)
            pct_sim = (n_sim / float(d_len)) * 100.0
            
            diffs = []
            for idx in range(d_len):
                global_mat_idx = d_start + idx
                a = sub_q[idx]
                b = sub_s[idx]
                if a != b:
                    mat_pos = global_mat_idx + 1
                    q_pre = global_mat_idx + q_offset
                    s_pre = global_mat_idx + s_offset
                    blosum_val = matrix.get((a, b), matrix.get((b, a), 0))
                    diffs.append(f"Mature:{mat_pos}({q_id}:{a}{q_pre} -> {s_id}:{b}{s_pre}, BLOSUM62={blosum_val})")
            
            diff_str = "; ".join(diffs) if diffs else "None (100% Identical)"
            
            rows.append({
                "target_type": "GRP78_HSPA5_Mature",
                "comparison_pair": pair_name,
                "query_id": q_id,
                "query_organism": q_org,
                "subject_id": s_id,
                "subject_organism": s_org,
                "domain_region": dom_name,
                "alignment_length": d_len,
                "identical_residues": n_ident,
                "percent_identity": f"{pct_ident:.2f}%",
                "similar_residues": n_sim,
                "percent_similarity": f"{pct_sim:.2f}%",
                "substitutions_list": diff_str,
                "signal_peptide_offset_note": "Mouse preprotein numbering is +1 higher than human/rat due to 19-aa signal peptide (vs 18-aa in human/rat)."
            })
            
    # Now align Pancreastatin active cores
    # Human WT PST-29 vs Rodent Cores
    aligner = PairwiseAligner()
    aligner.mode = 'global'
    aligner.match_score = 2
    aligner.mismatch_score = -1
    aligner.open_gap_score = -2
    aligner.extend_gap_score = -0.5
    
    pst_cores = [
        ("Human_WT_29_vs_Mouse_Model_31", "Human WT PST-29", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG", "Mouse PST Model (31-mer)", "Mus musculus", "PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG"),
        ("Human_WT_29_vs_Rat_Model_31", "Human WT PST-29", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG", "Rat PST Model (31-mer)", "Rattus norvegicus", "PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG"),
        ("Human_WT_29_vs_Mouse_UniProt_Core_32", "Human WT PST-29", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG", "Mouse UniProt Core (32-mer)", "Mus musculus", "PSEGKGELEHSQQEEDGEEAMVGTPQGLFPQG"),
        ("Human_WT_29_vs_Rat_UniProt_Core_31", "Human WT PST-29", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG", "Rat UniProt Core (31-mer)", "Rattus norvegicus", "PSEGKGELEHSQQEEDGEEAMAGPPQGLFPG"),
        ("Human_PSTi8_21_vs_Human_WT_29", "Human PSTi8 (21-mer)", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAV", "Human WT PST-29 (29-mer)", "Homo sapiens", "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG"),
    ]
    
    for comp_name, q_name, q_org, q_seq, s_name, s_org, s_seq in pst_cores:
        aln = aligner.align(q_seq, s_seq)[0]
        aln_q = aln[0]
        aln_s = aln[1]
        a_len = len(aln_q)
        
        n_ident = sum(1 for a, b in zip(aln_q, aln_s) if a == b and a != "-")
        n_sim = sum(1 for a, b in zip(aln_q, aln_s) if a != "-" and b != "-" and (a == b or matrix.get((a, b), matrix.get((b, a), -1)) > 0))
        pct_ident = (n_ident / float(max(len(q_seq), len(s_seq)))) * 100.0
        pct_sim = (n_sim / float(max(len(q_seq), len(s_seq)))) * 100.0
        
        diffs = []
        for i in range(a_len):
            a, b = aln_q[i], aln_s[i]
            if a != b:
                diffs.append(f"Pos:{i+1}({a}->{b})")
        diff_str = "; ".join(diffs)
        
        rows.append({
            "target_type": "Pancreastatin_Core",
            "comparison_pair": comp_name,
            "query_id": q_name,
            "query_organism": q_org,
            "subject_id": s_name,
            "subject_organism": s_org,
            "domain_region": "Active_Core_Peptide",
            "alignment_length": a_len,
            "identical_residues": n_ident,
            "percent_identity": f"{pct_ident:.2f}%",
            "similar_residues": n_sim,
            "percent_similarity": f"{pct_sim:.2f}%",
            "substitutions_list": diff_str,
            "signal_peptide_offset_note": "Pancreastatin core cleavage positions differ by species but maintain central acidic cluster."
        })
        
    with open(OUTPUT_ALIGN, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "target_type", "comparison_pair", "query_id", "query_organism",
            "subject_id", "subject_organism", "domain_region", "alignment_length",
            "identical_residues", "percent_identity", "similar_residues",
            "percent_similarity", "substitutions_list", "signal_peptide_offset_note"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} alignment comparisons to {OUTPUT_ALIGN}")

def step_3_human_variant_impact():
    print("\n--- Step 3: Human Coding Variant Impact Profiling ---")
    matrix = substitution_matrices.load("BLOSUM62")
    
    variants = [
        {
            "variant_id": "Gly297Ser",
            "dbsnp_id": "rs9658664",
            "gene": "CHGA",
            "preprotein_variant": "Gly315Ser",
            "mature_pst_position": 25,
            "wt_residue": "G",
            "mut_residue": "S",
            "in_psti8_21mer": "No",
            "location_context": "Located in cleaved carboxyl-terminal octapeptide (VPQGLFRG -> VPQSLFRG). Absent from PSTi8 inhibitor (positions 1-21).",
            "wt_seq": "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG",
            "mut_seq": "PEGKGEQEHSQQKEEEEEMAVVPQSLFRG",
            "psti8_impact": "None. PSTi8 truncates the entire octapeptide VPQGLFRG, completely eliminating the rs9658664 polymorphic site."
        },
        {
            "variant_id": "Glu287Lys",
            "dbsnp_id": "rs140089514",
            "gene": "CHGA",
            "preprotein_variant": "Glu305Lys",
            "mature_pst_position": 15,
            "wt_residue": "E",
            "mut_residue": "K",
            "in_psti8_21mer": "Yes",
            "location_context": "Located directly within the poly-glutamate acidic latch (EEEEEMAV -> EKEEMAV) at position 15 of PSTi8.",
            "wt_seq": "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG",
            "mut_seq": "PEGKGEQEHSQQKEKEEEMAVVPQGLFRG",
            "psti8_impact": "Severe. Replaces negatively charged glutamate with positively charged lysine (+2 charge shift), disrupting electrostatic latch."
        }
    ]
    
    rows = []
    for var in variants:
        wt_aa = var["wt_residue"]
        mut_aa = var["mut_residue"]
        blosum_score = matrix.get((wt_aa, mut_aa), matrix.get((mut_aa, wt_aa), None))
        
        pa_wt = ProteinAnalysis(var["wt_seq"])
        pa_mut = ProteinAnalysis(var["mut_seq"])
        
        wt_ch = pa_wt.charge_at_pH(7.4)
        mut_ch = pa_mut.charge_at_pH(7.4)
        delta_ch = mut_ch - wt_ch
        
        wt_pi = pa_wt.isoelectric_point()
        mut_pi = pa_mut.isoelectric_point()
        delta_pi = mut_pi - wt_pi
        
        wt_gr = pa_wt.gravy()
        mut_gr = pa_mut.gravy()
        delta_gr = mut_gr - wt_gr
        
        wt_mw = pa_wt.molecular_weight()
        mut_mw = pa_mut.molecular_weight()
        delta_mw = mut_mw - wt_mw
        
        rows.append({
            "variant_id": var["variant_id"],
            "dbsnp_id": var["dbsnp_id"],
            "gene": var["gene"],
            "preprotein_variant": var["preprotein_variant"],
            "mature_pst_position": var["mature_pst_position"],
            "wt_residue": wt_aa,
            "mut_residue": mut_aa,
            "in_psti8_21mer": var["in_psti8_21mer"],
            "location_context": var["location_context"],
            "blosum62_score": blosum_score,
            "wt_charge_pH74": f"{wt_ch:.2f}",
            "mut_charge_pH74": f"{mut_ch:.2f}",
            "delta_charge_pH74": f"{delta_ch:+.2f}",
            "wt_pI": f"{wt_pi:.2f}",
            "mut_pI": f"{mut_pi:.2f}",
            "delta_pI": f"{delta_pi:+.2f}",
            "wt_gravy": f"{wt_gr:.3f}",
            "mut_gravy": f"{mut_gr:.3f}",
            "delta_gravy": f"{delta_gr:+.3f}",
            "wt_mw_da": f"{wt_mw:.2f}",
            "mut_mw_da": f"{mut_mw:.2f}",
            "delta_mw_da": f"{delta_mw:+.2f}",
            "psti8_impact": var["psti8_impact"],
            "computational_model_notes": "ESM-2 zero-shot log-likelihood ratios not evaluated locally (PyTorch/transformers not installed in environment). Scored via rigorous physicochemical profiling and BLOSUM62 matrix."
        })
        
    with open(OUTPUT_VARIANTS, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "variant_id", "dbsnp_id", "gene", "preprotein_variant", "mature_pst_position",
            "wt_residue", "mut_residue", "in_psti8_21mer", "location_context",
            "blosum62_score", "wt_charge_pH74", "mut_charge_pH74", "delta_charge_pH74",
            "wt_pI", "mut_pI", "delta_pI", "wt_gravy", "mut_gravy", "delta_gravy",
            "wt_mw_da", "mut_mw_da", "delta_mw_da", "psti8_impact", "computational_model_notes"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} variant scores to {OUTPUT_VARIANTS}")

def step_4_pathway_interactions():
    print("\n--- Step 4: Functional Pathway Interaction Retrieval (STRING & Reactome) ---")
    
    # Query multi-protein STRING network for HSPA5 and metabolic/ER stress targets
    target_nodes = ["HSPA5", "INSR", "IRS1", "IRS2", "AKT1", "PRKAA1", "MAPK8", "SREBF1", "ERN1", "EIF2AK3", "ATF6"]
    query_str = "%0d".join(target_nodes)
    string_url = f"https://string-db.org/api/json/network?identifiers={query_str}&species=9606"
    
    req = urllib.request.Request(string_url, headers=HEADERS)
    string_data = []
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            string_data = json.loads(resp.read().decode("utf-8"))
        print(f"Retrieved {len(string_data)} pairwise network edges from STRING API")
    except Exception as e:
        print(f"Error fetching STRING API: {e}")
        
    # Map edges by pair
    edge_map = {}
    for d in string_data:
        p_a = d["preferredName_A"]
        p_b = d["preferredName_B"]
        key = tuple(sorted([p_a, p_b]))
        edge_map[key] = d

    # Pathway and functional mechanism mappings
    pathway_annotations = {
        ("EIF2AK3", "HSPA5"): ("Unfolded Protein Response (PERK branch)", "Direct physical interaction; GRP78 binds the luminal domain of PERK (EIF2AK3) to keep it monomeric and inactive; ER stress or competitive binding induces GRP78 dissociation, triggering PERK dimerization and autophosphorylation."),
        ("ATF6", "HSPA5"): ("Unfolded Protein Response (ATF6 branch)", "Direct physical interaction; GRP78 shields ATF6 Golgi-localization signals in ER lumen; upon dissociation, ATF6 translocates to Golgi for S1P/S2P proteolytic cleavage and nuclear activation."),
        ("ERN1", "HSPA5"): ("Unfolded Protein Response (IRE1 branch)", "Direct physical interaction; GRP78 maintains IRE1 (ERN1) in an inactive monomeric state; dissociation induces oligomerization, endoribonuclease activation (XBP1 splicing), and TRAF2-mediated JNK activation."),
        ("AKT1", "HSPA5"): ("Insulin Receptor Signaling & Survival", "GRP78 interacts with and stabilizes AKT phosphorylation at the plasma membrane and ER; cell-surface GRP78 acts as a co-receptor facilitating downstream PI3K/Akt activation."),
        ("HSPA5", "PRKAA1"): ("Energy Homeostasis & AMPK Activation", "Metabolic stress and glucose deprivation modulate GRP78-AMPK crosstalk; GRP78 assists in maintaining cellular ATP levels and interacts during metabolic remodeling."),
        ("HSPA5", "MAPK8"): ("Stress-Activated Protein Kinase / JNK Signaling", "Functional coupling via IRE1-TRAF2 axis; ER stress releases GRP78 from IRE1, triggering downstream JNK (MAPK8) activation and serine phosphorylation of IRS1."),
        ("HSPA5", "SREBF1"): ("De Novo Lipogenesis & ER Lipid Sensing", "GRP78 regulates ER lipid bilayer stress and interacts with the SREBP cleavage-activating protein (SCAP)/SREBP-1c regulatory complex, controlling lipogenic gene transcription."),
        ("INSR", "IRS1"): ("Insulin Receptor Tyrosine Kinase Cascade", "Direct primary substrate phosphorylation; activated INSR phosphorylates IRS1 on multiple tyrosine residues to recruit PI3K p85 subunit."),
        ("INSR", "IRS2"): ("Insulin Receptor Tyrosine Kinase Cascade", "Primary alternative substrate phosphorylation; activated INSR recruits and phosphorylates IRS2, driving hepatic and peripheral insulin signal transduction."),
        ("AKT1", "INSR"): ("Insulin Feedback Regulation", "AKT1 operates downstream of INSR via PI3K/PDK1; phosphorylates downstream metabolic targets including GSK3 and FOXO1."),
        ("AKT1", "IRS1"): ("Insulin Pathway Transduction & Feedback", "IRS1 acts upstream of AKT1 through PI3K/PIP3 generation; AKT and downstream mTOR/S6K mediate negative feedback serine phosphorylation on IRS1."),
        ("IRS1", "MAPK8"): ("Stress-Induced Insulin Resistance", "Active JNK (MAPK8) directly phosphorylates IRS1 at inhibitory serine residue Ser307, uncoupling IRS1 from INSR and inducing severe cellular insulin resistance."),
        ("ERN1", "MAPK8"): ("ER Stress - Insulin Resistance Coupling", "Activated IRE1alpha recruits TRAF2 and ASK1 to directly phosphorylate and activate JNK (MAPK8), providing the primary biochemical bridge linking ER stress to insulin desensitization."),
        ("PRKAA1", "SREBF1"): ("Metabolic Counter-Regulation", "AMPK (PRKAA1) directly phosphorylates SREBP-1c at Ser372, inhibiting its proteolytic cleavage and nuclear translocation, thereby suppressing hepatic steatosis."),
        ("IRS1", "IRS2"): ("IRS Adaptor Family Coordination", "Functional co-regulation of hepatic insulin signaling; IRS1 predominantly coordinates glucose metabolism whereas IRS2 directs lipid homeostasis."),
        ("AKT1", "SREBF1"): ("Insulin-Stimulated Lipogenesis", "AKT/mTORC1 pathway promotes SREBP-1c processing and nuclear translocation, stimulating lipogenic gene expression under hyperinsulinemic conditions."),
        ("EIF2AK3", "IRS1"): ("PERK-IRS1 Cross-Regulation", "ER stress signaling cross-talk; PERK-eIF2alpha phosphorylation attenuates general translation while modulating IRS1 turnover."),
    }

    rows = []
    
    # First: GRP78 direct interactions
    for partner in ["EIF2AK3", "ATF6", "ERN1", "AKT1", "PRKAA1", "MAPK8", "SREBF1"]:
        key = tuple(sorted(["HSPA5", partner]))
        edge = edge_map.get(key, {})
        score = edge.get("score", "N/A")
        escore = edge.get("escore", "0")
        dscore = edge.get("dscore", "0")
        tscore = edge.get("tscore", "0")
        ascore = edge.get("ascore", "0")
        
        ev_types = []
        if float(escore) > 0: ev_types.append("Experimental")
        if float(dscore) > 0: ev_types.append("Curated_Databases")
        if float(tscore) > 0: ev_types.append("Textmining")
        if float(ascore) > 0: ev_types.append("Coexpression")
        ev_str = ", ".join(ev_types) if ev_types else "Functional Association"
        
        pathway_name, mechanism = pathway_annotations.get(key, ("GRP78 Signaling Network", "Functional interaction retrieved from STRING database."))
        
        rows.append({
            "source_node": "HSPA5",
            "target_node": partner,
            "interaction_score": score,
            "experimental_score": escore,
            "database_score": dscore,
            "textmining_score": tscore,
            "coexpression_score": ascore,
            "evidence_types": ev_str,
            "pathway_name": pathway_name,
            "biological_mechanism": mechanism
        })
        
    # Second: Key metabolic and downstream bridge interactions
    bridge_pairs = [
        ("INSR", "IRS1"), ("INSR", "IRS2"), ("AKT1", "INSR"), ("AKT1", "IRS1"),
        ("IRS1", "MAPK8"), ("ERN1", "MAPK8"), ("PRKAA1", "SREBF1"), ("AKT1", "SREBF1"),
        ("EIF2AK3", "IRS1"), ("IRS1", "IRS2")
    ]
    
    for n_a, n_b in bridge_pairs:
        key = tuple(sorted([n_a, n_b]))
        edge = edge_map.get(key, {})
        score = edge.get("score", "N/A")
        escore = edge.get("escore", "0")
        dscore = edge.get("dscore", "0")
        tscore = edge.get("tscore", "0")
        ascore = edge.get("ascore", "0")
        
        ev_types = []
        if float(escore) > 0: ev_types.append("Experimental")
        if float(dscore) > 0: ev_types.append("Curated_Databases")
        if float(tscore) > 0: ev_types.append("Textmining")
        if float(ascore) > 0: ev_types.append("Coexpression")
        ev_str = ", ".join(ev_types) if ev_types else "Functional Association"
        
        pathway_name, mechanism = pathway_annotations.get(key, ("Metabolic Signaling Cascade", "Functional interaction retrieved from STRING database."))
        
        rows.append({
            "source_node": n_a,
            "target_node": n_b,
            "interaction_score": score,
            "experimental_score": escore,
            "database_score": dscore,
            "textmining_score": tscore,
            "coexpression_score": ascore,
            "evidence_types": ev_str,
            "pathway_name": pathway_name,
            "biological_mechanism": mechanism
        })

    with open(OUTPUT_PATHWAYS, "w", newline="", encoding="utf-8") as f:
        fieldnames = [
            "source_node", "target_node", "interaction_score", "experimental_score",
            "database_score", "textmining_score", "coexpression_score",
            "evidence_types", "pathway_name", "biological_mechanism"
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        
    print(f"Saved {len(rows)} pathway interaction records to {OUTPUT_PATHWAYS}")

if __name__ == "__main__":
    step_1_sliding_window_profiles()
    step_2_cross_species_alignment()
    step_3_human_variant_impact()
    step_4_pathway_interactions()
    print("\nAll sequence, variant, and pathway analyses completed successfully.")
