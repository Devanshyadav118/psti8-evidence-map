---
prompt_id: 14
slug: collect_structural_assets
status: done
commit: 5819d87
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-02
---
# 14 Collect and verify 1D, 2D, and 3D structural assets

```text
Step 0: Save this entire prompt text verbatim to prompts/14_collect_structural_assets.md first, with YAML front matter (prompt_id: 14, slug: collect_structural_assets, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-02). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md. Task: collect and verify 1D, 2D, and 3D molecular and structural assets for PSTi8, wild-type Pancreastatin (PST), human PST coding variants, and GRP78 (HSPA5) across human, mouse, and rat using free APIs (UniProt REST, RCSB PDB, AlphaFold DB) and local Python (Biopython, RDKit). Do not call Exa or Firecrawl (0 credits). Do not edit existing literature registries. Never invent accession numbers or coordinates from memory.

1. Create directory structure:
   - data/structures/1d_sequences/
   - data/structures/2d_chemical/
   - data/structures/3d_models/
   - scripts/collect_structures.py

2. Write and run scripts/collect_structures.py to perform the following:
   a. 1D Sequence Retrieval (UniProt REST API):
      - Fetch full canonical FASTA sequences and metadata JSON for Chromogranin A (Human: P10645, Mouse: P26339, Rat: P10354) and GRP78 / HSPA5 (Human: P11021, Mouse: P20029, Rat: P06761). Save in data/structures/1d_sequences/.
      - Extract and verify the exact peptide sequences and residue coordinates:
        * Human WT PST-29: PEGKGEQEHSQQKEEEEEMAVVPQGLFRG (verify exact start/end positions in P10645)
        * Human PST-52 (full 52-mer hCgA 250-301)
        * PSTi8 (21-mer C-terminally truncated inhibitor): PEGKGEQEHSQQKEEEEEMAV
        * Human PST coding variants: Gly297Ser (rs9658667) and Glu287Lys
      - Compute 1D physicochemical descriptors using Biopython ProtParam (length, molecular weight, net charge at pH 7.4, isoelectric point pI, GRAVY hydropathy, acidic/basic residue counts) and save to data/structures/1d_sequences/peptide_1d_properties.csv.

   b. 2D Chemical Representations (RDKit):
      - Using RDKit (install via pip if missing), build the exact 2D molecular structures for PSTi8, WT PST-29, and Gly297Ser PST-29, explicitly modeling both the free C-terminus (-COOH) and the biologically active C-terminally amidated form (-CONH2).
      - Export canonical isomeric SMILES (.smi), 2D structure-data files (.sdf), and 2D chemical depiction images (.svg) into data/structures/2d_chemical/. Record exact monoisotopic and average molecular weights in peptide_1d_properties.csv.

   c. 3D Experimental & Predicted Receptor Structures (RCSB PDB & AlphaFold DB):
      - Query RCSB PDB REST API and download experimental crystal structures for Human GRP78:
        * 3LDL (GRP78 ATPase / Nucleotide-Binding Domain bound to ATP)
        * 5EVZ (GRP78 NBD complex)
        * 5E84 and 5E85 (Full-length GRP78 open and closed conformations)
      - Fetch AlphaFold DB full-length predicted structures (.pdb and _pae.json) for Human CHGA (AF-P10645-F1) and Human GRP78 (AF-P11021-F1) to verify baseline per-residue pLDDT confidence across the PST region.
      - Save all 3D files in data/structures/3d_models/ and generate a manifest table data/structures/structures_manifest.csv (columns: asset_id, molecule, species, dimension, source_db, accession_or_pdb, resolution_or_plddt, file_path, notes).

3. Create docs/structural_data_inventory.md summarizing:
   - All retrieved 1D, 2D, and 3D assets with exact UniProt/PDB accessions.
   - Physicochemical comparison between WT PST-29, Gly297Ser PST-29, and PSTi8 (highlighting how removing the C-terminal 8 residues VPQGLFRG changes net charge, hydropathy, and size).
   - Ready-to-copy job inputs (exact sequences and ion/ligand settings) for running de novo 3D co-folding on the AlphaFold 3 Web Server (PST + GRP78 vs. PSTi8 + GRP78).

4. Update INDEX.md, prompts/INDEX.md, and STATE.md. Run ./scripts/sync.sh and output a clean summary of all files generated and key physicochemical findings.
```
