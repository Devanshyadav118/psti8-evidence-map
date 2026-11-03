---
prompt_id: 21
slug: osf_preregistration_and_dual_screening
status: done
commit: 0dddb37
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-03
---

Step 0: Save this prompt verbatim to prompts/21_osf_preregistration_and_dual_screening.md (front matter: prompt_id: 21, slug: osf_preregistration_and_dual_screening, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-03). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, STATE.md, docs/gap_map.md, docs/audit_report.md, data/evidence_table.csv, and data/syrcle_arrive_matrix.csv.

Task: (1) author the formal prospective OSF protocol registration document conforming to PRISMA-P and SYRCLE guidelines, and (2) generate a reproducible dual-screening and data extraction audit sheet for independent verification across all 20 primary studies. Do not call Exa or Firecrawl (0 credits). Quotes strictly under 15 words.

1. OSF Protocol Registration Document (docs/osf_protocol_registration.md):
   - Title: Targeting GRP78 with Pancreastatin Inhibitor PSTi8: Protocol for a Systematic Review, Preclinical Sex-Bias Audit, and In Silico Structural Investigation.
   - Structured sections matching the OSF Systematic Review Registration Schema:
     a. Administrative information (authors, contact, open repo URL, CC BY 4.0 license, funding: none, conflicts of interest: none).
     b. Background and rationale (pancreastatin/CHGA biology, GRP78 hypothesis, and the NIH SABV mandate).
     c. Research questions (preclinical efficacy across disease indications, adherence to ARRIVE 2.0 / SYRCLE reporting, biological sex representation, 2x2 factorial interaction testing, and in silico target engagement).
     d. Search strategy and sources (PubMed, Crossref, Europe PMC, PMC, bioRxiv/medRxiv; exact boolean search syntax documented).
     e. Eligibility criteria (PICO framework: Population: non-human mammalian in vivo models; Intervention: synthetic PSTi8 peptide; Comparator: vehicle or active control; Outcomes: metabolic, inflammatory, histological, or pharmacokinetic endpoints).
     f. Study screening and data extraction methods (dual independent screening procedure, reconciliation protocol, automated script validation).
     g. Risk of bias and reporting quality appraisal (10-domain SYRCLE tool, 10-item ARRIVE 2.0 Essential Set).
     h. Quantitative synthesis and statistical modeling (factorial interaction contrast formulas, non-central t power calculations, descriptive reporting proportions).
     i. In silico structural biology methods (AlphaFold 3 co-folding with ATP/Mg2+, sliding-window charge/hydropathy profiling, and control experiment specifications).

2. Dual-Screening & Extraction Verification Sheet (scripts/generate_dual_screening_sheet.py):
   - Generate data/dual_screening_audit.csv containing all 20 studies from data/evidence_table.csv with the following standardized audit columns:
     * study_id, doi, title, first_author, year
     * screener1_inclusion (included/excluded), screener1_sex_extracted (male/female/both/not_read), screener1_interaction_status (confirmed_absent/unreported)
     * screener2_inclusion, screener2_sex_extracted, screener2_interaction_status
     * agreement_status (concordant/discrepant), reconciliation_notes
   - Pre-populate Screener 1 columns from data/evidence_table.csv; set Screener 2 columns to pending for human/independent secondary review.

3. Update STATE.md, INDEX.md, prompts/INDEX.md, run ./scripts/sync.sh, and show a summary only.
