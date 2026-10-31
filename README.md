# PSTi8 Evidence Map

This repository provides a systematic literature audit and evidence map of preclinical animal and pharmacokinetic studies evaluating **PSTi8** (`PEGKGEQEHSQQKEEEEEMAV-NH₂`, a 21-amino-acid peptide inhibitor of pancreastatin). It documents study designs, disease indications, reporting of biological sex, statistical methodology, and factorial interaction testing.

All data points in this repository represent extracted summary values linked to source locators in published literature; no copyrighted full-text papers are distributed here.

---

## Important Caveats & Scope Limitations

> [!WARNING]
> Please note the following critical limitations of this dataset and repository:
> 
> 1. **Work in Progress:** This repository is an active, ongoing research audit subject to continuous updates and refinements as additional papers and primary sources are examined.
> 2. **Some Papers Abstract-Only:** Due to institutional subscription paywalls, several primary studies (e.g., published in Elsevier or Springer journals) have been evaluated solely on the basis of their published abstracts and indexed metadata (`abstract_only`). Specific methodological details (such as sample size, exact animal sex, or estrous staging) not disclosed in abstracts are labeled `NOT_READ` or `not_reported (abstract-only)`.
> 3. **Some Sex Values Inferred from Model Type:** In certain paywalled studies where the published abstract does not explicitly state animal sex in text, sex values have been classified as `inferred_from_model` (e.g., single-sex surgical/endocrine models such as letrozole/DHEA-induced PCOS or VCD/ovariectomy perimenopause) or `NOT_READ`. These classifications reflect inference from model design rather than explicit textual verification from the primary methods section.
> 4. **Not Peer-Reviewed:** The synthesis, evidence table, power models, and audit reports contained in this repository are working scholarly notes and research artifacts; they have not undergone formal peer review.
> 5. **Not Medical Advice:** This repository is strictly for academic and computational research purposes and does not constitute medical, clinical, or pharmacological advice.

---

## Repository Structure

- `data/evidence_table.csv`: Core 22-column evidence matrix of all 11 catalogued PSTi8 preclinical studies.
- `data/papers_registry.csv`: Master registry of 26 verified PSTi8 primary studies, preprints, and related reviews.
- `data/power_results.csv`: Statistical power model scenarios evaluating $2 \times 2$ factorial Sex × Treatment interaction testing across daily and cumulative DAI endpoints.
- `docs/schema.md`: Complete schema and categorical value definitions for the evidence table.
- `docs/audit_report.md`: Systematic sex-coverage audit report and methodological gap analysis.
- `docs/search_strategy.md`: Systematic search strategy, databases, queries, and PRISMA-aligned inclusion/exclusion criteria.
- `docs/power_analysis.md`: Detailed statistical power analysis documentation, mathematical derivation, and effect-size ranges.
- `scripts/`: Reproducible Python analytical scripts for power calculations and verification.

---

## License

This repository, including all datasets, documentation, scholarly notes, and code in `scripts/`, is licensed under the **Creative Commons Attribution 4.0 International Public License (CC BY 4.0)**. See the [LICENSE](LICENSE) file for the full legal text.

### Attribution Requirement
When sharing, adapting, citing, or distributing content from this repository, appropriate credit must be provided as follows:
> Singh, Devansh Pratap (2026). *PSTi8 Evidence Map: Systematic Literature Audit and Preclinical Sex-Bias Review*. GitHub repository: [https://github.com/Devanshyadav118/psti8-evidence-map](https://github.com/Devanshyadav118/psti8-evidence-map)

### Third-Party Literature Notice
Cited primary research papers, journal articles, and publisher materials remain under their respective publishers' and authors' copyright. This repository contains only extracted values, summary statistics, bibliometrics, and original paraphrased scholarly notes.

