---
prompt_id: 01
slug: tool_policy_setup
status: DONE (2026-10-31, repo commit be74f43)
tool: Antigravity
model: "Gemini 3.8 Flash (High) (earlier runs: Gemini 3.6 Flash (High))"
legacy_name: '"Prompt 1" / "Step 1"'
---
# 01 Tool usage policy setup (already run, kept for the record)

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Outcome:** AGENTS.md has a "Tool Usage Policy" section, `.gitignore` protects secrets and `data/fulltext_cache/`, `docs/tool_usage_log.md` exists (Firecrawl budget 1,000 credits; 998 left after 2 test credits). The agent also made one Exa and one Firecrawl test call although the prompt said not to. It cost 2 credits and was logged.

## Prompt as given

```text
Read AGENTS.md, INDEX.md, STATE.md. Task: set up the tool usage policy for Exa and Firecrawl. Do not run any searches or scrapes in this task.

1. Add a "Tool usage policy" section to AGENTS.md with these rules:
   - Exa is for discovery (finding papers, checking whether a topic already exists). Firecrawl is for reading ONE specific page we already have a URL for. Never use Firecrawl crawl or map.
   - Try free routes first: PubMed, Crossref, PMC, Europe PMC. Use Exa or Firecrawl only when those cannot answer.
   - Before any batch that would use more than 10 credits, list the planned calls and the credit estimate and wait for my OK.
   - Log every Exa and Firecrawl call in docs/tool_usage_log.md (date | tool | query or URL | credits used | running total).
   - Never commit API keys, .env files, or full-text copies of copyrighted papers. Cached full text goes only in data/fulltext_cache/, which is gitignored.
   - Paraphrase only; no quote longer than 15 words in any file.
   - If a tool is unavailable or out of credits, say so and stop that step instead of guessing.
2. Create docs/tool_usage_log.md with a header row and one line saying no calls have been made yet.
3. Add data/fulltext_cache/, .env and *.key to .gitignore (create it if missing, keep existing lines).
4. List which MCP tools are connected (Exa, Firecrawl) in your summary. Do not call them.
5. Add a dated line to STATE.md saying the policy was added.
6. Run ./scripts/sync.sh and show me a summary only.
```

## Known gap in the repo version of the policy
The repo's AGENTS.md policy does not yet contain: the ">10 credits ask first" rule, the "free routes first" rule, or the "no quote over 15 words" rule from this prompt. Prompt 13 adds them.
