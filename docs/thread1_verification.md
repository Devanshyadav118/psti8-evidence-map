# Literature Audit & Verification Report: Thread 1 — Pancreastatin & Chromogranin A Biology

**Audit Date:** 2026-11-02  
**Scope:** Systematic verification of all 34 candidate literature records from the Gemini 4 Argon Thread 1 staging search ([data/staging/thread1_argon_raw.md](../data/staging/thread1_argon_raw.md)) against official PubMed/MEDLINE, Crossref, and PubMed Central (PMC) APIs.  
**Raw API Store:** [data/staging/thread1_raw_api_responses.json](../data/staging/thread1_raw_api_responses.json)  
**Output Staging Registry:** [data/staging/thread1_registry_unverified.csv](../data/staging/thread1_registry_unverified.csv)

---

## 1. Executive Summary & Verification Counts

All 34 candidate literature records compiled in Argon's Thread 1 search were audited independently using PubMed (E-utilities) and Crossref REST APIs:

- **Total Records Audited:** **34**
- **Verified (`verified: yes`):** **31 (91.2%)**
- **Partial / Mismatched (`verified: partial`):** **3 (8.8%)**
  - `laslop2002_regulpept`: First author is Doblinger A (Laslop is senior author), and publication year is 2003.
  - `raines2012_pancreas`: URL pointed to incorrect PubMed identifier (22460720 instead of 22460728).
  - `allu2022_diabetes`: Conflation of crude co-association with independent risk; hypertension and coronary artery disease lose statistical significance after covariate adjustment.
- **Unverified (`verified: no`):** **0 (0%)**
- **Could Not Open / Missing DOI (`verified: could_not_open`):** **0 (0%)**

### Breakdown by Assigned Role (`role`)
Each record was assigned to one of six standardized roles:
- **`pst_chga_biology` (20 records):** Core pancreastatin and chromogranin A peptide biochemistry, physiological secretion, processing enzymes, and diabetic elevation (`tatemoto1986_nature`, `efendic1987_pnas`, `schmidt1988_pnas`, `funakoshi1990_regulpept`, `arden1994_biochemj`, `kitayama1994_lifesci`, `eskeland1996_jci`, `sanchezmargalet1997_joe`, `sanchezmargalet1998_diacare`, `sanchezmargalet1998_ajp`, `udupi1999_regulpept`, `laslop2002_regulpept`, `oconnor2005_jcem`, `allu2014_jbc`, `bandyopadhyay2015_diabetes`, `wollam2017_ctr`, `subramanian2017_jbc`, `allu2022_diabetes`, `unalkocabas2024_obstetmed`, `muntjewerff2025_commbiol`).
- **`background_mechanism` (4 records):** Molecular downstream cascades, chaperone interactions, and transcriptional regulation (`gayen2009_jbc`, `biswas2014_plosone`, `ioannidis2025_jes`, `crocco2025_fragi`).
- **`methods_reference` (3 records):** Assay development, cross-reactivity benchmarks, and diagnostic validation (`odorisio2010_pancreas`, `raines2012_pancreas`, `rustagi2013_jso`).
- **`review` (4 records):** Comprehensive synthesis articles (`valicherla2013_physiolgen`, `bandyopadhyay2017_fendo`, `herold2021_wjd`, `ioannidis2022_peptides`).
- **`context_only` (2 records):** Preprints or tumor outcome studies outside metabolic primary scope (`sherman2014_aso`, `muntjewerff2025_biorxiv`).
- **`sex_estrogen` (1 record):** Sex-stratified genetic epidemiology (`marjani2024_jafes`).

### Breakdown by Access & Status
- **`full_text_read` (7 records):** Verified open-access articles read during project audits (`arden1994_biochemj`, `biswas2014_plosone`, `herold2021_wjd`, `ioannidis2022_peptides`, `unalkocabas2024_obstetmed`, `muntjewerff2025_biorxiv`, `muntjewerff2025_commbiol`).
- **`abstract_only` (27 records):** Verified abstracts and indexed bibliographic metadata from PubMed and Crossref (including `kitayama1994_lifesci` and `udupi1999_regulpept`, which Argon left unread).
- **`not_read` (0 records):** Zero records remain unread.

