# Registry Merge Report: Verified Staging to Master Papers Registry

**Date:** 2026-11-02  
**Task:** Merge verified staging literature registries into the master registry [data/papers_registry.csv](../data/papers_registry.csv) per prompt 07 instructions.  
**Pre-Merge Backup:** [data/staging/papers_registry_pre_merge.csv](../data/staging/papers_registry_pre_merge.csv) (26 baseline Thread 3 rows)  
**Quarantined Rejections:** [data/staging/rejected_rows.csv](../data/staging/rejected_rows.csv) (3 unverified Thread 6 rows)  
**Merge Automation Script:** [scripts/merge_registries.py](../scripts/merge_registries.py)  

---

## 1. Executive Summary

This report documents the consolidation of verified literature from Threads 1, 2, 3, and 6 into the authoritative master registry [data/papers_registry.csv](../data/papers_registry.csv). Prior to this operation, the master registry held only the initial 26 verified records from Thread 3 (primary PSTi8 preclinical literature and direct reviews). Following verification audits across all completed topic threads, verified candidate records (`verified: yes` and `verified: partial`) were integrated, while unverified records (`verified: no`) were quarantined.

- **Baseline master records (pre-merge):** 26
- **Total candidate records evaluated across 4 threads:** 119
- **Quarantined records (`verified: no`):** 3 (all from Thread 6)
- **Duplicate DOIs merged across threads:** 0 (all 116 records have unique DOIs)
- **Total records in master registry (post-merge):** **116**
- **Phase 1 target progress:** The target was 40–60 entries; the master registry now contains 116 authenticated studies across 4 research threads.

---

## 2. Row Counts Per Thread (Before and After)

Every staged registry was cross-referenced with its corresponding verification report ([docs/thread1_verification.md](thread1_verification.md), [docs/thread2_verification.md](thread2_verification.md), [docs/thread3_verification.md](thread3_verification.md), and [docs/thread6_verification.md](thread6_verification.md)):

| Thread Name / Topic Scope | Staged Rows | Verified `yes` | Verified `partial` | Verified `no` (Quarantined) | Duplicates Merged | Pre-Merge in Master | Post-Merge in Master |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Thread 3:** PSTi8 Direct Preclinical Studies | 26 | 25 | 1 | 0 | 0 | 26 | 26 |
| **Thread 1:** Pancreastatin / CHGA Pathway Biology | 34 | 31 | 3 | 0 | 0 | 0 | 34 |
| **Thread 2:** Signaling Mechanisms & ER Stress / GRP78 | 32 | 32 | 0 | 0 | 0 | 0 | 32 |
| **Thread 6:** Methods & Preclinical Reporting Standards | 27 | 14 | 10 | 3 | 0 | 0 | 24 |
| **Total** | **119** | **102** | **14** | **3** | **0** | **26** | **116** |

---

## 3. Deduplication and Preprint Tracking

### A. Case-Insensitive DOI Deduplication
All DOIs were normalized (lowercased, stripped of leading `https://doi.org/` or `doi:` prefixes, and trimmed of whitespace). Cross-thread indexing revealed zero duplicate DOIs across the four threads. Each thread addressed a distinct biological or methodological domain without redundant citations:
- Thread 3 covered direct PSTi8 pharmacodynamics, pharmacokinetics, and related syntheses.
- Thread 1 covered foundational pancreastatin discovery, CHGA genetics, and physiological processing.
- Thread 2 covered downstream insulin resistance signaling cascades, GRP78 interactions, and ER stress pathways.
- Thread 6 covered animal research reporting standards (ARRIVE 2.0, SYRCLE), sex reporting audits, and automated systematic review methodologies.

### B. Handling Preprints and Published Versions (`published_version_of`)
A new column `published_version_of` was added to [data/papers_registry.csv](../data/papers_registry.csv) to track preprints alongside their subsequent peer-reviewed journal publications. Where both the preprint and the published version appear in the registry, both entries are preserved and bidirectionally cross-linked:
1. **Goand et al. (Thread 3):**
   - Preprint: `goand2022_ssrn` (SSRN Electronic Journal 2022, DOI `10.2139/ssrn.4153464`) $\rightarrow$ `published_version_of: goand2023_peptides`.
   - Journal Publication: `goand2023_peptides` (*Peptides* 2023, DOI `10.1016/j.peptides.2022.170902`) $\rightarrow$ `published_version_of: goand2022_ssrn`.
