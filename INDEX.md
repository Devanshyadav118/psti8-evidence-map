# INDEX.md — File & Folder Map

> Master directory listing for the PSTi8 sex-bias research vault. Keep this up to date.

## Root

| File | Purpose |
| :--- | :--- |
| [AGENTS.md](AGENTS.md) | Agent instructions: project goal, operational rules, schema constraints |
| [CLAUDE.md](CLAUDE.md) | Standard redirect pointer → AGENTS.md |
| [INDEX.md](INDEX.md) | This file — directory listing with one-line descriptions |
| [LICENSE](LICENSE) | Creative Commons Attribution 4.0 International (CC BY 4.0) License |
| [README.md](README.md) | Project overview, caveats, repository structure, and license notice |
| [STATE.md](STATE.md) | Project status, completed tasks, next actions, and identified evidence gaps |

## sources/

Read-only inputs, literature guides, and external reference lists.

| File | Purpose |
| :--- | :--- |
| [sources/study_guide.md](sources/study_guide.md) | Seed literature catalogue of all 11 published PSTi8 studies |

## notes/papers/

One structured markdown note per published paper, featuring standardized YAML frontmatter.

| File | Purpose |
| :--- | :--- |
| [notes/papers/valicherla2018.md](notes/papers/valicherla2018.md) | Foundational discovery paper: T2D models in male rodents (Sci Rep 2018) |
| [notes/papers/gupta2019_obesity.md](notes/papers/gupta2019_obesity.md) | Hyperinsulinemia-induced obesity & MAPK/NOX3-JNK signaling (Eur J Pharmacol 2019) |
| [notes/papers/singh2019_menopause.md](notes/papers/singh2019_menopause.md) | Peri/post-menopausal insulin resistance in female rats (Peptides 2019) |
| [notes/papers/gupta2020_skeletal.md](notes/papers/gupta2020_skeletal.md) | Skeletal muscle GLUT4 translocation & IR in HFD+STZ mice (Eur J Pharmacol 2020) |
| [notes/papers/singh2020_heliyon.md](notes/papers/singh2020_heliyon.md) | Perimenopausal steatohepatitis, ER stress & SIRT-1/SREBP-1c in female rats (Heliyon 2020) |
| [notes/papers/reza2022_lfs.md](notes/papers/reza2022_lfs.md) | Hepatic FFA oxidative stress, NOX3 & JNK in mice/HepG2 (Life Sci 2022) |
| [notes/papers/valicherla2022_pk.md](notes/papers/valicherla2022_pk.md) | Preclinical PK, bioavailability & male vs female comparison in SD rats (Molecules 2022) |
| [notes/papers/dadge2023_nash.md](notes/papers/dadge2023_nash.md) | NASH / MCD model & macrophage immunomodulation (Cytokine 2023; first author Goand UK) |
| [notes/papers/yadav2024_pcos_let.md](notes/papers/yadav2024_pcos_let.md) | Letrozole + HFD-induced PCOS in female rats (Steroids 2024) |
| [notes/papers/yadav2025_pcos_dhea.md](notes/papers/yadav2025_pcos_dhea.md) | DHEA + HFD-induced PCOS in female rats (JPET 2025) |
| [notes/papers/tshikudi2024_colitis.md](notes/papers/tshikudi2024_colitis.md) | Colitis & sex-divergent colonic epithelial response in male vs female mice (IJMS 2024) |

## data/

Master tabular datasets and analytical outputs.