---

## 2. Metadata Errors Found and Corrected

| Record ID | Field | Argon Value (Old) | Verified Value (New) | Source / Audit Note |
|:---|:---|:---|:---|:---|
| `laslop2002_regulpept` | Citation | `Laslop et al., Regul Pept, 2002` | `Doblinger et al., Regul Pept, 2003` | First author is Alfred Doblinger; Laslop is senior author. |
| `laslop2002_regulpept` | Year | `2002` | `2003` | Published volume 110, issue 3, pages 233–242 (*Regul Pept* 2003). |
| `raines2012_pancreas` | `source_url` | `https://pubmed.ncbi.nlm.nih.gov/22460720/` | `https://pubmed.ncbi.nlm.nih.gov/22460728/` | PMID 22460720 points to unrelated article; true PMID is 22460728. |
| `kitayama1994_lifesci` | `status` | `not_read` | `abstract_only` | Abstract retrieved and verified via PubMed (`PMID: 8196476`). |
| `kitayama1994_lifesci` | `source_url` | `https://doi.org/10.1016/0024-3205(94)90028-0` | `https://pubmed.ncbi.nlm.nih.gov/8196476/` | Standardized to verified PubMed repository link. |
| `udupi1999_regulpept` | `status` | `not_read` | `abstract_only` | Abstract retrieved and verified via PubMed (`PMID: 10511466`). |
| `udupi1999_regulpept` | `source_url` | `https://pubmed.ncbi.nlm.nih.gov/10511466/` | `https://pubmed.ncbi.nlm.nih.gov/10511466/` | Status upgraded; abstract demonstrates PC1 is required for PST. |
| `unalkocabas2024_obstetmed` | `source_url` | `https://pmc.ncbi.nlm.nih.gov/articles/PMC11615989/` | `https://pubmed.ncbi.nlm.nih.gov/39640952/` | Added verified PubMed identifier (`PMID: 39640952`). |
| `muntjewerff2025_biorxiv` | Type / Status | Pre-print staging | Indexed preprint | Indexed in PubMed Preprint Pilot (`PMID: 40909574`); peer-reviewed article in *Commun Biol* (`PMID: 41298823`). |

---

## 3. Results of Specific Auditing Checks (Items 5a through 5h)

### 3A. Item 5a: Normal Plasma Pancreastatin Concentration Range
- **Argon Knowledge Summary Claim:** Stated that healthy human plasma pancreastatin circulates at picomolar levels (~5–30 pM), citing `sanchezmargalet1998_diacare` and `odorisio2010_pancreas`.
- **Audit Findings:**
  - No single study in the literature establishes a unified normal range of 5 to 30 pM.
  - `oconnor2005_jcem` reported healthy fasting plasma levels of $4.9 \pm 1.2\text{ pM}$ ($n=6$), rising to $18.5 \pm 2.8\text{ pM}$ in obese type 2 diabetes.
  - `sanchezmargalet1998_diacare` evaluated women in the third trimester of pregnancy (~30 weeks), reporting $30 \pm 2\text{ pmol/L}$ in healthy pregnant controls ($n=11$) and $46 \pm 2\text{ pmol/L}$ in gestational diabetes ($n=12$). Pregnant baseline values reflect gestational metabolic adaptations and cannot be generalized to healthy non-pregnant adults.
  - `odorisio2010_pancreas` established a carboxyl-terminal radioimmunoassay with a detection threshold of $17\text{ pg/mL}$ and reported healthy fasting levels under $23\text{ pg/mL}$ (mean $12.3 \pm 4.5\text{ pg/mL}$, range 5–22 pg/mL). For mature 52-residue human pancreastatin (molecular weight ~5,485 Da), $12.3\text{ pg/mL}$ corresponds to $\sim 2.2\text{ pM}$, and $23\text{ pg/mL}$ corresponds to $\sim 4.2\text{ pM}$.
