#!/usr/bin/env python3
"""
scripts/clean_receptor_structures.py

Sanitize and curate high-resolution GRP78 (HSPA5) experimental crystal structures
and AlphaFold models for in silico molecular docking and structural investigation.
Resolves crystallographic construct artifacts documented in docs/receptor_construct_audit.md.
"""

import os
import sys
from Bio.PDB import PDBParser, PDBIO, Select

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIR_3D = os.path.join(REPO_ROOT, "data", "structures", "3d_models")
DIR_CLEANED = os.path.join(DIR_3D, "cleaned")

os.makedirs(DIR_CLEANED, exist_ok=True)

class ChainAndLigandSelect(Select):
    def __init__(self, target_chain='B', keep_resnames=None, max_res_id=None, min_res_id=None):
        self.target_chain = target_chain
        self.keep_resnames = set(keep_resnames) if keep_resnames else set()
        self.max_res_id = max_res_id
        self.min_res_id = min_res_id

    def accept_residue(self, residue):
        chain_id = residue.get_parent().id
        if chain_id != self.target_chain:
            return 0
        
        res_name = residue.get_resname().strip()
        hetero_flag, res_seq, insert_code = residue.get_id()
        
        # Check range if standard amino acid
        if hetero_flag == " ":
            if self.min_res_id is not None and res_seq < self.min_res_id:
                return 0
            if self.max_res_id is not None and res_seq > self.max_res_id:
                return 0
            return 1
        
        # Check ligand acceptance
        if res_name in self.keep_resnames:
            return 1
        return 0

def clean_3ldl():
    print("Processing PDB 3LDL (Chain B + Mg2+ + ATP)...")
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("3LDL", os.path.join(DIR_3D, "PDB_3LDL.pdb"))
    
    # In 3LDL, Chain B contains Mg + ATP
    io = PDBIO()
    io.set_structure(struct)
    out_path = os.path.join(DIR_CLEANED, "PDB_3LDL_ChainB_MgATP.pdb")
    
    # In 3LDL, check ligand resnames
    keep_ligands = {"ATP", "MG"}
    io.save(out_path, ChainAndLigandSelect(target_chain='B', keep_resnames=keep_ligands))
    print(f"Saved: {out_path}")

def clean_5evz():
    print("Processing PDB 5EVZ (Chain A + Mg2+ + ADP + PO4)...")
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("5EVZ", os.path.join(DIR_3D, "PDB_5EVZ.pdb"))
    
    io = PDBIO()
    io.set_structure(struct)
    out_path = os.path.join(DIR_CLEANED, "PDB_5EVZ_ChainA_MgADP_Pi.pdb")
    
    keep_ligands = {"ADP", "MG", "PO4"}
    io.save(out_path, ChainAndLigandSelect(target_chain='A', keep_resnames=keep_ligands))
    print(f"Saved: {out_path}")

def clean_5e85():
    print("Processing PDB 5E85 (Chain A residues 418-637, apo SBD without fused self-peptide 638-653)...")
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("5E85", os.path.join(DIR_3D, "PDB_5E85.pdb"))
    
    io = PDBIO()
    io.set_structure(struct)
    out_path = os.path.join(DIR_CLEANED, "PDB_5E85_SBD_apo_cleaned.pdb")
    
    # 5E85 has fused peptide 638-653 (SENLYFQGSNRLLLTG)
    io.save(out_path, ChainAndLigandSelect(target_chain='A', keep_resnames=set(), min_res_id=418, max_res_id=637))
    print(f"Saved: {out_path}")

def clean_alphafold_models():
    print("Processing AlphaFold GRP78 model (AF_P11021_F1_model.pdb)...")
    parser = PDBParser(QUIET=True)
    struct = parser.get_structure("AF_P11021", os.path.join(DIR_3D, "AF_P11021_F1_model.pdb"))
    
    io = PDBIO()
    io.set_structure(struct)
    
    # 1. Full mature GRP78: residues 19-654 (cleaving signal peptide 1-18)
    out_mature = os.path.join(DIR_CLEANED, "AF_P11021_mature_GRP78_19_654.pdb")
    io.save(out_mature, ChainAndLigandSelect(target_chain='A', keep_resnames=set(), min_res_id=19, max_res_id=654))
    print(f"Saved: {out_mature}")
    
    # 2. Structured core domain: residues 26-633 (matching crystallographic construct boundaries, removing signal peptide 1-18, N-loop 19-25, and disordered KDEL C-tail 634-654)
    out_core = os.path.join(DIR_CLEANED, "AF_P11021_core_26_633.pdb")
    io.save(out_core, ChainAndLigandSelect(target_chain='A', keep_resnames=set(), min_res_id=26, max_res_id=633))
    print(f"Saved: {out_core}")

if __name__ == "__main__":
    clean_3ldl()
    clean_5evz()
    clean_5e85()
    clean_alphafold_models()
    print("Receptor structure cleaning complete.")
