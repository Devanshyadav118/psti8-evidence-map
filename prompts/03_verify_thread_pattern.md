---
prompt_id: 03
slug: verify_thread_pattern
status: TEMPLATE (Thread 2 run DONE, commit 96dc0fe; reuse for Threads 4, 5, 6)
tool: Antigravity
model: Gemini 3.8 Flash (High)
legacy_name: "Prompt 2 pattern"
---
# 03 Verification prompt pattern for Threads 4, 5, 6 (and how Thread 2 was verified)

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Note:** The original Thread 2 verification prompt was written in an earlier chat and was not saved. The text below is reconstructed from what the agent did (its action log and summary) and from the Thread 1 verification prompt. It is the template to use for Threads 4, 5, 6: replace N with the thread number.

## Prompt template

```text
Step 0: If prompts/03_verify_threadN.md does not exist, save this entire prompt text verbatim to that path first (replace N), with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md (including the Tool Usage Policy), INDEX.md, STATE.md, data/staging/threadN_argon_raw.md, and docs/thread2_verification.md plus scripts/verify_thread2.py as the pattern to follow. Task: verify every row of the Thread N registry. Argon's "verified: yes" is not trusted.

Do not edit data/papers_registry.csv, data/evidence_table.csv or the raw Argon file. Never fill facts from memory. Free routes first (PubMed, Crossref, PMC, Europe PMC); Exa/Firecrawl only if a free route cannot answer, logged in docs/tool_usage_log.md. Quotes under 15 words; paraphrase.

1. Extract the REGISTRY CSV block. Count the data rows yourself and compare with the counts in Argon's LIMITS section; report any mismatch.
2. For every row, query PubMed and Crossref (batches of about 10 rows; save raw API responses to data/staging/threadN_raw_api_responses.json). Check DOI resolves, title, first author, year, journal, PMID/PMCID, and that the abstract supports the one_line_relevance.
3. For any number or quantitative claim in a one_line_relevance, say whether it is in the abstract or only in the full text (with the locator, e.g. Fig 1 caption). If only in the full text and the full text was not read, mark it unverified.
4. Biological sex: record sex_in_abstract only from the abstract or the open full text with a locator. MeSH terms are a hint only; label them "MeSH-indexed", never as the Methods. Otherwise NOT_READ.
5. Set verified (yes / partial / no / could_not_open) and status (abstract_only / full_text_read / not_read) honestly. Add columns role and verification_note. Role must be one of: primary_evidence, pst_chga_biology, background_mechanism, sex_estrogen, methods_reference, review, context_only.
6. Cell-type and species check: flag any paper whose model (cancer cell line, different tissue, different species) does not match what the one_line_relevance implies.
7. Knowledge Summary check: for every bullet under Established, count independent labs among verified rows. A lab network counts as one. Report bullets that rest on one lab.
8. Check every preprint for a published version and every 2025-2026 DOI on Crossref.
9. Write data/staging/threadN_registry_unverified.csv and docs/threadN_verification.md (counts, every correction old -> new, Argon's errors, rows needing human full-text reading). Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only.
```

## What the Thread 2 run found (use as a sanity benchmark)
32 rows verified; Argon's LIMITS said 28 (arithmetic error); two rows Argon called unread (`taniguchi2006_cmet`, `kubota2008_cmet`) were real; `zhang2013_plosone` was done in breast and prostate cancer cell lines, not liver; some numbers were only in full-text captions. See `sources/repo_snapshot/docs/thread2_verification.md`.