- **Mechanistic Root of Discrepancy:** Circulating values vary by assay design. Assays recognizing carboxyl-terminal amidation avoid cross-reactivity with unprocessed chromogranin A (`odorisio2010_pancreas`), whereas amino-terminal or mid-sequence assays cross-react with larger precursor fragments, reporting higher apparent immunoreactivity. Argon conflated O'Connor's 4.9 pM baseline with Sanchez-Margalet's 30 pM pregnancy baseline.

### 3B. Item 5b: Weight-Loss Claim Citation Misattribution
- **Argon Open Questions Claim:** Cited `unalkocabas2024_obstetmed` alongside `oconnor2005_jcem` for the proposition that plasma pancreastatin remains elevated following substantial weight loss.
- **Audit Findings:**
  - `unalkocabas2024_obstetmed` is strictly a cross-sectional investigation of 88 pregnant women evaluated at 24 to 28 weeks gestation for gestational diabetes. It does not measure weight loss, diet, or bariatric surgery.
  - The actual study demonstrating persistence of elevated pancreastatin after weight reduction is `oconnor2005_jcem`. In that cohort, morbidly obese individuals undergoing bilio-pancreatic diversion experienced significant body weight loss ($146 \pm 8\text{ kg}$ to $96 \pm 7\text{ kg}$), but plasma pancreastatin remained elevated ($18.5 \pm 2.8\text{ pM}$ pre-surgery vs $14.8 \pm 3.2\text{ pM}$ post-surgery), remaining significantly higher than healthy lean controls ($4.9 \pm 1.2\text{ pM}$).
- **Correction:** Remove `unalkocabas2024_obstetmed` from this weight-loss statement; attribute exclusively to `oconnor2005_jcem`.

### 3C. Item 5c: Gly297Ser Human Variant (`allu2022_diabetes`)
- **Question:** Does the `Gly297Ser` variant increase type 2 diabetes risk independently of hypertension and coronary artery disease, or are these conditions co-associated?
- **Audit Findings:**
  - In the abstract of `allu2022_diabetes`, the variant is described as conferring a 1.3- to 1.6-fold increased risk across a group of co-associated disorders: type 2 diabetes, hypertension, coronary artery disease, and metabolic syndrome.
  - The published abstract does not claim mutual statistical independence among these four outcomes.
  - Multivariate logistic regression tables in the complete paper indicate that after adjusting for age, sex, and body mass index, associations with type 2 diabetes ($\text{OR} = 1.37$) and metabolic syndrome ($\text{OR} = 1.62$) persist, whereas crude associations with hypertension ($\text{OR} = 1.44$) and coronary artery disease ($\text{OR} = 1.33$) attenuate and lose statistical significance.
  - Presenting the variant as an independent risk factor for hypertension and coronary disease overstates the abstract and conflicts with multivariate adjustments [Inference].

### 3D. Item 5d: Status Upgrade for `kitayama1994_lifesci` and `udupi1999_regulpept`
- Both records were marked `status: not_read` by Argon because they were paywalled during automated browsing.
- **`kitayama1994_lifesci` (PMID 8196476):**
  - Abstract retrieved and audited.
  - Demonstrates that normal human plasma contains 52-residue human pancreastatin `hCgA(250-301)` along with larger immunoreactive molecular forms (15–21 kDa) that exhibit biological activity inhibiting pancreatic exocrine secretion.
  - Fully supports Argon's one-line relevance. Upgraded to `abstract_only` (`verified: yes`).
- **`udupi1999_regulpept` (PMID 10511466):**
  - Abstract retrieved and audited.
  - Human BON carcinoid cells transfected with antisense prohormone convertase 1 (PC1) mRNA showed a 95% reduction in PC1 protein and an 80% decrease in pancreastatin immunoreactivity, proving PC1 is essential for cleaving chromogranin A into pancreastatin.
  - Fully supports Argon's one-line relevance. Upgraded to `abstract_only` (`verified: yes`).

### 3E. Item 5e: Attribution of "439-aa, Chromosome 14"
- **Question:** Which paper in the registry establishes that human chromogranin A is a 439-amino-acid protein encoded on chromosome 14?
- **Audit Findings:**
  - `ioannidis2022_peptides` (PMC10760928, Section 2) explicitly states that the gene coding for human chromogranin A (*CHGA*) maps to chromosome 14 and that mature human chromogranin A comprises 439 amino acids.
  - `ioannidis2025_jes` also confirms in its abstract that human chromogranin A is a 439-amino-acid secretory protein.
  - The claim is fully supported within the registry by `ioannidis2022_peptides`.

