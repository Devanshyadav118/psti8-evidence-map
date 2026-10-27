# Evidence Table Schema

Column definitions for `data/evidence_table.csv`.

## Allowed Categorical Values

Use exactly: `yes` / `no` / `not_applicable` / `NOT_READ`.

## Columns

| Column | Type | Description |
|--------|------|-------------|
| `paper_id` | string | Short unique ID, e.g. `valicherla2018` |
| `citation` | string | Author(s), year, journal — abbreviated |
| `doi` | string | Full DOI (e.g. `10.1038/s41598-018-27018-8`) |
| `access` | enum | `full` / `abstract` / `not_read` |
| `species_strain` | string | Species and strain (e.g. `mouse / C57BL/6J`) |
| `sex_male` | enum | Males used? `yes` / `no` / `NOT_READ` |
| `sex_female` | enum | Females used? `yes` / `no` / `NOT_READ` |
| `n_per_group` | string | Sample size per experimental group (e.g. `n=6`) |
| `disease_model` | string | Disease/condition modelled (e.g. `HFD-STZ T2D`) |
| `route` | string | Route of PSTi8 administration (e.g. `i.p.`, `intrarectal`) |
| `dose` | string | PSTi8 dose (e.g. `1 mg/kg`) |
| `duration` | string | Treatment duration (e.g. `28 days`) |
| `estrous_controlled` | enum | Was estrous cycle staged or controlled? |
| `sex_analyzed_as_variable` | enum | Was sex included as a factor in statistical analysis? |
| `stats_method` | string | Primary statistical test(s) used |
| `interaction_tested` | enum | Was a sex × treatment interaction tested? |
| `key_endpoints` | string | Main outcome measures (brief) |
| `key_result` | string | One-sentence summary of main finding |
| `locator` | string | Section/table/figure where key data appear |
| `notes` | string | Free-text notes, caveats, or flags |

## Notes

- One row per study (or per experiment if a paper reports independent cohorts).
- If a paper contains only in-vitro work with no sex variable, still include it
  and mark sex columns `not_applicable`.
- `NOT_READ` means the paper (or that section) has not yet been accessed.
