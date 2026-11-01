#!/usr/bin/env python3
"""
scripts/collect_structures.py

Systematic acquisition and verification of 1D, 2D, and 3D molecular and structural assets
for PSTi8, wild-type Pancreastatin (PST), human PST coding variants, and GRP78 (HSPA5)
across human, mouse, and rat using UniProt REST, RCSB PDB, AlphaFold DB, Biopython, and RDKit.
"""

import os
import sys
import json
import csv
import urllib.request
import urllib.error
import time

from Bio.SeqUtils.ProtParam import ProteinAnalysis
from rdkit import Chem
from rdkit.Chem import Descriptors, AllChem, Draw

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DATA_DIR = os.path.join(REPO_ROOT, "data", "structures")
DIR_1D = os.path.join(DATA_DIR, "1d_sequences")
DIR_2D = os.path.join(DATA_DIR, "2d_chemical")
DIR_3D = os.path.join(DATA_DIR, "3d_models")

HEADERS = {"User-Agent": "PSTi8-Structural-Audit/1.0 (mailto:devanshyadav118@gmail.com)"}

def ensure_dirs():
    for d in [DIR_1D, DIR_2D, DIR_3D]:
        os.makedirs(d, exist_ok=True)
    print("Created directory structure under data/structures/")

def fetch_url(url, dest_path=None, retries=3):
    req = urllib.request.Request(url, headers=HEADERS)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            if dest_path:
                with open(dest_path, "wb") as f:
                    f.write(data)
            return data
        except Exception as e:
            if attempt == retries - 1:
                raise e
            time.sleep(1.0)

def step_1a_fetch_uniprot():
    print("\n--- Step 1A: Fetching UniProt Canonical Sequences & Metadata ---")
    targets = {
        "P10645": ("CHGA", "HUMAN", "Chromogranin A"),
        "P26339": ("CHGA", "MOUSE", "Chromogranin A"),
        "P10354": ("CHGA", "RAT", "Chromogranin A"),
        "P11021": ("GRP78", "HUMAN", "Endoplasmic reticulum chaperone BiP / HSPA5"),
        "P20029": ("GRP78", "MOUSE", "Endoplasmic reticulum chaperone BiP / Hspa5"),
        "P06761": ("GRP78", "RAT", "Endoplasmic reticulum chaperone BiP / Hspa5"),
    }
    
    uniprot_records = {}
    for acc, (gene, species, desc) in targets.items():
        base_name = f"{acc}_{gene}_{species}"
        fasta_file = os.path.join(DIR_1D, f"{base_name}.fasta")
        json_file = os.path.join(DIR_1D, f"{base_name}.json")
        
        fasta_url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
        json_url = f"https://rest.uniprot.org/uniprotkb/{acc}.json"
        
        print(f"Fetching {base_name} ({desc})...")
        fasta_bytes = fetch_url(fasta_url, fasta_file)
        json_bytes = fetch_url(json_url, json_file)
        
        json_data = json.loads(json_bytes.decode("utf-8"))
        seq = json_data["sequence"]["value"]
        uniprot_records[acc] = {
            "gene": gene,
            "species": species,
            "description": desc,
            "sequence": seq,
            "length": len(seq),
            "fasta_path": fasta_file,
            "json_path": json_file,
            "json_data": json_data
        }
        print(f"  Saved {base_name}.fasta and .json (len={len(seq)})")
        time.sleep(0.2)
        
    return uniprot_records