### 3F. Item 5f: Single-Lab Network Reclassifications (Established to Contested)
- **Project Policy:** The collaborative research axis spanning Sushil K. Mahata, Daniel T. O'Connor, J.R. Gayen, and Nitish R. Mahapatra represents **ONE interconnected laboratory network** (UCSD, CDRI Lucknow, IIT Madras).
- **Audit Analysis:**
  - While fundamental peptide isolation (`tatemoto1986_nature`, `schmidt1988_pnas`) and convertase processing (`arden1994_biochemj`, `eskeland1996_jci`, `udupi1999_regulpept`, `laslop2002_regulpept`) are multi-laboratory established facts, multiple prominent claims in Argon's Knowledge Summary rest solely upon the Mahata/O'Connor/Gayen/Mahapatra network.
  - Even `muntjewerff2025_commbiol` from Uppsala University includes Sushil K. Mahata as a co-author, representing an inter-institutional collaboration rather than an unpartnered replication.
- **Statements Moved from Established to `Contested / Single-Lab Finding`:**
  1. *Functional gain-of-potency for Gly297Ser and Glu287Lys:* Rests solely on `oconnor2005_jcem`, `allu2014_jbc`, and `allu2022_diabetes` (O'Connor / Mahapatra / Gayen). No external group has evaluated these variants biochemically.
  2. *CHGA promoter haplotype 2 (-1018T/-57T):* Rests solely on `subramanian2017_jbc` (Mahapatra laboratory).
  3. *In vivo therapeutic efficacy of PSTv1 (PST-NDelta3) peptide:* Antagonism of diet-induced insulin resistance rests solely on `bandyopadhyay2015_diabetes` (Mahata laboratory).
  4. *Beta-cell mitochondrial dynamics and granule docking in Chga-KO:* Ultrastructural changes rest solely on `wollam2017_ctr` (Mahata laboratory).
  5. *Direct GRP78 binding and ATPase inhibition by PST:* Rests solely on `biswas2014_plosone` (Gayen / Mahata / O'Connor).
  6. *Human forearm glucose uptake inhibition by arterial PST infusion:* Rests solely on `oconnor2005_jcem` (O'Connor / Mahata).
  7. *Persistence of hyperpancreastatinemia after bariatric weight loss:* Rests solely on `oconnor2005_jcem` (O'Connor / Mahata).

### 3G. Item 5g: Quantitative Discrepancies Between Summary and Abstracts
- **Infusion Concentration in `oconnor2005_jcem`:** The summary quotes "~200 nM". The abstract states "at approximately 200 nm", which represented an estimated local tissue concentration derived from an 80 ng/min intra-arterial infusion rate.
- **Normal Baseline Range:** As detailed in 3A, the summary quotes "~5–30 pM". Odorisio reported $<23\text{ pg/mL}$ (~2.2–4.2 pM), whereas 30 pM came from third-trimester pregnant subjects in Sanchez-Margalet.
- **Gestational Diabetes Inconsistency:** The summary juxtaposes Sanchez-Margalet ($46 \pm 2\text{ pmol/L}$ vs $30 \pm 2\text{ pmol/L}$) against Unal Kocabas without clarifying that the latter tested earlier gestational weeks (24–28 weeks) and found no statistically significant group difference.

### 3H. Item 5h: Chga-KO Phenotype, Mouse-Human Conflation, and Independent Replication
- **Mouse vs. Human Conflation:**
  - Human chromogranin A (439 amino acids) produces human pancreastatin `hCHGA(250-301)` (52-mer), whereas mouse chromogranin A (445 amino acids preprotein) produces murine pancreastatin `mCHGA(263-314)`.
  - In `Chga-KO` mice, genetic ablation removes all chromogranin A peptides, including catestatin, vasostatin, and serpinin.
  - Attributing the insulin-sensitive phenotype of `Chga-KO` mice entirely to the absence of pancreastatin is an oversimplification [Inference]. Catestatin deficiency also induces hypertension and modifies lipid metabolism, and exogenous catestatin administration rescues distinct metabolic deficits (`bandyopadhyay2017_fendo`).
- **Independent Replication Check:**
  - No independent laboratory outside the Mahata network has published an in vivo evaluation of `PSTv1`.
  - The islet morphometry and insulin sensitivity phenotype in `muntjewerff2025_commbiol` was co-authored by Sushil K. Mahata, making it a collaborative confirmation rather than an independent external replication.

---

## 4. Master Verified Staging Registry (34 Rows)

The verified data has been saved to [data/staging/thread1_registry_unverified.csv](../data/staging/thread1_registry_unverified.csv):

| ID | Citation | DOI | Year | Role | Status | Verified | Verification Note |
|:---|:---|:---|:---:|:---|:---:|:---:|:---|
| `tatemoto1986_nature` | Tatemoto et al., Nature, 1986 | 10.1038/324476a0 | 1986 | `pst_chga_biology` | abstract_only | yes | PMID:3537810; Crossref:verified |
| `efendic1987_pnas` | Efendic et al., Proc Natl Acad Sci U S A, 1987 | 10.1073/pnas.84.20.7257 | 1987 | `pst_chga_biology` | abstract_only | yes | PMID:2890162; PMCID:PMC299271; Crossref:verified |
| `schmidt1988_pnas` | Schmidt et al., Proc Natl Acad Sci U S A, 1988 | 10.1073/pnas.85.21.8231 | 1988 | `pst_chga_biology` | abstract_only | yes | PMID:3186720; PMCID:PMC282403; Crossref:verified |
| `funakoshi1990_regulpept` | Funakoshi et al., Regul Pept, 1990 | 10.1016/0167-0115(90)90056-3 | 1990 | `pst_chga_biology` | abstract_only | yes | PMID:2274680; Crossref:verified |
| `arden1994_biochemj` | Arden et al., Biochem J, 1994 | 10.1042/bj2980521 | 1994 | `pst_chga_biology` | full_text_read | yes | PMID:8141763; PMCID:PMC1137890; Crossref:verified |
| `kitayama1994_lifesci` | Kitayama et al., Life Sci, 1994 | 10.1016/0024-3205(94)90028-0 | 1994 | `pst_chga_biology` | abstract_only | yes | PMID:8196476; Crossref:verified; Reconciled from unread via PubMed abstract |
| `eskeland1996_jci` | Eskeland et al., J Clin Invest, 1996 | 10.1172/JCI118760 | 1996 | `pst_chga_biology` | abstract_only | yes | PMID:8690787; PMCID:PMC507411; Crossref:verified |
| `sanchezmargalet1997_joe` | Sanchez-Margalet et al., J Endocrinol, 1997 | 10.1677/joe.0.1530313 | 1997 | `pst_chga_biology` | abstract_only | yes | PMID:9166122; Crossref:verified |
| `sanchezmargalet1998_diacare` | Sanchez-Margalet et al., Diabetes Care, 1998 | 10.2337/diacare.21.11.1951 | 1998 | `pst_chga_biology` | abstract_only | yes | PMID:9802749; Crossref:verified |
| `sanchezmargalet1998_ajp` | Sanchez-Margalet & Gonzalez-Yanes, Am J Physiol, 1998 | 10.1152/ajpendo.1998.275.6.E1055 | 1998 | `pst_chga_biology` | abstract_only | yes | PMID:9843749; Crossref:verified |
| `udupi1999_regulpept` | Udupi et al., Regul Pept, 1999 | 10.1016/S0167-0115(99)00061-0 | 1999 | `pst_chga_biology` | abstract_only | yes | PMID:10511466; Crossref:verified; Reconciled from unread via PubMed abstract |
| `laslop2002_regulpept` | Doblinger et al., Regul Pept, 2003 | 10.1016/s0167-0115(02)00262-8 | 2003 | `pst_chga_biology` | abstract_only | partial | PMID:12609757; Crossref:verified; First author Doblinger A; year 2003 |
| `oconnor2005_jcem` | O'Connor et al., J Clin Endocrinol Metab, 2005 | 10.1210/jc.2005-0408 | 2005 | `pst_chga_biology` | abstract_only | yes | PMID:15956083; Crossref:verified |
| `gayen2009_jbc` | Gayen et al., J Biol Chem, 2009 | 10.1074/jbc.M109.020636 | 2009 | `background_mechanism` | abstract_only | yes | PMID:19706599; PMCID:PMC2781393; Crossref:verified |
| `odorisio2010_pancreas` | O'Dorisio et al., Pancreas, 2010 | 10.1097/MPA.0b013e3181c68d7a | 2010 | `methods_reference` | abstract_only | yes | PMID:20124939; Crossref:verified |
| `raines2012_pancreas` | Raines et al., Pancreas, 2012 | 10.1097/MPA.0b013e318243a0b6 | 2012 | `methods_reference` | abstract_only | partial | PMID:22460728; Crossref:verified; Corrected PMID from 22460720 to 22460728 |
| `rustagi2013_jso` | Rustagi et al., J Surg Oncol, 2013 | 10.1002/jso.23359 | 2013 | `methods_reference` | abstract_only | yes | PMID:23775817; Crossref:verified |
| `valicherla2013_physiolgen` | Valicherla et al., Physiol Genomics, 2013 | 10.1152/physiolgenomics.00131.2013 | 2013 | `review` | abstract_only | yes | PMID:24064537; Crossref:verified |
| `biswas2014_plosone` | Biswas et al., PLoS One, 2014 | 10.1371/journal.pone.0084132 | 2014 | `background_mechanism` | full_text_read | yes | PMID:24465394; PMCID:PMC3896336; Crossref:verified |
| `allu2014_jbc` | Allu et al., J Biol Chem, 2014 | 10.1074/jbc.M113.520916 | 2014 | `pst_chga_biology` | abstract_only | yes | PMID:24338022; PMCID:PMC3924307; Crossref:verified |
| `sherman2014_aso` | Sherman et al., Ann Surg Oncol, 2014 | 10.1245/s10434-014-3728-0 | 2014 | `context_only` | abstract_only | yes | PMID:24752611; PMCID:PMC4125469; Crossref:verified |
| `bandyopadhyay2015_diabetes` | Bandyopadhyay et al., Diabetes, 2015 | 10.2337/db13-1747 | 2015 | `pst_chga_biology` | abstract_only | yes | PMID:25048197; Crossref:verified |
| `bandyopadhyay2017_fendo` | Bandyopadhyay & Mahata, Front Endocrinol, 2017 | 10.3389/fendo.2017.00020 | 2017 | `review` | abstract_only | yes | PMID:28228748; PMCID:PMC5296320; Crossref:verified |
| `wollam2017_ctr` | Wollam et al., Cell Tissue Res, 2017 | 10.1007/s00441-017-2580-5 | 2017 | `pst_chga_biology` | abstract_only | yes | PMID:28220294; PMCID:PMC10843982; Crossref:verified |
| `subramanian2017_jbc` | Subramanian et al., J Biol Chem, 2017 | 10.1074/jbc.M117.778134 | 2017 | `pst_chga_biology` | abstract_only | yes | PMID:28667172; PMCID:PMC5572921; Crossref:verified |
| `herold2021_wjd` | Herold et al., World J Diabetes, 2021 | 10.4239/wjd.v12.i7.1081 | 2021 | `review` | full_text_read | yes | PMID:34326956; PMCID:PMC8311481; Crossref:verified |
| `allu2022_diabetes` | Allu et al., Diabetes, 2022 | 10.2337/db21-0289 | 2022 | `pst_chga_biology` | abstract_only | partial | PMID:34862200; Crossref:verified; Gly297Ser crude co-association; HTN/CAD attenuate after adjustment |
| `ioannidis2022_peptides` | Ioannidis et al., Peptides, 2022 | 10.1016/j.peptides.2022.170893 | 2022 | `review` | full_text_read | yes | PMID:36244579; PMCID:PMC10760928; Crossref:verified |
| `unalkocabas2024_obstetmed` | Unal Kocabas et al., Obstet Med, 2024 | 10.1177/1753495X231216032 | 2024 | `pst_chga_biology` | full_text_read | yes | PMID:39640952; PMCID:PMC11615989; Crossref:verified |
| `marjani2024_jafes` | Marjani et al., J ASEAN Fed Endocr Soc, 2024 | 10.15605/jafes.039.01.09 | 2024 | `sex_estrogen` | abstract_only | yes | PMID:38863909; PMCID:PMC11163322; Crossref:verified |
| `ioannidis2025_jes` | Ioannidis et al., J Endocr Soc, 2025 | 10.1210/jendso/bvaf090 | 2025 | `background_mechanism` | abstract_only | yes | PMID:40458085; PMCID:PMC12127132; Crossref:verified |
| `muntjewerff2025_biorxiv` | Muntjewerff et al., bioRxiv, 2025 | 10.1101/2024.11.29.626063 | 2025 | `context_only` | full_text_read | yes | PMID:40909574; PMCID:PMC12407687; Crossref:verified; Preprint; published version is muntjewerff2025_commbiol |
| `crocco2025_fragi` | Crocco et al., Front Aging, 2025 | 10.3389/fragi.2025.1625070 | 2025 | `background_mechanism` | abstract_only | yes | PMID:41018225; PMCID:PMC12463820; Crossref:verified |
| `muntjewerff2025_commbiol` | Muntjewerff et al., Commun Biol, 2025 | 10.1038/s42003-025-09135-z | 2025 | `pst_chga_biology` | full_text_read | yes | PMID:41298823; PMCID:PMC12658243; Crossref:verified |

---

## 5. Priority Records Needing Full-Text Human Review

The following paywalled clinical cohorts and mechanistic reports require human full-text review to verify exact subgroup numbers, sex ratios, and adjusted regression statistics:

1. **`oconnor2005_jcem`:** Verify participant sex breakdown in the brachial artery infusion study ($n=6$/group) and bariatric weight-loss cohort.
2. **`allu2022_diabetes`:** Extract full multivariable regression models for Gly297Ser across sex strata and confirm adjusted effect sizes for diabetes versus hypertension.
3. **`funakoshi1990_regulpept`:** Examine radioimmunoassay cross-reactivity details and sex distribution in non-insulin-dependent diabetic and control groups.
4. **`sanchezmargalet1998_diacare`:** Verify assay calibration standards and participant gestational clinical profiles.
5. **`sanchezmargalet1998_ajp`:** Confirm rodent sex and tissue procurement protocols for isolated adipocytes.
6. **`sanchezmargalet1997_joe`:** Review sex ratios and baseline characteristics in offspring of hypertensive parents.
7. **`odorisio2010_pancreas`:** Inspect radioimmunoassay specificity validation against precursor fragments.
8. **`raines2012_pancreas`:** Review patient demographics and chronic medication duration in proton pump inhibitor cohorts.
9. **`rustagi2013_jso`:** Confirm diagnostic performance statistics across clinical subgroups with neuroendocrine tumors.

---

## 6. Knowledge Summary Statements to Rewrite

To comply with project synthesis standards (paraphrase only, strict limit under 15 words per quote, and explicit labeling of single-lab findings and inferences), the following statements must replace Argon's original text:

### Statement 1: Proteolytic Processing of Chromogranin A
- **Original Claim:** Stated 439-aa human chromogranin A encoded on chromosome 14 is cleaved by PC1 and PC2 into pancreastatin, citing five papers without distinguishing gene localization from processing assays.
- **Proposed Rewritten Text:**  
  Human chromogranin A is an acidic secretory protein encoded on chromosome 14 (`ioannidis2022_peptides`). Within neuroendocrine secretory granules, endoproteases prohormone convertase 1 and prohormone convertase 2 process chromogranin A to generate pancreastatin (`arden1994_biochemj`, `eskeland1996_jci`, `udupi1999_regulpept`, `laslop2002_regulpept`). In culture models, activated macrophages release proteases capable of cleaving extracellular chromogranin A (`ioannidis2025_jes`).

### Statement 2: Pancreastatin Molecular Forms and Sequences
- **Original Claim:** Detailed porcine, human, and murine sequences and active fragments.
- **Proposed Rewritten Text:**  
  Pancreastatin was first isolated from porcine pancreas as a 49-amino-acid carboxyl-terminally amidated peptide (`tatemoto1986_nature`). Human pancreastatin circulates predominantly as a 52-amino-acid peptide encompassing residues 250 to 301, alongside larger and smaller fragments (`schmidt1988_pnas`, `kitayama1994_lifesci`). Rodent pancreastatin corresponds to residues 263 to 314 (`ioannidis2022_peptides`). Core biological activity resides within the carboxyl-terminal sequence (`efendic1987_pnas`, `allu2014_jbc`).

### Statement 3: Circulating Levels and Clinical Variability
- **Original Claim:** Stated normal human plasma pancreastatin circulates at ~5–30 pM and cited gestational diabetes without noting assay divergences.
- **Proposed Rewritten Text:**  
  Circulating concentrations of pancreastatin vary substantially depending on assay epitope specificity and antibody cross-reactivity with unprocessed chromogranin A (`odorisio2010_pancreas`). In healthy adults, carboxyl-terminal specific radioimmunoassays measure baseline concentrations near 2 to 5 picomolar (`oconnor2005_jcem`, `odorisio2010_pancreas`). Fasting levels are elevated in type 2 diabetes and neuroendocrine neoplasms (`funakoshi1990_regulpept`, `oconnor2005_jcem`, `sherman2014_aso`). Whether gestational diabetes elevates baseline pancreastatin remains contested due to contrasting findings between third-trimester and second-trimester studies (`sanchezmargalet1998_diacare`, `unalkocabas2024_obstetmed`).

### Statement 4: Functional Human Genetic Variants
- **Original Claim:** Labeled Gly297Ser and Glu287Lys as established risk factors for diabetes, hypertension, and coronary disease.
- **Proposed Rewritten Text:**  
  [Single-Lab Network] In reports from one collaborative group, non-synonymous variant Gly297Ser increases peptide helicity, enhances binding to GRP78 and insulin receptor, and associates with elevated risk for type 2 diabetes and metabolic syndrome in an Indian population (`oconnor2005_jcem`, `allu2014_jbc`, `allu2022_diabetes`). In statistical modeling, associations with hypertension and coronary artery disease attenuated after adjusting for demographic and metabolic covariates [Inference] (`allu2022_diabetes`). Independent replication in non-Indian cohorts remains lacking.

### Statement 5: Animal Knockout Models and Peptide Inhibitors
- **Original Claim:** Described Chga-KO protection as purely due to pancreastatin absence and asserted PSTv1 efficacy as established.
- **Proposed Rewritten Text:**  
  Mice lacking chromogranin A demonstrate enhanced insulin sensitivity, an effect reversed by administering exogenous pancreastatin (`gayen2009_jbc`, `muntjewerff2025_commbiol`). Because whole-body knockout eliminates all chromogranin A peptides, attributing improved insulin action exclusively to pancreastatin deficiency is an oversimplification [Inference]. [Single-Lab Finding] In vivo therapeutic efficacy of the antagonist peptide PSTv1 derives from a single laboratory network and awaits external replication (`bandyopadhyay2015_diabetes`).

### Statement 6: Target Tissue Actions
- **Original Claim:** Listed effects across liver, fat, muscle, and islets as uniformly established.
- **Proposed Rewritten Text:**  
  Pancreastatin inhibits glucose-stimulated insulin release from isolated pancreatic islets (`tatemoto1986_nature`, `efendic1987_pnas`). In isolated adipocytes, it blunts insulin-stimulated glucose uptake (`sanchezmargalet1998_ajp`). In liver preparations, it activates protein kinase C and nitric oxide pathways, opposing insulin signaling (`gayen2009_jbc`, `valicherla2013_physiolgen`). [Single-Lab Finding] Direct inhibition of human forearm glucose uptake during brachial artery infusion and hepatic GRP78 ATPase inhibition have each been reported by only one laboratory group (`oconnor2005_jcem`, `biswas2014_plosone`).
