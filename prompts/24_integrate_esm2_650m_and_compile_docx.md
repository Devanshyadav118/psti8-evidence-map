---
prompt_id: 24
slug: integrate_esm2_650m_and_compile_docx
target: "Meta Muse"
status: running
date: 2026-11-06
---

Step 0: Save this prompt verbatim to prompts/24_integrate_esm2_650m_and_compile_docx.md (front matter: prompt_id: 24, slug: integrate_esm2_650m_and_compile_docx, target: "Meta Muse", status: running, date: 2026-11-06). When the run ends, update status to done and record the git commit hash.

Read AGENTS.md, STATE.md, manuscript/manuscript.md, data/structures/1d_sequences/esm2_650m_dms_scores.csv, and docs/decisions/2026-11-06_prompt23_paywall_reconciliation.md.

Task: (1) integrate the ESM-2 650M deep mutational scanning metrics into the manuscript and variant tables, (2) update docs/pathway_and_variant_analysis.md, and (3) compile manuscript/Targeting_GRP78_PSTi8_Manuscript.docx for journal submission.

1. Update Variant Scoring Datasets:
   - In data/structures/1d_sequences/variant_scores.csv, append or update the ESM-2 650M LLR column with the exact values:
     * Gly297Ser (rs9658664): LLR = -0.4453
     * Glu287Lys (rs140089514): LLR = -3.2734
   - Update data/structures/structures_manifest.csv to verify esm2_650m_dms_scores.csv is tracked.

2. Manuscript Text Integration (manuscript/manuscript.md):
   - In Section 3.7 ("Resolution of the Gly297Ser Genetic Paradox and Structural Refractoriness of PSTi8"), update the language model mutational scanning paragraphs to report:
     * Full 650-million-parameter ESM-2 model (facebook/esm2_t33_650M_UR50D) across all 580 variants.
     * The poly-Glu latch (positions 14-21) mean LLR of -3.1296 vs. C-terminal anchor (positions 22-29) mean LLR of -0.9186 (~3.4x greater evolutionary constraint).
     * Gly297Ser near-neutral score (-0.4453) vs. Glu287Lys severe deleterious score (-3.2734).
     * Met19Glu as the single most favored substitution (LLR = +4.58), demonstrating that a 6th glutamate in the latch is evolutionarily preferred.
   - In Section 2 ("Methods - In Silico Structural Biology"), update the ESM-2 description to reflect the full 650M model execution.

3. Update Documentation:
   - In docs/pathway_and_variant_analysis.md, add a dedicated subsection recording the 650M DMS metrics, the 3.4x constraint ratio, and the Met19Glu finding.

4. Compile Submission Word Document:
   - Compile manuscript/manuscript.md to manuscript/Targeting_GRP78_PSTi8_Manuscript.docx using pandoc (or a lightweight Python script using python-docx if pandoc is unavailable).
   - Verify that the resulting .docx opens cleanly and preserves tables, headers, and reference lists.

5. Update STATE.md, INDEX.md, and prompts/INDEX.md. Run ./scripts/sync.sh and report:
   - Confirmation of manuscript text updates.
   - Path and size of the compiled .docx file.
   - Latest git commit hash on main.
