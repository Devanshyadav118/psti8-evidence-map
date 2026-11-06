# Decision: Prompt 23 paywall reconciliation — preserve `inferred_from_model` sex labels

Date: 2026-11-06
Prompt: [23_muse_gpu_sync_and_esm2_650m_dms.md](../prompts/23_muse_gpu_sync_and_esm2_650m_dms.md)

## What was done
All 14 paywalled primary studies were re-verified against PubMed/Crossref and
Europe PMC: every one has a confirmed PubMed record and no open-access full
text (no PMCID, openAccess=N). All 14 remain `abstract_only` in
`data/papers_registry.csv` and `access: abstract` in `data/evidence_table.csv`.
Unstated sample size, exact sex, and estrous staging remain strictly
`NOT_READ` (124 `NOT_READ` cells across the 20-row evidence table). No missing
values were inferred or imputed in this run. The paywall constraint is now
formally documented as a PRISMA 2020 (Item 23) limitation in
`docs/audit_report.md` Section 5 and `manuscript/manuscript.md` §4.7 (corrected
"10 of the 20" to "14 of the 20 (70.0%)").

## The open question (needs the author's call)
Four of the 14 carry sex labelled `inferred_from_model` with explicit
provenance (`singh2019_menopause`, `yadav2024_pcos_let`,
`yadav2025_pcos_dhea` — female-only endocrine/surgical models;
`gupta2019_obesity` — male-only model). These labels predate Prompt 23 and
are documented in the README (caveat 3) and the audit report.

Prompt 23 ("Do not infer or impute missing data from disease models") and
AGENTS.md Rule 11 (sex must be verified in the abstract or open text,
otherwise `NOT_READ`) both point the other way: under a strict reading, all
four should become `NOT_READ`, which would move sex-NOT_READ from 10 to 14 of
20 studies and change the audit report matrix, the manuscript's §3.3/§4.7
numbers, and the STATE.md gap counts.

This run preserved the four labels (they are marked honestly — the label
itself says "inferred") and did not silently rewrite the submission-ready
manuscript's numbers. If the author wants the strict reading, the follow-up is:
set `sex_male`/`sex_female`/`sex_source` to `NOT_READ` for those four rows and
recompute the audit report, manuscript, and gap map consistently.

## Related fix (same run)
Manuscript §4.6 still said "5 independent random model seeds (modelSeeds:
[1, 2, 3, 4, 5])" after Prompt 20 had corrected the wording everywhere else;
fixed to "5 diffusion samples from one seed (modelSeeds: [1])".
