# STATE.md — Project Status

**Last Updated:** 2026-11-01  
**Vault:** `psti8-sex-bias-review`

---

## 1. Project Phase & Execution Status

### Phase 0: Sex-Bias Evidence Table ✅ COMPLETE

All primary phases (Scaffold, Step 2 extraction, and Tasks A, B, C) are **complete**.

- [x] **Step 1 — Vault Scaffold:** Directory hierarchy, `AGENTS.md`, `CLAUDE.md`, `docs/schema.md`, `sources/study_guide.md`, `docs/decisions/`.
- [x] **Step 2 — Data Extraction & Note Authoring:**
  - [x] Populated [data/evidence_table.csv](data/evidence_table.csv) with all 11 published PSTi8 studies across 22 standardized schema columns (including `sex_source`, split estrous columns, and `not_reported`).
  - [x] Created all 11 individual markdown files in [notes/papers/](notes/papers/) with YAML frontmatter, locators, and access tags.
- [x] **Task A — Sex-Coverage Audit:**
  - [x] Authored [docs/audit_report.md](docs/audit_report.md) with disease-by-sex matrix, two-sex study breakdown, list of unreported/`NOT_READ` studies, and explicit boundary statements. Colitis findings accurately reflect daily vs cumulative/macroscopic endpoints and descriptive characterization.
  - [x] Classified evidence gaps into (a) confirmed absent, (b) unreported, and (c) cannot assess because NOT_READ, with exact counts.
- [x] **Task B — Statistical Power Analysis:**
  - [x] Documented extraction and derivation of $L$ and $\sigma$ from Figure 1 of Tshikudi et al. (2024).
  - [x] Implemented exact Student's t-distribution critical values and non-central t CDF in [scripts/power_analysis.py](scripts/power_analysis.py).
  - [x] Addressed error bar ambiguity: modeled both direct SD ($\sigma \in [0.8, 1.0]$) and converted SEM-to-SD ($\sigma \in [1.4, 1.8]$).
  - [x] Headlined realistic interaction contrast range ($L \in [1.0, 2.5]$) and dedicated cumulative-DAI endpoint section ($\sigma_{\text{cum}} \in [2.5, 4.0]$, $L_{\text{cum}} \in [1.0, 3.5]$).
  - [x] Exported 33 sensitivity scenarios to [data/power_results.csv](data/power_results.csv) and authored synthesis in [docs/power_analysis.md](docs/power_analysis.md).
- [x] **Task C — Verification Protocol & Handoff:**
  - [x] Generated [docs/spot_check_list.md](docs/spot_check_list.md) with 10 randomly sampled table rows for audit.
  - [x] Updated [INDEX.md](INDEX.md) and [STATE.md](STATE.md).
  - [x] Added "Papers to Obtain" list resolving paywalled `NOT_READ` fields.

### Phase 1: RESEARCH 🔄 IN PROGRESS

**Goal:** Compile what is known and unknown about PSTi8, the pancreastatin/CHGA pathway, and related T2D biology, to identify a feasible computational or literature contribution.

