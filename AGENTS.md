# AGENTS.md — Agent Instructions

## Project Goal

**Phase 0 (complete):** Build an evidence table of **all published PSTi8 studies** (animal and cell), focused on whether biological sex was included, balanced, and analyzed as a variable.

**Phase 1 (active — RESEARCH):** Compile what is known and unknown about PSTi8, the pancreastatin/CHGA pathway, and related type 2 diabetes biology, to identify a feasible computational or literature contribution.

**Phase 2 (planned):** Execute the contribution identified in Phase 1.

No wet-lab work; literature extraction, data curation, and computational analysis only.

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
| `docs/research_plan.md` | Phase 1 research plan: 6 topic threads, queries, criteria |
| `docs/search_log.md` | Reproducible log of every literature search performed |
| `docs/tool_usage_log.md` | Usage log for external tools (Exa, Firecrawl) |
| `notes/topics/` | One synthesis note per research topic thread |
| `data/papers_registry.csv` | Master registry of all papers encountered (any thread) |

## Tool Usage Policy

1. **Exa:** Discovery and semantic search. Use freely and log queries in `docs/tool_usage_log.md`.
2. **Firecrawl:** Hard budget of 1,000 credits total. Use only to scrape one specific open-access page (`firecrawl_scrape`). Never crawl or map (`firecrawl_crawl`, `firecrawl_map` prohibited). Maximum 25 pages per task unless the user explicitly approves.
3. **Citation Verification Gate:** PubMed and Crossref remain the authoritative gate for verifying any citation, DOI, author list, or publication metadata before it enters `data/papers_registry.csv` or `data/evidence_table.csv`.
4. **Security & Secrets:** Never store or commit API keys, access tokens, `.env` files, or MCP configuration files in this repository. All credentials must reside exclusively in user configuration.
5. **Copyright:** Never commit full text of copyrighted or paywalled papers to the repository. Only open-access extracts, paraphrased notes, and summary tables with locators may be stored.

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
