Every prompt given to an agent for this project is saved here before it runs.

# Prompts Index

| id | file | what it does | tool | model | status | date | repo commit (if known) |
|:---:|---|---|---|---|:---:|:---:|---|
| 01 | [01_tool_policy_setup.md](01_tool_policy_setup.md) | Tool usage policy setup for Exa/Firecrawl, gitignore secrets/cache, create tool_usage_log.md | Antigravity | Gemini 3.8 Flash (High) | done | 2026-10-31 | `be74f43` |
| 02 | [02_verify_thread1.md](02_verify_thread1.md) | Verify all 34 Thread 1 (pancreastatin/CHGA biology) rows against PubMed/Crossref | Antigravity | Gemini 3.8 Flash (High) | done | 2026-11-02 | `5c40be1` |
| 03 | [03_verify_thread_pattern.md](03_verify_thread_pattern.md) | Reusable verification prompt pattern for candidate threads (used for Thread 2; reuse for Threads 4–6) | Antigravity | Gemini 3.8 Flash (High) | template | 2026-10-31 | `96dc0fe` |
| 04 | [04_argon_search_template.md](04_argon_search_template.md) | Argon literature search prompt template and scope blocks (AI Studio) for Threads 2, 4, 5, 6 | Google AI Studio | Gemini 4 Argon | template | 2026-10-31 | - |
| 05 | [05_thread2_audit_addendum.md](05_thread2_audit_addendum.md) | Thread 2 audit addendum (lab independence, GRP78 conflict, sex reporting, one-liners) | Antigravity | Gemini 3.8 Flash (High) | done | 2026-10-31 | `35d3a8c` / `7893768` |
| 06 | [06_thread2_addendum_fixes.md](06_thread2_addendum_fixes.md) | Fix quote length, inference labels, and sex provenance in Thread 2 addendum | Antigravity | Gemini 3.8 Flash (High) | done | 2026-11-01 | `0eb8bf9` |
| 07 | [07_merge_registries.md](07_merge_registries.md) | Merge verified registries (Thread 2, Thread 1, Thread 3) into master data/papers_registry.csv | Antigravity | Gemini 3.8 Flash (High) | pending | 2026-10-31 | - |
| 08 | [08_add_thread3_to_evidence_table.md](08_add_thread3_to_evidence_table.md) | Add ~9 new Thread 3 primary studies from staging to data/evidence_table.csv, recompute sex audit | Antigravity | Gemini 3.8 Flash (High) | pending | 2026-10-31 | - |
| 09 | [09_fulltext_extraction.md](09_fulltext_extraction.md) | Open-access full-text extraction with strict Firecrawl credit pre-approval checks | Antigravity | Gemini 3.8 Flash (High) | pending | 2026-10-31 | - |
| 10 | [10_novelty_check_direction1.md](10_novelty_check_direction1.md) | Novelty search check for existing PSTi8 preclinical systematic reviews and sex-as-variable audits | Antigravity | Gemini 3.8 Flash (High) | running | 2026-11-02 | - |
| 11 | [11_gap_map.md](11_gap_map.md) | Gap map synthesis and contribution direction selection (Direction 1 vs 2) | Antigravity / Gemini Project | Claude Opus 4.6 / Gemini 3.8 Flash / Gemini 4 Argon | pending | 2026-10-31 | - |
| 12 | [12_new_chat_starter.md](12_new_chat_starter.md) | Standardized starter prompt for opening new chat sessions in the Gemini Project | Gemini Project | Gemini 4 Argon | ready | 2026-10-31 | - |
| 13 | [13_antigravity_save_prompts.md](13_antigravity_save_prompts.md) | Save prompt library into repo, index all prompts, and add prompt-saving & policy rules to AGENTS.md | Antigravity | Gemini 3.8 Flash (High) | done | 2026-11-01 | `ea9750c` |
