---
prompt_id: 15
slug: verify_thread6
status: running
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-02
---
# 15 Verify Thread 6 Registry (Methods and Reporting Standards)

```text
Step 0: Save this entire prompt text verbatim to prompts/15_verify_thread6.md first, with front matter (prompt_id: 15, slug: verify_thread6, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-02). When the run ends, update status to done and add the commit hash.

Read AGENTS.md (including the Tool Usage Policy), INDEX.md, STATE.md, data/staging/thread6_argon_raw.md, and docs/thread2_verification.md plus scripts/verify_thread2.py as the pattern to follow. Task: verify every row of the Thread 6 registry (Methods and Reporting Standards). Argon's "verified: yes" is not trusted.

Do not edit data/papers_registry.csv, data/evidence_table.csv, or the raw Argon file. Never fill facts from memory. Free routes first (PubMed E-utilities, Crossref, PMC, Europe PMC). Do not call Exa or Firecrawl unless a free route cannot answer; if you do, log it in docs/tool_usage_log.md. Quotes must be strictly under 15 words; paraphrase everything else.

1. Extract the REGISTRY CSV block from data/staging/thread6_argon_raw.md. Count the data rows and compare with the counts in Argon's LIMITS section; report any mismatch.
2. For every row, query PubMed and Crossref (in batches; save raw API responses to data/staging/thread6_raw_api_responses.json). Check:
   - DOI resolves on Crossref.
   - Title, first author, year, and journal match the row.
   - PMID in source_url matches the DOI.
   - The abstract or open text supports the one_line_relevance.
3. For any quantitative claim in a one_line_relevance, confirm whether it is in the abstract or only in the full text (with locator). If only in the full text and unverified, mark it unverified.
4. Set verified honestly (yes / partial / no / could_not_open) and status (abstract_only / full_text_read / not_read). Add columns role and verification_note. Role must be one of: methods_reference, review, primary_evidence, pst_chga_biology, background_mechanism, sex_estrogen, context_only. (Thread 6 items will primarily be methods_reference or review).
5. Check preprints for peer-reviewed published versions (e.g., check lieberum2025_medrxiv).
6. Knowledge Summary audit:
   - Confirm that the ARRIVE 2.0, SYRCLE, SABV audit, and PRISMA statements have independent laboratory / consortium consensus.
   - Verify that the simulation finding regarding two-way ANOVA factorial power without sample size doubling (phillips2023_plosbiol) is accurately categorized as a single-lab simulation study under Contested.
   - Ensure all quotes in the report are under 15 words.
7. Write the verified staging table to data/staging/thread6_registry_unverified.csv.
8. Write the verification report to docs/thread6_verification.md (counts, every metadata correction old -> new, and rows needing human review).
9. Update prompts/INDEX.md, INDEX.md, and STATE.md. Run ./scripts/sync.sh and show me a summary only.
```