2. **Muntjewerff et al. (Thread 1):**
   - Preprint: `muntjewerff2025_biorxiv` (bioRxiv 2024, DOI `10.1101/2024.11.29.626063`) $\rightarrow$ `published_version_of: muntjewerff2025_commbiol`.
   - Journal Publication: `muntjewerff2025_commbiol` (*Communications Biology* 2025, DOI `10.1038/s42003-025-09135-z`) $\rightarrow$ `published_version_of: muntjewerff2025_biorxiv`.

For all other 112 records without a paired preprint/journal counterpart, `published_version_of` remains empty.

---

## 4. Quarantined and Rejected Rows

In accordance with instruction 2, candidate rows with `verified: no` or `could_not_open` were quarantined into [data/staging/rejected_rows.csv](../data/staging/rejected_rows.csv) along with specific rejection rationales:

| Record ID | Claimed Citation & DOI | Quarantined Status | Rejection Reason |
| :--- | :--- | :---: | :--- |
| `booth2020_systrev` | Booth et al., *Syst Rev*, 2020<br>`10.1186/s13643-020-01261-5` | `no` | Fabricated DOI returns HTTP 404. Source URL PMID 32005283 points to unrelated surgical trial in *Trials* (Han K et al.). Preclinical PROSPERO guidance appeared elsewhere. |
| `vandervaart2020_jaha` | van der Vaart et al., *JAHA*, 2020<br>`10.1161/JAHA.120.016866` | `no` | Fabricated metadata. DOI returns HTTP 404. Source URL PMID 32869702 resolves to Candellier A in *Perit Dial Int*. Authentic PreclinicalTrials.eu papers were authored by van der Naald M. |
| `vandernaald2024_jce` | van der Naald et al., *JCE*, 2024<br>`10.1016/j.jclinepi.2024.111257` | `no` | Fabricated/mismatched citation. DOI resolves to adaptive clinical trial design by Wang Y (PMID 38218461); URL PMID 38278428 points to Xie L in *Front Aging Neurosci*. |

---

## 5. Controlled Role Vocabulary Mapping

Instruction 4 established a single controlled vocabulary for study roles:
- `primary_evidence`: Direct preclinical studies of the pancreastatin inhibitor PSTi8.
- `pst_chga_biology`: Physiological and biochemical studies of pancreastatin and chromogranin A.
- `background_mechanism`: Downstream cellular cascades, ER stress, GRP78 chaperone biology, and metabolic signaling.
- `sex_estrogen`: Studies evaluating sex as a biological variable, estrogen modulation, or sexual dimorphism.
- `methods_reference`: Reporting standards (ARRIVE), risk of bias tools (SYRCLE), statistical methods, or review screening benchmarks.
- `review`: Comprehensive synthesis articles, scoping reviews, or systematic overviews.
- `context_only`: Secondary context papers not directly fitting the primary pathways.

### Role Mapping Audit
Because prior thread verification steps adhered strictly to this taxonomy, zero arbitrary role strings were present in the staging registries. The exact mappings across the staging tables are summarized below:

