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
| [docs/thread3_verification.md](docs/thread3_verification.md) | Thread 3 audit report: verification of 26 candidate studies against PubMed/Crossref |
| [docs/staging_new_studies.md](docs/staging_new_studies.md) | Catalogue of verified new primary PSTi8 studies with strict sex reporting extraction |
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
| [scripts/rebuild_papers_registry.py](scripts/rebuild_papers_registry.py) | Rebuild script syncing verified records into master papers registry |
| [scripts/save_verified_csv.py](scripts/save_verified_csv.py) | Serializer formatting verified staging records to CSV |
| [scripts/run_batch.py](scripts/run_batch.py) | CLI runner processing verification batches |
| [scripts/update_evidence_table.py](scripts/update_evidence_table.py) | Utility updating citations and authenticated DOIs in evidence table |

## notes/topics/

Topic synthesis notes produced during Phase 1 research.

| File | Purpose |
| :--- | :--- |
| *(empty — awaiting plan approval and search execution)* | |
