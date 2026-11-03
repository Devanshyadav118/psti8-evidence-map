# STATE.md — Project Status

**Last Updated:** 2026-11-03  
**Vault:** `psti8-sex-bias-review`

---

## 1. Project Phase & Execution Status

### Phase 0: Sex-Bias Evidence Table ✅ COMPLETE
All primary phases (Scaffold, Step 2 extraction, and Tasks A, B, C) are **complete**.

### Phase 1: RESEARCH ✅ COMPLETE

**Goal:** Compile what is known and unknown about PSTi8, the pancreastatin/CHGA pathway, and related T2D biology, to identify a feasible computational or literature contribution.

- [x] **Thread 1 Verification:** 34 verified studies in [data/staging/thread1_registry_unverified.csv](data/staging/thread1_registry_unverified.csv) and [docs/thread1_verification.md](docs/thread1_verification.md).
- [x] **Thread 2 Verification:** 32 verified studies in [docs/thread2_verification.md](docs/thread2_verification.md) and [docs/thread2_audit_addendum.md](docs/thread2_audit_addendum.md).
- [x] **Thread 3 Verification:** 26 candidate studies audited in [docs/thread3_verification.md](docs/thread3_verification.md); 9 new primary studies added to [data/evidence_table.csv](data/evidence_table.csv) (20 total).
- [x] **Thread 6 Verification:** 24 verified studies in [docs/thread6_verification.md](docs/thread6_verification.md).
- [x] **Master Registry Consolidation:** Merged 116 authenticated studies into [data/papers_registry.csv](data/papers_registry.csv).
- [x] **Direction 1 Novelty Check:** Confirmed 0 systematic reviews, 0 meta-analyses, and 0 registered protocols exist in [docs/novelty_check_direction1.md](docs/novelty_check_direction1.md).
- [x] **Structural Assets Manifest:** Catalogued 49 1D, 2D, and 3D assets in [data/structures/structures_manifest.csv](data/structures/structures_manifest.csv).
- [x] **Computational Sequence Profiling & Alignment:** Sliding-window profiles (199 windows), cross-species alignment (100% SBDbeta invariance), variant scoring, and STRING/Reactome interactome in [docs/pathway_and_variant_analysis.md](docs/pathway_and_variant_analysis.md).
- [x] **Master Evidence Gap Map:** Synthesized complete evidence matrix, power modeling, and Route A decision in [docs/gap_map.md](docs/gap_map.md).
- [x] **Crystallographic Construct Audit & Receptor Sanitization:** Documented all construct traps (PDB 5E84 loop deletion, 5E85 cis-tethered peptide, 3LDL Mg occupancy) in [docs/structural_audit_argon.md](docs/structural_audit_argon.md) and [docs/receptor_construct_audit.md](docs/receptor_construct_audit.md); generated clean models in [data/structures/3d_models/cleaned/](data/structures/3d_models/cleaned/).
- [x] **ESM-2 DMS & ESMFold Predictions:** Performed 580-point deep mutational scan and ESMFold peptide predictions via [scripts/run_esm2_analysis.py](scripts/run_esm2_analysis.py).
- [x] **AlphaFold 3 Quaternary Co-Folding Analysis:** Parsed all 5 seeds across 4 complexes in [scripts/analyze_af3_complexes.py](scripts/analyze_af3_complexes.py), generating [data/structures/3d_models/af3_complex_metrics.csv](data/structures/3d_models/af3_complex_metrics.csv) and [data/structures/3d_models/af3_interface_contacts.csv](data/structures/3d_models/af3_interface_contacts.csv); validated steric wedge mechanism and resolved Gly297Ser paradox.
- [x] **All 6 Topic Synthesis Notes Authored:** Complete notes in [notes/topics/](notes/topics/) (`01` through `06`) with zero quotes over 15 words.
- [x] **Comprehensive SYRCLE / ARRIVE Matrix:** Evaluated all 20 primary studies in [data/syrcle_arrive_matrix.csv](data/syrcle_arrive_matrix.csv) via [scripts/generate_syrcle_arrive_matrix.py](scripts/generate_syrcle_arrive_matrix.py).
- [x] **5 Publication-Grade Figures Generated:** Generated high-resolution 300 DPI PNG, SVG, and PDF figures in [figures/](figures/) via [scripts/generate_manuscript_figures.py](scripts/generate_manuscript_figures.py).