- [x] Created [docs/research_plan.md](docs/research_plan.md) with 6 topic threads, search queries, inclusion criteria, and paper targets.
- [x] Created [docs/search_strategy.md](docs/search_strategy.md) documenting systematic literature search strategy, databases, queries, and PRISMA criteria.
- [x] Created [data/papers_registry.csv](data/papers_registry.csv) with header + 11 existing PSTi8 studies pre-loaded.
- [x] Created [docs/search_log.md](docs/search_log.md).
- [x] Created `notes/topics/` directory for topic synthesis notes.
- [x] Updated AGENTS.md with phase structure and new folder map entries.
- [x] **Thread 3 Verification Audit Complete:**
  - Audited all 26 candidate studies from Gemini 4 Argon search ([data/staging/thread3_argon_raw.md](data/staging/thread3_argon_raw.md)) against PubMed and Crossref APIs.
  - Processed in 3 sequential batches into [data/staging/thread3_registry_unverified.csv](data/staging/thread3_registry_unverified.csv) (25 verified `yes`, 1 `partial`, 0 `no`, 0 `could_not_open`).
  - Authored comprehensive verification report in [docs/thread3_verification.md](docs/thread3_verification.md).
  - Catalogued 9 verified NEW primary studies (+ 1 preprint) in [docs/staging_new_studies.md](docs/staging_new_studies.md).
  - Resolved 5 suspected repo errors (Garg vs Reza in 10.1016/j.lfs.2021.120221, Goand vs Dadge in 10.1016/j.cyto.2023.156354, Hossain first author & correct DOI 10.1038/s41598-018-27018-8, Singla 2026 PCOS review unverified for PSTi8, and confirmed Garg 2023 STZ paper in Eur J Pharmacol).
  - Uncovered 4 major pre-existing DOI errors in repo catalog (`valicherla2018`, `singh2020_heliyon`, `valicherla2022_pk`, `tshikudi2024_colitis`).
  - Archived old ungrounded registry to [data/staging/papers_registry_seed_old.csv](data/staging/papers_registry_seed_old.csv) and rebuilt [data/papers_registry.csv](data/papers_registry.csv) with 26 rows, `role` column, and honest `status` tags (`full_text_read` only for 4 verified open-access studies).
  - Corrected citations for `valicherla2018`, `reza2022_lfs`, and `dadge2023_nash` in [data/evidence_table.csv](data/evidence_table.csv); documented in [docs/decisions/2026-10-27_paper-id-convention.md](docs/decisions/2026-10-27_paper-id-convention.md) and [docs/decisions/2026-10-31_fix-registry-seed-dois-and-statuses.md](docs/decisions/2026-10-31_fix-registry-seed-dois-and-statuses.md).
- [x] **Repository Licensing & Governance (CC BY 4.0):**
  - Applied **Creative Commons Attribution 4.0 International (CC BY 4.0)** across the entire repository (including all datasets, markdown notes, and `scripts/`).
  - Added [LICENSE](LICENSE) containing the full legal text with copyright holder Devansh Pratap Singh.
  - Updated [README.md](README.md) with attribution guidelines and publisher copyright boundary notices.
  - Documented in [docs/decisions/2026-10-31_license-cc-by-4.0.md](docs/decisions/2026-10-31_license-cc-by-4.0.md).
- [x] **Repository Consistency & Indexing:**
  - Audited and updated [INDEX.md](INDEX.md) to catalogue `LICENSE`, all analytical scripts in `scripts/`, staging datasets, and new decision records with zero broken links.
- [x] **MCP Tool Integration & Usage Policy:**
  - Formulated and documented Tool Usage Policy in [AGENTS.md](AGENTS.md): Exa for semantic search/discovery; Firecrawl for single-page open-access scrapes with strict 1,000 credit cap (never crawl/map, max 25 pages/task); PubMed/Crossref as gate for citation verification; strict exclusion of credentials and full text.
  - Added `data/fulltext_cache/`, `*.env`, and local MCP config files to [.gitignore](.gitignore).
  - Created [docs/tool_usage_log.md](docs/tool_usage_log.md) tracking queries, URLs, purposes, and credit usage.
  - Tested both MCP tools: verified Exa semantic search on `"PSTi8 pancreastatin inhibitor"` and Firecrawl single-page scrape on open-access article `PMC5992141` (2 credits consumed, 998 remaining).
