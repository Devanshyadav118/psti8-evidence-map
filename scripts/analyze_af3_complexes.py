#!/usr/bin/env python3
"""
scripts/analyze_af3_complexes.py
Comprehensive analysis of AlphaFold 3 co-folding runs:
GRP78 mature + ATP + Mg2+ with PSTi8, WT PST-29, E287K, and G297S.
Outputs:
  - data/structures/3d_models/af3_complex_metrics.csv (all 5 seeds per complex)
  - data/structures/3d_models/af3_interface_contacts.csv (atomic contacts < 4.0 A in model_0)
"""

import os
import glob
import json
import csv
from Bio.PDB.MMCIFParser import MMCIFParser

COMPLEXES = [
    {
        "complex_id": "fold_af3_grp78_mature_psti8_21_atp_mg",
        "peptide_name": "PSTi8",
        "peptide_len": 21,
        "variant_type": "inhibitor",
        "description": "PSTi8 (1-21) competitive antagonist with mature GRP78, ATP, and Mg2+"
    },
    {
        "complex_id": "fold_af3_grp78_mature_wt_pst29_atp_mg",
        "peptide_name": "WT_PST29",
        "peptide_len": 29,
        "variant_type": "wild_type",
        "description": "Wild-type human PST-29 with mature GRP78, ATP, and Mg2+"
    },
    {
        "complex_id": "fold_af3_grp78_mature_e287k_pst29_atp_mg",
        "peptide_name": "E287K_PST29",
        "peptide_len": 29,
        "variant_type": "human_variant",
        "description": "Human coding variant Glu287Lys (rs140089514, mature E15K) with mature GRP78, ATP, and Mg2+"
    },
    {
        "complex_id": "fold_af3_grp78_mature_g297s_pst29_atp_mg",
        "peptide_name": "G297S_PST29",
        "peptide_len": 29,
        "variant_type": "human_variant",
        "description": "Diabetogenic human coding variant Gly297Ser (rs9658664, mature G25S) with mature GRP78, ATP, and Mg2+"
    }
]