### Phase 2: MANUSCRIPT DRAFTING (Route A) 🔄 IN PROGRESS

**Target Journal:** *Biology of Sex Differences* (Springer Nature; Impact Factor ~4.9; turnaround ~6–8 weeks)  
**Working Title:** *Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms*  
**Manuscript Strategy:** Hybrid systematic review, SABV methodological critique, and atomic-resolution neural co-folding mechanism investigation.

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
- [x] **Threads 1, 2, 3, 6 searched and verified** (Thread 1 audited in [docs/thread1_verification.md](docs/thread1_verification.md); Thread 2 audited in [docs/thread2_verification.md](docs/thread2_verification.md); Thread 3 audited in [docs/thread3_verification.md](docs/thread3_verification.md); Thread 6 audited in [docs/thread6_verification.md](docs/thread6_verification.md)).
- [ ] **Open Thread tasks:** Threads 4, 5 not searched.
- [x] **2026-11-02: Direction 1 Novelty Check Complete:**
  - Conducted 19 targeted Exa semantic searches covering systematic reviews, preclinical meta-analyses, protocol registrations (OSF, PROSPERO, PreclinicalTrials.eu), preprint archives (bioRxiv, medRxiv), SABV audits, and known review evaluations; logged all calls in [docs/tool_usage_log.md](docs/tool_usage_log.md) (0 Firecrawl credits consumed).
  - Critically audited five existing reviews citing PSTi8 (`garg2023_review`, `lu2025_fimmu`, `maj2025_fimmu`, `christoffersson2026_fcdhc`, `ioannidis2022_peptides`), confirming all are narrative syntheses lacking PRISMA methodology, SYRCLE risk of bias, ARRIVE 2.0 reporting quality, or SABV audits.
  - Confirmed zero registered review protocols or preclinical animal trial protocols exist on OSF, PROSPERO, or PreclinicalTrials.eu.
  - Formulated formal novelty verdict in [docs/novelty_check_direction1.md](docs/novelty_check_direction1.md): Direction 1 is **partly novel / completely untouched as a formal systematic synthesis**; defined 5 pillars ensuring definitive novelty.
- [x] **2026-11-02: Thread 1 verification complete:**
  - Audited all 34 candidate records from [data/staging/thread1_argon_raw.md](data/staging/thread1_argon_raw.md) against PubMed and Crossref APIs.
  - Reconciled metadata and statuses in [data/staging/thread1_registry_unverified.csv](data/staging/thread1_registry_unverified.csv) (31 verified `yes`, 3 `partial`, 0 `no`, 0 `could_not_open`).
  - Saved raw API payloads in [data/staging/thread1_raw_api_responses.json](data/staging/thread1_raw_api_responses.json).
  - Resolved specific audit items 5a–5h: normal plasma PST range (~5–30 pM conflates assays); weight-loss claim misattribution corrected to O'Connor 2005; Gly297Ser crude co-association vs attenuated adjusted effects for HTN/CAD in `allu2022_diabetes`; confirmed 439-aa and chromosome 14 supported by `ioannidis2022_peptides`; reclassified single-lab network claims (Mahata/O'Connor/Gayen/Mahapatra treated as one network); evaluated mouse vs human conflation and lack of unpartnered external replication for Chga-KO and PSTv1.
  - Documented findings in [docs/thread1_verification.md](docs/thread1_verification.md).
