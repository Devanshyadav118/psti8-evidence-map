---
prompt_id: 07
slug: merge_registries
status: running
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-02
---
# 07 Merge verified registries into data/papers_registry.csv

```text
Step 0: If prompts/07_merge_registries.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id: 07, slug: merge_registries, date: 2026-11-02, model: "Gemini 3.8 Flash (High)", status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md. Task: merge verified staging registries into data/papers_registry.csv. Back up the current file to data/staging/papers_registry_pre_merge.csv first. Do not edit evidence_table.csv.

1. Read every data/staging/threadN_registry_unverified.csv that has a matching docs/threadN_verification.md (Thread 1, Thread 2, Thread 3, and Thread 6).
2. Include only rows with verified=yes or partial. Quarantine rows marked no or could_not_open into data/staging/rejected_rows.csv with the reason.
3. Deduplicate by DOI (case-insensitive). The 26 Thread 3 rows are already in data/papers_registry.csv; do not duplicate them. If a paper appears in several threads, keep one row and list all threads in the thread column (e.g. "Thread 1, Thread 2"). If a preprint and its published version both appear, keep both and add a published_version_of column.
4. Role vocabulary (one controlled list): primary_evidence (direct PSTi8 preclinical studies), pst_chga_biology, background_mechanism, sex_estrogen, methods_reference, review, context_only. Map existing roles to this list without changing meaning and list every mapping you made in the report.
5. Keep the existing columns plus verification_note, role and thread. Do not overwrite corrections already in existing rows.
6. Write docs/registry_merge_report.md: row counts per thread before and after, duplicates merged, rows rejected, role mappings, and anything uncertain.
7. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only.
```
