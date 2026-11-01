---
prompt_id: 09
slug: fulltext_extraction
status: PENDING
tool: Antigravity (Exa and Firecrawl MCP connected)
model: Gemini 3.8 Flash (High)
legacy_name: "Prompt 6"
---
# 09 Open-access full-text extraction

**Model:** Gemini 3.8 Flash (High) in Antigravity, with the Exa and Firecrawl MCP tools connected (they were tested on 2026-10-31).
**Budget:** Firecrawl 1,000 credits total, 998 left at handoff. Max 25 pages per task without approval. One page per call, never crawl or map.

## Prompt

```text
Step 0: If prompts/09_fulltext_extraction.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md (including the Tool Usage Policy), INDEX.md, STATE.md, data/papers_registry.csv. Task: extract data from open-access PSTi8 papers that are currently abstract-only.

1. List registry rows with role=primary_evidence, access=open and status=abstract_only. Show me the list and the credits you plan to use, and wait for my OK.
2. After my OK, for each paper locate the open full text with free routes first (PMC, Europe PMC, publisher open page). Use Exa only to find a URL, and Firecrawl scrape (one page, never crawl) only if the free routes cannot return the text. Cache text only in data/fulltext_cache/ (gitignored, never committed).
3. Write or update notes/papers/<id>.md with paraphrased extraction and locators: species/strain, sex, n per group, dose, route, duration, stats method, sex analyzed as a variable, interaction tested, estrous reporting. Write NOT_READ for anything not found. Do not copy text longer than 15 words.
4. Update evidence_table.csv for these papers only, keeping sex_source accurate.
5. Log every Exa and Firecrawl call in docs/tool_usage_log.md (tool, URL or query, credits used, running total).
6. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only.
```