- [x] **Thread 2 Verification Audit Complete:**
  - Audited all 32 candidate studies from Gemini 4 Argon search ([data/staging/thread2_argon_raw.md](data/staging/thread2_argon_raw.md)) against PubMed and Crossref APIs in 3 batches.
  - Reconciled row count: resolved discrepancy between 32 CSV rows and the "28" stated in Argon's LIMITS section (32 verified `yes`, 0 `no`, 0 `could_not_open`).
  - Populated [data/staging/thread2_registry_unverified.csv](data/staging/thread2_registry_unverified.csv) with added `role` column (`background_mechanism`: 17, `sex_estrogen`: 6, `methods_reference`: 2, `review`: 7) and honest status tags (8 `full_text_read`, 24 `abstract_only`).
  - Saved raw API payloads for all 32 studies in [data/staging/thread2_raw_api_responses.json](data/staging/thread2_raw_api_responses.json).
  - Verified bioRxiv DOIs with prefix `10.64898` (`franczak2026_biorxiv`, `monteillet2026_biorxiv`) and all 2026 publications on Crossref/PubMed.
  - Reconciled `taniguchi2006_cmet` and `kubota2008_cmet` from unread to verified `abstract_only`.
  - Flagged cell-type constraint in `zhang2013_plosone` (used breast/prostate cancer cells, not hepatocytes).
  - Verified quantitative figures against abstracts and open full-text captions (`alves2025_pathophys`, `depaoli2025_jes`, `matsumoto2003_jci`).
  - Authored comprehensive verification report in [docs/thread2_verification.md](docs/thread2_verification.md).
- [x] **Thread 2 Audit Addendum Complete:**
  - Evaluated laboratory independence across all 9 Established knowledge summary bullets: identified single-lab dependencies for hepatocyte NOX3 (`li2010_febslett`/`gao2010_jbc`, Jian Li lab), in vivo hepatocyte $G_q$ chemogenetics (`li2013_endocrinology`, Jürgen Wess lab), circulating GRP78 infusion in NASH (`angelini2022_natcommun`, Geltrude Mingrone lab), and allosteric YUM70 GRP78 ATPase inhibition (`samanta2021_canres`, Pinku Mukherjee lab).
  - Formalized dedicated structured entry on the GRP78 mechanistic paradox reconciling intracellular chaperone folding (`kammoun2009_jci`), heterozygous adaptive UPR hormesis (`ye2010_diabetes`), and circulating pathogenic GRP78 signaling (`angelini2022_natcommun`).
  - Audited biological sex reporting across abstracts: identified exactly 25 rows where sex was unstated (`sex=NOT_READ`) vs 7 rows where sex was explicitly reported.
  - Audited one-liner claims exceeding abstract statements: catalogued 8 rows with specific locators (figure captions and full-text methods).
  - Documented findings in [docs/thread2_audit_addendum.md](docs/thread2_audit_addendum.md).
- [x] **2026-11-01: Prompt library added:**
  - Standardized prompt library established in [prompts/](prompts/) with 13 prompt files indexed in [prompts/INDEX.md](prompts/INDEX.md).
  - Validated YAML frontmatter across all files (`prompt_id`, `slug`, `status`, `tool`, `model`).
  - Added "Prompt Saving Rule" and extended "Tool Usage Policy" (free routes first, credit pre-approval, 15-word quote limit, Argon verification gate, single-lab network rule, MeSH sex provenance) to [AGENTS.md](AGENTS.md).
- [ ] Incorporate verified new studies and corrected DOIs into master tables in next phase.
- [x] **Threads 1, 2, 3 searched; Threads 2 and 3 verified** (Thread 2 audited in [docs/thread2_verification.md](docs/thread2_verification.md); Thread 3 audited in [docs/thread3_verification.md](docs/thread3_verification.md)).
- [ ] **Open Thread tasks:** Thread 1 not yet verified (unverified staging in [data/staging/thread1_argon_raw.md](data/staging/thread1_argon_raw.md)); Threads 4, 5, 6 not searched.
- [x] **2026-11-01: Thread 2 audit addendum fixes & checklist update:**
  - Fixed quote length in [docs/thread2_audit_addendum.md](docs/thread2_audit_addendum.md) (all quotes $\le 15$ words with exact word counts).
  - Added explicit [Inference] labels and testable hypothesis disclaimer to Mechanistic Reconciliation.
  - Corrected sex provenance column for abstract-only rows (MeSH hints vs unread Methods locators removed).
  - Added formal "Statements to downgrade from Established to Contested (single-lab)" section for bullets 2, 3, 7, 8.
  - Cleaned up stray 1-byte file `data/staging/thread2_argon_raw..md` via `git rm`.
  - Replaced stale "Execute searches for Threads 1, 2, 4, 5, 6" checklist item with precise done/open thread tracking.
