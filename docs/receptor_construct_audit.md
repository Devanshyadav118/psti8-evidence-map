# GRP78 / BiP (HSPA5) Crystallographic Construct Audit & Receptor Sanitization Protocol

**Date:** 2026-11-02  
**Author / Tool:** Antigravity (Gemini 3.8 Flash High)  
**Script Reference:** [`scripts/clean_receptor_structures.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/clean_receptor_structures.py)  
**Cleaned 3D Models Directory:** [`data/structures/3d_models/cleaned/`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/)

---

## 1. Executive Summary

Molecular docking, virtual screening, and structural modeling of pancreastatin (PST) and pancreastatin inhibitor (PSTi8) against their proposed molecular target, GRP78 / BiP (`HSPA5`), require rigorous validation of crystallographic receptor structures. Experimental PDB crystal structures of Hsp70-family chaperones frequently contain non-physiological engineered mutations, altered loop regions, inhibitory metal substitutions, and crystallographic fusion peptides that block or distort the client-binding pocket.

This audit evaluates the four primary experimental crystal structures of Human GRP78 available in RCSB PDB (`3LDL`, `5EVZ`, `5E84`, `5E85`) and the full-length AlphaFold model (`AF-P11021-F1`), identifies critical construct traps, and specifies the exact sanitization protocols applied to generate docking-ready receptor models.

---

## 2. Detailed Construct Audit Across Human GRP78 PDB Structures

### 1. PDB 3LDL (2.30 Å Resolution, NBD Domain)
- **Reference:** Wisniewska et al., *PLoS One* 2010 (DOI: [10.1371/journal.pone.0008625](https://doi.org/10.1371/journal.pone.0008625)).
- **Construct Details:** Human GRP78 nucleotide-binding domain (NBD), mature residues 26–407 (preprotein residues 26–407). Expression in *E. coli* with N-terminal His-tag.
- **Ligand State:** Crystallized in the presence of $\text{Mg}^{2+}\text{-ATP}$.
- **Critical Caveat & Asymmetry:**
  - The asymmetric unit contains two independent protein chains (Chain A and Chain B).
  - **Chain B** is fully coordinated with both an ATP molecule and the catalytic divalent magnesium cofactor ($\text{Mg}^{2+}$).
  - **Chain A** contains bound ATP but **lacks the catalytic $\text{Mg}^{2+}$ ion**, resulting in an uncoordinated, non-physiological triphosphate orientation.
- **Sanitization Protocol:**
  - **Output File:** [`PDB_3LDL_ChainB_MgATP.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_3LDL_ChainB_MgATP.pdb).
  - Chain A is excised. Chain B is preserved with its complete $\text{Mg}^{2+}\text{-ATP}$ catalytic complex. Non-essential solvent molecules and crystallization buffer components are stripped.

