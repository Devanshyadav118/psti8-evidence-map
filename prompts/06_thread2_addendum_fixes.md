---
prompt_id: 06
slug: thread2_addendum_fixes
status: PENDING (new, written 2026-10-31 after checking the addendum against the repo)
tool: Antigravity
model: Gemini 3.8 Flash (High)
depends_on: docs/thread2_audit_addendum.md (in repo)
---
# 06 Fix the four rule problems in the Thread 2 audit addendum, plus two cleanups

**Model:** Gemini 3.8 Flash (High) in Antigravity. No Exa or Firecrawl needed.
**Why:** Checked against the repo, the addendum is useful (it flags four single-lab bullets and writes up the GRP78 conflict) but it breaks project rules:
1. Three "verbatim abstract" quotes in section 2 are 48, 59 and 57 words. The rule is paraphrase, quotes under 15 words.
2. The "Mechanistic Reconciliation" section states interpretation as fact (for example an ATF6 and "hormesis" explanation; ATF6 is not in the quoted abstracts) and speculates about PSTi8 pharmacology.
3. Section 3 gives "Methods Section 2.1"-style sex locators for papers that were only read at abstract level. That cannot have come from reading the Methods. MeSH terms are an indexing hint only.
4. It reports the single-lab bullets but does not list the exact statements to downgrade.

## Prompt

```text
Step 0: If prompts/06_thread2_addendum_fixes.md does not exist, save this entire prompt text verbatim to that path first, with front matter (prompt_id, date, model, status: running). When the run ends, update status and add the commit hash.

Read AGENTS.md, INDEX.md, STATE.md, docs/thread2_audit_addendum.md, docs/thread2_verification.md. Task: fix four rule problems in the Thread 2 audit addendum and clean up two repo issues. Do not call Exa or Firecrawl. Do not edit data/papers_registry.csv, data/evidence_table.csv or any raw Argon file.

1. Quote length. In section 2 of docs/thread2_audit_addendum.md the three "Verbatim Abstract-Level Finding" cells quote 48, 59 and 57 words. AGENTS.md allows paraphrase only and no quote over 15 words. Replace each cell with a paraphrase plus at most one quote of under 15 words. Count the words of every quote you keep and search the whole file for any other quote over 15 words.
2. Inference labeling. In "Mechanistic Reconciliation", mark every sentence that is not stated in the three abstracts as [Inference] (for example the ATF6 and EDEM-hormesis explanation, the intracellular/extracellular split, and the whole "Relevance to PSTi8 Pharmacology" paragraph). Keep the text, but label it, and add one sentence saying it is a hypothesis to test, not a finding.
3. Sex provenance. In section 3 the column "Full-Text / Indexing True Sex (For Context)" gives Methods locators (for example "Methods Section 2.1") for papers whose status is abstract_only. For every row whose status in data/staging/thread2_registry_unverified.csv is not full_text_read, replace the entry with "MeSH-indexed: Male", "MeSH-indexed: Male, Female" or "not checked", and remove any Methods locator you did not actually read. Say at the top of section 3 that MeSH indexing is a hint and must not be used to fill sex fields in evidence_table.csv.
4. Single-lab downgrade list. Add a section "Statements to downgrade from Established to Contested (single-lab)" listing, for bullets 2, 3, 7 and 8 of the Established section of data/staging/thread2_argon_raw.md: the bullet number, a paraphrase of the sentence that rests on one lab, the lab, and the new label. Do not edit thread2_argon_raw.md (the raw file stays as Argon wrote it).
5. Repo cleanup. data/staging/ contains a stray file named "thread2_argon_raw..md" (double dot, 1 byte). Confirm it is empty or only whitespace, then remove it with git rm. If it has real content, do not remove it and tell me.
6. STATE.md. The Phase 1 checklist still shows "Execute searches for Threads 1, 2, 4, 5, 6" unchecked. Replace it with two lines: done (Threads 1, 2, 3 searched; Threads 2 and 3 verified) and open (Thread 1 not yet verified; Threads 4, 5, 6 not searched). Add a dated line about this fix.
7. Update INDEX.md if any file was added or removed. Run ./scripts/sync.sh and show me a summary only (what changed in each of the six items).
```

## What to check in the summary
- Item 1: the longest remaining quote in the file is under 15 words.
- Item 3: no "Methods" locator remains for a row that is not full_text_read.
- Item 5: the stray file was removed (or kept with a reason).
