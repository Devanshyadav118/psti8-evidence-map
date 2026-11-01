---
prompt_id: 13
slug: antigravity_save_prompts
status: DONE (2026-11-01, repo commit ea9750c)
tool: Antigravity
model: Gemini 3.8 Flash (High)
---
# 13 Save all prompts into the repo and add the prompt-saving rule

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Before you run it:** copy the `prompts/` folder from the handoff zip into the repo root (in Obsidian or the file manager). The repo will then contain `prompts/01_...md` to `prompts/13_...md`. This prompt checks them, indexes them, adds the rule to AGENTS.md and syncs.

## Prompt

```text
Read AGENTS.md, INDEX.md, STATE.md. Task: set up a permanent prompt library in the repo. Do not call Exa or Firecrawl. Do not edit data/papers_registry.csv, data/evidence_table.csv or any raw Argon file.

1. Check that the folder prompts/ exists and list its files. If it is missing or empty, stop and tell me; do not invent prompt text.
2. Every file in prompts/ must start with YAML front matter containing: prompt_id, slug, status, tool, model. If any is missing, add it from the file's heading without changing the prompt text inside the code block. Do not edit any prompt text.
3. Create prompts/INDEX.md: a table with columns id | file | what it does | tool | model | status | date | repo commit (if known), sorted by id, and one line at the top: "Every prompt given to an agent for this project is saved here before it runs."
4. Add this section to AGENTS.md (keep all existing content):

   ## Prompt Saving Rule
   1. Every prompt that a human gives to an agent for this project is saved verbatim in prompts/ as prompts/NN_slug.md BEFORE the agent starts the work (Step 0 of the prompt).
   2. Front matter: prompt_id, slug, status (running / done / failed / pending), tool, model, date.
   3. When the run ends, update status and add the repo commit hash. Never edit the prompt text after it has run; if it must change, save a new file with the next id.
   4. Keep prompts/INDEX.md in sync, and list prompts/ in INDEX.md.

5. Also add these rules to the Tool Usage Policy in AGENTS.md if they are not already there: try free routes first (PubMed, Crossref, PMC, Europe PMC) before Exa or Firecrawl; before any batch above 10 credits, list planned calls and the credit estimate and wait for my OK; no quote longer than 15 words in any file; Argon output is never trusted until verified against PubMed/Crossref; a lab network counts as one lab; MeSH indexing is a hint, not a source for sex fields.
6. Add prompts/ and prompts/INDEX.md to INDEX.md. Add a dated line to STATE.md: "Prompt library added".
7. Run ./scripts/sync.sh and show me a summary only (files found, files fixed, rules added).
```