- [x] **2026-11-01: Thread 2 audit addendum fixes & checklist update:**
  - Fixed quote length in [docs/thread2_audit_addendum.md](docs/thread2_audit_addendum.md) (all quotes $\le 15$ words with exact word counts).
  - Added explicit [Inference] labels and testable hypothesis disclaimer to Mechanistic Reconciliation.
  - Corrected sex provenance column for abstract-only rows (MeSH hints vs unread Methods locators removed).
  - Added formal "Statements to downgrade from Established to Contested (single-lab)" section for bullets 2, 3, 7, 8.
  - Cleaned up stray 1-byte file `data/staging/thread2_argon_raw..md` via `git rm`.
  - Replaced stale "Execute searches for Threads 1, 2, 4, 5, 6" checklist item with precise done/open thread tracking.
- [x] **2026-11-02: 1D, 2D, and 3D Structural Asset Collection Complete:**
  - Retrieved canonical FASTA sequences and UniProt metadata for CHGA (`P10645`, `P26339`, `P10354`) and GRP78 (`P11021`, `P20029`, `P06761`).
  - Extracted exact coordinates for human WT PST-29 (preprotein 291–319), human PST-52 (268–319), PSTi8 (291–311), Gly297Ser PST-29 (pos 315 G$\rightarrow$S), and Glu287Lys PST-29 (pos 305 E$\rightarrow$K).
  - Computed 1D physicochemical descriptors with Biopython ProtParam in [data/structures/1d_sequences/peptide_1d_properties.csv](data/structures/1d_sequences/peptide_1d_properties.csv): truncating C-terminal octapeptide `VPQGLFRG` shifts net charge from -5.06 to -6.06, drops GRAVY from -1.531 to -2.133, and concentrates Glu density to 38.1%.
  - Generated RDKit 2D chemical representations (.sdf, .smi, .svg) for free carboxylate (-COOH) and biologically active amidated (-CONH2) states across all peptide variants in [data/structures/2d_chemical/](data/structures/2d_chemical/).
  - Downloaded 4 experimental RCSB PDB crystal structures of GRP78 (`3LDL`, `5EVZ`, `5E84`, `5E85`) and 2 full-length AlphaFold DB predictions with PAE matrices (`AF-P10645-F1`, `AF-P11021-F1`) in [data/structures/3d_models/](data/structures/3d_models/).
  - Authored [docs/structural_data_inventory.md](docs/structural_data_inventory.md) synthesizing biophysical mechanisms, disorder profiles, and ready-to-run AlphaFold 3 Web Server co-folding input JSON blocks for WT PST-29, PSTi8, and Gly297Ser against human GRP78.
  - Generated complete structural catalog in [data/structures/structures_manifest.csv](data/structures/structures_manifest.csv).
- [x] **2026-11-02: Thread 6 verification complete (Methods and Reporting Standards):**
  - Audited all 27 candidate records from [data/staging/thread6_argon_raw.md](data/staging/thread6_argon_raw.md) against PubMed, Crossref, and Europe PMC APIs.
  - Reconciled metadata and statuses in [data/staging/thread6_registry_unverified.csv](data/staging/thread6_registry_unverified.csv) (14 verified `yes`, 10 `partial`, 3 `no`, 0 `could_not_open`).
  - Saved raw API payloads in [data/staging/thread6_raw_api_responses.json](data/staging/thread6_raw_api_responses.json).
  - Uncovered extensive metadata fabrication by Argon: 7 non-existent DOIs (HTTP 404), 9 mismatched DOIs pointing to unrelated adjacent papers, and URL PMIDs pointing to irrelevant clinical articles.
  - Discovered peer-reviewed journal publication for `lieberum2025_medrxiv` in *Journal of Clinical Epidemiology* (May 2025; Vol. 181: 111746; DOI `10.1016/j.jclinepi.2025.111746`, PMID `40021099`).
  - Audited consensus across ARRIVE 2.0 (Delphi consensus across 73 experts in 19 countries), SYRCLE (international consortium adapted from Cochrane), SABV policy audits (6 independent institutions), and PRISMA 2020.
  - Verified that Phillips et al. 2023 (`10.1371/journal.pbio.3002129`) two-way ANOVA factorial power simulation without sample size doubling is accurately categorized as a single-lab simulation study under Contested.
  - Audited all quantitative claims in one-liners: separated abstract-level metrics from full-text-only locators and identified hallucinated metrics.
  - Authored comprehensive audit report in [docs/thread6_verification.md](docs/thread6_verification.md).
