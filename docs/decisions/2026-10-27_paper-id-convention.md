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
