---
prompt_id: 17
slug: integrate_af3_esm2_and_generate_figures
status: done
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-03
commit: 195d352
---

Step 0: Save this entire prompt text verbatim to prompts/17_integrate_af3_esm2_and_generate_figures.md first, with front matter (prompt_id: 17, slug: integrate_af3_esm2_and_generate_figures, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-03). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, docs/gap_map.md, docs/structural_data_inventory.md, and docs/pathway_and_variant_analysis.md.

Task: (1) add AF3 MSA folders to .gitignore so git stays lightweight, (2) save the complete AlphaFold 3 interface contact and confidence datasets into CSV and docs, (3) clean experimental PDBs per crystallographic construct audit, (4) author the 6 topic synthesis notes in notes/topics/, and (5) generate the SYRCLE/ARRIVE matrix and 5 publication-grade figures in figures/. Do not call Exa or Firecrawl (0 credits). Quotes strictly under 15 words.

1. Git Hygiene for AlphaFold 3 Outputs:
   - Append `data/structures/3d_models/**/msas/` and `*.a3m` to `.gitignore` so the ~204 MB MSA files are ignored while all `.cif` structures, `*_summary_confidences_*.json`, and `*_job_request.json` files are tracked in git.

2. AlphaFold 3 Interface Contact & Confidence Tables (`scripts/analyze_af3_complexes.py`):
   - Parse all 5 seeds (`model_0` to `model_4`) across the 4 AF3 folders in `data/structures/3d_models/fold_af3_grp78_mature_*`:
     * Save all seed confidence metrics (complex_id, seed_rank, ranking_score, iptm, ptm, pairwise_chain_iptm_AB, min_pae_AB, fraction_disordered) to `data/structures/3d_models/af3_complex_metrics.csv`.
     * Save all atomic residue-residue contacts (<4.0 A in model_0) with domain annotations (NBD 26-407, Interdomain Linker 408-419, SBDbeta 427-537, SBDalpha 538-633) to `data/structures/3d_models/af3_interface_contacts.csv`.
   - Append the 4 top-ranked AF3 `.cif` complexes and the 2 new CSVs to `data/structures/structures_manifest.csv`.
   - Update `docs/structural_data_inventory.md` (Section 6) and `docs/gap_map.md` (Section 4) with the three key AF3 discoveries:
     a. Refutation of direct ATPase catalytic pocket binding: PSTi8 (ranking 0.85, ipTM 0.81, min PAE 2.30 A) binds as an unshielded steric wedge at the Interdomain Linker (residues 408-416) and SBDbeta entrance (residues 433-478) via its C-terminal E18-M19-A20-V21 tip (0 NBD contacts), projecting its E14-E17 polyanionic core into solvent.
     b. WT PST-29 (ranking 0.81, ipTM 0.76, 140 contacts) acts as a tri-domain allosteric clamp spanning the NBD (6 residues: M178-L399), Linker (7 residues), and SBDbeta cleft (19 residues) driven by its hydrophobic VPQGLFRG anchor.
     c. Resolution of the Gly297Ser (rs9658664) paradox: polar Ser25 clashes with the hydrophobic SBDbeta pocket, cutting contacts by 43.6% (140 -> 79), eliminating NBD bridging (6 -> 0), and dropping pairwise ipTM from 0.47 to 0.28 (min PAE 2.89 -> 5.54 A), whereas PSTi8 excises residues 22-29 and is completely immune.

3. Crystallographic Receptor Sanitization (`scripts/clean_receptor_structures.py`):
   - Using Biopython (`Bio.PDB`), save cleaned receptor structures in `data/structures/3d_models/cleaned/`:
     * `PDB_3LDL_ChainB_MgATP.pdb` (Chain B + ATP + MG; Chain A lacks MG)
     * `PDB_5EVZ_ChainA_MgADP_Pi.pdb` (Chain A + ADP + PO4 + MG)
     * `PDB_5E85_SBD_apo_cleaned.pdb` (Chain A 418-637 with fused 638-653 SENLYFQGSNRLLLTG peptide removed)
     * `AF_P11021_mature_GRP78_19_654.pdb`
   - Document construct caveats (including why raw PDB 5E84 has T229A and the L3,4 loop 457-TASDNQP-463 replaced by VGG) in `docs/structural_audit_argon.md`.

4. Complete the 6 Topic Synthesis Notes (`notes/topics/`) & SYRCLE/ARRIVE Matrix:
   - Ensure all 6 topic synthesis notes exist in `notes/topics/` (`01_chga_processing_and_pst_biology.md` through `06_structural_biophysics_and_variants.md`) incorporating the new AF3 findings, with zero quotes over 15 words.
   - Generate `data/syrcle_arrive_matrix.csv` across all 20 primary studies in `data/evidence_table.csv`.

5. Generate 5 Publication-Grade Figures (`scripts/generate_manuscript_figures.py` -> `figures/` in 300 DPI `.png` and `.svg`/`.pdf`):
   - `fig1_preclinical_sex_audit`: Disease model sex distribution (N=20) & ARRIVE 2.0 / SABV compliance rates.
   - `fig2_factorial_power_and_pk`: 2x2 Sex x Treatment interaction power curves (`data/power_results.csv`) & male vs female PK comparison (`valicherla2022_pk`).
   - `fig3_peptide_biophysics_and_disorder`: Sliding-window charge/hydropathy (`EEEEEMAV` vs `VPQGLFRG`) & AlphaFold CHGA monomer pLDDT disorder profile.
   - `fig4_af3_cofolding_and_contacts`: Panel A: AF3 ipTM, pTM, pairwise ipTM, and min PAE comparison across PSTi8, WT PST-29, E287K, and G297S. Panel B: Contact count breakdown across GRP78 domains (NBD vs Interdomain Linker vs SBDbeta) showing the allosteric linker wedge mechanism and G297S collapse.
   - `fig5_grp78_conservation_and_interactome`: Panel A: 100% cross-species SBDbeta conservation (Human, Mouse, Rat). Panel B: STRING/Reactome signaling network (ER luminal IRE1-TRAF2-JNK1-IRS1 Ser307 vs cell-surface GRP78-AKT1).

6. Update `STATE.md`, `INDEX.md`, and `prompts/INDEX.md`. Run `./scripts/sync.sh` and show me a summary only.