### 2. PDB 5EVZ (1.85 Å Resolution, NBD Domain)
- **Reference:** Hughes et al., *Bioorg Med Chem Lett* 2016 (DOI: [10.1016/j.bmcl.2016.03.042](https://doi.org/10.1016/j.bmcl.2016.03.042)).
- **Construct Details:** Wild-type Human GRP78 NBD (residues 26–407). High-resolution refinement at 1.85 Å.
- **Ligand State:** Post-hydrolysis product complex containing $\text{ADP} + \text{phosphate} (\text{PO}_4^{3-}) + \text{Mg}^{2+}$.
- **Construct Authenticity:** Both chains (Chain A and Chain B) maintain complete catalytic coordination with no engineered loop deletions.
- **Sanitization Protocol:**
  - **Output File:** [`PDB_5EVZ_ChainA_MgADP_Pi.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_5EVZ_ChainA_MgADP_Pi.pdb).
  - Chain A is isolated with its fully resolved $\text{ADP}\cdot\text{P}_i\cdot\text{Mg}^{2+}$ complex, representing the high-affinity post-hydrolysis state of the chaperone ATPase domain.

### 3. PDB 5E84 (2.99 Å Resolution, Engineered Full-Length BiP)
- **Reference:** Yang et al., *Science* 2015 (DOI: [10.1126/science.aad5431](https://doi.org/10.1126/science.aad5431)).
- **Construct Details:** Full-length human BiP construct (residues 25–633) in the domain-docked, ATP-bound conformation.
- **CRITICAL CONSTRUCT TRAP (Fatal for Peptide Docking):**
  1. **Engineered Inactivating Mutation:** Carries the active-site substitution `Thr229Ala` (`T229A`), impairing ATP hydrolysis.
  2. **Substrate-Binding Loop Deletion (`L3,4'`):** To stabilize the domain-docked conformation, the authors **excised the entire 7-residue substrate-binding loop L3,4** (`457-TASDNQP-463`) in the $\text{SBD}\beta$ domain and replaced it with a short 3-residue `Val-Gly-Gly` (`VGG`) linker. This deletion completely disrupts the client-binding cleft and abolishes physiological peptide substrate binding.
  3. **Zinc Substitution:** The nucleotide pocket contains zinc ($\text{Zn}^{2+}$) instead of physiological magnesium ($\text{Mg}^{2+}$).
- **Sanitization Protocol:**
  - **Status:** **REJECTED FOR DIRECT PEPTIDE DOCKING.** PDB 5E84 must **never** be used for substrate peptide docking because its client-binding cleft is physically mutilated. It is retained solely as an illustrative template for macro-domain interdomain docking orientations.

### 4. PDB 5E85 (2.57 Å Resolution, Isolated SBD Domain)
- **Reference:** Yang et al., *Science* 2015 (DOI: [10.1126/science.aad5431](https://doi.org/10.1126/science.aad5431)).
- **Construct Details:** Human GRP78 substrate-binding domain (SBD, mature residues 418–637), encompassing both the $\text{SBD}\beta$ $\beta$-sandwich and the $\text{SBD}\alpha$ helical lid.
- **CRITICAL CONSTRUCT TRAP (Cis-Self-Inhibition):**
  - The construct was expressed with a carboxyl-terminal 16-amino-acid extension comprising a TEV protease recognition site fused to a high-affinity model peptide substrate:
    $$\text{Residues 638–653: } \mathbf{SENLYFQGSNRLLLTG}$$
  - In the crystal lattice, **this fused tail wraps backward and inserts directly into its own $\text{SBD}\beta$ binding cleft in cis**, occupying the binding groove (specifically the hydrophobic `NRLLLT` motif).
  - Attempting to dock external peptides (such as PST or PSTi8) into raw PDB 5E85 causes severe steric clashes because the pocket is already occupied by this engineered crystallographic artifact.
- **Sanitization Protocol:**
  - **Output File:** [`PDB_5E85_SBD_apo_cleaned.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_5E85_SBD_apo_cleaned.pdb).
  - Chain A residues 418–637 are extracted. Residues 638–653 (the fused `SENLYFQGSNRLLLTG` peptide) and all non-protein heteroatoms are cleaved, generating a clean, unobstructed apo $\text{SBD}$ receptor.

---

## 3. AlphaFold Full-Length Model Sanitization (`AF-P11021-F1`)

To complement truncated crystallographic fragments, the complete predicted monomer coordinates of Human GRP78 (`AF_P11021_F1_model.pdb`, mean pLDDT 90.0) were curated:

1. **Full Mature Receptor Model:**
   - **Output File:** [`AF_P11021_mature_GRP78_19_654.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/AF_P11021_mature_GRP78_19_654.pdb).
   - Residues 1–18 represent the endoplasmic reticulum signal peptide (`MKLSLVAAMLLLLSAARA`), which is co-translationally cleaved in vivo upon luminal entry. Cleaving residues 1–18 produces the physiologically authentic mature 636-amino-acid receptor (residues 19–654).
2. **Structured Core Domain Model:**
   - **Output File:** [`AF_P11021_core_26_633.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/AF_P11021_core_26_633.pdb).
   - Further excises the flexible amino-terminal loop (residues 19–25) and the unstructured carboxyl-terminal ER retention motif (`KDEL`, residues 634–654), matching the exact construct boundaries of structured biochemical assays.

---

## 4. Manifest of Cleaned & Validated 3D Models

| Model Identifier | Source Construct | Retained Elements | Cleaved Artifacts | File Path |
|:---|:---|:---|:---|:---|
| `PDB_3LDL_ChainB_MgATP` | PDB 3LDL (2.30 Å) | Chain B (NBD 26–407) + $\text{Mg}^{2+}\text{-ATP}$ | Chain A (apo $\text{Mg}^{2+}$), buffer ions | [`data/structures/3d_models/cleaned/PDB_3LDL_ChainB_MgATP.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_3LDL_ChainB_MgATP.pdb) |
| `PDB_5EVZ_ChainA_MgADP_Pi` | PDB 5EVZ (1.85 Å) | Chain A (NBD 26–407) + $\text{ADP}\cdot\text{P}_i\cdot\text{Mg}^{2+}$ | Chain B, waters, crystallization agents | [`data/structures/3d_models/cleaned/PDB_5EVZ_ChainA_MgADP_Pi.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_5EVZ_ChainA_MgADP_Pi.pdb) |
| `PDB_5E85_SBD_apo_cleaned` | PDB 5E85 (2.57 Å) | Chain A (SBD 418–637) | Cis-fused peptide tail 638–653 (`SENLYFQGSNRLLLTG`) | [`data/structures/3d_models/cleaned/PDB_5E85_SBD_apo_cleaned.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/PDB_5E85_SBD_apo_cleaned.pdb) |
| `AF_P11021_mature_GRP78` | AlphaFold DB | Mature GRP78 (Residues 19–654) | Signal peptide (Residues 1–18) | [`data/structures/3d_models/cleaned/AF_P11021_mature_GRP78_19_654.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/AF_P11021_mature_GRP78_19_654.pdb) |
| `AF_P11021_core_26_633` | AlphaFold DB | Structured Core (Residues 26–633) | Signal peptide (1–18), N-loop (19–25), C-tail (634–654) | [`data/structures/3d_models/cleaned/AF_P11021_core_26_633.pdb`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/cleaned/AF_P11021_core_26_633.pdb) |
