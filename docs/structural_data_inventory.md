# Molecular & Structural Data Inventory: PSTi8, Pancreastatin Variants, and GRP78 (HSPA5)

**Date:** 2026-11-02  
**Scope:** Verified 1D sequence, 2D chemical, and 3D macromolecular structural asset library supporting biophysical and in silico modeling of pancreastatin inhibitor PSTi8, wild-type human pancreastatin, genetic variants, and their molecular target GRP78 (HSPA5).  
**Master Manifest:** [data/structures/structures_manifest.csv](../data/structures/structures_manifest.csv)  
**Physicochemical Dataset:** [data/structures/1d_sequences/peptide_1d_properties.csv](../data/structures/1d_sequences/peptide_1d_properties.csv)

---

## 1. Executive Summary & Asset Map

A total of **28 authenticated molecular and structural assets** were retrieved, verified, and generated across three dimensions (1D, 2D, and 3D) without consuming external search API credits:

- **1D Sequence Assets (14 files):** Canonical FASTA and metadata JSON entries for Chromogranin A (CHGA) and GRP78 (HSPA5) across human, mouse, and rat ([UniProt REST API](https://rest.uniprot.org)), plus verified peptide FASTA files.
- **2D Chemical Assets (24 files):** RDKit-generated isomeric SMILES (`.smi`), 2D Structure-Data Files (`.sdf`), and vector graphics (`.svg`) for PSTi8, WT PST-29, Gly297Ser PST-29, and Glu287Lys PST-29 in both free carboxylate (`-COOH`) and physiological amidated carboxamide (`-CONH2`) states.
- **3D Macromolecular Structures (8 files):** Four experimental high-resolution crystal structures of Human GRP78 from RCSB PDB (`3LDL`, `5EVZ`, `5E84`, `5E85`) and two full-length AlphaFold DB predicted models with Predicted Aligned Error matrices (`AF-P10645-F1`, `AF-P11021-F1`).

---

## 2. 1D Sequence Registry & Peptide Coordinates

### Canonical UniProt Target Summary

| Target Gene | Protein Name | Organism | UniProt ID | Preprotein Length | Signal Peptide | Mature Length |
|:---|:---|:---|:---:|:---:|:---:|:---:|
| **CHGA** | Chromogranin A | *Homo sapiens* | `P10645` | 457 aa | 1–18 (18 aa) | 19–457 (439 aa) |
| **Chga** | Chromogranin A | *Mus musculus* | `P26339` | 463 aa | 1–18 (18 aa) | 19–463 (445 aa) |
| **Chga** | Chromogranin A | *Rattus norvegicus* | `P10354` | 466 aa | 1–18 (18 aa) | 19–466 (448 aa) |
| **HSPA5** | GRP78 / BiP | *Homo sapiens* | `P11021` | 654 aa | 1–18 (18 aa) | 19–654 (636 aa) |
| **Hspa5** | GRP78 / BiP | *Mus musculus* | `P20029` | 655 aa | 1–19 (19 aa) | 20–655 (636 aa) |
| **Hspa5** | GRP78 / BiP | *Rattus norvegicus* | `P06761` | 654 aa | 1–18 (18 aa) | 19–654 (636 aa) |

### Pancreastatin Peptides & Derivatives

All coordinates are verified against canonical human Chromogranin A (`P10645`):

1. **Human Full Pancreastatin (PST-52):**
   - *Sequence:* `GESRSEALAVDGAGKPGAEEAQDPEGKGEQEHSQQKEEEEEMAVVPQGLFRG`
   - *Coordinates:* Mature residues 250–301 (Preprotein residues 268–319; 52 amino acids).
2. **Human Wild-Type Core Pancreastatin (WT PST-29):**
   - *Sequence:* `PEGKGEQEHSQQKEEEEEMAVVPQGLFRG`
   - *Coordinates:* Mature residues 273–301 (Preprotein residues 291–319; 29 amino acids).
   - *Note:* In vivo biological activity requires carboxyl-terminal amidation (`-CONH2`, derived from glycine cleavage).
3. **Human Pancreastatin Inhibitor PSTi8 (21-mer):**
   - *Sequence:* `PEGKGEQEHSQQKEEEEEMAV`
   - *Coordinates:* Mature residues 273–293 (Preprotein residues 291–311; 21 amino acids).
   - *Design:* Truncates the carboxyl-terminal octapeptide `VPQGLFRG` while retaining the acidic core.
4. **Cleaved Carboxyl-Terminal Octapeptide:**
   - *Sequence:* `VPQGLFRG`
   - *Coordinates:* Mature residues 294–301 (Preprotein residues 312–319; 8 amino acids).
5. **Human Gly297Ser Variant (rs9658664):**
   - *Sequence:* `PEGKGEQEHSQQKEEEEEMAVVPQSLFRG`
   - *Coordinates:* Position 25 of PST-29 (mature residue 297, preprotein residue 315 mutated from Glycine to Serine).
6. **Human Glu287Lys Variant:**
   - *Sequence:* `PEGKGEQEHSQQKEKEEEMAVVPQGLFRG`
   - *Coordinates:* Position 15 of PST-29 (mature residue 287, preprotein residue 305 mutated from Glutamic acid to Lysine).
7. **Rodent Pancreastatin Sequences:**
   - *Mouse PST-54 (`P26339`, 276–329):* `DDGQSDSQAVDGDGKTEASEALPSEGKGELEHSQQEEDGEEAMVGTPQGLFPQG`
   - *Rat PST-52 (`P10354`, 281–332):* `DDDGQSESQAVNGKTGASEAVPSEGKGELEHSQQEEDGEEAMAGPPQGLFPG`

---

## 3. Physicochemical Comparison: WT PST-29 vs. PSTi8 vs. Gly297Ser

Values were calculated using Biopython ProtParam and RDKit descriptors (recorded in [data/structures/1d_sequences/peptide_1d_properties.csv](../data/structures/1d_sequences/peptide_1d_properties.csv)):

| Descriptor | Human WT PST-29 | PSTi8 (21-mer Inhibitor) | Human Gly297Ser PST-29 | Human Glu287Lys PST-29 | Cleaved 8-mer (`VPQGLFRG`) |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Peptide Length** | 29 aa | 21 aa | 29 aa | 29 aa | 8 aa |
| **Average MW (Free -COOH)** | 3283.54 Da | 2428.53 Da | 3313.57 Da | 3282.60 Da | 873.01 Da |
| **Monoisotopic MW (Free)** | 3281.526 Da | 2427.050 Da | 3311.536 Da | 3280.578 Da | 872.487 Da |
| **Average MW (Amidated -CONH2)** | 3282.56 Da | 2427.55 Da | 3312.58 Da | 3281.62 Da | N/A |
| **Monoisotopic MW (Amidated)** | 3280.542 Da | 2426.066 Da | 3310.552 Da | 3279.594 Da | N/A |
| **Net Charge (pH 7.4)** | **-5.06** | **-6.06** | **-5.06** | **-3.06** | **+0.52** |
| **Isoelectric Point (pI)** | 4.47 | 4.26 | 4.47 | 4.84 | 9.72 |
| **GRAVY Hydropathy** | **-1.531** | **-2.133** | **-1.545** | **-1.545** | **+0.050** |
| **Acidic Residues (Asp + Glu)** | 8 (0 D, 8 E) | 8 (0 D, 8 E) | 8 (0 D, 8 E) | 7 (0 D, 7 E) | 0 |
| **Basic Residues (Arg + Lys + His)**| 4 (1 R, 2 K, 1 H) | 3 (0 R, 2 K, 1 H) | 4 (1 R, 2 K, 1 H) | 5 (1 R, 3 K, 1 H) | 1 (1 R) |
| **Glutamic Acid (E) Content** | 27.6% (8/29) | 38.1% (8/21) | 27.6% (8/29) | 24.1% (7/29) | 0.0% (0/8) |

### Key Biophysical Insights: How Truncation Creates an Inhibitor
1. **Net Negative Charge Shift:** Removing the C-terminal octapeptide removes an Arginine residue (`Arg28` of PST-29), shifting net charge from $-5.06$ to $-6.06$ at neutral pH. PSTi8 is significantly more polyanionic.
2. **Substantial Hydrophilicity Increase:** The cleaved 8-mer `VPQGLFRG` is moderately hydrophobic (GRAVY $+0.050$) and contains hydrophobic residues (Val, Pro, Leu, Phe). Removing this tail drops the GRAVY score of PSTi8 to $-2.133$ (compared to $-1.531$ for WT PST-29). PSTi8 possesses extreme aqueous solubility and minimal non-specific hydrophobic aggregation.
3. **Glutamic Acid Density:** Over 38% of PSTi8 residues are glutamic acids (`8/21`), concentrated in an uninterrupted poly-Glu block (`EEEEEM`). This acidic tract is hypothesized to mimic competitive binding to basic clefts in GRP78 without triggering downstream catalytic activation [Inference].
4. **Charge and Mass Shifts in Genetic Variants:**
   - `Gly297Ser` introduces a polar serine hydroxyl group, adding $+30.03\text{ Da}$ and slightly increasing hydrophilicity without changing net charge.
   - `Glu287Lys` replaces an acidic carboxylate with a basic amino group, creating a $+2.0$ unit net charge shift (from $-5.06$ to $-3.06$) and increasing the isoelectric point to $4.84$.

---

## 4. 2D Chemical Representations & SMILES Catalog

All chemical structures were assembled and validated in RDKit with both termini explicitly resolved:

| Peptide Form | Terminus | Canonical Isomeric SMILES | File Links |
|:---|:---:|:---|:---|
| **PSTi8 (21-mer)** | Free (`-COOH`) | `CSCC[C@H](NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CO)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(=O)O)NC(=O)CNC(=O)[C@H](CCCCN)NC(=O)CNC(=O)[C@H](CCC(=O)O)NC(=O)[C@@H]1CCCN1)C(=O)N[C@@H](C)C(=O)N[C@@H](C(C)C)C(=O)O` | [SDF](../data/structures/2d_chemical/human_psti8_21_free_cooh.sdf) • [SMI](../data/structures/2d_chemical/human_psti8_21_free_cooh.smi) • [SVG](../data/structures/2d_chemical/human_psti8_21_free_cooh.svg) |
| **PSTi8 (21-mer)** | Amidated (`-CONH2`) | `CSCC[C@H](NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CO)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(=O)O)NC(=O)CNC(=O)[C@H](CCCCN)NC(=O)CNC(=O)[C@H](CCC(=O)O)NC(=O)[C@@H]1CCCN1)C(=O)N[C@@H](C)C(=O)N[C@@H](C(C)C)C(N)=O` | [SDF](../data/structures/2d_chemical/human_psti8_21_amidated_conh2.sdf) • [SMI](../data/structures/2d_chemical/human_psti8_21_amidated_conh2.smi) • [SVG](../data/structures/2d_chemical/human_psti8_21_amidated_conh2.svg) |
| **WT PST-29** | Free (`-COOH`) | `CSCC[C@H](NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CO)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(=O)O)NC(=O)CNC(=O)[C@H](CCCCN)NC(=O)CNC(=O)[C@H](CCC(=O)O)NC(=O)[C@@H]1CCCN1)C(=O)N[C@@H](C)C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](C(C)C)C(=O)N1CCC[C@H]1C(=O)N[C@@H](CCC(N)=O)C(=O)NCC(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](CCCNC(=N)N)C(=O)NCC(=O)O` | [SDF](../data/structures/2d_chemical/human_wt_pst_29_free_cooh.sdf) • [SMI](../data/structures/2d_chemical/human_wt_pst_29_free_cooh.smi) • [SVG](../data/structures/2d_chemical/human_wt_pst_29_free_cooh.svg) |
| **WT PST-29** | Amidated (`-CONH2`) | `CSCC[C@H](NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CO)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(=O)O)NC(=O)CNC(=O)[C@H](CCCCN)NC(=O)CNC(=O)[C@H](CCC(=O)O)NC(=O)[C@@H]1CCCN1)C(=O)N[C@@H](C)C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](C(C)C)C(=O)N1CCC[C@H]1C(=O)N[C@@H](CCC(N)=O)C(=O)NCC(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](CCCNC(=N)N)C(=O)NCC(N)=O` | [SDF](../data/structures/2d_chemical/human_wt_pst_29_amidated_conh2.sdf) • [SMI](../data/structures/2d_chemical/human_wt_pst_29_amidated_conh2.smi) • [SVG](../data/structures/2d_chemical/human_wt_pst_29_amidated_conh2.svg) |
| **Gly297Ser PST-29** | Amidated (`-CONH2`) | `CSCC[C@H](NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCCCN)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CO)NC(=O)[C@H](Cc1c[nH]cn1)NC(=O)[C@H](CCC(=O)O)NC(=O)[C@H](CCC(N)=O)NC(=O)[C@H](CCC(=O)O)NC(=O)CNC(=O)[C@H](CCCCN)NC(=O)CNC(=O)[C@H](CCC(=O)O)NC(=O)[C@@H]1CCCN1)C(=O)N[C@@H](C)C(=O)N[C@@H](C(C)C)C(=O)N[C@@H](C(C)C)C(=O)N1CCC[C@H]1C(=O)N[C@@H](CCC(N)=O)C(=O)N[C@@H](CO)C(=O)N[C@@H](CC(C)C)C(=O)N[C@@H](Cc1ccccc1)C(=O)N[C@@H](CCCNC(=N)N)C(=O)NCC(N)=O` | [SDF](../data/structures/2d_chemical/human_g297s_pst_29_amidated_conh2.sdf) • [SMI](../data/structures/2d_chemical/human_g297s_pst_29_amidated_conh2.smi) • [SVG](../data/structures/2d_chemical/human_g297s_pst_29_amidated_conh2.svg) |

---

## 5. 3D Macromolecular Structures: Experimental Crystal vs. Predicted Models

### Experimental PDB Crystal Structures (Human GRP78 / BiP)

All coordinate files are saved in [data/structures/3d_models/](../data/structures/3d_models/):

1. **`PDB_3LDL.pdb` (Resolution: 2.30 Å):**
   - *Domain:* Human GRP78 Nucleotide-Binding Domain (NBD / ATPase domain, residues 25–427).
   - *Ligands:* Bound ATP analog and magnesium ion ($\text{Mg}^{2+}$).
   - *Utility:* Defines the catalytic pocket where pancreastatin reportedly interferes with GRP78 ATPase activity.
2. **`PDB_5EVZ.pdb` (Resolution: 1.85 Å):**
   - *Domain:* High-resolution crystal structure of human GRP78 ATPase domain.
   - *Utility:* Ultra-high resolution template for active-site hydrogen bonding analysis.
3. **`PDB_5E84.pdb` (Resolution: 2.99 Å):**
   - *Domain:* Full-length human BiP / GRP78 in the **ATP-bound domain-docked open state**.
   - *Conformation:* The NBD and substrate-binding domain (SBD) are packed together, with the substrate-binding lid open.
4. **`PDB_5E85.pdb` (Resolution: 2.57 Å):**
   - *Domain:* Isolated substrate-binding domain (SBD) representing the **domain-undocked closed state**.
   - *Conformation:* Helical lid closed over the peptide substrate binding groove.

### AlphaFold DB Predicted Models & Intrinsic Disorder Analysis

1. **Human Chromogranin A (`AF_P10645_F1_model.pdb` / `pae.json`):**
   - *Full Protein Mean pLDDT:* **58.81** (predominantly low confidence).
   - *Full Pancreastatin Domain (PST-52, residues 268–319):* Mean pLDDT = **38.97** (very low confidence, < 50).
   - *WT PST-29 Region (residues 291–319):* Mean pLDDT = **36.83**.
   - *PSTi8 Region (residues 291–311):* Mean pLDDT = **36.40**.
   - *C-terminal 8-mer (`VPQGLFRG`, residues 312–319):* Mean pLDDT = **37.95**.
   - *Structural Interpretation:* CHGA and its pancreastatin domain are intrinsically disordered in solution [Inference]. In monomeric prediction, AlphaFold correctly models the domain as an unstructured random coil. Meaningful tertiary structure requires induced-fit folding upon interaction with binding partners.
2. **Human GRP78 / HSPA5 (`AF_P11021_F1_model.pdb` / `pae.json`):**
   - *Full Protein Mean pLDDT:* **89.99** (high confidence).
   - *Nucleotide-Binding Domain (residues 19–425):* Mean pLDDT = **94.95** (very high confidence, > 90).
   - *Substrate-Binding Domain (residues 426–654):* Mean pLDDT = **84.29** (well-structured $\beta$-sandwich and $\alpha$-helical lid).

---

## 6. Ready-to-Run AlphaFold 3 Co-Folding Job Inputs

Because pancreastatin is an intrinsically disordered peptide that undergoes conformational change upon binding, monomeric predictions are insufficient. Below are ready-to-copy input specifications for the **AlphaFold 3 Web Server** ([alphafoldserver.com](https://alphafoldserver.com)) to model the induced-fit complex between human GRP78 and either WT PST-29 or PSTi8.

### Job 1: WT Pancreastatin + Full GRP78 + ATP + $\text{Mg}^{2+}$
```json
{
  "name": "AF3_GRP78_mature_WT_PST29_ATP_Mg",
  "modelSeeds": [1],
  "sequences": [
    {
      "proteinChain": {
        "sequence": "EEEDKKEDVGTVVGIDLGTTYSCVGVFKNGRVEIIANDQGNRITPSYVAFTPEGERLIGDAAKNQLTSNPENTVFDAKRLIGRTWNDPSVQQDIKFLPFKVVEKKTKPYIQVDIGGGQTKTFAPEEISAMVLTKMKETAEAYLGKKVTHAVVTVPAYFNDAQRQATKDAGTIAGLNVMRIINEPTAAAIAYGLDKREGEKNILVFDLGGGTFDVSLLTIDNGVFEVVATNGDTHLGGEDFDQRVMEHFIKLYKKKTGKDVRKDNRAVQKLRREVEKAKRALSSQHQARIEIESFYEGEDFSETLTRAKFEELNMDLFRSTMKPVQKVLEDSDLKKSDIDEIVLVGGSTRIPKIQQLVKEFFNGKEPSRGINPDEAVAYGAAVQAGVLSGDQDTGDLVLLDVCPLTLGIETVGGVMTKLIPRNTVVPTKKSQIFSTASDNQPTVTIKVYEGERPLTKDNHLLGTFDLTGIPPAPRGVPQIEVTFEIDVNGILRVTAEDKGTGNKNKITITNDQNRLTPEEIERMVNDAEKFAEEDKKLKERIDTRNELESYAYSLKNQIGDKEKLGGKLSSEDKETMEKAVEEKIEWLESHQDADIEDFKAKKKELEEIVQPIISKLYGSAGPPPTGEEDTAEKDEL",
        "count": 1
      }
    },
    {
      "proteinChain": {
        "sequence": "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG",
        "count": 1
      }
    },
    {
      "ligand": {
        "ligand": "ATP",
        "count": 1
      }
    },
    {
      "ion": {
        "ion": "MG",
        "count": 1
      }
    }
  ]
}
```

### Job 2: Pancreastatin Inhibitor PSTi8 + Full GRP78 + ATP + $\text{Mg}^{2+}$
```json
{
  "name": "AF3_GRP78_mature_PSTi8_21_ATP_Mg",
  "modelSeeds": [1],
  "sequences": [
    {
      "proteinChain": {
        "sequence": "EEEDKKEDVGTVVGIDLGTTYSCVGVFKNGRVEIIANDQGNRITPSYVAFTPEGERLIGDAAKNQLTSNPENTVFDAKRLIGRTWNDPSVQQDIKFLPFKVVEKKTKPYIQVDIGGGQTKTFAPEEISAMVLTKMKETAEAYLGKKVTHAVVTVPAYFNDAQRQATKDAGTIAGLNVMRIINEPTAAAIAYGLDKREGEKNILVFDLGGGTFDVSLLTIDNGVFEVVATNGDTHLGGEDFDQRVMEHFIKLYKKKTGKDVRKDNRAVQKLRREVEKAKRALSSQHQARIEIESFYEGEDFSETLTRAKFEELNMDLFRSTMKPVQKVLEDSDLKKSDIDEIVLVGGSTRIPKIQQLVKEFFNGKEPSRGINPDEAVAYGAAVQAGVLSGDQDTGDLVLLDVCPLTLGIETVGGVMTKLIPRNTVVPTKKSQIFSTASDNQPTVTIKVYEGERPLTKDNHLLGTFDLTGIPPAPRGVPQIEVTFEIDVNGILRVTAEDKGTGNKNKITITNDQNRLTPEEIERMVNDAEKFAEEDKKLKERIDTRNELESYAYSLKNQIGDKEKLGGKLSSEDKETMEKAVEEKIEWLESHQDADIEDFKAKKKELEEIVQPIISKLYGSAGPPPTGEEDTAEKDEL",
        "count": 1
      }
    },
    {
      "proteinChain": {
        "sequence": "PEGKGEQEHSQQKEEEEEMAV",
        "count": 1
      }
    },
    {
      "ligand": {
        "ligand": "ATP",
        "count": 1
      }
    },
    {
      "ion": {
        "ion": "MG",
        "count": 1
      }
    }
  ]
}
```

### Job 3: Gly297Ser Variant + Full GRP78 + ATP + $\text{Mg}^{2+}$
```json
{
  "name": "AF3_GRP78_mature_G297S_PST29_ATP_Mg",
  "modelSeeds": [1],
  "sequences": [
    {
      "proteinChain": {
        "sequence": "EEEDKKEDVGTVVGIDLGTTYSCVGVFKNGRVEIIANDQGNRITPSYVAFTPEGERLIGDAAKNQLTSNPENTVFDAKRLIGRTWNDPSVQQDIKFLPFKVVEKKTKPYIQVDIGGGQTKTFAPEEISAMVLTKMKETAEAYLGKKVTHAVVTVPAYFNDAQRQATKDAGTIAGLNVMRIINEPTAAAIAYGLDKREGEKNILVFDLGGGTFDVSLLTIDNGVFEVVATNGDTHLGGEDFDQRVMEHFIKLYKKKTGKDVRKDNRAVQKLRREVEKAKRALSSQHQARIEIESFYEGEDFSETLTRAKFEELNMDLFRSTMKPVQKVLEDSDLKKSDIDEIVLVGGSTRIPKIQQLVKEFFNGKEPSRGINPDEAVAYGAAVQAGVLSGDQDTGDLVLLDVCPLTLGIETVGGVMTKLIPRNTVVPTKKSQIFSTASDNQPTVTIKVYEGERPLTKDNHLLGTFDLTGIPPAPRGVPQIEVTFEIDVNGILRVTAEDKGTGNKNKITITNDQNRLTPEEIERMVNDAEKFAEEDKKLKERIDTRNELESYAYSLKNQIGDKEKLGGKLSSEDKETMEKAVEEKIEWLESHQDADIEDFKAKKKELEEIVQPIISKLYGSAGPPPTGEEDTAEKDEL",
        "count": 1
      }
    },
    {
      "proteinChain": {
        "sequence": "PEGKGEQEHSQQKEEEEEMAVVPQSLFRG",
        "count": 1
      }
    },
    {
      "ligand": {
        "ligand": "ATP",
        "count": 1
      }
    },
    {
      "ion": {
        "ion": "MG",
        "count": 1
      }
    }
  ]
}
```
*(Note: GRP78 sequence represents mature human residues 19–654, omitting the 18-amino-acid endoplasmic reticulum targeting signal peptide `MKLSLVAAMLLLLSAARA` which is cleaved in vivo.)*
