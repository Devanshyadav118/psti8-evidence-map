---
prompt_id: 25
slug: antigravity_project_context_briefing
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
status: running
date: 2026-11-06
---

You are Antigravity (Gemini 3.8 Flash, high effort), working inside the PSTi8 evidence-map repository on this machine. This prompt loads the entire project context so you understand what is happening right now and what was done before. Read the files it points to, confirm your understanding in a short summary, and then WAIT for instructions — do not start new work until asked.

## 1. What this project is

A public, CC BY 4.0 systematic evidence audit of published preclinical studies on PSTi8 (pancreastatin inhibitor peptide, PEGKGEQEHSQQKEEEEEMAV-NH2), plus an in silico structural investigation of how PSTi8 engages its target GRP78/HSPA5.

- Repository: https://github.com/Devanshyadav118/psti8-evidence-map (public). Local working copy: the directory you are running in.
- Target journal: *Biology of Sex Differences* (Springer Nature).
- Owner: Devansh Pratap Singh (Devansh Yadav, 23, India). He is in his hometown for Diwali right now, without his PC, working through his phone. He briefs in consolidated bursts and expects one report and one action list back — no drip-feed of questions.

## 2. Where the project stands (2026-11-06 evening, HEAD 28d7125)

- **Phase 0 (complete):** evidence table of all published PSTi8 studies.
- **Phase 1 (complete):** literature audit + computational/structural analysis. Threads 1, 2, 3, 6, 7 searched and verified. **Threads 4 and 5 are NOT yet searched** (Thread 4: disease context — T2D/NASH/PCOS/menopause; Thread 5: competing CHGA-peptide approaches).
- **Phase 2 (manuscript drafted):** full submission-ready manuscript in `manuscript/manuscript.md` (6,122 words, BMC IMRaD format) + `manuscript/cover_letter.md` + compiled `manuscript/Targeting_GRP78_PSTi8_Manuscript.docx` (59,910 bytes). Known limitation of the .docx: LaTeX `$...$` math is literal text, not typeset equations.

Core numbers (all verified against PubMed/Crossref, never from memory):
- 20 primary preclinical studies in `data/evidence_table.csv` (20 rows x 22 columns); 116 verified papers in `data/papers_registry.csv`.
- Sex coverage: both sexes in 3 studies (15.0%), single-sex in 7 (35.0%), unstated in 10 (50.0%). Formal Sex x Treatment interaction tested in 0 of 20 studies. Baseline estrous staging in 0% of female cohorts.
- **14 of the 20 studies are behind publisher paywalls** (Elsevier, Springer, ASPET) with no open full text anywhere (Europe PMC: PMIDs confirmed, no PMCID, openAccess=N). They stay marked honestly as `abstract_only` / `NOT_READ` — nothing is inferred or imputed from disease models or MeSH terms. This is formally documented as a PRISMA 2020 limitation in `docs/audit_report.md` Section 5 and manuscript Section 4.7.

## 3. The structural story (the science)

- PSTi8 is a 21-mer truncation of pancreastatin (PST-29, PEGKGEQEHSQQKEEEEEMAVVPQGLFRG; full-length human CHGA UniProt P10645, PST-29 at preprotein residues 291-319).
- Mechanism: AlphaFold 3 co-folding refutes ATP-pocket docking; PSTi8 acts as an allosteric steric wedge at the interdomain linker-hinge (Ile426) and SBD-beta entrance. The GRP78 substrate-binding cleft is 100.00% conserved across human/mouse/rat.
- ESM-2 deep mutational scans (580 variants, masked marginal LLR, full 457-aa CHGA context):
  - 8M model (Prompt 17): Gly297Ser LLR -0.2043, Glu287Lys LLR -2.0224.
  - **650M model (Prompt 23, `data/structures/1d_sequences/esm2_650m_dms_scores.csv`): Gly297Ser (rs9658664) LLR -0.4453 (near-neutral/tolerated); Glu287Lys (rs140089514) LLR -3.2734 (severely deleterious). Poly-Glu latch (positions 14-21) mean LLR -3.1296 vs C-terminal anchor (positions 22-29) mean -0.9186 — ~3.4x greater evolutionary constraint on the latch. Most favored substitution in the whole scan: Met19Glu (+4.58, a 6th glutamate in the latch). Most deleterious: Glu16Cys (-9.78).**
  - Consequence: Gly297Ser is diabetogenic via GRP78 interface disruption (AF3: contacts 140 -> 79, ipTM 0.47 -> 0.28), NOT via global destabilization — and PSTi8 is structurally immune to it because residue 25 is excised in the 21-mer.