| Staging Source File | Raw Staging Role | Controlled Master Role | Meaning Preserved | Count |
| :--- | :--- | :--- | :---: | :---: |
| `thread3_registry_unverified.csv` / Master | `primary_evidence` | `primary_evidence` | Direct PSTi8 experimental studies | 21 |
| `thread3_registry_unverified.csv` / Master | `review` | `review` | Reviews focusing on PST/PSTi8 | 4 |
| `thread3_registry_unverified.csv` / Master | `context_only` | `context_only` | Related reproductive context (`singla2026_jri`) | 1 |
| `thread1_registry_unverified.csv` | `pst_chga_biology` | `pst_chga_biology` | CHGA/PST physiological actions | 20 |
| `thread1_registry_unverified.csv` | `background_mechanism` | `background_mechanism` | Gq-PLC, nitric oxide, glycogenolysis | 4 |
| `thread1_registry_unverified.csv` | `methods_reference` | `methods_reference` | Assays, antibodies, and peptide tools | 3 |
| `thread1_registry_unverified.csv` | `review` | `review` | Reviews of chromogranin family | 4 |
| `thread1_registry_unverified.csv` | `context_only` | `context_only` | Contextual papers (`tatnell1991`, `skrabanja1998`) | 2 |
| `thread1_registry_unverified.csv` | `sex_estrogen` | `sex_estrogen` | Estrogen regulation of CHGA processing | 1 |
| `thread2_registry_unverified.csv` | `background_mechanism` | `background_mechanism` | Hepatic insulin cascades, GRP78, ER stress | 17 |
| `thread2_registry_unverified.csv` | `sex_estrogen` | `sex_estrogen` | Sex dimorphism in ER stress & insulin resistance | 6 |
| `thread2_registry_unverified.csv` | `methods_reference` | `methods_reference` | Biophysical methods (HSPA5 chaperone assays) | 2 |
| `thread2_registry_unverified.csv` | `review` | `review` | ER stress and chaperone reviews | 7 |
| `thread6_registry_unverified.csv` | `methods_reference` | `methods_reference` | ARRIVE 2.0, SYRCLE, PRISMA, LLM benchmarks | 21 |
| `thread6_registry_unverified.csv` | `review` | `review` | Scoping reviews of methods / SABV policies | 3 |

### Final Distribution of Roles in Master Registry
- `methods_reference`: **26 (22.4%)**
- `primary_evidence`: **21 (18.1%)**
- `background_mechanism`: **21 (18.1%)**
- `pst_chga_biology`: **20 (17.2%)**
- `review`: **18 (15.5%)**
- `sex_estrogen`: **7 (6.0%)**
- `context_only`: **3 (2.6%)**
- **Total:** **116 (100.0%)**

---

## 6. Access and Verification Status Profile

### A. Verification Integrity
- **`verified: yes`:** **102 (87.9%)** — Fully matched against PubMed and Crossref APIs.
- **`verified: partial`:** **14 (12.1%)** — Authentic literature identified where staging search output contained minor typographical or journal naming errors.
- **`verified: no`:** **0 in master** (100% quarantined into `rejected_rows.csv`).

### B. Access Mode
- **`open`:** **79 (68.1%)** — Accessible via PubMed Central, bioRxiv, Europe PMC, or publisher open access.
- **`paywalled`:** **36 (31.0%)** — Subscription access; verified via official MEDLINE abstract and Crossref metadata.
- **`unknown`:** **1 (0.9%)** — `tatnell1991_biochemj` (historical archive paper).

### C. Reading Status
- **`abstract_only`:** **90 (77.6%)** — Verified through complete indexed abstract, author, and citation records.
- **`full_text_read`:** **26 (22.4%)** — Verified with complete full-text evaluation.

---

## 7. Notes and Decision Log

1. **Preservation of Existing Records:** The 26 baseline Thread 3 rows previously verified in `data/papers_registry.csv` were maintained with 100% fidelity. Existing fields, corrections, and notes were preserved without overwrite.
2. **Bidirectional Preprint Linking:** Rather than deleting preprints or leaving cross-references unlinked, preprints and their published counterparts are linked bidirectionally in `published_version_of`. Consumers filtering by either preprint or published paper can locate the paired record.
3. **Status of `lieberum2025_medrxiv`:** While the verification audit confirmed that Lieberum et al. is published peer-reviewed in *Journal of Clinical Epidemiology* (May 2025; Vol. 181: 111746; DOI `10.1016/j.jclinepi.2025.111746`, PMID `40021099`), only one row existed in the staging file. This row was merged with its verified peer-reviewed publication documented in `verification_note` rather than fabricating a second artificial row.
4. **Strict Quote Limit Adherence:** In accordance with project instructions, all descriptions and notes are paraphrased; no quoted text exceeds 14 words.
