---
prompt_id: 02
slug: verify_thread1
status: running
date: 2026-11-02
tool: Antigravity
model: Gemini 3.8 Flash (High)
depends_on: data/staging/thread1_argon_raw.md (in repo)
legacy_name: '"Thread 1 verification" / "Step 2"'
---
# 02 Verify Thread 1 (pancreastatin / CHGA biology)

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Why now:** Thread 1 is the only searched thread that has not been verified. Argon marked all 34 rows `verified: yes` although it could not open pages, so nothing from this file may be merged yet.
**Expected output:** `data/staging/thread1_registry_unverified.csv` (the name the merge prompt expects), `docs/thread1_verification.md`, STATE.md and INDEX.md updated, one sync commit.

## Facts about the input (checked against the repo)
34 registry rows: 29 primary, 4 review, 1 preprint. Status: 32 `abstract_only`, 2 `not_read` (`kitayama1994_lifesci`, `udupi1999_regulpept`). All 34 are marked verified=yes by Argon.

## Prompt

```text
Step 0: If prompts/02_verify_thread1.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, change status to done or failed and add the commit hash.

Read AGENTS.md (including the Tool Usage Policy), INDEX.md, STATE.md, data/staging/thread1_argon_raw.md, docs/thread2_verification.md (as the pattern to follow). Task: verify every row of the Thread 1 registry. Argon's "verified: yes" is not trusted; Argon could not open pages.

Do not edit data/papers_registry.csv or data/evidence_table.csv or the raw Argon file. Never fill facts from memory. Free routes first (PubMed E-utilities, Crossref, PMC, Europe PMC). Do not call Exa or Firecrawl unless a free route cannot answer; if you do, log it in docs/tool_usage_log.md. Quotes must be under 15 words; paraphrase everything else.

1. Extract the REGISTRY CSV block from data/staging/thread1_argon_raw.md (34 rows).
2. For each row check: the DOI resolves (Crossref); title, first author, year and journal match the row; the PMID in source_url matches the DOI; the abstract supports the one_line_relevance. Fix wrong metadata and record every change as old value -> new value. If a DOI or page cannot be opened, set verified=could_not_open and say why. Pay extra attention to muntjewerff2025_biorxiv (preprint whose source_url points to PubMed; confirm what that PMID is and name the published version in verification_note) and to the 13 rows marked paywalled.
3. Set verified to one of: yes (opened and matched), partial (paper is real but the relevance line or a detail needed correcting), no (wrong or not found), could_not_open. Set status honestly (abstract_only / full_text_read / not_read) based on what YOU read. Do not expect most rows to be "yes with no change"; a perfect score needs proof in the note.
4. Add columns verification_note and role. Role must be one of: pst_chga_biology (primary studies of pancreastatin/CHGA biology, genetics, assays), background_mechanism, sex_estrogen, methods_reference, review, context_only. Put preprint in the type column, not in role. If a preprint has a published version, name it in verification_note.
5. Check these known issues in the Knowledge Summary and report each as confirmed, fixed or unresolved:
   a. "Plasma PST ~5-30 pM in healthy subjects" mixes different assays and populations. O'Connor 2005 reports about 4.9 pM controls and 18.5 pM in obese T2D (n=6 per group). Sanchez-Margalet 1998 reports 30 vs 46 pmol/L in pregnancy (11 controls vs 12 GDM). A single normal range is misleading. Also check what odorisio2010_pancreas actually reports.
   b. The weight-loss claim ("PST stays elevated after weight loss") appears in Open Questions cited to unalkocabas2024_obstetmed, a GDM paper that has nothing to do with weight loss. The supported source is oconnor2005_jcem. Check it and say what the abstract supports.
   c. Gly297Ser (allu2022_diabetes): the abstract reports about 1.3-1.6-fold risk for T2D, hypertension, CAD and metabolic syndrome, but the full-text table reportedly shows hypertension and CAD lose significance after age, sex and BMI adjustment while T2D and metabolic syndrome stay significant. Check what is verifiable from open text and soften the "Established" wording if needed.
   d. kitayama1994_lifesci and udupi1999_regulpept are status=not_read but are cited under "Established". Downgrade them or find an open abstract (PubMed abstract counts as abstract_only).
   e. "439-aa, chromosome 14" has no citation; find support (expected ioannidis2022_peptides, PMC10760928).
   f. Any bullet under Established that rests on one lab or one lab network must move to Contested as single-lab. The Mahata / O'Connor / Gayen (UCSD) / Mahapatra network counts as ONE lab network. List every bullet you move.
   g. Any number in the summary that does not match its cited paper.
   h. Mouse-vs-human claims: the "Established" Chga-KO / PSTv1 bullet relies on Mahata-lab papers plus muntjewerff2025_commbiol; decide whether two independent labs really support it.
6. Write the verified rows to data/staging/thread1_registry_unverified.csv with the same columns as data/staging/thread2_registry_unverified.csv. Write docs/thread1_verification.md with: counts of yes/partial/no/could_not_open; every metadata correction (old -> new); every known issue and its outcome; rows that need a human to look at the full text; Knowledge Summary statements that should be rewritten, with the replacement wording as a paraphrase and marked [Inference] where it goes beyond a source.
7. Update STATE.md and INDEX.md. Run ./scripts/sync.sh and show me a summary only (counts, top corrections, unresolved items).
```

## What to check in the summary before accepting
- Number of rows still `yes` (a big drop from 34 is a good sign; 34/34 again is a warning).
- All eight known issues (a-h) have an answer.
- kitayama1994 and udupi1999 downgraded; the Gly297Ser wording softened.
- Any DOI corrections listed with old -> new.
- Quote lengths under 15 words in docs/thread1_verification.md (the Thread 2 addendum broke this rule; see prompt 06).
