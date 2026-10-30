# Research Plan — Phase 1: RESEARCH

**Created:** 2026-10-31  
**Status:** PLAN (awaiting approval before execution)  
**Goal:** Compile what is known and unknown about PSTi8, the pancreastatin/CHGA pathway, and related type 2 diabetes biology, to identify a feasible computational or literature contribution.

---

## Overview

Phase 0 (complete) built a sex-bias evidence table for all 11 published PSTi8 studies. Phase 1 broadens the scope to understand the biological, pharmacological, and methodological landscape around PSTi8, organized into six topic threads.

Each thread below specifies: **search queries**, **inclusion criteria**, **target paper count**, and the **notes/** output location.

---

## Thread 1 — Pancreastatin / CHGA Biology and Variants

**Question:** What is pancreastatin, how is it processed from chromogranin A, and what functional variants (e.g., PST rs9658667 / Gly297Ser) are known?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `pancreastatin chromogranin A processing secretory granule` | PubMed |
| 2 | `pancreastatin receptor signaling mechanism of action` | PubMed |
| 3 | `CHGA rs9658667 Gly297Ser pancreastatin variant` | PubMed |
| 4 | `pancreastatin insulin secretion glucose homeostasis review` | PubMed |
| 5 | `chromogranin A cleavage products catestatin vasostatin pancreastatin` | PubMed |

### Inclusion Criteria

- Papers describing pancreastatin biosynthesis, processing, receptor(s), or signaling.
- Genetic association studies of CHGA/PST variants with metabolic outcomes.
- Reviews of chromogranin A–derived peptides that cover pancreastatin substantively.
- Exclude: Papers mentioning pancreastatin only as a biomarker without mechanistic content.

### Target

8–12 papers (mix of foundational reviews and key primary studies).

### Output

- `notes/topics/01_pancreastatin_chga.md`
- Entries added to `data/papers_registry.csv`

---

## Thread 2 — Signaling Pathways: GRP78/UPR, Insulin Receptor/IRS, PKC, NOX3-JNK, AKT

**Question:** What are the established signaling cascades through which pancreastatin causes insulin resistance, and how does PSTi8 reverse them?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `pancreastatin insulin resistance signaling pathway` | PubMed |
| 2 | `pancreastatin GRP78 unfolded protein response ER stress` | PubMed |
| 3 | `pancreastatin PKC epsilon insulin receptor substrate` | PubMed |
| 4 | `pancreastatin NOX3 NADPH oxidase JNK hepatocyte` | PubMed |
| 5 | `pancreastatin AKT phosphorylation GLUT4 translocation` | PubMed |
| 6 | `PSTi8 signaling mechanism insulin sensitization` | PubMed |
| 7 | `chromogranin A derived peptide insulin resistance mechanism` | PubMed |

### Inclusion Criteria

- Primary studies measuring phosphorylation, protein expression, or gene expression of the named pathway nodes (GRP78, IRβ, IRS-1/2, PKCε, NOX3, JNK, AKT, GLUT4) in response to pancreastatin or PSTi8.
- Reviews with pathway diagrams or mechanistic synthesis.
- Exclude: Papers that only cite these pathways in passing within a discussion.

### Target

6–10 papers (substantial overlap with Thread 3 PSTi8 preclinical studies).

### Output

- `notes/topics/02_signaling_pathways.md`
- Entries added to `data/papers_registry.csv`

---

## Thread 3 — PSTi8 Preclinical Evidence (Expanded)

**Question:** What is the full preclinical evidence base for PSTi8 — efficacy, toxicity, PK, formulation, and any unpublished/preprint data?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `PSTi8 pancreastatin inhibitor peptide` | PubMed |
| 2 | `PEGKGEQEHSQQKEEEEEMAV` | PubMed, Google Scholar |
| 3 | `PSTi8 preclinical animal model` | PubMed |
| 4 | `PSTi8 toxicity safety pharmacology` | PubMed, Google Scholar |
| 5 | `PSTi8 formulation delivery nanoparticle` | PubMed, Google Scholar |
| 6 | `pancreastatin inhibitor peptide` | bioRxiv, medRxiv |
| 7 | `PSTi8 patent` | Google Patents |

### Inclusion Criteria

- Any study (primary, review, preprint, patent, conference abstract) that tests PSTi8 or a structurally related pancreastatin-inhibiting peptide in vitro or in vivo.
- No date restriction.
- Include negative or null results.

### Target

11 known studies + any additional studies or preprints found (target: identify 0–5 previously unknown items).

### Output

- `notes/topics/03_psti8_preclinical.md` (synthesis beyond what Phase 0 captured)
- Entries added to `data/papers_registry.csv`
- Update `data/evidence_table.csv` if new studies are found

---

## Thread 4 — Disease Context: T2D, NASH, PCOS, Menopause, Drug Landscape

**Question:** Where does PSTi8 sit in the broader therapeutic landscape for its target diseases? What are the established and emerging treatments, and what are the unmet needs regarding sex-specific evidence?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `type 2 diabetes sex differences pathophysiology review` | PubMed |
| 2 | `NASH NAFLD sex differences treatment review` | PubMed |
| 3 | `PCOS insulin resistance treatment landscape review` | PubMed |
| 4 | `menopause metabolic syndrome insulin resistance peptide therapy` | PubMed |
| 5 | `insulin sensitizer drug pipeline preclinical 2020 2024` | PubMed |
| 6 | `type 2 diabetes animal model sex bias male female` | PubMed |
| 7 | `colitis sex differences treatment response` | PubMed |

### Inclusion Criteria

- Recent reviews (2018–2026) of disease biology and treatment landscape for T2D, NASH, PCOS, or post-menopausal metabolic syndrome.
- Studies documenting sex differences in disease prevalence, progression, or treatment response.
- Competitor / pipeline reviews for insulin-sensitizing peptides.
- Exclude: Clinical trials of approved drugs (e.g., metformin, GLP-1 RAs) unless they specifically report sex-stratified outcomes.

### Target

8–12 papers (focused reviews, not exhaustive clinical literature).

### Output

- `notes/topics/04_disease_context.md`
- Entries added to `data/papers_registry.csv`

---

## Thread 5 — Related and Competing Approaches

**Question:** Are there other pancreastatin-targeting strategies, CHGA-derived peptide therapeutics, or peptide-based insulin sensitizers being developed?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `pancreastatin antibody neutralization metabolic` | PubMed |
| 2 | `catestatin metabolic syndrome insulin resistance` | PubMed |
| 3 | `chromogranin A peptide therapeutic diabetes` | PubMed |
| 4 | `anti-pancreastatin strategy insulin sensitization` | PubMed, Google Scholar |
| 5 | `peptide insulin sensitizer preclinical development` | PubMed |

### Inclusion Criteria

- Studies testing anti-pancreastatin antibodies, catestatin, or other CHGA-derived peptides for metabolic endpoints.
- Peptide-based insulin sensitizers distinct from GLP-1 agonists (to find PSTi8's competitive niche).
- Exclude: GLP-1 agonists, SGLT2 inhibitors, and other well-established drug classes (unless compared head-to-head with a CHGA-derived peptide).

### Target

5–8 papers.

### Output

- `notes/topics/05_competing_approaches.md`
- Entries added to `data/papers_registry.csv`

---

## Thread 6 — Methods and Reporting Standards

**Question:** What are the community standards for sex-inclusive preclinical research, and how do PSTi8 studies compare?

### Search Queries

| # | Query | Database |
|---|-------|----------|
| 1 | `ARRIVE guidelines sex inclusion preclinical research` | PubMed |
| 2 | `NIH sex as biological variable SABV policy` | PubMed |
| 3 | `sex bias preclinical pharmacology male only studies` | PubMed |
| 4 | `SAGER guidelines sex gender reporting research` | PubMed |
| 5 | `power analysis sex treatment interaction animal study sample size` | PubMed |
| 6 | `reproducibility crisis sex differences animal models` | PubMed |

### Inclusion Criteria

- Policy documents, guideline papers, and empirical audits of sex-inclusion in preclinical research.
- Methods papers on powering factorial designs for sex × treatment interactions.
- Meta-research on sex-reporting quality in pharmacology/endocrinology journals.
- Exclude: Clinical (human-only) reporting guidelines unless they explicitly cover preclinical extensions.

### Target

6–10 papers (mix of guidelines and empirical audits).

### Output

- `notes/topics/06_methods_standards.md`
- Entries added to `data/papers_registry.csv`

---

## Execution Protocol

1. **Search order:** Threads 1–6 sequentially. Within each thread, run PubMed queries first, then Google Scholar / preprint servers.
2. **Logging:** Every search query, date, database, number of results, and papers selected is logged in [docs/search_log.md](search_log.md).
3. **Registry:** Every paper encountered gets a row in [data/papers_registry.csv](../data/papers_registry.csv) regardless of inclusion decision. Papers excluded get `status: excluded` with a reason.
4. **Notes:** Each thread produces one summary note in `notes/topics/` synthesizing findings and identifying gaps.
5. **Rules compliance:** All AGENTS.md rules apply. `NOT_READ` for any paper not accessed in full. Locators for every extracted value. Paraphrase only.
6. **Sync:** `./scripts/sync.sh` after every batch of file changes.
7. **Stopping criterion:** When diminishing returns are reached (successive queries yield <10% new relevant hits), move to the next thread or close the thread.

---

## Deliverables at End of Phase 1

- [ ] 6 topic summary notes in `notes/topics/`
- [ ] Populated `data/papers_registry.csv` (target: 40–60 entries)
- [ ] Complete `docs/search_log.md`
- [ ] Updated `STATE.md` with Phase 1 completion status and synthesis of findings
- [ ] Identification of 2–3 candidate computational/literature contributions for Phase 2
