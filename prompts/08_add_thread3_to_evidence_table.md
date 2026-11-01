---
prompt_id: 08
slug: add_thread3_to_evidence_table
status: PENDING
tool: Antigravity
model: Gemini 3.8 Flash (High); Claude Sonnet 4.6 if quota is back
depends_on: docs/staging_new_studies.md, docs/schema.md (both in repo)
legacy_name: "Prompt 5"
---
# 08 Add the new Thread 3 primary studies to the evidence table

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Why:** `data/evidence_table.csv` still has 11 studies; Thread 3 verification found about 9 new primary studies (plus 1 preprint) that are listed in `docs/staging_new_studies.md` but not yet in the table. The sex-coverage denominator in `docs/audit_report.md` must then be recomputed.

## Prompt

```text
Step 0: If prompts/08_add_thread3_to_evidence_table.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, docs/schema.md, docs/staging_new_studies.md, data/evidence_table.csv. Task: add the verified new Thread 3 primary studies to data/evidence_table.csv using the current schema.

1. Add one row per primary study listed in docs/staging_new_studies.md (gupta2019_dex, valicherla2020_jpba, singh2020_fetuina, reza2021_mito, goand2023_peptides, goand2023_lifesci, garg2023_ejp, garg2023_aminoacids, tshikudi2024_jcag). Treat goand2022_ssrn as a preprint of goand2023_peptides, not a separate study. Keep existing paper IDs unchanged.
2. Fill sex fields and sex_source only from the abstract or open-access full text with a locator; otherwise NOT_READ. Do not infer sex from model type. MeSH terms are a hint only and must not be used to fill sex fields. For open-access papers (singh2020_fetuina, tshikudi2024_jcag) read the open text and fill all columns with locators.
3. Regenerate the counts in docs/audit_report.md (denominator, studies including both sexes, sex analyzed as a variable, interaction tested) so every number matches the table, and list which numbers rest on abstract-only evidence.
4. Update docs/spot_check_list.md with 10 new rows to check by hand.
5. Do not use Exa or Firecrawl. Quotes under 15 words. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary of changes only.
```
