---
prompt_id: 10
slug: novelty_check_direction1
status: done
date: 2026-11-02
tool: Antigravity (Exa)
model: Gemini 3.8 Flash (High)
commit: a8d8686
legacy_name: "Prompt 7"
---
# 10 Direction 1 novelty check (systematic review + sex-as-variable audit of PSTi8 preclinical studies)

**Model:** Gemini 3.8 Flash (High) in Antigravity with Exa. Second opinion: Gemini 4 Argon with Google Search.
**Why early:** if someone has already published this review, the rest of the plan changes. A search that returns nothing is not proof of novelty.

## Prompt

```text
Step 0: If prompts/10_novelty_check_direction1.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md (Tool Usage Policy), INDEX.md, STATE.md. Task: check whether the planned project already exists: a systematic review or sex-coverage audit of preclinical PSTi8 / pancreastatin-inhibitor studies.

1. Run at least 15 Exa searches (different angles: "systematic review PSTi8", "pancreastatin inhibitor review", "sex as a biological variable chromogranin A peptide", "preclinical meta-analysis pancreastatin", protocol registrations on OSF, PROSPERO and PreclinicalTrials.eu, bioRxiv/medRxiv preprints, and 2025-2026 items). Do not use Firecrawl except to read one specific page that Exa cannot return. Log every Exa call in docs/tool_usage_log.md.
2. Record every query and result in docs/novelty_check_direction1.md with URL, date, and a one-line verdict (same topic / related / unrelated).
3. List every existing review that covers PSTi8 and state what it does and does not cover (for example sex reporting, risk of bias, ARRIVE compliance). Existing known reviews: garg2023_review, lu2025_fimmu, maj2025_fimmu, christoffersson2026_fcdhc, ioannidis2022_peptides.
4. End with a verdict: novel / partly novel / already done, and what would make it novel. Mark anything unverified. Do not overstate: absence of search results is not proof of novelty.
5. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only.
```