- [x] **2026-11-02: Merged verified staging registries into master data/papers_registry.csv:**
  - Backed up initial 26-row Thread 3 registry to [data/staging/papers_registry_pre_merge.csv](data/staging/papers_registry_pre_merge.csv).
  - Quarantined 3 unverified Thread 6 candidate records (`booth2020_systrev`, `vandervaart2020_jaha`, `vandernaald2024_jce`) to [data/staging/rejected_rows.csv](data/staging/rejected_rows.csv) with explicit reasons.
  - Case-insensitively deduplicated DOIs across all threads: 0 cross-thread duplicate DOIs identified.
  - Merged 90 new verified records (34 from Thread 1, 32 from Thread 2, 24 from Thread 6) into master registry, expanding [data/papers_registry.csv](data/papers_registry.csv) from 26 to **116 verified records** (exceeding 40–60 target).
  - Added `published_version_of` column cross-linking preprints to published counterparts (`goand2022_ssrn` $\leftrightarrow$ `goand2023_peptides`, `muntjewerff2025_biorxiv` $\leftrightarrow$ `muntjewerff2025_commbiol`).
  - Standardized controlled role vocabulary (`methods_reference`: 26, `primary_evidence`: 21, `background_mechanism`: 21, `pst_chga_biology`: 20, `review`: 18, `sex_estrogen`: 7, `context_only`: 3).
  - Preserved existing Thread 3 corrections and metadata integrity without overwriting.
  - Authored comprehensive audit report in [docs/registry_merge_report.md](docs/registry_merge_report.md).
- [x] **2026-11-02: Incorporated 9 verified Thread 3 primary studies into data/evidence_table.csv:**
  - Expanded master evidence table [data/evidence_table.csv](data/evidence_table.csv) from 11 to **20 primary preclinical studies** across 22 schema columns.
  - Added 9 verified primary studies: `gupta2019_dex`, `valicherla2020_jpba`, `singh2020_fetuina`, `reza2021_mito`, `goand2023_peptides`, `goand2023_lifesci`, `garg2023_ejp`, `garg2023_aminoacids`, `tshikudi2024_jcag`.
  - Treated preprint `goand2022_ssrn` as the preprint of `goand2023_peptides` without artificial row duplication.
  - Extracted full-text locators for open-access papers (`singh2020_fetuina`: PMC7533370 Section 2.2 male C57BL/6; `tshikudi2024_jcag`: published conference abstract A269 male & female C57BL/6).
  - Maintained strict `NOT_READ` for 7 paywalled studies where animal sex was unstated in the abstract, adhering strictly to the MeSH non-inference rule.
  - Regenerated [docs/audit_report.md](docs/audit_report.md): denominator expanded to 20 studies; both sexes evaluated in 3 studies (15.0%); single-sex in 7 studies (35.0%); unstated/paywalled in 10 studies (50.0%); formal factorial interaction tested in 0 studies (0.0%).
  - Authored Batch 2 spot-check list in [docs/spot_check_list.md](docs/spot_check_list.md) detailing 10 newly added rows and locators for independent audit.
