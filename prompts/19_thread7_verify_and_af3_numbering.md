---
prompt_id: 19
slug: thread7_verify_and_af3_numbering
status: done
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-03
commit: c010d3a
---

Step 0: Save this prompt verbatim to prompts/19_thread7_verify_and_af3_numbering.md (front matter: prompt_id 19, status running, tool Antigravity, model "Gemini 3.8 Flash (High)", date 2026-11-03). Update status and commit hash at the end.

Read AGENTS.md, STATE.md, data/staging/thread7_argon_raw.md, data/papers_registry.csv, docs/gap_map.md. Argon's output is UNTRUSTED.

1. Verify all 8 Thread 7 registry rows via PubMed/Crossref/PMC only. Map each to existing registry IDs (do not create duplicate IDs: valicherla2018_scirep = valicherla2018, tshikudi2024_ijms = tshikudi2024_colitis). Add only truly new rows (likely biswas2014_plosone, allu2014_jbc) to data/papers_registry.csv with role=pst_chga_biology.
2. From open full text (PMC3896336, PMC3924308, PMC5993748, PMC11641510) confirm or correct: (a) Biswas ATPase IC50 value(s); (b) Allu 2014 helix residues and % helicity; (c) which GRP78 residues Hossain 2018 report for PSTi8 and PST docking (Table 1) and which structure numbering the PDB 5E84 chain uses relative to UniProt P11021; (d) whether Tshikudi 2024 reports a Sex x Treatment interaction or analysed sexes separately (cite the section and figure). Quotes under 15 words.
3. Check Argon's absence claims ("no GRP78 knockdown", "no SPR/ITC", "no AlphaFold model") with 5 Exa searches each, and word the result as "not found in N searches", never "none exist". Log Exa calls in docs/tool_usage_log.md; no Firecrawl.
4. AF3 numbering fix (important): AF3 residue IDs are 1-based along the submitted chain, which begins at UniProt residue 19. Re-derive domain boundaries (NBD, linker, SBDbeta, SBDalpha) from the crystal structures 3LDL and 5EVZ and UniProt P11021, convert all AF3 contact residues to UniProt numbering (+18), re-label domains, and correct every statement in docs/structural_data_inventory.md, docs/gap_map.md and notes/topics/06 that used chain numbers with UniProt domain labels.
5. Compare AF3 contact residues (all 5 samples, UniProt numbering) with the Hossain 2018 docking residues from step 2c. Report overlap per complex. Wording: "partial overlap", "AF3 predicts"; do not say "refutes" or "confirms".
6. Write docs/thread7_verification.md and add a "Target-engagement evidence" section to docs/gap_map.md. Update STATE.md, INDEX.md, prompts/INDEX.md. Run ./scripts/sync.sh and show a summary only.
