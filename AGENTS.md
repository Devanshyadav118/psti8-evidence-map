# AGENTS.md — Agent Instructions

## Project Goal

Build an evidence table of **all published PSTi8 studies** (animal and cell),
focused on whether biological sex was included, balanced, and analyzed as a
variable.  No wet-lab work; literature extraction and data curation only.

PSTi8 = pancreastatin inhibitor peptide, sequence PEGKGEQEHSQQKEEEEEMAV-NH₂.

## First Steps for Any Agent

1. Read [INDEX.md](INDEX.md) to understand the file layout.
2. Read [STATE.md](STATE.md) for current status and next actions.
3. Update [STATE.md](STATE.md) **before ending any session**.

## Folder Map

| Path | Purpose |
|------|---------|
| `sources/` | Seed papers, study guide, other read-only inputs |
| `notes/papers/` | One markdown note per paper (frontmatter required) |
| `data/evidence_table.csv` | Master evidence table (see schema) |
| `docs/schema.md` | Column definitions for the evidence table |
| `docs/decisions/` | Short dated decision records |

## Rules

1. **Never fill a field from memory.** If you did not read the datum in the
   paper, write `NOT_READ`.
2. Each paper note **must** have YAML frontmatter:
   `paper_id`, `doi`, `access` (full / abstract / not_read),
   `last_updated`, `status`.
3. Every extracted value gets a **locator** (section, table, or figure number).
   Paraphrase; do not paste long passages from papers.
4. Prefer **open-access** sources (PMC, MDPI). If a paper is paywalled, record
   `access: abstract` or `access: not_read`; do **not** guess content.
5. Keep notes short and single-topic. Use **relative markdown links**
   (e.g., `[schema](docs/schema.md)`), not only `[[wikilinks]]`.
6. Record non-obvious choices in `docs/decisions/` as short dated notes
   (filename format: `YYYY-MM-DD_topic.md`).
7. **Always auto-sync to GitHub.** Whenever files are modified, created, or deleted in the vault, automatically commit and push to GitHub (`origin main`) using `./scripts/sync.sh` before finishing any turn.

## Evidence Table Schema

See [docs/schema.md](docs/schema.md) for full column definitions.

Allowed categorical values: `yes` / `no` / `not_applicable` / `NOT_READ`.
