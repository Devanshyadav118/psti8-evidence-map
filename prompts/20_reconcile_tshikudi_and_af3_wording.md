---
prompt_id: 20
slug: reconcile_tshikudi_and_af3_wording
status: done
commit: 1481f91
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-03
---

Step 0: Save this prompt verbatim to prompts/20_reconcile_tshikudi_and_af3_wording.md (front matter: prompt_id 20, status running, tool Antigravity, model "Gemini 3.8 Flash (High)", date 2026-11-03). Update status and commit hash at the end.

Read AGENTS.md, STATE.md, docs/thread7_verification.md, docs/audit_report.md, notes/papers/tshikudi2024_colitis.md, data/evidence_table.csv.

1. Tshikudi 2024 (10.3390/ijms252312757): re-open the open full text (PMC11641590) and read ALL statistics statements (Methods 4.x and every figure legend). Report exactly which tests were used for which panels, whether any two-way ANOVA or Sex x Treatment interaction is reported anywhere, and the correct section numbers. Quote under 15 words. Then correct docs/audit_report.md, docs/gap_map.md, docs/power_analysis.md, notes/papers/tshikudi2024_colitis.md and data/evidence_table.csv so all agree, and recount the interaction_tested summary (confirmed absent vs unreported).
2. Replace "5 seeds" / "20 models" with "5 diffusion samples from one seed (modelSeeds [1])" in every doc, script comment and note.
3. Fix the linker description: motif VGGSTRIPKIQQLVK is NBD (UniProt 362-376); the linker motif is LLDVCPLTLG (UniProt 416-425). Correct docs/structural_data_inventory.md, docs/gap_map.md and notes/topics/06.
4. Re-read Allu 2014 (PMC3924307) and give the residue numbering the paper itself uses for the helix and salt bridges, noting that position 284 of PST-29 is Gln and HSQQKEE is residues 281-287 in mature PST numbering. Do not repeat numbers you cannot confirm.
5. In the Cross-Platform Comparison section of gap_map.md state: Hossain 2018 docked onto isolated NBD (PDB 3LDP) only; the AF3 jobs had ATP+Mg in the NBD cleft; the 0-residue overlap therefore reflects setup differences and is neither agreement nor disagreement. Add TODO list for AF3 controls: NBD-only (26-407) apo and ADP + PSTi8; scrambled PSTi8; two random 21-mers; HWDFAWPW positive control; PSTi8-E15K; 5 different seeds; Boltz-2/Chai-1 orthogonal run.
6. Update STATE.md, INDEX.md, prompts/INDEX.md, run ./scripts/sync.sh, show a summary only.