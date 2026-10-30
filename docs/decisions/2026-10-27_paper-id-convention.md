# Decision: Paper ID Convention

**Date:** 2026-10-27

## Context

Need a consistent, human-readable scheme for `paper_id` values used across
file names, the evidence table, and cross-references.

## Decision

Use `firstauthor_lastname + year` in lowercase, with a short topic suffix
when the same first-author has multiple papers in the same year.

Examples:
- `valicherla2018` (only one Valicherla 2018 paper)
- `gupta2019_obesity` (distinguishes from other Gupta papers)
- `singh2020_heliyon` (journal used as disambiguator)

## Rationale

- Short and grep-friendly.
- Avoids numeric IDs that carry no meaning.
- Suffixes prevent collisions without over-complicating the scheme.

## Note on ID / First-Author Discrepancies (2026-10-31)

Subsequent bibliographic audit against PubMed revealed three cases where the established `paper_id` diverges from the true first author:
1. `valicherla2018`: First author is **Zakir Hossain** (`Hossain Z et al.`, PMID 29880906). Gopal R. Valicherla is second author.
2. `reza2022_lfs`: First author is **Richa Garg** (`Garg R et al.`, PMID 34902437). Mohammad Irshad Reza is not an author on this paper (Reza is first author on a different 2021 Life Sciences paper, PMID 34453940).
3. `dadge2023_nash`: First author is **Umesh Kumar Goand** (`Goand UK et al.`, PMID 37690261). S. Dadge is not an author on this paper.

**Decision:** To maintain relational integrity and prevent broken links across file names (`notes/papers/`), cross-references, git history, and master datasets, the existing `paper_id` keys are preserved permanently. True first authorship is reflected in the `citation` column of all tables and notes.