- [x] **2026-11-02: Open-access full-text extraction complete (Prompt 09):**
  - Identified 2 open-access primary studies previously classified as `status: abstract_only`: `singh2020_fetuina` and `tshikudi2024_jcag`.
  - Retrieved open full texts via free academic APIs (NCBI E-utilities / PMC XML / Crossref; 0 Exa / Firecrawl credits consumed).
  - Cached full-text XML payloads in gitignored `data/fulltext_cache/` (`PMC7533370` and `tshikudi2024_jcag.json`).
  - Authored detailed paper notes with paraphrased extractions, locators, and strict 15-word quote limits: [notes/papers/singh2020_fetuina.md](notes/papers/singh2020_fetuina.md) and [notes/papers/tshikudi2024_jcag.md](notes/papers/tshikudi2024_jcag.md).
  - Updated [data/papers_registry.csv](data/papers_registry.csv) setting both records to `status: full_text_read`.
  - Updated [data/evidence_table.csv](data/evidence_table.csv) setting `access: full` for both records with verified locators.
- [x] **2026-11-02: Computational sequence profiling, variant impact scoring, and GRP78 pathway interactome complete (Prompt 16):**
  - Generated sliding-window physicochemical profiles (window=5, step=1) in [data/structures/1d_sequences/sliding_window_profiles.csv](data/structures/1d_sequences/sliding_window_profiles.csv) (199 rows), establishing that the poly-Glu cluster (`EEEEEMAV`) forms an intense electrostatic latch (net charge -4.997 at pH 7.4; hydropathy -3.500) while the C-terminal octapeptide (`VPQGLFRG`) acts as a hydrophobic anchor; truncating the octapeptide in PSTi8 removes the anchor and creates a stable non-aggregating competitive antagonist.
  - Aligned mature GRP78 (636 aa) across human (`P11021`), mouse (`P20029`), and rat (`P06761`) in [data/structures/1d_sequences/cross_species_alignment.csv](data/structures/1d_sequences/cross_species_alignment.csv) (23 comparisons), identifying 99.53% identity across species and exactly **100.00% sequence identity** in the substrate-binding cleft ($\text{SBD}\beta$, residues 427–537; 0 differences), explaining why human-derived PSTi8 is efficacious in rodent models; explicitly noted mouse +1 preprotein signal peptide offset.
  - Profiled human coding variants in [data/structures/1d_sequences/variant_scores.csv](data/structures/1d_sequences/variant_scores.csv): proved that high-potency diabetogenic variant Gly297Ser (`rs9658664`, pos 25) resides in the cleaved 8-mer outside PSTi8, rendering PSTi8 naturally immune to this risk allele; quantified charge inversion (+2.00) for Glu287Lys (`rs140089514`).
  - Extracted 17 high-confidence functional interactome records from STRING and Reactome in [data/structures/pathway_interactions.csv](data/structures/pathway_interactions.csv), delineating physical interactions with UPR sensors (`PERK`/`EIF2AK3`, `ATF6`, `IRE1`/`ERN1`, all scores 0.999), cell-surface kinase scaffolds (`AKT1`, score 0.960), and the `IRE1-TRAF2-JNK1-IRS1` Ser307 insulin resistance cascade.
  - Authored comprehensive synthesis report in [docs/pathway_and_variant_analysis.md](docs/pathway_and_variant_analysis.md) with strict paraphrasing and zero quotes over 15 words.
- [x] **2026-11-02: Master Evidence Gap Map & Phase 2 Manuscript Architecture Complete (Prompt 11):**
  - Synthesized findings across all 20 primary preclinical studies, 116 verified papers, and 32 structural assets in [docs/gap_map.md](docs/gap_map.md).
  - Formulated comprehensive evidence matrix cross-tabulating disease models, animal sex, strain, sample sizes, and reporting standards.
  - Documented major SABV deficits: 100% male bias in T2D/obesity; 0% baseline estrous staging compliance; 0/20 formal factorial interaction tests ($p_{\text{sex} \times \text{treatment}}$); and severe interaction underpowering (<19% power in $n=6$ cohorts).
  - Reconciled biophysical models: electrostatic latch (`EEEEEMAV`, charge -4.997) vs. hydrophobic anchor (`VPQGLFRG`), intrinsically disordered nature of monomeric PST (pLDDT < 50), 100.00% conservation of GRP78 substrate cleft across human/rodents, and structural excision of high-potency variant Gly297Ser in PSTi8.
  - Appraised candidate directions across novelty, impact, feasibility, and 2026 desk-rejection risk; selected **Route A: The Hybrid Systematic Evidence Audit + In Silico Structural Investigation**.
  - Formulated full section-by-section manuscript architecture and targeted peer-reviewed journals (*Biology of Sex Differences*, *Frontiers in Endocrinology*, *Peptides*).
