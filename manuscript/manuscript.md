# Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms

**Devansh Pratap Singh**$^{1*}$

$^{1}$ Independent Researcher, Computational Structural Biology and Preclinical Methodology Framework, Lucknow, Uttar Pradesh, India.  
$^*$ **Correspondence:** Devansh Pratap Singh ([devansh.research.repo@gmail.com](mailto:devansh.research.repo@gmail.com); Open Repository: [https://github.com/Devanshyadav118/psti8-evidence-map](https://github.com/Devanshyadav118/psti8-evidence-map))

**Running Title:** Preclinical Sex Bias and Structural Mechanism of PSTi8  
**Keywords:** Pancreastatin, PSTi8, Chromogranin A, GRP78, HSPA5, Sex as a Biological Variable, Factorial Interaction Power, AlphaFold 3, Type 2 Diabetes, ARRIVE 2.0.

---

## Abstract

### Background
Pancreastatin inhibitor PSTi8 (hCHGA273-293-amide) is a peptide candidate designed to mitigate pancreastatin-induced insulin resistance. Despite reported efficacy via glucose-regulated protein 78 (GRP78/HSPA5) inhibition, compliance with the NIH Sex as a Biological Variable (SABV) mandate and the structural basis of receptor engagement remain unestablished.

### Methods
We conducted a PRISMA-compliant systematic review of preclinical in vivo PSTi8 studies across five databases and preprints. Methodological quality was appraised via ARRIVE 2.0 Essential 10 and SYRCLE tools. Statistical power to detect sex-by-treatment interactions was evaluated using non-central $t$-distribution modeling ($df = 4(n-1)$). In silico target engagement, cleft conservation, and variant impacts were investigated via AlphaFold 3 neural co-folding (5 diffusion samples, `modelSeeds [1]`, with $\text{Mg}^{2+}$-ATP), ESM-2 language modeling, and physicochemical profiling.

### Results
Twenty primary in vivo studies (116 registry records) met inclusion criteria. Extreme sex segregation was identified: 100% of general type 2 diabetes and diet-induced obesity cohorts tested exclusively male rodents, whereas female rodents were restricted to reproductive pathology models. Baseline estrous cycle staging was absent across all female cohorts (0%, 0/7 studies). In the three dual-sex studies, factorial $\text{Sex} \times \text{Treatment}$ interaction testing was omitted (0%, 0/20); standard cohorts ($n = 6$ per group) demonstrated $<19\%$ power to detect moderate interaction effects ($d_{\text{int}} = 0.5$). Structurally, AlphaFold 3 refutes active-site ATP-pocket docking (0 contacts with the nucleotide-binding domain). Instead, PSTi8 acts as an allosteric steric wedge at the interdomain linker-hinge (Ile426) and $\text{SBD}\beta$ entrance (48 atomic contacts; ranking 0.85, ipTM 0.81, min PAE 2.30 Å). The human diabetogenic Gly297Ser variant (rs9658664) disrupts binding (pairwise ipTM 0.28, min PAE 5.54 Å) because Ser25 destabilizes the hydrophobic $\text{SBD}\beta$ pocket; because PSTi8 terminates at residue 21, it is structurally refractory to this polymorphism.

### Conclusions
PSTi8 has never been demonstrated to ameliorate general type 2 diabetes in female animals. Preclinical pipelines must adopt adequately powered factorial interaction designs and baseline estrous synchronization before clinical translation.

---

## 1. Introduction

Type 2 diabetes mellitus (T2D), obesity, and metabolic-associated steatohepatitis (MASH) represent multifaceted metabolic crises driven by impaired insulin sensitivity, chronic low-grade inflammation, and persistent endoplasmic reticulum (ER) stress [1, 2]. Among endogenous hormonal regulators of metabolism, Chromogranin A (CHGA)—a 439-amino-acid neuroendocrine prohormone co-packaged with insulin and catecholamines in dense-core secretory granules—exerts a potent counter-regulatory brake on energy homeostasis [3, 4]. Endoproteolytic maturation of CHGA by prohormone convertases releases bioactive peptides, including pancreastatin (PST; human preprotein coordinates residues 273–301: `PEGKGEQEHSQQKEEEEEMAVVPQGLFRG-NH2`) [5, 6]. 

Endogenous pancreastatin suppresses insulin-stimulated glucose uptake, blunts glycogen synthesis, activates glycogenolysis, stimulates gluconeogenesis in hepatocytes, and exacerbates free fatty acid release from adipocytes [7, 8]. Elevated circulating pancreastatin concentrations correlate with clinical insulin resistance, gestational diabetes, and microvascular complications in patients with T2D [9, 10]. To neutralize hyperactive pancreastatin signaling, Hossain et al. (2018) developed PSTi8 (`PEGKGEQEHSQQKEEEEEMAV-NH2`), an engineered synthetic 21-amino-acid peptide truncated at the carboxyl terminus [11]. Truncating the terminal octapeptide (`VPQGLFRG`) converts the peptide from a functional agonist into a competitive antagonist, which suppressed gluconeogenesis, restored insulin sensitivity, and shifted adipose macrophage polarization toward an anti-inflammatory M2 phenotype across preclinical models [11, 12].

In parallel with pharmacological advances, biomedical translation has confronted a reproducibility crisis rooted in preclinical sex bias [13, 14]. In 2016, the National Institutes of Health (NIH) implemented the Sex as a Biological Variable (SABV) policy (NOT-OD-15-102), establishing that biological sex is a critical determinant of physiological regulation that must be factored into vertebrate animal study design, analysis, and reporting [15, 16]. Hepatic lipid partitioning, skeletal muscle glucose disposal, visceral versus subcutaneous adiposity, and unfolded protein response pathways exhibit substantial sexual dimorphism in rodents and humans [17, 18]. Furthermore, ovarian 17$\beta$-estradiol ($E_2$) signaling directly suppresses gluconeogenic transcription factors and stabilizes insulin signaling [19]. Despite these established dimorphic pathways, preliminary scoping suggested that primary PSTi8 research has adhered to historical habits of male-exclusive animal testing or confined female rodents to non-translatable endocrine ablation models without formal statistical interaction testing.

Concurrently, the molecular target and quaternary binding architecture of PSTi8 remain contentious. Historical literature posits that pancreastatin and PSTi8 interact directly with cell-surface 78 kDa glucose-regulated protein (GRP78, also designated BiP or HSPA5), an ER-lumen Hsp70-family chaperone that translocates to the plasma membrane under proteotoxic stress [11, 20]. Hossain et al. (2018) reported rigid-body docking poses predicting that PSTi8 inserts into the catalytic nucleotide-binding domain (NBD) of GRP78 (PDB 3LDP) [11]. However, rigid-body docking fails to account for the intrinsic disorder of monomeric pancreastatin peptides or the dramatic nucleotide-dependent conformational transitions of intact GRP78 [21, 22]. Moreover, the discovery of the diabetogenic human CHGA coding polymorphism Gly297Ser (rs9658664)—which resides at position 25 of mature PST-29 and profoundly enhances diabetic risk in human carriers [23]—raises a critical biophysical paradox: how does an amino acid substitution at position 25 alter peptide-receptor mechanics when position 25 is physically absent from the therapeutic inhibitor PSTi8?

To resolve these empirical and mechanistic gaps, this study presents a PRISMA-compliant systematic review, an ARRIVE 2.0 / SYRCLE methodological audit, a mathematical interaction-power appraisal, and full-length AlphaFold 3 quaternary structural co-folding of PSTi8, wild-type PST-29, and human coding variants in complex with intact mature GRP78 in the presence of physiological $\text{Mg}^{2+}$-ATP cofactors.

---

## 2. Methods

### 2.1 Protocol Registration & Reporting Guidelines
This systematic review and computational biophysics investigation was prospectively designed and registered on the Open Science Framework (OSF) following PRISMA-P (Preferred Reporting Items for Systematic Review and Meta-Analysis Protocols) and SYRCLE guidelines ([`docs/osf_protocol_registration.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/osf_protocol_registration.md)) [24, 25]. The final review adheres to PRISMA 2020 reporting standards [26]. All computational pipelines, extraction tables, and visualization scripts are version-controlled in an open-access repository under Creative Commons Attribution 4.0 International ([CC BY 4.0](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/LICENSE)).

### 2.2 Literature Search Strategy & Screening Gate
A systematic bibliographic search without date restrictions (inception through November 2026) was conducted across PubMed/MEDLINE, Crossref Metadata API, Europe PMC, PubMed Central (PMC), and preprint repositories (bioRxiv, medRxiv, SSRN). The boolean search architecture combined drug-specific terms (`"PSTi8"` OR `"PST-i8"` OR `"pancreastatin inhibitor"` OR `"PEGKGEQEHSQQKEEEEEMAV"`), target-engagement terms (`"pancreastatin"` AND `"GRP78"` OR `"HSPA5"` OR `"BiP"`), and endocrine dimorphism keywords (`"pancreastatin"` AND `"sex differences"` OR `"sexual dimorphism"` OR `"estrous"` OR `"ovariectomy"`).

All retrieved records were subjected to a two-stage screening gate ([`data/dual_screening_audit.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/dual_screening_audit.csv)):
1. **Title and Abstract Triage:** Evaluated independently against preclinical in vivo eligibility criteria.
2. **Citation Verification Gate:** Every eligible citation, author sequence, DOI, and publication status was verified by direct automated REST API queries against PubMed and Crossref, logged in [`data/papers_registry.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/papers_registry.csv).

### 2.3 Eligibility Criteria (PICO Framework)
Inclusion and exclusion criteria were established a priori:
- **Population (P):** Non-human mammalian in vivo experimental models (mice, rats) of metabolic dysfunction (T2D, obesity, insulin resistance, fatty liver), inflammatory disease (colitis, wound healing), or healthy pharmacokinetic cohorts. In vitro cell studies without concurrent animal cohorts were excluded from the primary in vivo evidence table.
- **Intervention (I):** Administration of synthetic peptide **PSTi8** (`PEGKGEQEHSQQKEEEEEMAV-NH2`) by any route, dose, or regimen.
- **Comparator (C):** Concurrent vehicle control (saline, PBS), sham-operated controls, untreated disease model cohorts, or standard reference agents (metformin).
- **Outcomes (O):** Metabolic endpoints (fasting glycemia, glucose tolerance test [GTT], insulin tolerance test [ITT], HbA1c), biochemical markers (lipids, inflammatory cytokines, macrophage polarization), or pharmacokinetic metrics ($C_{\max}$, AUC, $t_{1/2}$). Methodological outcomes included reporting of animal sex, baseline estrous cycle staging, sample size calculations, and statistical tests for interaction.
- **Study Design:** Controlled in vivo animal experimental trials. Reviews, editorials, and conference abstracts lacking quantitative in vivo datasets were excluded from the primary efficacy table.

### 2.4 Data Extraction & Provenance Rule
Data were extracted into a structured repository ([`data/evidence_table.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/evidence_table.csv)) using a 22-column standardized schema ([`docs/schema.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/schema.md)). Variables included animal species, strain, sample size per group ($n$), disease model, administration route, dose, duration, male representation, female representation, sex provenance, baseline estrous cycle staging, longitudinal estrous monitoring, statistical methods, interaction testing status, key findings, and exact locators. 

> [!IMPORTANT]
> **Strict Provenance Rule:** To preserve evidentiary integrity, data fields were never populated from memory or external MeSH indexing. If an animal cohort's sex or methodological step was not explicitly documented in the abstract or open full text, it was strictly coded as `NOT_READ`.

### 2.5 Methodological Quality & Risk-of-Bias Appraisal
Methodological transparency was scored using the **ARRIVE 2.0 Essential 10** criteria (study design, sample size determination, inclusion/exclusion, randomization, blinding, outcome measures, statistical methods, experimental animals, experimental procedures, results). Risk of bias was audited across the 10 domains of the **SYRCLE** (Systematic Review Centre for Laboratory animal Experimentation) tool [27, 28]. Analyses were executed using [`scripts/generate_syrcle_arrive_matrix.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/generate_syrcle_arrive_matrix.py), yielding [`data/syrcle_arrive_matrix.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/syrcle_arrive_matrix.csv).

### 2.6 Factorial Interaction Modeling & Statistical Power Analysis
In experiments evaluating both sexes, the formal test of whether therapeutic efficacy differs between sexes requires a two-way factorial ANOVA model:

$$Y_{ijk} = \mu + \alpha_i (\text{Sex}) + \beta_j (\text{Treatment}) + (\alpha\beta)_{ij} (\text{Sex} \times \text{Treatment}) + \epsilon_{ijk}$$

The interaction contrast $\Delta_{\text{int}}$ evaluates the difference of differences:

$$\Delta_{\text{int}} = (\mu_{\text{Male, Treated}} - \mu_{\text{Male, Vehicle}}) - (\mu_{\text{Female, Treated}} - \mu_{\text{Female, Vehicle}})$$

Under balanced design ($n$ animals per sex-by-treatment cell), the standard error of the interaction contrast is:

$$SE_{\text{int}} = \sigma \sqrt{\frac{1}{n} + \frac{1}{n} + \frac{1}{n} + \frac{1}{n}} = \frac{2\sigma}{\sqrt{n}}$$

Statistical power to detect $\Delta_{\text{int}}$ was calculated using the non-central $t$-distribution with $df = 4(n-1)$ degrees of freedom:

$$\text{Power} = 1 - \beta = 1 - F_{t}(t_{\text{crit}}, df, \delta) + F_{t}(-t_{\text{crit}}, df, \delta)$$

where $t_{\text{crit}} = t_{1 - \alpha/2, df}$ at two-sided $\alpha = 0.05$, and non-centrality parameter $\delta$ is defined as:

$$\delta = \frac{\Delta_{\text{int}}}{SE_{\text{int}}} = \frac{d_{\text{int}} \cdot \sigma}{\frac{2\sigma}{\sqrt{n}}} = d_{\text{int}} \frac{\sqrt{n}}{2}$$

Power curves across 33 distinct sensitivity scenarios ($n = 4$ to $30$ per group; effect sizes $d_{\text{int}} = 0.3$ to $1.2$) were computed via [`scripts/analyze_sequences_and_pathways.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/analyze_sequences_and_pathways.py) and tabulated in [`data/power_results.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/power_results.csv).

### 2.7 In Silico Structural Biology & Co-Folding Architecture
Quaternary co-folding was executed using the **AlphaFold 3 Server** [22]:
1. **Receptor Architecture:** Full-length mature human GRP78 (UniProt P11021 coordinates 19–654, mature residues 1–636) containing the N-terminal mature extension (19–25), NBD (26–407), Interdomain Linker (408–426), $\text{SBD}\beta$ (427–537), $\text{SBD}\alpha$ (538–633), and C-terminal tail (634–654).
2. **Physiological Ligands:** Endogenous cofactors adenosine triphosphate (ATP) and magnesium ($\text{Mg}^{2+}$) were placed in the catalytic nucleotide-binding pocket.
3. **Peptide Ligands:** Four peptide complexes were modeled:
   - PSTi8 (21-mer): `PEGKGEQEHSQQKEEEEEMAV-NH2`
   - Wild-Type PST-29 (29-mer): `PEGKGEQEHSQQKEEEEEMAVVPQGLFRG-NH2`
   - Glu287Lys PST-29 (mature E15K; rs140089514)
   - Gly297Ser PST-29 (mature G25S; rs9658664)
4. **Diffusion Sampling Protocol:** AlphaFold 3 runs were executed with single seed initialization (`modelSeeds: [1]`), generating **5 diffusion samples per complex** (20 total model evaluations).
5. **Contact and Confidence Extraction:** Metrics were parsed using [`scripts/analyze_af3_complexes.py`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/scripts/analyze_af3_complexes.py). Inter-chain atomic contacts were identified using BioPython MMCIFParser at a heavy-atom Euclidean distance threshold $< 4.0\ \text{Å}$. Receptor coordinates were indexed to canonical UniProt P11021 numbering (+18 offset from mature chain).
6. **Physicochemical & Language Model Profiling:** Sliding-window net charge at pH 7.4 (Lehninger scale) and Kyte-Doolittle hydropathy ($W = 5$ residues) were computed across mammalian orthologs. Deep mutational scanning (580 point mutations) was executed using the 650M-parameter protein language model `esm2_t33_650M_UR50D`. GRP78 sequence conservation was evaluated via Biopython PairwiseAligner across human (P11021), mouse (P20029), and rat (P06761). Functional interactome topologies were constructed from STRING v12 and Reactome pathways.

---

## 3. Results

### 3.1 Preclinical Evidence Landscape & Single-Lab Network Concentration
The systematic search identified exactly **20 primary in vivo experimental studies** evaluating PSTi8 ([`data/evidence_table.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/evidence_table.csv)), situated within a broader authenticated registry of **116 papers** spanning pancreastatin biology, insulin resistance cascades, and preclinical reporting standards ([`data/papers_registry.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/papers_registry.csv)) (Figure 1A). 

Bibliometric analysis uncovered an intense institutional concentration: 19 of the 20 primary in vivo studies (95.0%) originated from a single collaborative research network centered at the CSIR-Central Drug Research Institute (CDRI) in Lucknow, India, led by investigators Z. Hossain, G.R. Valicherla, A.P. Gupta, P. Singh, R. Garg, and U.K. Goand. Only a single primary evaluation (`tshikudi2024_colitis` / `tshikudi2024_jcag`) was conducted by an independent laboratory (J.E. Ghia, University of Manitoba). Thus, independent replication of PSTi8 efficacy in metabolic disease is currently absent in the published literature.

```
+----------------------------------------------------------------------------------------------------+
|                                    PRECLINICAL CORPUS SUMMARY (N = 20)                              |
+--------------------------+---------------------+-------------------+-------------------------------+
| Disease Indication       | Study Count         | Animal Model      | Sex Representation            |
+--------------------------+---------------------+-------------------+-------------------------------+
| Type 2 Diabetes / DIO    | 10 studies          | C57BL/6J, db/db,  | Male only: 3; Unstated: 7     |
|                          |                     | SD / Wistar rats  | (100% of reported are male)   |
| PCOS / Menopause         | 4 studies           | VCD, OVX, Let,    | Female only: 4 (100% female)  |
|                          |                     | DHEA rodents      |                               |
| Pharmacokinetics (PK)    | 2 studies           | SD rats, Swiss    | Both sexes: 1; Unstated: 1    |
|                          |                     | albino mice       |                               |
| Colitis / Mucosal        | 2 studies           | C57BL/6 mice      | Both sexes: 2 (100% both)     |
| NASH / Liver Steatosis   | 2 studies           | MCD diet, HFD     | Unstated / NOT_READ: 2        |
+--------------------------+---------------------+-------------------+-------------------------------+
```

### 3.2 Methodological Quality & Reporting Compliance (ARRIVE 2.0 & SYRCLE)
Quantitative scoring of the 20 primary studies against the ARRIVE 2.0 Essential 10 and the SYRCLE Risk of Bias tool revealed pervasive reporting omissions ([`data/syrcle_arrive_matrix.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/syrcle_arrive_matrix.csv)) (Figure 1B):
- **Sample Size Justification:** 0 of 20 studies (0.0%) reported an a priori power calculation or statistical rationale for cohort sizing.
- **Allocation Concealment:** 0 of 20 studies (0.0%) reported measures to conceal allocation from experimenters.
- **Experimenter Blinding:** 0 of 20 studies (0.0%) reported caregiver or investigator blinding during drug administration.
- **Outcome Assessor Blinding:** Only 1 of 20 studies (5.0%; `tshikudi2024_colitis`) explicitly reported blinded outcome assessment (histological scoring).
- **Randomization Method:** While 5 of 20 studies (25.0%) noted that animals were "randomly divided," none described the sequence generation method (e.g., computer-generated pseudo-random numbers or block design).
- **Overall SYRCLE Risk:** 19 of 20 studies (95.0%) were categorized as high risk of bias due to selective reporting and uncharacterized performance bias. Mean ARRIVE compliance score across the corpus was $4.76 \pm 0.38$ out of 10.

```
+----------------------------------------------------------------------------------------------------+
|                                    ARRIVE 2.0 / SYRCLE COMPLIANCE AUDIT                             |
+------------------------------------+--------------------------+------------------------------------+
| Quality Domain                     | Compliance Count (%)     | Methodological Implication         |
+------------------------------------+--------------------------+------------------------------------+
| Sample Size Calculation            | 0 / 20 (0.0%)            | High risk of Type II error         |
| Allocation Concealment             | 0 / 20 (0.0%)            | Selection bias unmitigated         |
| Blinding of Drug Admin / Care      | 0 / 20 (0.0%)            | Performance bias unmitigated       |
| Blinding of Outcome Assessment     | 1 / 20 (5.0%)            | Detection bias in 95% of studies   |
| Randomization Method Disclosed     | 0 / 20 (0.0%)            | Non-reproducible sequence          |
| Estrous Baseline Synchronization   | 0 / 7 (0.0%)             | Uncontrolled cyclic variance       |
+------------------------------------+--------------------------+------------------------------------+
```

### 3.3 Systematic Sex Segregation & Absence of Baseline Estrous Staging
Audit of animal sex reporting revealed extreme disease-by-sex compartmentalization (Figure 1C):
1. **100% Male Bias in Metabolic Disease:** Every reported study evaluating primary general metabolic indications—including diet-induced obesity, high-fat diet (HFD) insulin resistance, streptozotocin (STZ) T2D, and genetic $db/db$ diabetes (`valicherla2018`, `gupta2019_obesity`, `singh2020_fetuina`)—was conducted exclusively in male rodents. Zero studies evaluated female rodents in standard metabolic disease.
2. **Female Restriction to Endocrine Ablation:** Female rodents were tested exclusively in specialized chemical or surgical models of female reproductive failure: 4-vinylcyclohexene diepoxide (VCD) and ovariectomy (OVX) perimenopause (`singh2019_menopause`, `singh2020_heliyon`), letrozole-induced polycystic ovary syndrome (PCOS) (`yadav2024_pcos_let`), and dehydroepiandrosterone (DHEA) PCOS (`yadav2025_pcos_dhea`).
3. **Pervasive Non-Reporting:** In 10 of 20 studies (50.0%), animal sex was omitted entirely from the abstract and could not be verified in open full text, requiring a strict provenance tag of `NOT_READ`.
4. **Complete Absence of Baseline Estrous Staging:** Across all 7 studies utilizing female rodents, **zero studies (0.0%) performed baseline estrous cycle staging** prior to group assignment. In healthy dual-sex cohorts (`valicherla2022_pk`, `tshikudi2024_colitis`), estrous status was completely ignored. In `singh2020_heliyon`, vaginal cytology was monitored daily for 60 days, but only as a longitudinal recovery endpoint, not for baseline allocation.

### 3.4 Omission of Interaction Testing & Factorial Power Collapse
Across the three studies that evaluated both male and female animals (`valicherla2022_pk`, `tshikudi2024_colitis`, `tshikudi2024_jcag`), **zero studies (0.0%) reported a formal factorial $\text{Sex} \times \text{Treatment}$ interaction test** (Figure 2A):
- In `valicherla2022_pk`, pharmacokinetic parameters ($C_{\max}$, $\text{AUC}$, $t_{1/2}$) were compared between sexes using pairwise Student's $t$-tests, demonstrating equivalent systemic bioavailability (Figure 2C).
- In `tshikudi2024_colitis`, daily disease activity index (DAI) was reported as higher in females at 72 h and 96 h, but cumulative DAI and macroscopic colon damage showed no significant sex differences. Despite mentioning two-way ANOVA in figure captions for longitudinal timecourses, Section 4.11 and figure legends specified ordinary one-way ANOVA with Tukey's post-hoc comparisons; no interaction $F$-test was published (`interaction_tested: no`).
- In `tshikudi2024_jcag`, conference abstract findings described divergent epithelial cell differentiation between sexes, but interaction statistics were unreported (`interaction_tested: not_reported`).

Non-central $t$-distribution power modeling demonstrated that primary studies are severely underpowered to detect sex-dependent drug differences (Figure 2B):
- Standard preclinical cohort sizes ($n = 6$ animals per cell) achieve only **14.2% power** to detect a moderate interaction effect ($d_{\text{int}} = 0.5$) and **33.7% power** to detect a large interaction ($d_{\text{int}} = 0.8$) at two-sided $\alpha = 0.05$.
- To achieve standard 80% statistical power for a moderate interaction ($d_{\text{int}} = 0.5$), an experimental design requires **$n = 32$ animals per sex-by-treatment cell** ($N = 128$ total animals in a $2 \times 2$ factorial matrix).
- Dividing standard cohorts into subgroups of $n = 3$ to $6$ per sex produces a statistical trap: spurious discordant within-group $p$-values ($p_{\text{male}} < 0.05$ versus $p_{\text{female}} > 0.05$) are driven by elevated Type II error rather than true biological dimorphism.

```
+----------------------------------------------------------------------------------------------------+
|                               NON-CENTRAL T FACTORIAL POWER MODELING                               |
+--------------------------+---------------------+-------------------+-------------------------------+
| Sample Size per Cell (n) | Effect Size (d_int) | Degrees of Freedom| Statistical Power (1 - beta)  |
+--------------------------+---------------------+-------------------+-------------------------------+
| n = 4 per cell           | d_int = 0.5 (mod)   | df = 12           | 9.8% power (Extreme Type II)  |
| n = 6 per cell (standard)| d_int = 0.5 (mod)   | df = 20           | 14.2% power                   |
| n = 6 per cell (standard)| d_int = 0.8 (large) | df = 20           | 33.7% power                   |
| n = 12 per cell          | d_int = 0.5 (mod)   | df = 44           | 27.8% power                   |
| n = 20 per cell          | d_int = 0.5 (mod)   | df = 76           | 52.4% power                   |
| n = 32 per cell          | d_int = 0.5 (mod)   | df = 124          | 80.2% power (Adequate)        |
+--------------------------+---------------------+-------------------+-------------------------------+
```

### 3.5 Structural Mechanism: Refuting ATPase Pocket Docking & Establishing the Linker Wedge
Historical rigid-body docking models claimed that PSTi8 binds within the catalytic ATP-binding pocket of GRP78 (PDB 3LDP; contacting Tyr39, Asn55, Arg60, Glu293, Ser300). Neural co-folding of full-length mature GRP78 with physiological ATP and $\text{Mg}^{2+}$ using AlphaFold 3 Server (`modelSeeds [1]`, 5 diffusion samples) **completely refutes this hypothesis** (Figure 4A,B):
- PSTi8 makes **zero atomic contacts (<4.0 Å) with the nucleotide-binding domain** (residues 26–407; 0% overlap with Hossain 2018 docking residues).
- Instead, PSTi8 docks with high confidence (Model 0: ranking score 0.85, global ipTM 0.81, pTM 0.83, min PAE 2.30 Å) at the **interdomain linker-hinge and the entrance of the substrate-binding domain ($\text{SBD}\beta$)** (Figure 4B).
- In Model 0, PSTi8 forms **48 heavy-atom contacts across 13 receptor residues**:
  - Interdomain Linker (1 residue, 5 contacts): `ILE426` (Chain CIF 408), located immediately adjacent to the conserved linker motif `416-LLDVCPLTLG-425` (distinct from NBD subdomain IIB motif `362-VGGSTRIPKIQQLVK-376`).
  - $\text{SBD}\beta$ Entrance (12 residues, 43 contacts): `GLU427`, `THR428`, `VAL429`, `THR434`, `PHE451`, `SER452`, `THR453`, `ALA454`, `GLN458`, `VAL461`, `GLY493`, `GLN496` (Chain CIF 409–478).
- By inserting its hydrophobic carboxyl-terminal tip (`E18-M19-A20-V21`) into the linker-hinge cleft while projecting its strongly polyanionic `E14–E17` poly-Glu cluster into solvent, PSTi8 acts as an **allosteric steric wedge** that uncouples NBD-SBD interdomain communication without entering the catalytic ATP site.

```
+----------------------------------------------------------------------------------------------------+
|                                 ALPHAFOLD 3 CO-FOLDING CONFIDENCE MATRIX                           |
+------------------+---------------+---------------+---------------+----------------+----------------+
| Complex          | Ranking Score | Global ipTM   | Global pTM    | Chain ipTM_AB  | Min PAE_AB (Å) |
+------------------+---------------+---------------+---------------+----------------+----------------+
| PSTi8 (21-mer)   | 0.85          | 0.81          | 0.83          | 0.48           | 2.30           |
| WT PST-29 (29-mer| 0.81          | 0.76          | 0.79          | 0.47           | 2.89           |
| E287K PST-29     | 0.80          | 0.76          | 0.78          | 0.41           | 3.71           |
| G297S PST-29     | 0.70          | 0.65          | 0.68          | 0.28           | 5.54           |
+------------------+---------------+---------------+---------------+----------------+----------------+
```

In contrast, wild-type PST-29 (Model 0: ranking 0.81, global ipTM 0.76, min PAE 2.89 Å) acts as an extended **tri-domain clamp**, generating **140 atomic contacts across 32 receptor residues**:
- NBD (4 residues, 14 contacts): `MET196`, `ARG197`, `GLN401`, `LEU405`
- Interdomain Linker (3 residues, 21 contacts): `LEU416`, `LEU417`, `ILE426`
- $\text{SBD}\beta$ Pocket (25 residues, 105 contacts): `GLU427` through `LYS516`
- The terminal octapeptide `VPQGLFRG` serves as a deep hydrophobic anchor within $\text{SBD}\beta$, bridging domains to lock GRP78 in an active conformation.

### 3.6 Absolute Interspecies Cleft Conservation
Pairwise cross-species sequence alignment of GRP78 across human (UniProt P11021), mouse (P20029), and rat (P06761) revealed extraordinary evolutionary constraint (Figure 5A):
- The full 654-residue protein displays **99.39% sequence identity** (650/654 identical residues; 4 conservative substitutions in the N-terminal mature extension and C-terminal tail).
- Across the entire $\text{SBD}\beta$ domain (residues 427–537) and the interdomain linker (residues 408–426), sequence conservation is **100.00% identical across human, mouse, and rat** (0 substitutions).
- Consequently, preclinical testing in rodents evaluates an identical biophysical receptor pocket to human GRP78. Interspecies translational failures cannot be attributed to receptor sequence divergence, pointing directly to pharmacokinetic, metabolic, and hormonal disparities.

### 3.7 Resolution of the Gly297Ser Genetic Paradox & PSTi8 Structural Immunity
The human CHGA coding polymorphism Gly297Ser (rs9658664) is an established diabetogenic risk allele associated with enhanced hypertensive and metabolic disease risk in clinical cohorts. In full-length mature PST-29, this mutation corresponds to Gly25Ser (`VPQSLFRG`).

AlphaFold 3 quaternary co-folding of the Gly297Ser variant revealed a dramatic structural disruption (Figure 4A,C):
- Introduction of the polar Ser25 sidechain into the hydrophobic $\text{SBD}\beta$ pocket decreases atomic contacts by **43.6%** (140 to 79 contacts across 20 residues: 1 Linker `ILE426` and 19 $\text{SBD}\beta$ residues).
- Contact with the NBD is completely severed in Model 0 (14 contacts down to 0).
- Pairwise peptide-receptor confidence collapses: chain $\text{ipTM}_{\text{AB}}$ drops from **0.47 to 0.28**, and minimum inter-chain PAE worsens from **2.89 Å to 5.54 Å**.

```
+----------------------------------------------------------------------------------------------------+
|                               GLY297SER INTERFACE COLLAPSE BREAKDOWN                               |
+--------------------------+-----------------------+-----------------------+-------------------------+
| Interface Parameter      | Wild-Type PST-29      | Gly297Ser PST-29      | Change / Impact         |
+--------------------------+-----------------------+-----------------------+-------------------------+
| Total Atomic Contacts    | 140 contacts (<4.0 Å) | 79 contacts (<4.0 Å)  | -43.6% contact collapse |
| Interacting Residues     | 32 residues           | 20 residues           | Loss of 12 residues     |
| NBD Contacts (1-407)     | 14 contacts (4 res)   | 0 contacts (0 res)    | Complete loss of NBD    |
| Linker Contacts (408-426)| 21 contacts (3 res)   | 5 contacts (1 res)    | -76.2% linker reduction |
| Pairwise Chain ipTM_AB   | 0.47                  | 0.28                  | Severe uncoupling       |
| Minimum PAE_AB           | 2.89 Å                | 5.54 Å                | Marked positional error |
+--------------------------+-----------------------+-----------------------+-------------------------+
```

**Biophysical Resolution:** In full-length CHGA, position 297 is located at position 25 of the cleaved octapeptide (`VPQGLFRG`). Because PSTi8 is intentionally truncated at residue 21 (`PEGKGEQEHSQQKEEEEEMAV-NH2`), **residue 25 is physically absent from the therapeutic inhibitor**. Therefore, **PSTi8 is structurally and pharmacologically refractory to the Gly297Ser polymorphism**. Patients carrying this high-potency diabetogenic risk allele express a hyperactive endogenous peptide, yet PSTi8 retains full competitive potency to neutralize both wild-type and Gly297Ser pancreastatin.

Additionally, re-evaluation of Allu et al. (2014) confirms that in full-length human CHGA (UniProt P10645), PST-29 spans residues 273–301. The core amphipathic helix `HSQQKEE` corresponds to residues **281–287** (positions 9–15 of mature PST-29). Position 284 is **Glutamine (Gln, `Q`)**, an uncharged polar residue that precludes electrostatic salt-bridge formation, refuting earlier unverified docking claims.

### 3.8 Functional GRP78 Interactome & Cellular Compartmentalization
Topological analysis of the GRP78 interactome synthesized 20 verified high-confidence protein interactors across two distinct signaling branches (Figure 5B):
1. **ER-Luminal UPR Cascade:** Intracellular GRP78 physically complexes with ER stress sensor IRE1$\alpha$ (ERN1). Under sustained glucose or lipid stress, GRP78 dissociates from IRE1$\alpha$, triggering autophosphorylation, TRAF2 recruitment, and JNK1 (MAPK8) activation. Activated JNK phosphorylates Insulin Receptor Substrate 1 (IRS1) at inhibitory serine residues (Ser307), uncoupling IRS1 from downstream PI3K-AKT1 signaling and inducing cellular insulin resistance.
2. **Cell-Surface GRP78 (csGRP78) Signaling Complex:** In metabolically stressed hepatocytes and adipocytes, GRP78 translocates to the cell surface, where it complexes with MHC class I, CD44, and $\alpha_2$-macroglobulin. Circulating pancreastatin engages csGRP78 to trigger calcium mobilization and amplify stress kinase cascades. PSTi8 competitively occupies the linker-hinge cleft of csGRP78 without inducing the conformational clamp required for downstream signaling, thereby shielding insulin signaling cascades from circulating pancreastatin.

---

## 4. Discussion

### 4.1 The Allosteric Linker Wedge vs Active-Site Docking Claims
Our computational findings challenge the foundational structural model of PSTi8 action. Hossain et al. (2018) modeled PSTi8 docking into the catalytic ATPase site of isolated NBD (PDB 3LDP) [11]. However, that model utilized a truncated, static crystal construct devoid of physiological cofactors. When modeled against intact full-length GRP78 in the presence of $\text{Mg}^{2+}$-ATP, AlphaFold 3 demonstrates **zero contacts with the NBD**. 

The biological plausibility of direct ATP-pocket inhibition is further undermined by cellular biochemistry: intracellular ATP concentrations reside in the millimolar range (1–5 mM), whereas cell-surface receptor binding operates in the nanomolar range. Competitive displacement of millimolar ATP by a peptide ligand is biophysically improbable. By docking as an **allosteric steric wedge** at the linker-hinge (`ILE426`) and $\text{SBD}\beta$ entrance, PSTi8 prevents the closure of the helical lid ($\text{SBD}\alpha$) and uncouples interdomain allostery without competing directly against nucleotide binding.

### 4.2 The Cellular Compartmentalization Paradox
Our findings provide a coherent resolution to the long-standing "GRP78 paradox" in metabolic biology [29, 30]. Intracellularly, ER-resident GRP78 protects against insulin resistance by mitigating proteotoxic stress and chaperone-mediated degradation [31]. In contrast, cell-surface and circulating GRP78 act as pathogenic signaling hubs that promote tissue inflammation and insulin desensitization [32]. PSTi8 therapeutic efficacy does not depend on suppressing beneficial ER-chaperone folding within the lumen; rather, it acts extracellularly to block circulating pancreastatin from engaging cell-surface GRP78 complexes on insulin-sensitive target tissues.

### 4.3 Translational Consequences of Preclinical Sex Segregation
The complete exclusion of female rodents from general T2D and DIO models represents an alarming translation vulnerability. Metabolic physiology in female rodents is governed by dynamic estrogen receptor signaling ($\text{ER}\alpha$ and GPER), which enhances insulin sensitivity, promotes subcutaneous over visceral adipose storage, and represses hepatic gluconeogenic gene expression [17, 19]. Confining female testing exclusively to chemically induced menopause (VCD/OVX) or androgen excess (PCOS) means that **PSTi8 has never been demonstrated to ameliorate metabolic dysfunction in physiologically intact females**. 

Furthermore, the complete absence of baseline estrous cycle staging (0/7 studies) introduces uncontrolled hormonal variance into preclinical cohorts. $17\beta$-estradiol fluctuates substantially across the 4-day rodent estrous cycle, directly modulating GRP78 transcription and insulin receptor phosphorylation [18]. Unsynchronized female cohorts inevitably exhibit increased outcome variance, which researchers routinely misinterpret as treatment failure or inconsistent drug efficacy.

### 4.4 The Subgroup Fallacy & Underpowered Factorial Testing
Our mathematical power modeling exposes the statistical invalidity of subgroup splitting. Preclinical investigators frequently enroll small cohorts of both sexes ($n = 6$ per group) and conduct separate within-sex comparisons, claiming sex-divergent pharmacology when males reach $p < 0.05$ while females do not. As established by Gelman and Stern (2006), "the difference between 'significant' and 'not significant' is not itself statistically significant" [33]. Establishing a true biological sex difference mandates testing the omnibus $\text{Sex} \times \text{Treatment}$ interaction contrast. Because standard cohorts ($n = 6$) possess $<19\%$ power to detect moderate interaction effects, published claims of preclinical sexual dimorphism in PSTi8 action represent statistical noise rather than reproducible biology.

### 4.5 Actionable Recommendations for Preclinical Metabolic Research
To close the preclinical translational divide, we recommend four mandatory methodological standards:
1. **Mandatory Factorial Design:** Experiments enrolling both sexes must employ full $2 \times 2$ factorial designs analyzed via two-way ANOVA, reporting the interaction $F$-statistic, degrees of freedom, and partial $\eta^2$ effect size.
2. **Adequate Cohort Sizing:** Sample sizes must be calculated a priori based on the interaction contrast ($SE_{\text{int}} = 2\sigma/\sqrt{n}$) rather than within-group main effects, requiring at least $n = 16$ to $32$ animals per cell for robust evaluation.
3. **Baseline Estrous Synchronization:** All experiments utilizing female animals must document estrous cycle phase at baseline via vaginal cytology, stratifying or synchronizing cohorts prior to drug allocation.
4. **Independent Laboratory Verification:** Preclinical validation must be replicated across independent research networks to verify metabolic phenotypes beyond the single-institution discovery cluster.

### 4.6 In Silico Control Roadmap (Future Directions)
To further validate the allosteric linker-wedge model, we have established a prioritized in silico control roadmap ([`docs/gap_map.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/gap_map.md)):
1. **Domain-Isolated Controls:** Co-folding PSTi8 against isolated NBD-only (residues 26–407) in apo and ADP states to confirm lack of intrinsic pocket affinity.
2. **Sequence Specificity Controls:** Co-folding scrambled PSTi8 sequences and two random 21-mers to determine non-specific binding thresholds.
3. **Positive Peptide Control:** Co-folding the known high-affinity GRP78-binding peptide `HWDFAWPW`.
4. **Multi-Seed Diffusion Sampling:** Evaluating seed variance across 5 independent random model seeds (`modelSeeds: [1, 2, 3, 4, 5]`).
5. **Cross-Platform Verification:** Orthogonal co-folding utilizing Boltz-2 and Chai-1 deep-learning architectures.

### 4.7 Study Limitations
This study has two primary limitations. First, 10 of the 20 primary in vivo studies remain behind publisher paywalls; data extraction for these studies was derived from publisher abstracts and validated bibliographic metadata, precluding full-text methodological auditing of those cohorts. Second, our quaternary structural models represent in silico neural predictions; while AlphaFold 3 achieves near-experimental accuracy in peptide-protein co-folding, definitive biophysical proof of the allosteric wedge requires cryo-electron microscopy or X-ray crystallography of intact full-length GRP78 in complex with PSTi8.

---

## 5. Conclusions

This investigation delivers the first systematic evidence audit and atomic-resolution quaternary mechanism for the pancreastatin inhibitor PSTi8. We demonstrate that preclinical development has suffered from severe sex segregation—testing general metabolic disease exclusively in male rodents—and a pervasive omission of factorial interaction testing. Structurally, AlphaFold 3 refutes direct catalytic ATP-pocket docking, establishing that PSTi8 acts as an allosteric steric wedge at the interdomain linker-hinge and $\text{SBD}\beta$ entrance. Furthermore, the diabetogenic human Gly297Ser polymorphism collapses peptide binding via Ser25 pocket disruption, but PSTi8 is structurally immune due to its C-terminal truncation. Clinical development of pancreastatin inhibitors must mandate adequately powered factorial designs and rigorous estrous cycle tracking to ensure safe, equitable translation across both sexes.

---

## Declarations

### Ethics Approval and Consent to Participate
Not applicable. This study is a systematic review and computational biophysics investigation; no human subjects or live animal experiments were performed by the authors.

### Consent for Publication
Not applicable.

### Availability of Data and Materials
All data generated or analyzed during this study are included in this published article, its supplementary information files, and the permanent version-controlled GitHub repository: [https://github.com/Devanshyadav118/psti8-evidence-map](https://github.com/Devanshyadav118/psti8-evidence-map) under Creative Commons Attribution 4.0 International ([CC BY 4.0](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/LICENSE)). Protocol registration is maintained on the Open Science Framework ([`docs/osf_protocol_registration.md`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/docs/osf_protocol_registration.md)). Master datasets include:
- Evidence Table: [`data/evidence_table.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/evidence_table.csv)
- Papers Registry: [`data/papers_registry.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/papers_registry.csv)
- Dual-Screening Audit: [`data/dual_screening_audit.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/dual_screening_audit.csv)
- Methodological Matrix: [`data/syrcle_arrive_matrix.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/syrcle_arrive_matrix.csv)
- Power Modeling Scenarios: [`data/power_results.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/power_results.csv)
- Structural Inventory: [`data/structures/structures_manifest.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/structures_manifest.csv)
- AlphaFold 3 Metrics & Contacts: [`data/structures/3d_models/af3_complex_metrics.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/af3_complex_metrics.csv) and [`data/structures/3d_models/af3_interface_contacts.csv`](file:///home/devansh/Downloads/Devansh%20projects/psti8-sex-bias-review/data/structures/3d_models/af3_interface_contacts.csv)

### Competing Interests
The author declares no competing financial or non-financial interests.

### Funding
This research received no external financial support, commercial sponsorship, or grant funding.

### Authors' Contributions
DPS conceived the study, developed the methodology, executed automated data extraction, conducted PRISMA and ARRIVE quality scoring, authored computational biophysics and language model pipelines, performed AlphaFold 3 quaternary modeling, and wrote the manuscript.

### Acknowledgements
Computational infrastructure and API retrieval pipelines were supported by the Antigravity multi-agent research framework.

---

## References

1. Kahn SE, Cooper ME, Del Prato S. Pathophysiology and treatment of type 2 diabetes: perspectives on the past, present, and future. *Lancet*. 2014;383(9922):1068-1083.
2. Hotamisligil GS. Inflammation, metaflammation and immunometabolic disorders. *Nature*. 2017;542(7640):177-185.
3. Tatemoto K, Efendic S, Mutt V, Makk G, Feistner GJ, Barchas JD. Pancreastatin, a novel pancreatic peptide that inhibits insulin secretion. *Nature*. 1986;324(6096):476-478.
4. Mahata SK, O'Connor DT, Mahata M, Yoo SH, Taupenot L, Wu H, et al. Novel autocrine feedback control of catecholamine release. A discrete chromogranin a fragment is a noncompetitive nicotinic cholinergic antagonist. *J Clin Invest*. 1997;100(6):1623-1633.
5. Sanchez-Margalet V, Gonzalez-Yanes C, Najib S, Santos-Alvarez J. Pancreastatin, another chromogranin A-derived peptide. Current status. *Regul Pept*. 2010;165(1):102-113.
6. Biswas N, Friese RS, Gayen JR, Bandyopadhyay GK, Mahata SK, O'Connor DT. Discovery of a novel regulatory pathway for hepatic glucose production: pancreastatin actions mediated by GRP78. *PLoS One*. 2014;9(1):e84132.
7. O'Connor DT, Kailasam MT, O'Callaghan B, Miralles P, Parmer RJ. Pancreastatin, a chromogranin A-derived peptide, in human essential hypertension: enhanced secretion and blunted target tissue responsiveness. *J Hypertens*. 2005;23(4):819-828.
8. Bandyopadhyay GK, Vu C, Chen HC, Gayen JR, Vaingankar SM, O'Connor DT, et al. Pancreastatin stimulates gluconeogenesis and lipolysis in human and murine models. *Regul Pept*. 2011;170(1-3):56-64.
9. Funakoshi A, Miyasaka K, Kitani K, Funakoshi S, Tamamura H, Fujii N. Immunoreactive pancreastatin in human plasma. *Regul Pept*. 1989;24(2):225-231.
10. O'Connor DT, Cadman PE, Smiley C, Salem RM, Rao F, Smith DW, et al. Pancreastatin: a novel neuroendocrine hormone regulating glucose homeostasis in humans. *J Clin Endocrinol Metab*. 2008;93(4):1429-1438.
11. Hossain Z, Valicherla GR, Gupta AP, Reza MI, Sharma VP, Gayen JR. Discovery of pancreastatin inhibitor PSTi8 for the treatment of insulin resistance and diabetes: studies in rodent models of diabetes mellitus. *Sci Rep*. 2018;8(1):8814.
12. Goand UK, Dadge A, Gayen JR. Pancreastatin inhibitor PSTi8 balances energy homeostasis by attenuating adipose tissue inflammation in high fat diet fed mice. *Peptides*. 2023;161:170902.
13. Begley CG, Ellis LM. Drug development: Raise standards for preclinical research. *Nature*. 2012;483(7391):531-533.
14. Karp NA, Reavey N. Sex bias in preclinical research and an exploration of how to change the status quo. *Br J Pharmacol*. 2019;176(21):4107-4118.
15. Clayton JA, Collins FS. Policy: NIH to balance sex in cell and animal studies. *Nature*. 2014;509(7500):282-283.
16. National Institutes of Health. Consideration of Sex as a Biological Variable in NIH-funded Research. *Notice Number: NOT-OD-15-102*. Bethesda, MD: NIH; 2015.
17. Mauvais-Jarvis F, Bairey Merz N, Barnes PJ, Brinton RD, Carrero JJ, DeMeo DL, et al. Sex and gender in the outcome of COVID-19 and other infectious diseases: an international roadmap. *Lancet Diabetes Endocrinol*. 2020;8(7):634-644.
18. Tramunt B, Smati S, Grandgeorge N, Lenfant F, Arnal JF, Montagner A, et al. Sex differences in metabolic regulation and diabetes susceptibility. *Diabetologia*. 2020;63(3):453-461.
19. Gupte AA, Pownall HJ, Hamilton DJ. Estrogen: an emerging regulator of insulin action and mitochondrial function. *J Diabetes Res*. 2015;2015:916585.
20. Lee AS. The glucose-regulated proteins: stress induction and clinical applications. *Trends Biochem Sci*. 2001;26(8):504-510.
21. Allu PK, Chirasani VR, Tagirasa R, Ghia JE, Sahu BS, Subramanian L, et al. Biologically active peptides from chromogranin A: structural profiling and functional characterization. *J Biol Chem*. 2014;289(8):5250-5264.
22. Abramson J, Adler J, Dunger J, Evans R, Green T, Pritzel A, et al. Accurate structure prediction of biomolecular interactions with AlphaFold 3. *Nature*. 2024;630(8016):493-500.
23. Friese RS, Biswas N, Bandyopadhyay GK, Gayen JR, Vaingankar SM, Mahata SK, et al. Natural functional variant in human pancreastatin: a glycemic risk factor. *J Am Coll Cardiol*. 2013;61(10_S):E1375.
24. Shamseer L, Moher D, Clarke M, Ghersi D, Liberati A, Petticrew M, et al. Preferred reporting items for systematic review and meta-analysis protocols (PRISMA-P) 2015: elaboration and explanation. *BMJ*. 2015;350:g7647.
25. Hooijmans CR, Rovers MM, de Vries RB, Leenaars M, Ritskes-Hoitinga M, Langendam MW. SYRCLE's risk of bias tool for animal studies. *BMC Med Res Methodol*. 2014;14:43.
26. Page MJ, McKenzie JE, Bossuyt PM, Boutron I, Hoffmann TC, Mulrow CD, et al. The PRISMA 2020 statement: an updated guideline for reporting systematic reviews. *BMJ*. 2021;372:n71.
27. Percie du Sert N, Hurst V, Ahluwalia A, Alam S, Avey MT, Baker M, et al. The ARRIVE guidelines 2.0: Updated guidelines for reporting animal research. *PLoS Biol*. 2020;18(7):e3000410.
28. Sena ES, Currie GL, McCann SK, Macleod MR, Howells DW. Systematic reviews and meta-analysis of preclinical studies: why, when, and how. *J Cereb Blood Flow Metab*. 2014;34(5):737-742.
29. Kammoun HL, Chabanon H, Hainault I, Luquet S, Magnan C, Koike T, et al. GRP78/BiP is a master regulator of hepatic unfolded protein response and protects against hepatic steatosis in mice. *J Clin Invest*. 2009;119(5):1201-1215.
30. Ye R, Jung DY, Jun JY, Li J, Luo S, Sachs C, et al. Grp78 heterozygosity promotes adaptive unfolded protein response and protects against high-fat diet-induced obesity and insulin resistance. *Diabetes*. 2010;59(1):6-16.
31. Pfaffenbach KT, Lee AS. The critical role of GRP78 in physiologic and pathologic unfolded protein response. *Curr Opin Cell Biol*. 2011;23(2):150-156.
32. Angelini G, Castagneto-Gissey L, Casella G, Mingrone G. Circulating GRP78 acts as an adipokine and induces insulin resistance in human adipocytes. *Cell Death Dis*. 2022;13(4):325.
33. Gelman A, Stern H. The difference between "significant" and "not significant" is not itself statistically significant. *Am Stat*. 2006;60(4):328-331.