def annotate_grp78_domain(canon_res_num):
    """
    Annotate GRP78 domain based on canonical UniProt P11021 coordinates.
    AF3 Chain A residue IDs are 1-based along mature sequence (1-636),
    corresponding to UniProt P11021 residues 19-654 (+18 offset).
    
    Canonical boundaries derived from 3LDL, 5EVZ, and UniProt P11021:
      N-terminal mature extension: 19-25
      NBD (ATPase Domain): 26-407 (crystal structures 3LDL/5EVZ residues 26-406/407)
      Interdomain Linker: 408-426 (core linker 411-425 + hinge Lys426)
      SBDbeta (Substrate-Binding Domain beta): 427-537
      SBDalpha (Helical Lid): 538-633
      C-terminal tail (KDEL): 634-654
    """
    if canon_res_num < 26:
        return "N-terminal Extension"
    elif canon_res_num <= 407:
        return "NBD"
    elif canon_res_num <= 426:
        return "Interdomain Linker"
    elif canon_res_num <= 537:
        return "SBDbeta"
    elif canon_res_num <= 633:
        return "SBDalpha"
    else:
        return "C-terminal Tail"

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    models_dir = os.path.join(base_dir, "data", "structures", "3d_models")
    
    # 1. Parse all 5 seeds for each complex
    metrics_rows = []
    print("=== Extracting AF3 Multi-Seed Metrics ===")
    
    for comp in COMPLEXES:
        cid = comp["complex_id"]
        cdir = os.path.join(models_dir, cid)
        
        for seed in range(5):
            summary_path = os.path.join(cdir, f"{cid}_summary_confidences_{seed}.json")
            if not os.path.exists(summary_path):
                print(f"Warning: {summary_path} not found.")
                continue
            
            with open(summary_path) as fp:
                data = json.load(fp)
            
            iptm = float(data.get("iptm", 0.0))
            ptm = float(data.get("ptm", 0.0))
            ranking_score = float(data.get("ranking_score", 0.0))
            fraction_disordered = float(data.get("fraction_disordered", 0.0))
            
            # Pairwise chain metrics (Chain A is receptor [0], Chain B is peptide [1])
            chain_pair_iptm = data.get("chain_pair_iptm", [[0, 0], [0, 0]])
            pairwise_iptm_ab = float(chain_pair_iptm[0][1]) if len(chain_pair_iptm) > 0 and len(chain_pair_iptm[0]) > 1 else None
            
            chain_pair_pae_min = data.get("chain_pair_pae_min", [[0, 0], [0, 0]])
            min_pae_ab = float(chain_pair_pae_min[0][1]) if len(chain_pair_pae_min) > 0 and len(chain_pair_pae_min[0]) > 1 else None
            
            metrics_rows.append({
                "complex_id": cid,
                "peptide_name": comp["peptide_name"],
                "variant_type": comp["variant_type"],
                "seed_rank": seed,
                "ranking_score": ranking_score,
                "iptm": iptm,
                "ptm": ptm,
                "pairwise_chain_iptm_AB": pairwise_iptm_ab,
                "min_pae_AB": min_pae_ab,
                "fraction_disordered": fraction_disordered
            })
            print(f"[{comp['peptide_name']}] Seed {seed}: Rank={ranking_score:.2f}, ipTM={iptm:.2f}, pTM={ptm:.2f}, Pair_ipTM={pairwise_iptm_ab:.2f}, Min_PAE={min_pae_ab:.2f} A")
            
    metrics_csv = os.path.join(models_dir, "af3_complex_metrics.csv")
    with open(metrics_csv, "w", newline="") as fp:
        fieldnames = [
            "complex_id", "peptide_name", "variant_type", "seed_rank",
            "ranking_score", "iptm", "ptm", "pairwise_chain_iptm_AB",
            "min_pae_AB", "fraction_disordered"
        ]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(metrics_rows)
    print(f"\nSaved {len(metrics_rows)} seed metric rows to: {metrics_csv}")
    
    # 2. Parse model_0 mmCIF atomic contacts (<4.0 A)
    print("\n=== Calculating Atomic Interface Contacts (<4.0 A) in Model 0 ===")
    parser = MMCIFParser(QUIET=True)
    contacts_rows = []
    
    for comp in COMPLEXES:
        cid = comp["complex_id"]
        cif_path = os.path.join(models_dir, cid, f"{cid}_model_0.cif")
        if not os.path.exists(cif_path):
            print(f"Warning: {cif_path} not found.")
            continue
        
        print(f"Parsing coordinates for {comp['peptide_name']}...")
        structure = parser.get_structure(comp["peptide_name"], cif_path)
        chain_a = structure[0]["A"] # GRP78
        chain_b = structure[0]["B"] # Peptide
        
        # Collect heavy atoms
        atoms_b = [a for a in chain_b.get_atoms() if not a.name.startswith("H")]
        atoms_a = [a for a in chain_a.get_atoms() if not a.name.startswith("H")]
        
        comp_contacts = []
        for ab in atoms_b:
            res_b = ab.get_parent()
            for aa in atoms_a:
                d = ab - aa
                if d < 4.0:
                    res_a = aa.get_parent()
                    comp_contacts.append({
                        "complex_id": cid,
                        "peptide_name": comp["peptide_name"],
                        "peptide_res_name": res_b.get_resname(),
                        "peptide_res_num": res_b.id[1],
                        "peptide_atom": ab.name,
                        "grp78_res_name": res_a.get_resname(),
                        "grp78_res_num_cif": res_a.id[1],
                        "grp78_res_num_canonical": res_a.id[1] + 18,
                        "grp78_atom": aa.name,
                        "grp78_domain": annotate_grp78_domain(res_a.id[1] + 18),
                        "distance_angstrom": round(float(d), 3)
                    })
        
        contacts_rows.extend(comp_contacts)
        unique_b = len(set([c["peptide_res_num"] for c in comp_contacts]))
        unique_a = len(set([c["grp78_res_num_cif"] for c in comp_contacts]))
        
        # Domain counts
        domain_counts = {}
        for c in comp_contacts:
            res_key = (c["grp78_res_num_cif"], c["grp78_domain"])
            domain_counts[res_key] = c["grp78_domain"]
        dom_breakdown = {}
        for (r, d) in domain_counts.keys():
            dom_breakdown[d] = dom_breakdown.get(d, 0) + 1
            
        print(f"  {comp['peptide_name']}: {len(comp_contacts)} atomic contacts, {unique_b} peptide residues, {unique_a} GRP78 residues")
        print(f"  Domain breakdown of contacting GRP78 residues: {dom_breakdown}")
        
    contacts_csv = os.path.join(models_dir, "af3_interface_contacts.csv")
    with open(contacts_csv, "w", newline="") as fp:
        fieldnames = [
            "complex_id", "peptide_name", "peptide_res_name", "peptide_res_num", "peptide_atom",
            "grp78_res_name", "grp78_res_num_cif", "grp78_res_num_canonical", "grp78_atom",
            "grp78_domain", "distance_angstrom"
        ]
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts_rows)
    print(f"\nSaved {len(contacts_rows)} atomic contact rows to: {contacts_csv}")
    print("=== AlphaFold 3 Analysis Complete ===")

if __name__ == "__main__":
    main()
