# Evidence Table Schema

Column definitions for `data/evidence_table.csv`.

## Allowed Categorical Values

Use exactly: `yes` / `no` / `not_applicable` / `not_reported` / `NOT_READ`.
(Annotated values such as `yes (abstract-only)` and `not_reported (abstract-only)` are used when primary full-text is paywalled and details are restricted to published abstracts).

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `paper_id` | string | Short unique ID, e.g. `valicherla2018` |
| `citation` | string | Author(s), year, journal — abbreviated |
| `doi` | string | Full DOI (e.g. `10.1038/s41598-018-27018-8`) |
| `access` | enum | `full` / `abstract` / `not_read` |
| `species_strain` | string | Species and strain (e.g. `mouse / C57BL/6J`) |
| `sex_male` | enum | Males used? `yes` / `no` / `not_reported` / `NOT_READ` |
| `sex_female` | enum | Females used? `yes` / `no` / `not_reported` / `NOT_READ` |
| `sex_source` | enum | Evidentiary source for sex determination: `full_text` / `abstract` / `inferred_from_model` / `not_applicable` / `NOT_READ` |
| `n_per_group` | string | Sample size per experimental group (e.g. `n=6`) |
| `disease_model` | string | Disease/condition modelled (e.g. `HFD-STZ T2D`) |
| `route` | string | Route of PSTi8 administration (e.g. `i.p.`, `intrarectal`) |
| `dose` | string | PSTi8 dose (e.g. `1 mg/kg`) |
| `duration` | string | Treatment duration (e.g. `28 days`) |
| `estrous_monitored_outcome` | enum | Was estrous cyclicity monitored as a phenotype/outcome? `yes` / `no` / `not_applicable` / `not_reported` / `NOT_READ` / `yes (abstract-only)` / `not_reported (abstract-only)` |
| `estrous_baseline_staged` | enum | Was estrous cycle staged/synchronized at baseline prior to treatment? `yes` / `no` / `not_applicable` / `not_reported` / `NOT_READ` / `not_reported (abstract-only)` |
| `sex_analyzed_as_variable` | enum | Was sex included as a factor in statistical analysis? |
| `stats_method` | string | Primary statistical test(s) used |
| `interaction_tested` | enum | Was a sex × treatment interaction tested? `yes` / `no` / `not_reported` / `not_applicable` / `NOT_READ` |
| `key_endpoints` | string | Main outcome measures (brief) |
| `key_result` | string | One-sentence summary of main finding |
| `locator` | string | Section/table/figure where key data appear |
| `notes` | string | Free-text notes, caveats, or flags |

## Notes

- One row per study (or per experiment if a paper reports independent cohorts).
- If a paper contains only in-vitro work with no sex variable, still include it
  and mark sex columns `not_applicable`.
- `NOT_READ` means the paper (or that section) has not yet been accessed due to paywall restrictions.
- `not_reported` means the full text was accessed and read, but the authors did not report the datum.
- `inferred_from_model` indicates sex was not explicitly stated in the abstract/text, but is deduced from single-sex surgical/endocrine disease models (e.g., ovariectomy, letrozole/DHEA PCOS).
