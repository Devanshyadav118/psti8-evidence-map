# Targeting GRP78 with Pancreastatin Inhibitor PSTi8: Protocol for a Systematic Review, Preclinical Sex-Bias Audit, and In Silico Structural Investigation

**Registry:** Open Science Framework (OSF) Systematic Review Registration  
**Registration Format:** OSF Systematic Review Registration Schema / PRISMA-P 2015 Checklist / SYRCLE Preclinical Protocol Guidelines  
**Protocol Version:** 1.0  
**Date:** 2026-11-03  
**Repository:** [psti8-evidence-map on GitHub](https://github.com/Devanshyadav118/psti8-evidence-map)  
**Local Vault Reference:** [`psti8-sex-bias-review`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review)

---

## 1. Administrative Information

### 1.1 Title
**Targeting GRP78 with Pancreastatin Inhibitor PSTi8: Protocol for a Systematic Review, Preclinical Sex-Bias Audit, and In Silico Structural Investigation.**

### 1.2 Authors & Affiliations
- **Devansh Pratap Singh** (Lead Investigator, Data Extraction & Computational Modeling)
  - Correspondence: [`Devanshyadav118/psti8-evidence-map`](https://github.com/Devanshyadav118/psti8-evidence-map)
- **Collaborative Antigravity Research Framework** (Automated API Harvesters, Structural Bioinformatics Pipelines)

### 1.3 Open Science & Governance
- **Open Access Repository:** [`https://github.com/Devanshyadav118/psti8-evidence-map`](https://github.com/Devanshyadav118/psti8-evidence-map)
- **Repository Licensing:** Creative Commons Attribution 4.0 International ([CC BY 4.0](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/LICENSE)).
- **Primary Data Assets:**
  - Master Evidence Table: [`data/evidence_table.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/evidence_table.csv)
  - Master Papers Registry: [`data/papers_registry.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/papers_registry.csv)
  - Dual-Screening Audit Sheet: [`data/dual_screening_audit.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/dual_screening_audit.csv)
  - Methodological Matrix: [`data/syrcle_arrive_matrix.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/syrcle_arrive_matrix.csv)
  - Statistical Power Scenarios: [`data/power_results.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/power_results.csv)
  - Structural Assets Manifest: [`data/structures/structures_manifest.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/structures_manifest.csv)
- **Funding:** No specific external grants or commercial sponsorships supported this review.
- **Conflicts of Interest:** The authors declare no financial or commercial conflicts of interest.
- **Target Journal:** *Biology of Sex Differences* (Springer Nature).

---

## 2. Background & Rationale

### 2.1 Chromogranin A & Pancreastatin Biology
Chromogranin A (CHGA) is a 439-amino-acid neuroendocrine prohormone stored in secretory granules of neuroendocrine and endocrine cells. Endoproteolytic processing of CHGA by prohormone convertases releases bioactive regulatory peptides, most notably pancreastatin (PST; human mature coordinates residues 273–301: `PEGKGEQEHSQQKEEEEEMAVVPQGLFRG-NH2`). 

Endogenous PST functions as a physiological counter-regulatory brake against insulin action. In hepatocytes and adipocytes, PST suppresses insulin-stimulated glucose uptake, inhibits glycogen synthesis, stimulates gluconeogenesis and glycogenolysis, and activates lipolysis. Elevation of circulating PST correlates with severe insulin resistance (IR), obesity, gestational diabetes, and type 2 diabetes mellitus (T2D).

### 2.2 PSTi8 Peptide Antagonist Development
To counteract PST-driven metabolic dysfunction, Hossain et al. (2018) designed PSTi8 (`PEGKGEQEHSQQKEEEEEMAV-NH2`), a synthetic 21-amino-acid peptide truncated at the C-terminus relative to full-length PST-29. Removal of the terminal octapeptide (`VPQGLFRG`) converts the peptide from a functional agonist into a competitive antagonist. Preclinical evaluations demonstrate that PSTi8 suppresses hepatic gluconeogenesis, enhances skeletal muscle glucose disposal, promotes M2 anti-inflammatory macrophage polarization, and restores insulin signaling in rodent disease models.

### 2.3 The GRP78 Target Hypothesis & Biophysical Gaps
Early pharmacological studies posited that PST and PSTi8 exert metabolic actions by interacting directly with cell-surface 78 kDa glucose-regulated protein (GRP78 / HSPA5 / BiP), an ER-resident Hsp70 molecular chaperone that undergoes cell-surface translocation under metabolic stress. Hossain et al. (2018) modeled PSTi8 docking into the catalytic nucleotide-binding domain (NBD) of GRP78 (PDB 3LDP). 

However, critical biophysical questions remain unresolved:
1. GRP78 canonical chaperone activity is driven by an ATP-induced conformational transition between the N-terminal NBD and the C-terminal substrate-binding domain ($\text{SBD}\beta/\text{SBD}\alpha$). Rigid-body docking into isolated apo NBD does not reflect the intact, ATP-loaded receptor state.
2. The naturally occurring human CHGA coding variant Gly297Ser (rs9658664), which resides at position 25 of PST-29, markedly exacerbates human diabetic risk and peptide potency; yet position 25 is absent in PSTi8, creating a structural paradox regarding variant susceptibility and competitive efficacy.

### 2.4 The NIH Sex-as-a-Biological-Variable (SABV) Mandate
In 2015–2016, the National Institutes of Health (NIH) enacted the Sex as a Biological Variable (SABV) policy (NOT-OD-15-102), establishing that biological sex is a fundamental biological determinant that must be incorporated into preclinical research designs. Glucose homeostasis, adiposity distribution, liver steatosis, and immune modulation exhibit profound sexual dimorphism in rodents and humans. Furthermore, estrogen receptor signaling directly modulates GRP78 expression and unfolded protein response (UPR) pathways.

Despite these known dimorphic mechanisms, preliminary scoping revealed that preclinical in vivo evaluations of PSTi8 were predominantly conducted in male rodents or restricted to female-specific pathology (PCOS, ovariectomy-induced menopause), with a pervasive absence of factorial $\text{Sex} \times \text{Treatment}$ statistical interaction testing.

---

## 3. Review Objectives & Research Questions

This systematic review and computational study addresses five primary questions:

1. **Preclinical Efficacy Spectrum:** What is the scope, reproducibility, and therapeutic efficacy of PSTi8 across all published non-human mammalian in vivo disease models (T2D, diet-induced obesity, NASH, PCOS, menopause-associated IR, DSS colitis, wound healing, and pharmacokinetics)?
2. **Methodological Rigor & Reporting Quality:** How comprehensively do primary in vivo PSTi8 studies adhere to the **ARRIVE 2.0 Essential 10** reporting standards and the **SYRCLE Risk of Bias** tool across 10 experimental domains?
3. **Biological Sex Representation (SABV Audit):** What proportion of primary in vivo PSTi8 studies include male animals, female animals, or both sexes; what proportion transparently report animal sex in the abstract versus body text; and what proportion monitor baseline estrous cyclicity?
4. **Factorial Interaction Testing ($2 \times 2$ ANOVA):** In primary studies that enroll both male and female animals, do the investigators test the formal $\text{Sex} \times \text{Treatment}$ interaction contrast, or do they commit the "subgroup fallacy" (claiming sex-specific effects based solely on separate within-sex comparisons)?
5. **In Silico Target Engagement & Quaternary Mechanism:** Using full-length AlphaFold 3 neural co-folding (in the presence of endogenous $\text{Mg}^{2+}$-ATP), ESM-2 language model mutational scanning, and sliding-window physicochemical profiling, what is the quaternary interface between PSTi8/PST-29 and GRP78, and how does the Gly297Ser polymorphism alter structural stability?

---

## 4. Search Strategy & Information Sources

### 4.1 Bibliographic Databases & Registries
A comprehensive, multi-database literature search without publication date limits (inception through November 2026) was conducted across:
1. **PubMed / MEDLINE** (National Library of Medicine)
2. **Crossref Metadata API**
3. **Europe PMC**
4. **PubMed Central (PMC)** open-access subset
5. **Preprint Platforms:** bioRxiv, medRxiv, SSRN

### 4.2 Search Syntax & Boolean Logic
Searches combined controlled vocabulary (MeSH where applicable) and extensive free-text keyword variants:

```text
# Query 1: PSTi8 Drug-Specific
("PSTi8" OR "PST-i8" OR "pancreastatin inhibitor" OR "pancreastatin inhibitory peptide" OR "PEGKGEQEHSQQKEEEEEMAV")

# Query 2: Target-Engagement & Signaling Pathway
("pancreastatin" OR "CHGA" OR "chromogranin A") AND ("GRP78" OR "HSPA5" OR "BiP" OR "glucose-regulated protein 78")

# Query 3: Biological Sex & Endocrine Dimorphism
("pancreastatin" OR "PSTi8") AND ("sex differences" OR "sexual dimorphism" OR "sex as a biological variable" OR "female" OR "estrous" OR "ovariectomy" OR "dimorphism")
```

### 4.3 Search Verification & Screening Gate
All search results were imported into a unified screening environment. Per the project's verification protocol, candidate records were authenticated via direct REST API queries to PubMed and Crossref before permanent indexing in [`data/papers_registry.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/papers_registry.csv).

---

## 5. Eligibility Criteria (PICO Framework)

Eligibility criteria were prospectively established following the PICO (Population, Intervention, Comparator, Outcome) structure tailored for preclinical animal research:

| Component | Inclusion Criteria | Exclusion Criteria |
| :--- | :--- | :--- |
| **Population (P)** | Non-human mammalian in vivo animal models (mice, rats) of any strain, age, or sex subjected to metabolic, inflammatory, hormonal, or physiological interventions. | Exclusively *in vitro* or *in silico* studies lacking in vivo animal cohorts; non-mammalian organisms; human clinical trials. |
| **Intervention (I)** | Exogenous administration of synthetic peptide **PSTi8** (`PEGKGEQEHSQQKEEEEEMAV-NH2`) by any route (i.p., s.c., i.v., osmotic pump, intrarectal) at any dose or duration. | Endogenous PST without inhibitor; non-peptide small molecules; unrelated chromogranin peptides (e.g., catestatin, vasostatin). |
| **Comparator (C)** | Concurrent vehicle control (saline, PBS, vehicle buffer), sham-operated animals, untreated disease controls, or active reference standards (e.g., metformin). | Studies without a concurrent control or comparator cohort. |
| **Outcomes (O)** | Quantitative measurement of metabolic parameters (glycemia, insulin, GTT/ITT, HbA1c), inflammatory/histological indices (cytokines, macrophage markers, histology), or pharmacokinetics ($C_{\max}$, AUC, $t_{1/2}$). Methodological outcomes: sex reporting, estrous tracking, statistical interaction testing. | Purely descriptive reports lacking quantitative physiological, biochemical, or histological endpoints. |
| **Study Design** | Controlled comparative in vivo experimental studies (peer-reviewed journal articles, conference abstract supplements, preprints). | Narrative reviews, editorials, commentaries, study protocols without data, patents. |

---

## 6. Study Selection & Data Extraction

### 6.1 Dual Independent Screening Procedure
A two-stage screening protocol is implemented to minimize reviewer bias:
1. **Stage 1 (Title/Abstract Screening):** Screener 1 (computational text-mining pipeline and primary reviewer) and Screener 2 (independent secondary reviewer) independently assess all identified bibliographic records against inclusion criteria.
2. **Stage 2 (Full-Text Eligibility):** Full text is retrieved for all potentially eligible records. Where full text is paywalled, records are audited from publisher abstracts and open metadata under strict provenance labeling.
3. **Tracking & Discrepancy Reconciliation:** Screening decisions and extracted data are recorded in [`data/dual_screening_audit.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/dual_screening_audit.csv). Inter-screener discrepancies are documented and adjudicated by consensus; persistent disagreements are referred to an independent third adjudicator.

### 6.2 Data Extraction Items & Provenance Rules
Data are extracted using a standardized data dictionary ([`docs/schema.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/schema.md)) capturing:
- **Bibliographic Data:** Paper ID, DOI, first author, publication year, journal citation, access status (`full` vs `abstract`).
- **Animal Model:** Species, strain, age, weight, disease model, induction protocol.
- **Sex Representation:** Male included (`yes`/`no`), Female included (`yes`/`no`), Provenance of sex (`full_text`, `abstract`, `inferred_from_model`, `NOT_READ`).
- **Sample Size:** Number of animals per group ($n$).
- **Intervention Regimen:** Dose, route of administration, frequency, treatment duration.
- **Estrous Cycle Reporting:** Baseline estrous staging (`yes`, `no`, `not_applicable`, `NOT_READ`), longitudinal monitoring as an outcome.
- **Statistical Methods:** Tests utilized, multiple testing corrections, factorial interaction testing status (`confirmed_absent`, `unreported`, `not_applicable`).
- **Key Outcomes:** Primary biochemical, physiological, and histological endpoints; author-stated conclusion.
- **Locators:** Exact section, table, or figure numbers in the primary source document.

> [!IMPORTANT]
> **Strict Provenance Rule:** Data fields must never be populated from unverified memory or external MeSH indexing. If a parameter is not explicitly disclosed in the primary text or abstract, it is strictly recorded as `NOT_READ`.

---

## 7. Methodological Quality & Risk of Bias Appraisal

### 7.1 SYRCLE Risk of Bias Tool for Animal Studies
Each included primary study is formally evaluated across the 10 domains of the Systematic Review Centre for Laboratory animal Experimentation (**SYRCLE**) tool:
1. **Sequence generation** (selection bias)
2. **Baseline characteristics** (selection bias)
3. **Allocation concealment** (selection bias)
4. **Random housing** (performance bias)
5. **Caregiver / investigator blinding** (performance bias)
6. **Random outcome assessment** (detection bias)
7. **Outcome assessor blinding** (detection bias)
8. **Incomplete outcome data** (attrition bias)
9. **Selective outcome reporting** (reporting bias)
10. **Other sources of bias** (e.g., unit-of-analysis errors, purity/synthesis reporting)

Each item is categorized as **Low Risk**, **High Risk**, or **Unclear / Unreported**.

### 7.2 ARRIVE 2.0 Essential 10 Compliance
Methodological transparency is quantitatively assessed using the **ARRIVE 2.0 Essential 10** criteria:
1. Study design
2. Sample size determination
3. Inclusion and exclusion criteria
4. Randomization
5. Blinding
6. Outcome measures
7. Statistical methods
8. Experimental animals (species, strain, sex, developmental stage)
9. Experimental procedures
10. Results / estimation

Compliance is scored on a standardized 0–10 scale in [`data/syrcle_arrive_matrix.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/syrcle_arrive_matrix.csv) via [`scripts/generate_syrcle_arrive_matrix.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/generate_syrcle_arrive_matrix.py).

---

## 8. Quantitative Synthesis & Statistical Modeling

### 8.1 Descriptive Reporting Proportions
Categorical parameters are summarized using frequency counts and exact percentages with 95% Clopper-Pearson binomial confidence intervals:
- Proportion of male-only, female-only, dual-sex, and sex-unreported studies.
- Proportion of studies adhering to blinding, randomization sequence generation, and sample size power calculations.
- Proportion of dual-sex studies conducting factorial interaction tests versus stratified subgroup analyses.

### 8.2 Factorial Interaction Contrast Modeling ($2 \times 2$ ANOVA)
To evaluate the mathematical validity of preclinical claims regarding sexual dimorphism, studies enrolling both sexes must evaluate the formal two-way factorial interaction between sex and drug treatment:

$$\text{Model: } Y_{ijk} = \mu + \alpha_i (\text{Sex}) + \beta_j (\text{Treatment}) + (\alpha\beta)_{ij} (\text{Sex} \times \text{Treatment}) + \epsilon_{ijk}$$

The interaction contrast $\Delta_{\text{int}}$ evaluates whether drug efficacy in males differs from drug efficacy in females:

$$\Delta_{\text{int}} = (\mu_{\text{Male, PSTi8}} - \mu_{\text{Male, Vehicle}}) - (\mu_{\text{Female, PSTi8}} - \mu_{\text{Female, Vehicle}})$$

Under balanced cell size $n$ per group, the standard error of the interaction contrast is:

$$SE_{\text{int}} = \sigma \sqrt{\frac{1}{n} + \frac{1}{n} + \frac{1}{n} + \frac{1}{n}} = \frac{2\sigma}{\sqrt{n}}$$

### 8.3 Non-Central $t$ Statistical Power Modeling
Statistical power to detect a true $\text{Sex} \times \text{Treatment}$ interaction effect is calculated using the non-central $t$-distribution with degrees of freedom $df = 4(n - 1)$:

$$\text{Power} = 1 - \beta = 1 - F_{t}(t_{\text{crit}}, df, \delta) + F_{t}(-t_{\text{crit}}, df, \delta)$$

where $t_{\text{crit}} = t_{1 - \alpha/2, df}$ at two-sided $\alpha = 0.05$, and the non-centrality parameter $\delta$ is:

$$\delta = \frac{\Delta_{\text{int}}}{SE_{\text{int}}} = \frac{d_{\text{int}} \cdot \sigma}{\frac{2\sigma}{\sqrt{n}}} = d_{\text{int}} \frac{\sqrt{n}}{2}$$

Power simulations across 33 distinct parametric scenarios ($n = 4$ to $30$ per sex; effect sizes $d_{\text{int}} = 0.3, 0.5, 0.8, 1.0, 1.2$) are modeled in [`scripts/analyze_sequences_and_pathways.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/analyze_sequences_and_pathways.py) and cataloged in [`data/power_results.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/power_results.csv).

---

## 9. In Silico Structural Biology & Biophysical Methods

### 9.1 Quaternary AlphaFold 3 Co-Folding Architecture
Quaternary complexes of full-length mature human GRP78 (UniProt P11021 coordinates 19–654, mature residues 1–636) are modeled using the **AlphaFold 3 Server** under physiological cofactor constraints:
1. **Receptor Chain:** Intact mature GRP78 containing N-terminal extension (19–25), NBD (26–407), Interdomain Linker (408–426), $\text{SBD}\beta$ (427–537), $\text{SBD}\alpha$ (538–633), and C-terminal tail (634–654).
2. **Cofactors:** ATP and divalent magnesium ion ($\text{Mg}^{2+}$) positioned in the catalytic nucleotide cleft.
3. **Peptide Ligands:**
   - **PSTi8 (21-mer):** `PEGKGEQEHSQQKEEEEEMAV-NH2`
   - **Wild-Type PST-29 (29-mer):** `PEGKGEQEHSQQKEEEEEMAVVPQGLFRG-NH2`
   - **Glu287Lys (rs140089514, mature E15K):** Coding variant in helical core.
   - **Gly297Ser (rs9658664, mature G25S):** Diabetogenic coding variant in C-terminal anchor.
4. **Diffusion Sampling Protocol:** AlphaFold 3 Server runs executed with `modelSeeds: [1]`, generating **5 diffusion samples per complex** (20 total model evaluations across 4 complexes).
5. **Confidence Metrics:** Multi-sample ranking score, global ipTM, pTM, pairwise peptide-receptor ipTM ($\text{ipTM}_{\text{AB}}$), and minimum inter-chain predicted aligned error ($\text{min PAE}_{\text{AB}}$), compiled in [`data/structures/3d_models/af3_complex_metrics.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/af3_complex_metrics.csv).
6. **Interface Contact Profiling:** Atomic contact extraction at a heavy-atom Euclidean distance threshold $< 4.0\ \text{Å}$, mapped to canonical UniProt P11021 numbering (+18 crystallographic offset) in [`data/structures/3d_models/af3_interface_contacts.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/af3_interface_contacts.csv).

### 9.2 Deep Mutational Scanning (ESM-2) & Language Model Scoring
Zero-shot variant impact is evaluated using the 650-million-parameter evolutionary scale protein language model `esm2_t33_650M_UR50D`. For every position $i$ along the 29-residue sequence and each of the 20 standard amino acids $x$, the log-likelihood ratio (LLR) score is computed:

$$\text{LLR}(i, x) = \log P(\text{residue}_i = x \mid \text{sequence}) - \log P(\text{residue}_i = \text{WT}_i \mid \text{sequence})$$

Yielding a full 580-point deep mutational matrix in [`data/structures/1d_sequences/variant_scores.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/1d_sequences/variant_scores.csv).

### 9.3 Sliding-Window Physicochemical Profiling
Electrostatic net charge at pH 7.4 (Lehninger pKa scale) and Kyte-Doolittle hydropathy are computed using a sliding window of size $W = 5$ residues (step size = 1) across human, mouse, and rat PST sequences in [`scripts/analyze_sequences_and_pathways.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/analyze_sequences_and_pathways.py).

### 9.4 Prioritized In Silico Control Experiments (TODO Roadmap)
To independently stress-test the AF3 structural predictions, a prioritized suite of in silico controls is established:
1. **Isolated NBD Control:** Co-folding PSTi8 against NBD-only (residues 26–407) in apo and ADP-bound states to isolate domain-specific affinity.
2. **Scrambled PSTi8 Control:** Co-folding a scrambled 21-mer sequence with identical amino acid composition to verify sequence specificity.
3. **Random 21-mer Controls:** Two independent randomly generated 21-mers to establish baseline non-specific peptide binding noise.
4. **Positive Peptide Control:** Co-folding the known GRP78-binding peptide `HWDFAWPW` into the canonical $\text{SBD}\beta$ pocket.
5. **PSTi8-E15K Mutant:** Co-folding PSTi8 bearing the Lys15 charge-inversion variant.
6. **Multi-Seed Diffusion Sampling:** Evaluating seed sensitivity across 5 independent random model seeds (`modelSeeds: [1, 2, 3, 4, 5]`).
7. **Orthogonal Validation:** Cross-platform co-folding using Boltz-2 and Chai-1 deep-learning engines.

---

## 10. Dissemination & Reporting Plan

- **Reporting Guidelines:** The completed systematic review will adhere to the **PRISMA 2020** statement (Preferred Reporting Items for Systematic Reviews and Meta-Analyses) and the **PRISMA-S** extension for literature searches.
- **Publication Venue:** Peer-reviewed submission to *Biology of Sex Differences* (Springer Nature).
- **Public Data Sharing:** All raw API outputs, extraction sheets, analysis scripts, 3D structures, and publication-ready figures are maintained in open, version-controlled git repositories under CC BY 4.0.

---

## 11. Protocol References

1. Shamseer L, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: elaboration and explanation. *BMJ*. 2015;350:g7647.
2. Hooijmans CR, et al. SYRCLE's risk of bias tool for animal studies. *BMC Med Res Methodol*. 2014;14:43.
3. Percie du Sert N, et al. The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biol*. 2020;18(7):e3000410.
4. Clayton JA, Collins FS. Policy: NIH to balance sex in cell and animal studies. *Nature*. 2014;509(7500):282-283.
5. Hossain Z, et al. Discovery of pancreastatin inhibitor PSTi8 for the treatment of insulin resistance and diabetes. *Sci Rep*. 2018;8(1):8814.
6. Abramson J, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*. 2024;630:493-500.