def step_1b_peptide_sequences(uniprot_records):
    print("\n--- Step 1B: Extracting & Validating Peptide Sequences ---")
    h_chga = uniprot_records["P10645"]["sequence"]
    
    # Coordinates in Human Preprotein (1-457; Signal peptide 1-18; Mature 19-457, len 439)
    # Mature 250-301 = Preprotein 268-319 (len 52)
    pst_52 = h_chga[267:319]
    # Mature 273-301 = Preprotein 291-319 (len 29)
    wt_pst_29 = h_chga[290:319]
    # PSTi8: Mature 273-293 = Preprotein 291-311 (len 21)
    psti8_21 = h_chga[290:311]
    # Cleaved C-terminal 8-mer: Preprotein 312-319
    cleaved_c_term_8 = h_chga[311:319]
    
    # Variants of PST-29:
    # Gly297Ser: Preprotein 315 G -> S (PST-29 pos 25)
    g297s_pst_29 = wt_pst_29[:24] + "S" + wt_pst_29[25:]
    # Glu287Lys: Preprotein 305 E -> K (PST-29 pos 15, Mature 287)
    e287k_pst_29 = wt_pst_29[:14] + "K" + wt_pst_29[15:]
    
    # Mouse PST from P26339 (UniProt feature 276-329)
    m_chga = uniprot_records["P26339"]["sequence"]
    mouse_pst_54 = m_chga[275:329]
    # Rat PST from P10354 (UniProt feature 281-332)
    r_chga = uniprot_records["P10354"]["sequence"]
    rat_pst_52 = r_chga[280:332]
    
    # Verify exact matches
    assert wt_pst_29 == "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG", f"WT PST-29 mismatch: {wt_pst_29}"
    assert psti8_21 == "PEGKGEQEHSQQKEEEEEMAV", f"PSTi8 mismatch: {psti8_21}"
    assert cleaved_c_term_8 == "VPQGLFRG", f"C-term 8 mismatch: {cleaved_c_term_8}"
    assert g297s_pst_29 == "PEGKGEQEHSQQKEEEEEMAVVPQSLFRG", f"G297S mismatch: {g297s_pst_29}"
    assert e287k_pst_29 == "PEGKGEQEHSQQKEKEEEMAVVPQGLFRG", f"E287K mismatch: {e287k_pst_29}"
    
    print("Verification successful:")
    print(f"  Human WT PST-29:  {wt_pst_29} (Preprotein 291-319, Mature 273-301)")
    print(f"  Human PSTi8-21:   {psti8_21} (Preprotein 291-311, Mature 273-293)")
    print(f"  Human G297S PST:  {g297s_pst_29} (G297S mutation at pos 25)")
    print(f"  Human E287K PST:  {e287k_pst_29} (E287K mutation at pos 15)")
    print(f"  Human PST-52:     {pst_52} (Preprotein 268-319, Mature 250-301)")
    print(f"  Cleaved 8-mer:    {cleaved_c_term_8} (Preprotein 312-319)")
    
    peptides = {
        "human_psti8_21": ("PSTi8 (21-mer inhibitor)", psti8_21, "Human", "273-293 (Mature) / 291-311 (Preprotein)"),
        "human_wt_pst_29": ("Pancreastatin WT (29-mer)", wt_pst_29, "Human", "273-301 (Mature) / 291-319 (Preprotein)"),
        "human_g297s_pst_29": ("Pancreastatin Gly297Ser (29-mer)", g297s_pst_29, "Human", "273-301 with rs9658664 G297S"),
        "human_e287k_pst_29": ("Pancreastatin Glu287Lys (29-mer)", e287k_pst_29, "Human", "273-301 with E287K"),
        "human_pst_52": ("Pancreastatin full (52-mer)", pst_52, "Human", "250-301 (Mature) / 268-319 (Preprotein)"),
        "cleaved_c_term_8": ("PST C-terminal 8-mer (cleaved in PSTi8)", cleaved_c_term_8, "Human", "294-301 (Mature) / 312-319 (Preprotein)"),
        "mouse_pst_54": ("Mouse Pancreastatin (54-mer)", mouse_pst_54, "Mouse", "276-329 (Preprotein)"),
        "rat_pst_52": ("Rat Pancreastatin (52-mer)", rat_pst_52, "Rat", "281-332 (Preprotein)"),
    }
    
    # Save peptides FASTA
    pep_fasta_path = os.path.join(DIR_1D, "pancreastatin_peptides_canonical.fasta")
    with open(pep_fasta_path, "w", encoding="utf-8") as f:
        for pid, (pname, seq, species, loc) in peptides.items():
            f.write(f">{pid} {pname} | Species: {species} | Coords: {loc}\n{seq}\n")
    print(f"Saved canonical peptide sequences to {pep_fasta_path}")
    
    return peptides

