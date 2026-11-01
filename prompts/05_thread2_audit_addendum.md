---
prompt_id: 05
slug: thread2_audit_addendum
status: "DONE (output: docs/thread2_audit_addendum.md; has four problems, see prompt 06)"
tool: Antigravity
model: Gemini 3.8 Flash (High)
legacy_name: "Step A"
---
# 05 Thread 2 audit addendum (already run)

**Model:** Gemini 3.8 Flash (High) in Antigravity.
**Outcome:** `docs/thread2_audit_addendum.md` exists in the repo and was committed (latest repo commit at handoff: 7893768). It answered all five questions. Problems found when checked against the repo are listed in `03_STATUS_AND_NEXT_STEPS.md` and fixed by prompt 06.

## Prompt as given

```text
Read AGENTS.md, INDEX.md, STATE.md. Task: read-only audit of docs/thread2_verification.md and data/staging/thread2_registry_unverified.csv. Change no files except a new docs/thread2_audit_addendum.md. Do not call Exa or Firecrawl.

Answer each with a file and line reference:
1. How many Knowledge Summary bullets in data/staging/thread2_argon_raw.md are marked Established, and for each: how many independent labs support it among the verified rows? List any that rest on one lab or one lab network.
2. Is the GRP78 conflict recorded anywhere? (kammoun2009_jci: GRP78 overexpression improves insulin signaling; ye2010_diabetes: Grp78+/- mice resist diet-induced insulin resistance; also angelini2022_natcommun.) If not, write it as an entry in the addendum with the registry ids and the exact abstract-level claims.
3. List every row where sex is not stated in the abstract, with sex=NOT_READ.
4. List rows where verified=yes but the one_line_relevance goes beyond what the abstract states. Quote under 15 words.
5. Run ./scripts/sync.sh and show me a summary only.
```

(The phrase "exact abstract-level claims" in item 2 led the agent to paste whole abstract passages of 48 to 59 words, which breaks the 15-word rule. Do not reuse that phrase.)
