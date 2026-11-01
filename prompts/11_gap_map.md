---
prompt_id: 11
slug: gap_map
status: PENDING (end of Phase 1; run after prompts 02, 06, 07, 08, 10)
tool: Antigravity draft, then Gemini 4 Argon second opinion
model: Claude Opus 4.6 in Antigravity if Claude quota is back (best); otherwise Gemini 3.8 Flash (High), then Gemini 4 Argon in the Gemini Project
legacy_name: "Prompt 8"
---
# 11 Gap map and direction choice

**Model:** Claude Opus 4.6 in Antigravity if available; otherwise Gemini 3.8 Flash (High) in Antigravity. Then paste the resulting `docs/gap_map.md` into **Gemini 4 Argon** (Gemini Project) and ask for a critical second opinion (ask it to find unsupported claims and missing gaps; do not ask it to rewrite).

## Prompt

```text
Step 0: If prompts/11_gap_map.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, data/papers_registry.csv, docs/audit_report.md, all notes/topics/*.md (if the folder is empty, say so), docs/thread1_verification.md, docs/thread2_verification.md, docs/thread2_audit_addendum.md, docs/thread3_verification.md, docs/novelty_check_direction1.md and any novelty notes in the project. Task: write docs/gap_map.md.

1. List every candidate contribution that is possible without a wet lab (at least: PSTi8 preclinical systematic review with sex-as-variable audit; sex-stratified CHGA genetics in public T2D data; GRP78 mechanism analysis; structure/docking check; any other gap you find in the notes). For each, give the evidence that the gap exists, with registry ids.
2. Score each 1-5 on: feasibility without a wet lab; novelty (only if the novelty notes support it); usefulness to a lab; publication route (study type, reporting guideline, likely journal type); what is needed beyond the author (second screener, full-text access, domain co-author).
3. Highlight real tensions in the literature that could become the paper's argument, for example: PST binds and inhibits GRP78 ATPase and PSTi8 is said to act through GRP78, yet liver GRP78 overexpression (kammoun2009_jci) and Grp78+/- haploinsufficiency (ye2010_diabetes) are both reported to improve insulin sensitivity, while circulating GRP78 infusion causes insulin resistance (angelini2022_natcommun, single lab); and all metabolic PSTi8 studies come from one lab with almost no two-sex designs. Mark anything that goes beyond the sources as [Inference].
4. Recommend one primary direction and one backup, with a 6-step plan and the tools needed (see the tool candidates in the project's psti8_bioinformatics_tools.xlsx). State clearly what is uncertain. Do not invent numbers. Quotes under 15 words.
5. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only.
```