def amidate_c_terminus(mol_free):
    """
    Specifically replaces the C-terminal alpha-carboxylic acid -OH with -NH2
    without modifying glutamic acid or aspartic acid side chains.
    """
    patt = Chem.MolFromSmarts("[NX3,NX4+][CX4,CX3H2][CX3](=O)[OX2H1]")
    matches = mol_free.GetSubstructMatches(patt)
    if not matches:
        raise ValueError("Could not locate C-terminal alpha-carboxylic acid group")
    
    m = matches[0]
    c_carbonyl = mol_free.GetAtomWithIdx(m[2])
    o_single = [nb for nb in c_carbonyl.GetNeighbors() 
                if nb.GetAtomicNum() == 8 and 
                mol_free.GetBondBetweenAtoms(c_carbonyl.GetIdx(), nb.GetIdx()).GetBondType() == Chem.BondType.SINGLE][0]
    
    rw = Chem.RWMol(mol_free)
    rw.GetAtomWithIdx(o_single.GetIdx()).SetAtomicNum(7)
    rw.GetAtomWithIdx(o_single.GetIdx()).SetNumExplicitHs(2)
    mol_amidated = rw.GetMol()
    Chem.SanitizeMol(mol_amidated)
    return mol_amidated

def step_2_build_2d_chemicals(peptides):
    print("\n--- Step 2: 2D Chemical Representations (RDKit) ---")
    targets_2d = [
        ("human_psti8_21", peptides["human_psti8_21"][1]),
        ("human_wt_pst_29", peptides["human_wt_pst_29"][1]),
        ("human_g297s_pst_29", peptides["human_g297s_pst_29"][1]),
        ("human_e287k_pst_29", peptides["human_e287k_pst_29"][1]),
    ]
    
    chemical_results = {}
    for pid, seq in targets_2d:
        print(f"Processing 2D structures for {pid}...")
        mol_free = Chem.MolFromSequence(seq)
        mol_amidated = amidate_c_terminus(mol_free)
        
        # Free C-term assets
        id_free = f"{pid}_free_cooh"
        smi_free = Chem.MolToSmiles(mol_free, isomericSmiles=True)
        mw_free = Descriptors.MolWt(mol_free)
        mono_free = Descriptors.ExactMolWt(mol_free)
        
        AllChem.Compute2DCoords(mol_free)
        sdf_free_path = os.path.join(DIR_2D, f"{id_free}.sdf")
        w_free = Chem.SDWriter(sdf_free_path)
        w_free.write(mol_free)
        w_free.close()
        
        smi_free_path = os.path.join(DIR_2D, f"{id_free}.smi")
        with open(smi_free_path, "w") as f:
            f.write(f"{smi_free}\t{id_free}\n")
            
        svg_free_path = os.path.join(DIR_2D, f"{id_free}.svg")
        svg_free = Draw.MolToSVG(mol_free, size=(900, 600))
        with open(svg_free_path, "w") as f:
            f.write(svg_free)
            
        # Amidated C-term assets
        id_amidated = f"{pid}_amidated_conh2"
        smi_amidated = Chem.MolToSmiles(mol_amidated, isomericSmiles=True)
        mw_amidated = Descriptors.MolWt(mol_amidated)
        mono_amidated = Descriptors.ExactMolWt(mol_amidated)
        
        AllChem.Compute2DCoords(mol_amidated)
        sdf_amidated_path = os.path.join(DIR_2D, f"{id_amidated}.sdf")
        w_amidated = Chem.SDWriter(sdf_amidated_path)
        w_amidated.write(mol_amidated)
        w_amidated.close()
        
        smi_amidated_path = os.path.join(DIR_2D, f"{id_amidated}.smi")
        with open(smi_amidated_path, "w") as f:
            f.write(f"{smi_amidated}\t{id_amidated}\n")
            
        svg_amidated_path = os.path.join(DIR_2D, f"{id_amidated}.svg")
        svg_amidated = Draw.MolToSVG(mol_amidated, size=(900, 600))
        with open(svg_amidated_path, "w") as f:
            f.write(svg_amidated)
            
        chemical_results[pid] = {
            "free": {
                "id": id_free, "smiles": smi_free, "mw": mw_free, "monoisotopic": mono_free,
                "sdf": sdf_free_path, "smi_file": smi_free_path, "svg": svg_free_path
            },
            "amidated": {
                "id": id_amidated, "smiles": smi_amidated, "mw": mw_amidated, "monoisotopic": mono_amidated,
                "sdf": sdf_amidated_path, "smi_file": smi_amidated_path, "svg": svg_amidated_path
            }
        }
        print(f"  {pid} Free:     MW={mw_free:.2f}, Mono={mono_free:.4f}")
        print(f"  {pid} Amidated: MW={mw_amidated:.2f}, Mono={mono_amidated:.4f}")
        
    return chemical_results