- These 650M metrics are integrated into manuscript Sections 2.7 and 3.7, `data/structures/1d_sequences/variant_scores.csv` (new column `esm2_650m_llr_full_chga_context`), and `docs/pathway_and_variant_analysis.md` (Prompt 24).

## 4. Open decisions and next work (do NOT start these unasked)

1. **Four `inferred_from_model` sex labels** (`singh2019_menopause`, `yadav2024_pcos_let`, `yadav2025_pcos_dhea`, `gupta2019_obesity`): preserved with explicit provenance. Under a strict reading of the no-inference rule they would become `NOT_READ` (sex-NOT_READ 10 -> 14 of 20), which would change the audit report, manuscript, and gap-map numbers. **Awaiting Devansh's call.** Full reasoning: `docs/decisions/2026-11-06_prompt23_paywall_reconciliation.md` — read it.
2. **Threads 4 and 5** still unsearched (see `prompts/INDEX.md` and `STATE.md`; Thread prompts use the prompt-03 verification pattern in `prompts/INDEX.md`).
3. **README update:** record the 14 unread papers' sex coverage and statistics in the public README, leaving unretrievable ones marked unread. The paywall call is now "leave unread", so this is unblocked — but wait for Devansh to ask.
4. **Manuscript submission:** the .docx exists; LaTeX math needs a proper rendering pass before submission if the journal requires it.

## 5. How to work in this repo (non-negotiable)

- **Read `AGENTS.md` first, then `STATE.md`, then `INDEX.md`.** AGENTS.md is the authority here.
- **Never fill a field from memory.** If you did not read the datum in the paper, write `NOT_READ`.
- **Citation verification gate:** PubMed and Crossref are authoritative for any citation, DOI, or author list before it enters the registry or evidence table. Free APIs before Exa/Firecrawl. Firecrawl has a hard 1,000-credit cap (never crawl/map, max 25 pages/task).
- **Quote limit:** paraphrase only; no quote longer than 15 words in any file.
- **Prompt-saving rule:** every prompt given to an agent for this project is saved verbatim in `prompts/` BEFORE the work runs (front matter: prompt_id, slug, status, tool, model, date). When a run ends, update status to done and record the git commit hash. Keep `prompts/INDEX.md` in sync.
- **Update `STATE.md` before ending any session.**
- **Sync:** after finishing a task, sync with `./scripts/sync.sh` (repo rule 7) — it stages, commits, pulls with rebase, and pushes to `origin main`. Never commit secrets, API keys, or full text of paywalled papers.
- **Model:** always Gemini 3.8 Flash on high (`--model gemini-3.8-flash-high`). Only change the model on Devansh's explicit instruction.
- **Permissions in this session:** you are running with `--mode auto` — routine work is auto-approved, but commands that leave the sandbox still ask. Full skip (`--dangerously-skip-permissions`) was explicitly declined earlier and is off the table; do not enable it and do not re-ask Devansh about it.
- **Environment notes:** this VM has no GPU and no CUDA (the 650M scan ran on CPU in bfloat16). `agy` must be invoked by full path (`~/.local/bin/agy`) in non-login shells. `/tmp` is a 512 MB tmpfs — never put large downloads there; use `~/.cache`. The remote-control instance `muse-vm` is live at https://antigravity.google.com (Devansh can reach you there from his phone).

## 6. First task (now)

1. Read `AGENTS.md`, `STATE.md`, `INDEX.md`, and `docs/decisions/2026-11-06_prompt23_paywall_reconciliation.md`.
2. Confirm, in a short summary (under 15 lines): what the repo is, what phase it is in, the three most important open items, and the rules you will follow.
3. Then WAIT for Devansh's next instruction. Do not start Threads 4/5, the README update, the inferred-label downgrade, or any submission step until he asks.
