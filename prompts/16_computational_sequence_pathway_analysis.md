---
prompt_id: 16
slug: computational_sequence_pathway_analysis
date: 2026-11-02
model: "Gemini 3.8 Flash (High)"
status: running
---
# 16 Computational Sequence, Variant, and Pathway Analysis

```text
Step 0: Save this entire prompt text verbatim to prompts/16_computational_sequence_pathway_analysis.md first, with front matter (prompt_id: 16, slug: computational_sequence_pathway_analysis, date: 2026-11-02, model: "Gemini 3.8 Flash (High)", status: running). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, and docs/structural_data_inventory.md. Task: perform local computational sequence profiling, cross-species alignment, variant impact scoring, and pathway interaction retrieval for PSTi8, WT PST-29, human variants, and GRP78 (HSPA5) using local Python and free REST APIs. Do not call Exa or Firecrawl (0 credits). Paraphrase all text; quotes must be strictly under 15 words.

1. Sliding-Window Physicochemical Profiles:
   - Write and execute a script to calculate sliding-window net charge at pH 7.4 and Kyte-Doolittle hydropathy (window size = 5, step = 1) across:
     * Human WT PST-29: PEGKGEQEHSQQKEEEEEMAVVPQGLFRG
     * Human PSTi8: PEGKGEQEHSQQKEEEEEMAV
     * Mouse PST: PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG (or UniProt P26339 coordinates)
     * Rat PST: PEGKGEQEHSQQEEEEEEEMAVVPQGLFRG (or UniProt P10354 coordinates)
   - Quantify the local electrostatic dipole created by the penta-glutamate cluster (EEEEEMAV) and the hydropathy drop from removing the C-terminal octapeptide VPQGLFRG.
   - Save data to data/structures/1d_sequences/sliding_window_profiles.csv.

2. Cross-Species Sequence Alignment:
   - Perform pairwise and multiple sequence alignment (using Biopython Bio.Align or Bio.pairwise2) comparing:
     * Human vs. Mouse vs. Rat Pancreastatin active cores.
     * Human GRP78 (P11021, mature 19-654) vs. Mouse GRP78 (P20029, mature 20-655) vs. Rat GRP78 (P06761, mature 19-654). Note explicitly the +1 residue numbering offset in mouse due to its 19-aa signal peptide.
   - Tabulate percent identity, percent similarity, and non-conserved substitutions in the NBD (ATPase domain) and SBD (substrate-binding domain).
   - Save to data/structures/1d_sequences/cross_species_alignment.csv.

3. Human Coding Variant Impact Profiling:
   - Profile the two verified human missense variants:
     * Gly297Ser (rs9658664; mature PST position 25, precursor CHGA P10645 Gly315Ser; located in the cleaved 8-mer VPQGLFRG outside PSTi8).
     * Glu287Lys (rs140089514; mature PST position 15, precursor CHGA Glu305Lys; located directly in the EEEEEMAV core of PSTi8).
   - Compute BLOSUM62 substitution scores, delta charge at pH 7.4, and delta isoelectric point (pI). If torch/transformers is installed and lightweight ESM-2 (e.g. facebook/esm2_t6_8M_UR50D) is cached or fast to run on CPU, compute zero-shot log-likelihood ratios; otherwise document the BLOSUM/charge metric.
   - Save to data/structures/1d_sequences/variant_scores.csv.

4. Pathway Interaction Retrieval (STRING & Reactome REST APIs):
   - Query STRING REST API (https://string-db.org/api/json/network?identifiers=HSPA5&species=9606) and Reactome Content Service API for human GRP78 (HSPA5).
   - Extract direct high-confidence functional interaction partners relevant to metabolic signaling: INSR, IRS1, IRS2, AKT1, PRKAA1, MAPK8, SREBF1, and ER stress sensors (ERN1/IRE1, EIF2AK3/PERK, ATF6).
   - Save structured records (source_node, target_node, interaction_score, evidence_types, pathway_name) to data/structures/pathway_interactions.csv.

5. Author Synthesis Report:
   - Create docs/pathway_and_variant_analysis.md synthesizing:
     * How the EEEEEMAV motif creates an electrostatic binding latch while VPQGLFRG acts as a hydrophobic anchor.
     * Why Gly297Ser increases PST potency while being absent in PSTi8.
     * Cross-species compatibility of administering human PSTi8 to rodent models.
     * How the GRP78 interactome connects extracellular vs. intracellular signaling.

6. Update prompts/INDEX.md, INDEX.md, and STATE.md. Run ./scripts/sync.sh and show me a summary only.
```