def step_1c_compute_physicochemical(peptides, chemical_results):
    print("\n--- Step 1C: Computing Physicochemical Descriptors ---")
    csv_path = os.path.join(DIR_1D, "peptide_1d_properties.csv")
    
    rows = []
    for pid, (pname, seq, species, loc) in peptides.items():
        anal = ProteinAnalysis(seq)
        length = len(seq)
        biopy_mw = anal.molecular_weight()
        pI = anal.isoelectric_point()
        gravy = anal.gravy()
        net_charge_74 = anal.charge_at_pH(7.4)
        
        aa_counts = anal.count_amino_acids()
        acidic_count = aa_counts["D"] + aa_counts["E"]
        basic_count = aa_counts["R"] + aa_counts["K"] + aa_counts["H"]
        glu_count = aa_counts["E"]
        lys_count = aa_counts["K"]
        
        # RDKit molecular weights if available
        chem = chemical_results.get(pid, {})
        free_avg_mw = chem.get("free", {}).get("mw", biopy_mw)
        free_mono_mw = chem.get("free", {}).get("monoisotopic", "N/A")
        amidated_avg_mw = chem.get("amidated", {}).get("mw", biopy_mw - 0.984 if chem else "N/A")
        amidated_mono_mw = chem.get("amidated", {}).get("monoisotopic", "N/A")
        
        row = {
            "peptide_id": pid,
            "name": pname,
            "species": species,
            "coordinates": loc,
            "sequence": seq,
            "length": length,
            "mw_free_cooh_avg": round(free_avg_mw, 3) if isinstance(free_avg_mw, float) else free_avg_mw,
            "mw_free_cooh_monoisotopic": round(free_mono_mw, 4) if isinstance(free_mono_mw, float) else free_mono_mw,
            "mw_amidated_conh2_avg": round(amidated_avg_mw, 3) if isinstance(amidated_avg_mw, float) else amidated_avg_mw,
            "mw_amidated_conh2_monoisotopic": round(amidated_mono_mw, 4) if isinstance(amidated_mono_mw, float) else amidated_mono_mw,
            "net_charge_pH_7_4": round(net_charge_74, 2),
            "isoelectric_point_pI": round(pI, 2),
            "gravy_hydropathy": round(gravy, 3),
            "acidic_residues_D_E": acidic_count,
            "basic_residues_R_K_H": basic_count,
            "glu_count": glu_count,
            "lys_count": lys_count
        }
        rows.append(row)
        
    fieldnames = [
        "peptide_id", "name", "species", "coordinates", "sequence", "length",
        "mw_free_cooh_avg", "mw_free_cooh_monoisotopic",
        "mw_amidated_conh2_avg", "mw_amidated_conh2_monoisotopic",
        "net_charge_pH_7_4", "isoelectric_point_pI", "gravy_hydropathy",
        "acidic_residues_D_E", "basic_residues_R_K_H", "glu_count", "lys_count"
    ]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved physicochemical descriptors to {csv_path}")
    return rows

