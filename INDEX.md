# INDEX.md — File & Folder Map

> Master directory listing for the PSTi8 sex-bias research vault. Keep this up to date.

## Root

| File | Purpose |
| :--- | :--- |
| [AGENTS.md](AGENTS.md) | Agent instructions: project goal, operational rules, schema constraints |
| [CLAUDE.md](CLAUDE.md) | Standard redirect pointer → AGENTS.md |
| [INDEX.md](INDEX.md) | This file — directory listing with one-line descriptions |
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
| [data/evidence_table.csv](data/evidence_table.csv) | Primary curated evidence table (11 studies × 20 schema columns) |
| [data/power_results.csv](data/power_results.csv) | Statistical power analysis results across 9 sensitivity scenarios |

## docs/

Audit reports, schemas, power analyses, spot-check protocols, and decision records.

| File | Purpose |
| :--- | :--- |
| [docs/schema.md](docs/schema.md) | 20-column data dictionary and allowable value definitions for evidence table |
| [docs/audit_report.md](docs/audit_report.md) | Task A audit report: sex-coverage matrix, estrous staging, scope boundaries |
| [docs/power_analysis.md](docs/power_analysis.md) | Task B report: DAI extraction, interaction power modeling, sample size trade-offs |
| [docs/spot_check_list.md](docs/spot_check_list.md) | Task C protocol: 10 randomized table rows with locators for independent audit |
| [docs/decisions/2026-10-27_paper-id-convention.md](docs/decisions/2026-10-27_paper-id-convention.md) | Decision record: paper_id naming convention across repository |

## scripts/

Executable Python analysis tools.

| File | Purpose |
| :--- | :--- |
| [scripts/power_analysis.py](scripts/power_analysis.py) | Standalone Python script computing 2×2 factorial interaction power and sensitivity |