- [x] **2026-11-02: Complete Phase 1 ESM-2 deep learning, PDB receptor sanitization, and 6 topic synthesis notes (Prompt 17):**
  - Executed real ESM-2 protein language modeling (`facebook/esm2_t6_8M_UR50D`) computing sequence embeddings and zero-shot masked marginal log-likelihood ratios (LLR) in both mature PST-29 and full CHGA contexts: confirmed Gly297Ser (`rs9658664`) is evolutionarily neutral/tolerated (LLR = +0.1884 mature, -0.2043 full), whereas Glu287Lys (`rs140089514`) is strongly deleterious to the latch (LLR = -1.3195 mature, -2.0224 full).
  - Executed 580-point in silico deep mutational scan (DMS) across all 29 positions of WT PST-29 saved to [data/structures/1d_sequences/esm2_variant_and_dms_scores.csv](data/structures/1d_sequences/esm2_variant_and_dms_scores.csv); updated [data/structures/1d_sequences/variant_scores.csv](data/structures/1d_sequences/variant_scores.csv).
  - Generated ESMFold 3D peptide predictions via ESM Atlas API for WT PST-29, PSTi8, Gly297Ser, and Glu287Lys in [data/structures/3d_models/esmfold_peptides/](data/structures/3d_models/esmfold_peptides/).
  - Executed crystallographic receptor sanitization protocol via [scripts/clean_receptor_structures.py](scripts/clean_receptor_structures.py) generating docking-ready GRP78 models in [data/structures/3d_models/cleaned/](data/structures/3d_models/cleaned/) (`PDB_3LDL_ChainB_MgATP.pdb`, `PDB_5EVZ_ChainA_MgADP_Pi.pdb`, `PDB_5E85_SBD_apo_cleaned.pdb`, `AF_P11021_mature_GRP78_19_654.pdb`, `AF_P11021_core_26_633.pdb`); documented construct traps in [docs/receptor_construct_audit.md](docs/receptor_construct_audit.md).
  - Authored all 6 comprehensive Phase 1 topic synthesis notes in [notes/topics/](notes/topics/) (`01_chga_processing_and_pst_biology.md`, `02_grp78_compartmentalization_and_signaling.md`, `03_psti8_preclinical_pharmacology.md`, `04_sex_differences_and_estrous_audit.md`, `05_factorial_power_and_reporting_standards.md`, `06_structural_biophysics_and_variants.md`).
  - Appended 10 new computational, structural, and receptor assets to [data/structures/structures_manifest.csv](data/structures/structures_manifest.csv) (total 42 assets).
- [x] Author 6 topic synthesis notes in `notes/topics/` (Complete).
- [x] Identify 2–3 candidate contributions for Phase 2 (Completed in [docs/gap_map.md](docs/gap_map.md); Route A selected).

### Phase 2: CONTRIBUTION 🔄 SCOPED & READY TO EXECUTE

**Selected Strategy:** **Route A — The Hybrid Systematic Evidence Audit + In Silico Structural Investigation**  
- **Working Title:** *Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms*  
- **Target Journal:** *Biology of Sex Differences* (Springer Nature; Impact Factor ~4.9; turnaround ~6–8 weeks); alternatives: *Frontiers in Endocrinology*, *Peptides*.  
- **Manuscript Plan:** 6 implementation steps outlined in [docs/gap_map.md](docs/gap_map.md).

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