| File | Purpose |
| :--- | :--- |
| [data/evidence_table.csv](data/evidence_table.csv) | Primary curated evidence table (11 studies × 22 schema columns) |
| [data/power_results.csv](data/power_results.csv) | Statistical power analysis results across 33 sensitivity scenarios (t-distribution) |
| [data/papers_registry.csv](data/papers_registry.csv) | Master registry of all papers encountered across all research threads |
| [data/staging/papers_registry_seed_old.csv](data/staging/papers_registry_seed_old.csv) | Archived initial ungrounded seed of papers_registry.csv |
| [data/staging/thread3_registry_unverified.csv](data/staging/thread3_registry_unverified.csv) | Verified Thread 3 staging registry with verification notes and bibliometric checks |
| [data/staging/all_26_verified_raw.json](data/staging/all_26_verified_raw.json) | Raw PubMed and Crossref API responses for all 26 verified Thread 3 records |
| [data/staging/thread3_argon_raw.md](data/staging/thread3_argon_raw.md) | Raw Gemini 4 Argon literature search output for Thread 3 (primary PSTi8 studies) |
| [data/staging/thread1_argon_raw.md](data/staging/thread1_argon_raw.md) | Raw Gemini 4 Argon literature search output for Thread 1 (pancreastatin/CHGA biology) |
| [data/staging/thread2_argon_raw.md](data/staging/thread2_argon_raw.md) | Raw Gemini 4 Argon literature search output for Thread 2 (signaling pathways) |
| [data/staging/thread2_registry_unverified.csv](data/staging/thread2_registry_unverified.csv) | Verified Thread 2 staging registry with role assignments and bibliometric checks |
| [data/staging/thread2_raw_api_responses.json](data/staging/thread2_raw_api_responses.json) | Raw PubMed and Crossref API responses for all 32 verified Thread 2 records |
| [data/staging/thread1_registry_unverified.csv](data/staging/thread1_registry_unverified.csv) | Verified Thread 1 staging registry with role assignments and bibliometric checks |
| [data/staging/thread1_raw_api_responses.json](data/staging/thread1_raw_api_responses.json) | Raw PubMed and Crossref API responses for all 34 verified Thread 1 records |
| [data/staging/thread6_argon_raw.md](data/staging/thread6_argon_raw.md) | Raw Gemini 4 Argon literature search output for Thread 6 (methods and reporting standards) |
| [data/staging/thread6_registry_unverified.csv](data/staging/thread6_registry_unverified.csv) | Verified Thread 6 staging registry with role assignments and bibliometric checks |
| [data/staging/thread6_raw_api_responses.json](data/staging/thread6_raw_api_responses.json) | Raw PubMed and Crossref API responses for all 27 verified Thread 6 records |
| [data/structures/structures_manifest.csv](data/structures/structures_manifest.csv) | Manifest cataloguing 28 1D, 2D, and 3D structural assets for PST/PSTi8 and GRP78 |
| [data/structures/1d_sequences/](data/structures/1d_sequences/) | Canonical FASTA, JSON metadata, and ProtParam physicochemical properties |
| [data/structures/2d_chemical/](data/structures/2d_chemical/) | RDKit-modeled .sdf, .smi, and .svg chemical representations of free and amidated peptides |
| [data/structures/3d_models/](data/structures/3d_models/) | RCSB PDB crystal structures (3LDL, 5EVZ, 5E84, 5E85) and AlphaFold DB models with PAE |

## docs/

Audit reports, schemas, power analyses, spot-check protocols, and decision records.

| File | Purpose |
| :--- | :--- |
| [docs/schema.md](docs/schema.md) | 22-column data dictionary and allowable value definitions for evidence table |
| [docs/audit_report.md](docs/audit_report.md) | Task A audit report: sex-coverage matrix, estrous staging, scope boundaries |
| [docs/power_analysis.md](docs/power_analysis.md) | Task B report: DAI extraction, interaction power modeling, sample size trade-offs |
| [docs/spot_check_list.md](docs/spot_check_list.md) | Task C protocol: 10 randomized table rows with locators for independent audit |
| [docs/research_plan.md](docs/research_plan.md) | Phase 1 research plan: 6 topic threads with queries, criteria, and targets |
| [docs/search_log.md](docs/search_log.md) | Reproducible log of every literature search performed during Phase 1 |
| [docs/search_strategy.md](docs/search_strategy.md) | Comprehensive search strategy, databases, queries, and PRISMA inclusion criteria |
| [docs/tool_usage_log.md](docs/tool_usage_log.md) | External tool usage log tracking Exa queries and Firecrawl credit consumption |
| [docs/thread1_verification.md](docs/thread1_verification.md) | Thread 1 audit report: verification of 34 pancreastatin/CHGA studies against PubMed/Crossref |
| [docs/thread2_verification.md](docs/thread2_verification.md) | Thread 2 audit report: verification of 32 signaling studies against PubMed/Crossref |
| [docs/thread2_audit_addendum.md](docs/thread2_audit_addendum.md) | Thread 2 audit addendum: laboratory independence, GRP78 paradox, sex reporting, and one-liner audit |
| [docs/thread3_verification.md](docs/thread3_verification.md) | Thread 3 audit report: verification of 26 candidate studies against PubMed/Crossref |
| [docs/thread6_verification.md](docs/thread6_verification.md) | Thread 6 audit report: verification of 27 methods and reporting studies against PubMed/Crossref |
| [docs/staging_new_studies.md](docs/staging_new_studies.md) | Catalogue of verified new primary PSTi8 studies with strict sex reporting extraction |
| [docs/novelty_check_direction1.md](docs/novelty_check_direction1.md) | Direction 1 novelty assessment: Exa search log, existing review critique, and verdict |
| [docs/structural_data_inventory.md](docs/structural_data_inventory.md) | Inventory of 1D/2D/3D structural assets, physicochemical comparisons, and AlphaFold 3 co-folding job inputs |
| [docs/decisions/2026-10-27_paper-id-convention.md](docs/decisions/2026-10-27_paper-id-convention.md) | Decision record: paper_id naming convention across repository |
| [docs/decisions/2026-10-31_fix-registry-seed-dois-and-statuses.md](docs/decisions/2026-10-31_fix-registry-seed-dois-and-statuses.md) | Decision record: fix registry seed DOIs, unsupported reading statuses, and archive old seed |
| [docs/decisions/2026-10-31_license-cc-by-4.0.md](docs/decisions/2026-10-31_license-cc-by-4.0.md) | Decision record: CC BY 4.0 open repository license and attribution terms |