def step_3_fetch_3d_models():
    print("\n--- Step 3: Fetching 3D Experimental & AlphaFold Models ---")
    manifest_rows = []
    
    # 3A: RCSB PDB Experimental Structures
    pdb_targets = {
        "3LDL": "Crystal structure of human GRP78 ATPase domain bound to ATP",
        "5EVZ": "Crystal structure of human GRP78 ATPase domain complex",
        "5E84": "Full-length BiP / GRP78 in ATP-bound domain-docked open conformation",
        "5E85": "Isolated substrate-binding domain (SBD) / domain-undocked conformation of BiP"
    }
    
    for pdb_id, note in pdb_targets.items():
        print(f"Fetching PDB {pdb_id}...")
        pdb_url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
        dest_path = os.path.join(DIR_3D, f"PDB_{pdb_id}.pdb")
        fetch_url(pdb_url, dest_path)
        
        # Get metadata from RCSB REST API
        meta_url = f"https://data.rcsb.org/rest/v1/core/entry/{pdb_id}"
        meta_bytes = fetch_url(meta_url)
        meta_json = json.loads(meta_bytes.decode("utf-8"))
        res = meta_json.get("rcsb_entry_info", {}).get("resolution_combined", [None])[0]
        res_str = f"{res:.2f} A" if res else "N/A"
        
        manifest_rows.append({
            "asset_id": f"PDB_{pdb_id}",
            "molecule": "GRP78 / HSPA5",
            "species": "Homo sapiens",
            "dimension": "3D_experimental",
            "source_db": "RCSB PDB",
            "accession_or_pdb": pdb_id,
            "resolution_or_plddt": res_str,
            "file_path": f"data/structures/3d_models/PDB_{pdb_id}.pdb",
            "notes": note
        })
        print(f"  PDB {pdb_id}: Resolution = {res_str}")
        time.sleep(0.2)
        
    # 3B: AlphaFold DB Models
    af_targets = {
        "P10645": ("Chromogranin A (CHGA)", "Homo sapiens"),
        "P11021": ("GRP78 / HSPA5", "Homo sapiens")
    }
    
    plddt_summary = {}
    for acc, (mol_name, sp) in af_targets.items():
        print(f"Fetching AlphaFold DB model for {mol_name} ({acc})...")
        api_url = f"https://alphafold.ebi.ac.uk/api/prediction/{acc}"
        api_bytes = fetch_url(api_url)
        api_json = json.loads(api_bytes.decode("utf-8"))[0]
        
        pdb_url = api_json["pdbUrl"]
        pae_url = api_json["paeDocUrl"]
        
        pdb_dest = os.path.join(DIR_3D, f"AF_{acc}_F1_model.pdb")
        pae_dest = os.path.join(DIR_3D, f"AF_{acc}_F1_pae.json")
        
        fetch_url(pdb_url, pdb_dest)
        fetch_url(pae_url, pae_dest)
        
        # Calculate pLDDT from PDB B-factors
        with open(pdb_dest, "r") as f:
            lines = f.readlines()
        plddt_scores = {}
        for l in lines:
            if l.startswith("ATOM") and l[12:16].strip() == "CA":
                rnum = int(l[22:26].strip())
                bf = float(l[60:66].strip())
                plddt_scores[rnum] = bf
                
        all_vals = list(plddt_scores.values())
        mean_plddt = sum(all_vals) / len(all_vals)
        
        plddt_summary[acc] = {
            "mean": mean_plddt,
            "scores": plddt_scores
        }
        
        manifest_rows.append({
            "asset_id": f"AF_{acc}_F1_PDB",
            "molecule": mol_name,
            "species": sp,
            "dimension": "3D_predicted",
            "source_db": "AlphaFold DB",
            "accession_or_pdb": f"AF-{acc}-F1",
            "resolution_or_plddt": f"mean pLDDT: {mean_plddt:.1f}",
            "file_path": f"data/structures/3d_models/AF_{acc}_F1_model.pdb",
            "notes": f"Full-length predicted monomer 3D coordinates ({len(all_vals)} residues)"
        })
        manifest_rows.append({
            "asset_id": f"AF_{acc}_F1_PAE",
            "molecule": mol_name,
            "species": sp,
            "dimension": "3D_predicted_error",
            "source_db": "AlphaFold DB",
            "accession_or_pdb": f"AF-{acc}-F1",
            "resolution_or_plddt": "PAE matrix",
            "file_path": f"data/structures/3d_models/AF_{acc}_F1_pae.json",
            "notes": "Predicted Aligned Error (PAE) matrix JSON document"
        })
        print(f"  AF-{acc}-F1: Mean pLDDT = {mean_plddt:.2f}")
        time.sleep(0.2)
        
    return manifest_rows, plddt_summary