- [ ] Populate `data/papers_registry.csv` (target: 40–60 entries).
- [ ] Author 6 topic synthesis notes in `notes/topics/`.
- [ ] Identify 2–3 candidate contributions for Phase 2.

### Phase 2: CONTRIBUTION (planned)

Not yet scoped. Will be defined after Phase 1 findings.

---

## 2. Five Biggest Evidence Gaps in Published PSTi8 Literature

Every evidence-gap statement is categorized by evidentiary status:
*(a) confirmed absent in papers read; (b) unreported in papers read; (c) cannot assess because NOT_READ.*

1. **Female Representation in General Cardiometabolic & Diabetic Studies (Total: 5 studies):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2018`, methods explicitly state only male C57BL/6J, male db/db, and male SD rats were used across all three diabetic models and PK cohorts.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (4 studies):* `gupta2019_obesity`, `gupta2020_skeletal`, `reza2022_lfs`, and `dadge2023_nash` are paywalled; their abstracts do not report whether female animals were included.
2. **Formal Testing of Sex × Treatment Interaction ($p_{\text{sex} \times \text{treatment}}$) (Total: 2 studies with both sexes):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2022_pk`, sex differences were evaluated using descriptive summaries and pairwise t-tests; no factorial interaction test was conducted.
   - *(b) Unreported in papers read (1 study):* In `tshikudi2024_colitis`, two-way ANOVA is specified in Section 4.9, but the omnibus interaction test statistic ($F$, df, $p_{\text{sex} \times \text{treatment}}$) is unreported; only within-sex pairwise post-hocs are presented.
   - *(c) Cannot assess because NOT_READ (0 studies):* Both studies evaluating both sexes were read in full.
3. **Baseline Estrous Cycle Staging and Phase Control (Total: 6 studies using female animals):**
   - *(a) Confirmed absent in papers read (2 studies):* In `valicherla2022_pk` and `tshikudi2024_colitis`, female animals were utilized, but neither methods section describes estrous cycle staging, phase monitoring, or baseline synchronization.
   - *(b) Unreported in papers read (0 studies):* In `singh2020_heliyon`, estrous monitoring is confirmed present via daily vaginal cytology, but was monitored longitudinally as an outcome (confirming perimenopause induction and cycle recovery) rather than used to stage animals prior to treatment.
   - *(c) Cannot assess because NOT_READ (3 studies):* `singh2019_menopause`, `yadav2024_pcos_let`, and `yadav2025_pcos_dhea` are paywalled; baseline staging cannot be determined from abstracts.
4. **Replication of Sex Divergence in Secondary Organ Systems (Total: 1 study):**
   - *(a) Confirmed absent in papers read (1 study):* Independent replication of the sex-divergent colonic epithelial response to PSTi8 is absent across all read papers.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (0 studies):* `tshikudi2024_colitis` was read in full.
   - *Colitis phenotype description:* In `tshikudi2024_colitis`, PSTi8 significantly elevated daily Disease Activity Index (DAI) scores in colitic females compared to vehicle controls at 72 h and 96 h ($p < 0.05$). However, when evaluating the cumulative Disease Activity Index (sum of DAI) and macroscopic damage scores (macro-scores), the paper reports a **non-significant difference** between PSTi8-treated female mice and PBS-treated female controls, as well as between PSTi8-treated male and female mice. In colitic males, PSTi8 delayed the onset of DAI elevation (from 24 h to 48 h) and preserved stem cells and differentiated colonic epithelial cells.
5. **Sex-Comparative Pharmacokinetics in Diseased or Chronically Treated Animals (Total: 1 study):**
   - *(a) Confirmed absent in papers read (1 study):* In `valicherla2022_pk`, PK parameters were compared across sexes only after single doses in healthy young Sprague Dawley rats; PK profiling under chronic dosing or diseased states is confirmed absent.
   - *(b) Unreported in papers read (0 studies).*
   - *(c) Cannot assess because NOT_READ (0 studies):* Full text was read.

---

## 3. Three Weakest Points of this Analysis