## scripts/

Executable Python analysis tools and automation scripts.

| File | Purpose |
| :--- | :--- |
| [scripts/power_analysis.py](scripts/power_analysis.py) | Standalone Python script computing 2×2 factorial interaction power and sensitivity |
| [scripts/sync.sh](scripts/sync.sh) | Automated sync script to stage, commit, pull, and push updates to GitHub |
| [scripts/fetch_all_raw.py](scripts/fetch_all_raw.py) | Batch retrieval script fetching raw bibliometrics from PubMed and Crossref |
| [scripts/verify_thread3.py](scripts/verify_thread3.py) | Verification harness auditing candidate literature against PubMed and Crossref |
| [scripts/verify_thread2.py](scripts/verify_thread2.py) | Verification harness auditing Thread 2 candidate literature against PubMed and Crossref |
| [scripts/verify_thread1.py](scripts/verify_thread1.py) | Verification harness auditing Thread 1 candidate literature against PubMed and Crossref |
| [scripts/rebuild_papers_registry.py](scripts/rebuild_papers_registry.py) | Rebuild script syncing verified records into master papers registry |
| [scripts/save_verified_csv.py](scripts/save_verified_csv.py) | Serializer formatting verified staging records to CSV |
| [scripts/run_batch.py](scripts/run_batch.py) | CLI runner processing verification batches |
| [scripts/update_evidence_table.py](scripts/update_evidence_table.py) | Utility updating citations and authenticated DOIs in evidence table |
| [scripts/collect_structures.py](scripts/collect_structures.py) | Automated pipeline retrieving and generating 1D, 2D, and 3D structural assets via UniProt, RCSB PDB, AlphaFold DB, and RDKit |
| [scripts/verify_thread6.py](scripts/verify_thread6.py) | Verification harness auditing Thread 6 candidate literature against PubMed and Crossref |

## notes/topics/

Topic synthesis notes produced during Phase 1 research.

| File | Purpose |
| :--- | :--- |
| *(empty — awaiting plan approval and search execution)* | |

## prompts/

Permanent prompt library storing every prompt given to an agent before execution.

| File | Purpose |
| :--- | :--- |
| [prompts/INDEX.md](prompts/INDEX.md) | Prompts master index: id, slug, purpose, model, status, and commit tracking |
| [prompts/01_tool_policy_setup.md](prompts/01_tool_policy_setup.md) | Prompt 01: Tool usage policy setup for Exa and Firecrawl |
| [prompts/02_verify_thread1.md](prompts/02_verify_thread1.md) | Prompt 02: Verification of Thread 1 (pancreastatin/CHGA biology) literature |
| [prompts/03_verify_thread_pattern.md](prompts/03_verify_thread_pattern.md) | Prompt 03: Verification prompt pattern for candidate threads |
| [prompts/04_argon_search_template.md](prompts/04_argon_search_template.md) | Prompt 04: Argon literature search template (Google AI Studio) |
| [prompts/05_thread2_audit_addendum.md](prompts/05_thread2_audit_addendum.md) | Prompt 05: Thread 2 audit addendum (lab independence, GRP78 conflict, sex reporting) |
| [prompts/06_thread2_addendum_fixes.md](prompts/06_thread2_addendum_fixes.md) | Prompt 06: Fix quote lengths, inference labels, and sex provenance in Thread 2 addendum |
| [prompts/07_merge_registries.md](prompts/07_merge_registries.md) | Prompt 07: Merge verified registries into master papers registry |
| [prompts/08_add_thread3_to_evidence_table.md](prompts/08_add_thread3_to_evidence_table.md) | Prompt 08: Add new Thread 3 primary studies to master evidence table |
| [prompts/09_fulltext_extraction.md](prompts/09_fulltext_extraction.md) | Prompt 09: Open-access full-text extraction |
| [prompts/10_novelty_check_direction1.md](prompts/10_novelty_check_direction1.md) | Prompt 10: Novelty check for PSTi8 preclinical systematic reviews |
| [prompts/11_gap_map.md](prompts/11_gap_map.md) | Prompt 11: Gap map synthesis and contribution direction selection |
| [prompts/12_new_chat_starter.md](prompts/12_new_chat_starter.md) | Prompt 12: Starter prompt for new Gemini Project chat sessions |
| [prompts/13_antigravity_save_prompts.md](prompts/13_antigravity_save_prompts.md) | Prompt 13: Save prompt library into repo and enforce prompt-saving rules |
| [prompts/14_collect_structural_assets.md](prompts/14_collect_structural_assets.md) | Prompt 14: Collect and verify 1D, 2D, and 3D molecular and structural assets for PST/PSTi8 and GRP78 |
| [prompts/15_verify_thread6.md](prompts/15_verify_thread6.md) | Prompt 15: Verification of Thread 6 (Methods and Reporting Standards) literature |