def write_manifest(manifest_rows):
    manifest_path = os.path.join(DATA_DIR, "structures_manifest.csv")
    fieldnames = [
        "asset_id", "molecule", "species", "dimension", "source_db",
        "accession_or_pdb", "resolution_or_plddt", "file_path", "notes"
    ]
    with open(manifest_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(manifest_rows)
    print(f"\nSaved master structures manifest to {manifest_path} ({len(manifest_rows)} entries)")

def main():
    print("=== PSTi8 & GRP78 Structural Asset Collection Harness ===")
    ensure_dirs()
    uniprot_records = step_1a_fetch_uniprot()
    peptides = step_1b_peptide_sequences(uniprot_records)
    chemical_results = step_2_build_2d_chemicals(peptides)
    prop_rows = step_1c_compute_physicochemical(peptides, chemical_results)
    manifest_rows, plddt_summary = step_3_fetch_3d_models()
    
    # Add 1D and 2D assets to manifest
    for acc, rec in uniprot_records.items():
        manifest_rows.append({
            "asset_id": f"UNIPROT_{acc}_FASTA",
            "molecule": f"{rec['gene']} ({rec['description']})",
            "species": f"{rec['species'].title()}",
            "dimension": "1D_sequence",
            "source_db": "UniProt",
            "accession_or_pdb": acc,
            "resolution_or_plddt": f"len={rec['length']}",
            "file_path": f"data/structures/1d_sequences/{acc}_{rec['gene']}_{rec['species']}.fasta",
            "notes": "Canonical FASTA sequence"
        })
        manifest_rows.append({
            "asset_id": f"UNIPROT_{acc}_JSON",
            "molecule": f"{rec['gene']} ({rec['description']})",
            "species": f"{rec['species'].title()}",
            "dimension": "1D_metadata",
            "source_db": "UniProt",
            "accession_or_pdb": acc,
            "resolution_or_plddt": f"len={rec['length']}",
            "file_path": f"data/structures/1d_sequences/{acc}_{rec['gene']}_{rec['species']}.json",
            "notes": "Full entry metadata JSON"
        })
        
    for pid, cdata in chemical_results.items():
        for term, sub in [("free", cdata["free"]), ("amidated", cdata["amidated"])]:
            sub_id = sub["id"]
            manifest_rows.append({
                "asset_id": sub_id.upper(),
                "molecule": pid,
                "species": "Homo sapiens",
                "dimension": "2D_chemical",
                "source_db": "RDKit",
                "accession_or_pdb": "SMILES/SDF",
                "resolution_or_plddt": f"MW: {sub['mw']:.2f}",
                "file_path": f"data/structures/2d_chemical/{sub['id']}.sdf",
                "notes": f"2D molecular structure ({term})"
            })
            
    write_manifest(manifest_rows)
    print("\n=== Structural Asset Collection Completed Successfully! ===")

if __name__ == "__main__":
    main()
