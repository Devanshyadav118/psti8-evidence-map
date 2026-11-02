---
prompt_id: 17
slug: complete_phase1_esm2_structures_and_topics
status: done
commit: 538dbc5
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-02
---
# 17 Complete Phase 1: ESM-2, Cleaned Structures, and Topic Synthesis Notes

```text
Step 0: Save this entire prompt text verbatim to prompts/17_complete_phase1_esm2_structures_and_topics.md first, with front matter (prompt_id: 17, slug: complete_phase1_esm2_structures_and_topics, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-02). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, docs/structural_data_inventory.md, docs/pathway_and_variant_analysis.md, and docs/gap_map.md.

Task: complete all remaining Phase 1 computational and synthesis deliverables before entering Phase 2: (1) execute real ESM-2 protein language model embeddings and zero-shot mutational scanning, plus ESMFold 3D peptide predictions, (2) sanitize the 3D GRP78 receptor PDB files per crystallographic construct audit, and (3) author the 6 Phase 1 topic synthesis notes in notes/topics/. Do not call Exa or Firecrawl (0 credits). Paraphrase all text; quotes strictly under 15 words.

1. Real ESM-2 Protein Language Model & ESMFold 3D Peptide Analysis (scripts/run_esm2_analysis.py):
   - Install CPU-only PyTorch and HuggingFace transformers (`pip install --break-system-packages torch --index-url https://download.pytorch.org/whl/cpu transformers`).
   - Load `facebook/esm2_t12_35M_UR50D` (or `facebook/esm2_t6_8M_UR50D`).
   - Compute sequence embeddings and pairwise cosine similarities across full-length Human CHGA (P10645), WT PST-29, PSTi8 (21-mer), Gly297Ser PST-29, Glu287Lys PST-29, Mouse PST, and Rat PST.
   - Compute zero-shot masked marginal log-likelihood ratios (LLR = log P(mut | context) - log P(wt | context)) in both full-length CHGA (P10645) and mature PST-29 context for:
     a. Gly297Ser (rs9658664, P10645 pos 315 / mature PST pos 25)
     b. Glu287Lys (rs140089514, P10645 pos 305 / mature PST pos 15)
     c. Full in silico deep mutational scan across all 29 positions of WT PST-29 (29 positions x 20 amino acids = 580 LLR values) to identify evolutionarily constrained vs. tolerant residues across the EEEEEMAV latch and VPQGLFRG anchor.
   - Save LLR and embedding metrics to `data/structures/1d_sequences/esm2_variant_and_dms_scores.csv` and update `data/structures/1d_sequences/variant_scores.csv` with the real ESM-2 LLR columns.
   - Query the ESM Atlas REST API (`https://api.esmatlas.com/foldSequence/v1/pdb/`) to fold 3D monomer ensembles for WT PST-29, PSTi8, Gly297Ser PST-29, and Glu287Lys PST-29, saving the resulting PDBs into `data/structures/3d_models/esmfold_peptides/`.

2. Crystallographic Receptor Sanitization & Construct Audit (scripts/clean_receptor_structures.py):
   - Create `docs/structural_audit_argon.md` (and `docs/receptor_construct_audit.md`) documenting the verified crystallographic caveats:
     * PDB 3LDL (2.30 A, human NBD 26-407): Chain B has Mg2+ + ATP, whereas Chain A lacks Mg2+.
     * PDB 5EVZ (1.85 A, human NBD 26-407): Wild-type NBD with ADP + PO4 + MG in both chains.
     * PDB 5E84 (2.99 A, human BiP 25-633): Crystallized with the engineered BiP-T229A-L3,4' construct carrying the active-site T229A mutation, replacement of the 7-residue SBDbeta substrate-binding loop L3,4 (457-TASDNQP-463) with a 3-residue VGG linker (abolishing SBDbeta peptide binding), and Zn2+ substituting for Mg2+.
     * PDB 5E85 (2.57 A, human SBD 418-637): Contains a C-terminally fused 16-aa TEV linker + substrate peptide (638-653, SENLYFQGSNRLLLTG) occupying the SBDbeta pocket in cis.
   - Using Biopython (`Bio.PDB`), generate cleaned, docking-ready 3D receptor structures in `data/structures/3d_models/cleaned/`:
     * `PDB_3LDL_ChainB_MgATP.pdb` (Chain B + ATP + MG)
     * `PDB_5EVZ_ChainA_MgADP_Pi.pdb` (Chain A + ADP + PO4 + MG)
     * `PDB_5E85_SBD_apo_cleaned.pdb` (Chain A residues 418-637 with the 638-653 SENLYFQGSNRLLLTG tail cleaved)
     * `AF_P11021_mature_GRP78_19_654.pdb` and `AF_P11021_core_26_633.pdb` (signal peptide 1-18 and disordered KDEL tail removed)
   - Append all new ESM-2, ESMFold, and cleaned PDB files to `data/structures/structures_manifest.csv`.

3. Author the 6 Phase 1 Topic Synthesis Notes (`notes/topics/`):
   - Create `notes/topics/` and write the 6 comprehensive Phase 1 synthesis notes (with YAML front matter, verified citations from `data/papers_registry.csv`, explicit `[Inference]` tags where appropriate, and zero quotes over 15 words):
     * `notes/topics/01_chga_processing_and_pst_biology.md` (Thread 1 synthesis: CHGA cleavage, assay discrepancies, plasma concentrations, single-lab vs established claims)
     * `notes/topics/02_grp78_compartmentalization_and_signaling.md` (Thread 2 synthesis: ER luminal UPR repression vs cell-surface/circulating GRP78 paradox, IRE1-JNK-IRS1 Ser307 cascade)
     * `notes/topics/03_psti8_preclinical_pharmacology.md` (Thread 3 synthesis: all 20 in vivo studies across T2D, MASH, PCOS, perimenopause, and colitis)
     * `notes/topics/04_sex_differences_and_estrous_audit.md` (SABV synthesis: 100% male bias in T2D/DIO, female restriction to reproductive models, 0% baseline estrous staging)
     * `notes/topics/05_factorial_power_and_reporting_standards.md` (Thread 6 + Power synthesis: ARRIVE 2.0, SYRCLE, subgroup testing fallacy, and why n=6 cohorts have <19% interaction power)
     * `notes/topics/06_structural_biophysics_and_variants.md` (Direction 3 synthesis: EEEEEMAV electrostatic latch vs VPQGLFRG hydrophobic anchor, ESM-2 LLR / DMS scan, Gly297Ser excision immunity, 100% SBDbeta conservation, and PDB construct traps)

4. Check off `- [x] Author 6 topic synthesis notes in notes/topics/` in `STATE.md`, update `INDEX.md`, `prompts/INDEX.md`, and `docs/pathway_and_variant_analysis.md` with the ESM-2 results. Run `./scripts/sync.sh` and show me a summary of the ESM-2 scores, cleaned PDBs, and topic notes.
```
