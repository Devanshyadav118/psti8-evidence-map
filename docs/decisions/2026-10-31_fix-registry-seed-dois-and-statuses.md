# Decision: Fix Registry Seed DOIs and Reading Statuses

**Date:** 2026-10-31  
**Status:** Decided & Implemented

## Context

The initial scaffold seed of `data/papers_registry.csv` contained two significant integrity issues:
1. **Four Erroneous DOIs:** Several DOIs in the original seed were corrupted or pointed to unrelated literature:
   - `valicherla2018`: Listed as `10.1038/s41598-018-22528-z` (404 Not Found on Crossref / absent in PubMed; authentic DOI is `10.1038/s41598-018-27018-8`).
   - `singh2020_heliyon`: Listed as `10.1016/j.heliyon.2020.e05500` (resolved to a paper on Ethiopian agroforestry woody species; authentic DOI is `10.1016/j.heliyon.2020.e05826`).
   - `valicherla2022_pk`: Listed as `10.3390/molecules27134153` (resolved to swine milk/plasma amino acid chromatography; authentic DOI is `10.3390/molecules27020339`).
   - `tshikudi2024_colitis`: Listed as `10.3390/ijms25189949` (resolved to lipopeptide Iturin W against *S. aureus*; authentic DOI is `10.3390/ijms252312757`).
2. **Unsupported Reading Statuses:** The seed file blanket-marked all 11 original studies as `status: read`. However, 7 of those papers (`gupta2019_obesity`, `singh2019_menopause`, `gupta2020_skeletal`, `reza2022_lfs`, `dadge2023_nash`, `yadav2024_pcos_let`, `yadav2025_pcos_dhea`) are behind commercial publisher paywalls (Elsevier, ASPET) where only abstracts were examined.

## Decision

1. **Backup Old Seed:** The original seed file was archived to `data/staging/papers_registry_seed_old.csv`.
2. **Rebuild with Authenticated Bibliometrics:** `data/papers_registry.csv` was rebuilt from `data/staging/thread3_registry_unverified.csv` with all 26 verified records from Thread 3.
3. **Strict Status Definitions:**
   - `full_text_read`: Assigned **only** to papers that are open access and were read in full text with notes in this project (`valicherla2018`, `singh2020_heliyon`, `valicherla2022_pk`, `tshikudi2024_colitis`).
   - `abstract_only`: Assigned to all other 22 entries (both paywalled primary studies and reviews where only abstract or open metadata was verified).
4. **Addition of Role Column:** Added `role` to distinguish `primary_evidence` (21 studies/preprints), `review` (4 reviews), and `context_only` (`singla2026_jri`).
5. **Fixed Date:** 2026-10-31.
