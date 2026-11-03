---
prompt_id: 22
slug: draft_full_manuscript
status: done
tool: Antigravity
model: "Gemini 3.8 Flash (High)"
date: 2026-11-03
---

Step 0: Save this prompt verbatim to prompts/22_draft_full_manuscript.md (front matter: prompt_id: 22, slug: draft_full_manuscript, status: running, tool: Antigravity, model: "Gemini 3.8 Flash (High)", date: 2026-11-03). When the run ends, update status to done and add the commit hash.

Read AGENTS.md, STATE.md, docs/gap_map.md, docs/osf_protocol_registration.md, docs/audit_report.md, docs/power_analysis.md, docs/structural_data_inventory.md, docs/pathway_and_variant_analysis.md, notes/topics/ (all 6 notes), data/evidence_table.csv, data/syrcle_arrive_matrix.csv, and data/structures/3d_models/af3_complex_metrics.csv.

Task: author the complete, submission-ready research manuscript in manuscript/manuscript.md following the Guide for Authors of Biology of Sex Differences (BioMed Central / Springer Nature).

Guidelines:
- Paraphrase all cited text; keep any direct quote strictly under 15 words.
- All numbers and percentages must match repository CSVs exactly (20 primary studies, 116 registry papers, 0/20 interaction tests, 0% baseline estrous staging, 100% male bias in T2D/DIO, AF3 ipTM 0.81 vs 0.76 vs 0.28).
- Do not call Exa or Firecrawl (0 credits).

Structure manuscript/manuscript.md into the following standard BMC IMRaD format:

1. Title & Front Matter:
   - Title: Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms
   - Authors: Devansh Pratap Singh (lead author/investigator)
   - Running Title: Preclinical Sex Bias and Structural Mechanism of PSTi8
   - Keywords: Pancreastatin, PSTi8, Chromogranin A, GRP78, HSPA5, Sex as a Biological Variable, Factorial Interaction Power, AlphaFold 3, Type 2 Diabetes, ARRIVE 2.0.

2. Abstract (Structured, <=350 words):
   - Background, Methods, Results, Conclusions.

3. Introduction:
   - Physiological role of Chromogranin A and pancreastatin in glycemic control and insulin resistance.
   - Development of synthetic peptide inhibitor PSTi8 (hCHGA273-293-amide).
   - The NIH Sex as a Biological Variable (SABV) mandate and the translation crisis in metabolic disease.
   - Unresolved structural biology: intrinsic disorder of pancreastatin, construct limitations of historical rigid docking, and the GRP78 compartmentalization paradox.
   - Formal study objectives.

4. Methods:
   - PRISMA 2020 systematic search strategy, eligibility criteria, and database coverage.
   - Dual-screening protocol and data extraction provenance.
   - Reporting quality and risk-of-bias appraisal (ARRIVE 2.0 Essential 10, SYRCLE 10-domain tool).
   - Statistical power modeling of 2x2 factorial interaction contrasts (SE = 2*sigma / sqrt(n), non-central t distribution).
   - In silico structural biology & co-folding: AlphaFold 3 complex modeling (5 diffusion samples from modelSeeds [1] with Mg2+-ATP), sliding-window charge/hydropathy profiling (window=5), cross-species alignment (Biopython PairwiseAligner), and STRING/Reactome interactome mapping.

5. Results:
   - 3.1 Preclinical evidence landscape & single-lab network concentration (20 primary studies; CDRI collaborative network).
   - 3.2 Methodological quality & reporting compliance (ARRIVE 2.0 Essential 10 and SYRCLE domain breakdowns from syrcle_arrive_matrix.csv).
   - 3.3 Systematic sex segregation & absence of baseline estrous staging (100% male exclusivity in T2D/DIO; restriction of females to endocrine models; 0% baseline estrous staging).
   - 3.4 Omission of interaction testing & factorial power collapse (0/20 studies reported Sex x Treatment interaction; power <19% in standard n=6 cohorts).
   - 3.5 Structural mechanism: Refuting direct ATPase pocket docking & establishing the interdomain linker wedge (PSTi8 ranking 0.85, ipTM 0.81, min PAE 2.30 A; 48 contacts at linker-SBDbeta hinge vs 140 contacts in WT PST-29 tri-domain clamp).
   - 3.6 Absolute interspecies cleft conservation (100.00% sequence identity in SBDbeta residues 427-537 across human, mouse, and rat).
   - 3.7 Resolution of the Gly297Ser genetic paradox & PSTi8 structural immunity (rs9658664 in cleaved C-terminal tail; polar Ser25 collapses AF3 ipTM to 0.28, while PSTi8 terminates at residue 21).
   - 3.8 Functional GRP78 interactome & cellular compartmentalization (ER luminal IRE1-TRAF2-JNK1-IRS1 Ser307 cascade vs cell-surface GRP78-AKT1 scaffold).

6. Discussion:
   - Allosteric interdomain wedge mechanism vs historical active-site docking claims.
   - The cellular compartmentalization paradox: intracellular chaperone protection vs circulating pathogenic signaling.
   - Translational consequences of male-exclusive preclinical pipelines.
   - Actionable preclinical design recommendations (factorial interaction designs, estrous tracking standards).
   - In silico control roadmap (prioritized controls: NBD-only apo/ADP, scrambled/random peptides, HWDFAWPW positive control, Boltz-2/Chai-1).
   - Study limitations (paywalled abstract-only literature constraints).

7. Declarations & References:
   - Ethics approval, Consent for publication, Competing interests (none), Funding (none), Authors' contributions, Acknowledgements.
   - Data and materials availability statement referencing the open CC BY 4.0 GitHub repository, OSF registration, and reproducible analysis scripts.

8. Update STATE.md, INDEX.md, prompts/INDEX.md, run ./scripts/sync.sh, and show a summary of sections and word counts.