1. **Information Incompleteness Driven by Paywalled Literature (`NOT_READ` Prevalence):**  
   54.5% (6 of 11) of the studies are behind Elsevier/ASPET paywalls. Following AGENTS.md Rule 1 ("never guess or fill from memory"), unverified details (e.g., exact $n$, dose, explicit animal sex) are coded strictly as `NOT_READ`.
2. **Reliance on Visual Estimation for Quantitative Parameters in Task B:**  
   In `tshikudi2024_colitis`, DAI values and variability measures are published solely as graphical bar and line charts in Figure 1, with no numerical tables or reported effect sizes ($d$, $\eta^2$). The baseline interaction contrasts ($L$) are approximations derived from graphs.
3. **Unavailability of Raw Omnibus Interaction Statistics:**  
   Primary literature did not report the $F_{\text{sex} \times \text{treatment}}$ statistic or MSE, requiring the power model to reconstruct contrasts from sample means rather than from empirical model error terms.

---

## 4. Papers to Obtain (Resolving `NOT_READ` Fields)

Obtaining full text for the following paywalled manuscripts will resolve the indicated missing data fields in [data/evidence_table.csv](data/evidence_table.csv):

| # | Paper ID | Citation & DOI | What Obtaining Full Text Resolves |
|---|---|---|---|
| 1 | `gupta2019_obesity` | Gupta et al., *Eur J Pharmacol* 2019<br>DOI: [10.1016/j.ejphar.2019.172723](https://doi.org/10.1016/j.ejphar.2019.172723) | • Confirm whether animals were exclusively male (only reported in secondary summaries)<br>• Extract exact sample size per group ($n$)<br>• Extract PSTi8 dose, administration route, and vehicle |
| 2 | `singh2019_menopause` | Valicherla/Singh et al., *Peptides* 2019<br>DOI: [10.1016/j.peptides.2019.170147](https://doi.org/10.1016/j.peptides.2019.170147) | • Clarify first-author citation attribution (Valicherla GR vs Singh)<br>• Determine whether estrous cycles were staged at baseline before OVX/VCD<br>• Extract sample size per group ($n$), PSTi8 dose, route, and chronic duration |
| 3 | `gupta2020_skeletal` | Gupta et al., *Eur J Pharmacol* 2020<br>DOI: [10.1016/j.ejphar.2020.173204](https://doi.org/10.1016/j.ejphar.2020.173204) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Extract group sample sizes ($n$), PSTi8 dose, and route in HFD+STZ mice<br>• Check whether female mice were included or discussed |
| 4 | `reza2022_lfs` | Reza et al., *Life Sci* 2022<br>DOI: [10.1016/j.lfs.2021.120221](https://doi.org/10.1016/j.lfs.2021.120221) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Extract in vivo group sizes ($n$), route of administration, and treatment schedule<br>• Check whether sex differences were evaluated in hepatic FFA stress |
| 5 | `dadge2023_nash` | Goand et al. (Dadge et al.), *Cytokine* 2023<br>DOI: [10.1016/j.cyto.2023.156354](https://doi.org/10.1016/j.cyto.2023.156354) | • Resolve currently unknown animal sex (`sex_male`, `sex_female`)<br>• Confirm first-author attribution (Goand UK vs Dadge)<br>• Extract sample sizes per group ($n$), route, dose, and duration in MCD diet-induced NASH |
| 6 | `yadav2024_pcos_let` | Yadav et al., *Steroids* 2024<br>DOI: [10.1016/j.steroids.2024.109558](https://doi.org/10.1016/j.steroids.2024.109558) | • Confirm exact rat strain<br>• Extract sample size per group ($n$), PSTi8 dose, and route of administration<br>• Determine whether estrous cycles were staged at baseline prior to letrozole induction |
| * | `yadav2025_pcos_dhea` | Yadav et al., *JPET* 2025<br>DOI: [10.1016/j.jpet.2025.103765](https://doi.org/10.1016/j.jpet.2025.103765) | • Confirm exact rat strain<br>• Extract sample size per group ($n$) and route of administration<br>• Verify baseline estrous staging protocols |
