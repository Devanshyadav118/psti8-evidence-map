# Literature Audit & Verification Report: Thread 2 — Signaling Pathways (2003–2026)

**Audit Date:** 2026-10-31  
**Scope:** Systematic verification of all 32 candidate literature records from the Gemini 4 Argon Thread 2 staging search ([data/staging/thread2_argon_raw.md](../data/staging/thread2_argon_raw.md)) against official PubMed/MEDLINE, Crossref, and PubMed Central (PMC) APIs.  
**Raw API Store:** [data/staging/thread2_raw_api_responses.json](../data/staging/thread2_raw_api_responses.json)  
**Output Staging Registry:** [data/staging/thread2_registry_unverified.csv](../data/staging/thread2_registry_unverified.csv)

---

## 1. Executive Summary & Verification Counts

All 32 candidate literature records compiled in Argon's Thread 2 search were audited independently using PubMed (E-utilities) and Crossref REST APIs:

- **Total Records Audited:** **32**
- **Verified (`verified: yes`):** **32 (100%)**
- **Unverified (`verified: no`):** **0 (0%)**
- **Partial / Mismatched:** **0 (0%)**
- **Could Not Open / Missing DOI:** **0 (0%)**

### Breakdown by Assigned Role (`role`)
Each record was categorized into one of four functional roles:
- **`background_mechanism` (17 records):** Core signaling cascades in insulin resistance and metabolic control (IRS1/2, PI3K/Akt, FoxO1, atypical PKC, NOX3, AMPK, GRP78/UPR).
- **`sex_estrogen` (6 records):** Direct evaluation of $17\beta$-estradiol, estrogen receptor-$\alpha$ ($\text{ER}\alpha$), sex differences, or sexually dimorphic metabolic disease models (`zhu2014_ajpendo`, `depaoli2024_ijms`, `alves2025_pathophys`, `depaoli2025_jes`, `franczak2026_biorxiv`, `monteillet2026_biorxiv`).
- **`methods_reference` (2 records):** Methodological tools, designer receptors, and chemical probes (`li2013_endocrinology` establishing chemogenetic Hep-Rq; `samanta2021_canres` discovering the GRP78 chemical inhibitor YUM70).
- **`review` (7 records):** Authoritative synthesis and review articles (`kimura2020_biomol`, `nasce2022_antiox`, `pan2022_ijerph`, `lee2025_pnas`, `yang2026_cells`, `li2026_theranostics`, `cruzvillarreal2026_kp`).

### Breakdown by Access & Status
- **`full_text_read` (8 records):** Open-access articles with verified full text available and examined (`matsumoto2003_jci`, `samanta2021_canres`, `nasce2022_antiox`, `depaoli2025_jes`, `franczak2026_biorxiv`, `li2026_theranostics`, `monteillet2026_biorxiv`, `cruzvillarreal2026_kp`).
- **`abstract_only` (24 records):** Verified abstracts and indexed metadata from PubMed/Crossref (including `taniguchi2006_cmet` and `kubota2008_cmet`, which Argon left as unread).
- **`not_read` (0 records):** Zero records remain unread.

---

## 2. Row Count Discrepancy & Reconciliation

Argon's narrative text in the LIMITS section stated:
> *"Two of the 28 registry rows—taniguchi2006_cmet and kubota2008_cmet... were not opened with google:browse... Of the 26 papers opened, 8 were read in full text, while the remaining 18 were opened on PubMed..."*

### Reconciliation
- **Actual Row Count in CSV Block:** **32 data rows** (lines 61 to 92 of `thread2_argon_raw.md`).
- **Discrepancy Source:** Argon performed faulty mental arithmetic:
  - Argon counted 8 `full_text_read` rows and subtracted from an assumed 26 opened rows to get 18 `abstract_only` rows ($26 - 8 = 18$), leading to an erroneous total of $18 + 8 + 2 = 28$.
  - In reality, the CSV block contains **22** `abstract_only` rows, **8** `full_text_read` rows, and **2** `not_read` rows ($22 + 8 + 2 = 32$).
  - All 32 rows are authentic, unique, and verified.

---

## 3. Results of Specific Auditing Checks

### A. bioRxiv DOIs with Prefix `10.64898` and 2026 Literature
- **`franczak2026_biorxiv` (DOI: `10.64898/2026.02.22.706993`):**  
  - *Confirmed:* Resolves directly on Crossref (`publisher: openRxiv`, `type: posted-content`, deposited 2026-02-24). Indexed in PubMed Central (`PMCID: PMC13160098`). Valid bioRxiv preprint.
- **`monteillet2026_biorxiv` (DOI: `10.64898/2026.07.18.739339`):**  
  - *Confirmed:* Resolves directly on Crossref (`publisher: openRxiv`, `type: posted-content`, deposited 2026-07-20). Valid bioRxiv preprint.
- **2026 Journal Articles:**
  - `yang2026_cells` (DOI: `10.3390/cells15020109`): Verified in PubMed (`PMID: 41597184`) and Crossref (*Cells*, MDPI).
  - `li2026_theranostics` (DOI: `10.7150/thno.136060`): Verified in PubMed (`PMID: 42370180`) and Crossref (*Theranostics*, Ivyspring).
  - `cruzvillarreal2026_kp` (DOI: `10.3390/kinasesphosphatases4030025`): Verified on Crossref (*Kinases and Phosphatases*, MDPI).

### B. Status of `taniguchi2006_cmet` and `kubota2008_cmet`
- Argon marked both records as `verified: no` and `status: not_read` because standalone URLs were not opened in its browsing session.
- **API Audit:**
  - `taniguchi2006_cmet` (DOI: `10.1016/j.cmet.2006.04.005`): Fully indexed in PubMed (`PMID: 16679292`) and Crossref (*Cell Metabolism* 2006; 3(6):343–353). Title, authors, and year match perfectly.
  - `kubota2008_cmet` (DOI: `10.1016/j.cmet.2008.05.007`): Fully indexed in PubMed (`PMID: 18590692`) and Crossref (*Cell Metabolism* 2008; 8(1):49–64). Title, authors, and year match perfectly.
- **Resolution:** Reconciled from `not_read` to `abstract_only` (`verified: yes`).

### C. Full-Text Availability for the 8 Open-Access Rows
Full text was confirmed freely available in open repositories for all 8 records:
1. `matsumoto2003_jci`: PMC open full text (`PMCID: PMC193669`).
2. `samanta2021_canres`: PMC open full text (`PMCID: PMC8137563`).
3. `nasce2022_antiox`: MDPI open access (`PMCID: PMC9220303`).
4. `depaoli2025_jes`: Oxford/PMC open access (`PMCID: PMC11968335`).
5. `franczak2026_biorxiv`: bioRxiv preprint open full text (`DOI: 10.64898/2026.02.22.706993`).
6. `li2026_theranostics`: Theranostics/PMC open access (`PMCID: PMC13294974`).
7. `monteillet2026_biorxiv`: bioRxiv preprint open full text (`DOI: 10.64898/2026.07.18.739339`).
8. `cruzvillarreal2026_kp`: MDPI open access (`DOI: 10.3390/kinasesphosphatases4030025`).

### D. Substantive Accuracy of Key Mechanistic Claims
- **`kammoun2009_jci`:** Verified. The abstract confirms adenoviral GRP78 overexpression in *ob/ob* mouse livers reduces ER stress, inhibits SREBP-1c cleavage, reduces hepatic triglycerides, and improves insulin sensitivity via IRS-2 restoration.
- **`ye2010_diabetes`:** Verified. The abstract confirms male Grp78(+/-) mice on HFD are protected from diet-induced obesity, hepatic steatosis, hyperinsulinemia, and insulin resistance via adaptive UPR in WAT (upregulating EDEM and ER chaperones).
- **`angelini2022_natcommun`:** Verified. The abstract confirms long-term continuous infusion of GRP78 and HSP70 causes hepatic and whole-body insulin resistance, hyperglycemia, and NASH in chow-fed rats, whereas anti-GRP78/HSP70 monoclonal antibodies reverse these phenotypes in HFD-fed rats.

### E. Cell Type Flag on `zhang2013_plosone`
- > [!CAUTION]
  > **Crucial Biological Flag:** `zhang2013_plosone` evaluated cell-surface GRP78 (`sGRP78`) complexing with the p85 subunit of PI3K **exclusively in human breast and prostate cancer cell lines** (MCF-7, LNCaP, etc.) resistant to hormonal therapy. It did **not** evaluate primary hepatocytes or hepatoma models. This cancer-specific context was omitted in Argon's general summary and must be strictly flagged when extrapolating to liver insulin signaling.

### F. Verbatim Reporting of Animal Sex
Per project rules, animal sex is reported strictly as stated in the abstract or open text without extrapolation:
- **Explicitly stated in abstract:**
  - `ye2010_diabetes`: Male mice ("Male Grp78(+/-) mice and their wild-type littermates").
  - `zhu2014_ajpendo`: Male mice ("assessed the importance of liver estrogen signaling in males using liver ERalpha-knockout (LKO) male mice").
  - `depaoli2024_ijms`: Male and ovariectomized female mice ("ovariectomized female and male ApoE-/-:Ins2+/Akita mice").
  - `alves2025_pathophys`: Male mice ("Male C57BL/6J mice were divided into four groups").
  - `depaoli2025_jes`: Male and female mice ("Male TALLYHO/JngJ mice... while females remain normoglycemic... Ovariectomized female mice...").
  - `franczak2026_biorxiv`: Female ovariectomized mice ("middle-aged female mice (36-40 weeks) following ovariectomy").
  - `monteillet2026_biorxiv`: Male and female mice ("both NCK1betaKO male and female mice... only males showed improved insulin secretion... Females, in contrast, exhibited impaired insulin secretion").
- **Unstated in abstract (reported only in full-text methods or MeSH indexing):**
  - `matsumoto2003_jci`: Male mice stated in full-text methods and MeSH; unstated in abstract.
  - `kammoun2009_jci`, `li2011_cmet`, `yecies2011_cmet`: Male mice indexed in MeSH; unstated in abstract.
  - `li2013_endocrinology`: Male and female mice indexed in MeSH; unstated in abstract.
  - `samanta2021_canres`: Female mice indexed in MeSH; unstated in abstract.
  - Remaining in vitro studies (`nakamura2009_jbc`, `li2010_febslett`, `gao2010_jbc`, `zhang2013_plosone`): Not applicable / cell lines.

### G. Quantitative Figures Quoted in One-Liners
- **`alves2025_pathophys`:**
  - Quoted: "reduces body fat by 28%, increases primary hepatocyte basal (19%) and maximal (34%) respiration, and in HFD-fed mice decreases hepatic triglycerides by 43% while improving hepatic insulin sensitivity by 145%".
  - *Audit:* **100% VERBATIM match.** All five percentages are present verbatim in the Crossref/publisher abstract text.
- **`depaoli2025_jes`:**
  - Quoted: "fasting glucose 27.55 vs 7.9 mmol/L in females".
  - *Audit:* **Supported by open full text, but absent from abstract.** In the published abstract, only the `>15 mM` threshold is stated. The specific numbers `27.55` and `7.9` appear verbatim in the Figure 1 caption of the open-access full text (`PMC11968335`).
- **`matsumoto2003_jci`:**
  - Quoted: "~50% lower refeeding-induced hepatic Srebp1c mRNA".
  - *Audit:* **Visual graph approximation.** The abstract states induction was "inhibited". The "~50%" figure is derived from Figure 2B of the open full text (`PMC193669`).

---

## 4. Unsupported or Erroneous Claims in Argon's Output

1. **Incorrect Registry Count in Limits Section:** Argon claimed there were 28 registry rows (26 opened + 2 unopened). The CSV block actually contained 32 rows ($22 \text{ abstract\_only} + 8 \text{ full\_text\_read} + 2 \text{ not\_read}$).
2. **False Unread Designation for `taniguchi2006_cmet` and `kubota2008_cmet`:** Argon claimed these two foundational *Cell Metabolism* papers could not be opened and marked them `verified: no`. Both DOIs are fully indexed and resolvable on PubMed and Crossref.
3. **Omission of Cancer Context in `zhang2013_plosone`:** Argon presented the cell-surface GRP78–PI3K p85 interaction as a general hepatic signaling mechanism, failing to disclose that the experimental work was conducted strictly in hormonal therapy-resistant breast and prostate cancer cells.
4. **Conflating Abstract-Only Content with Full-Text Graph Locators:** Argon presented quantitative values (`27.55 vs 7.9 mmol/L` in `depaoli2025_jes`, `~50%` in `matsumoto2003_jci`) without specifying that they originate from full-text figure captions and bar charts rather than published abstracts.

---

## 5. Master Verified Staging Registry (32 Rows)

The verified data has been saved to [data/staging/thread2_registry_unverified.csv](../data/staging/thread2_registry_unverified.csv) with the new `role` column, corrected statuses, and detailed verification notes:

| ID | Citation | DOI | Year | Role | Status | Verified | Verification Note |
|:---|:---|:---|:---:|:---|:---:|:---:|:---|
| `matsumoto2003_jci` | Matsumoto et al., J Clin Invest, 2003 | 10.1172/JCI18816 | 2003 | `background_mechanism` | full_text_read | yes | PMID:12975478; PMCID:PMC193669; Crossref:verified |
| `ozcan2004_science` | Ozcan et al., Science, 2004 | 10.1126/science.1103160 | 2004 | `background_mechanism` | abstract_only | yes | PMID:15486293; Crossref:verified |
| `mcmanus2005_emboj` | McManus et al., EMBO J, 2005 | 10.1038/sj.emboj.7600633 | 2005 | `background_mechanism` | abstract_only | yes | PMID:15791206; PMCID:PMC1142569; Crossref:verified |
| `dong2006_jci` | Dong et al., J Clin Invest, 2006 | 10.1172/JCI25735 | 2006 | `background_mechanism` | abstract_only | yes | PMID:16374520; PMCID:PMC1319221; Crossref:verified |
| `taniguchi2006_cmet` | Taniguchi et al., Cell Metab, 2006 | 10.1016/j.cmet.2006.04.005 | 2006 | `background_mechanism` | abstract_only | yes | PMID:16679292; Crossref:verified; Reconciled from unread |
| `kubota2008_cmet` | Kubota et al., Cell Metab, 2008 | 10.1016/j.cmet.2008.05.007 | 2008 | `background_mechanism` | abstract_only | yes | PMID:18590692; Crossref:verified; Reconciled from unread |
| `patel2008_mcb` | Patel et al., Mol Cell Biol, 2008 | 10.1128/MCB.00763-08 | 2008 | `background_mechanism` | abstract_only | yes | PMID:18694957; PMCID:PMC2577415; Crossref:verified |
| `kammoun2009_jci` | Kammoun et al., J Clin Invest, 2009 | 10.1172/JCI37007 | 2009 | `background_mechanism` | abstract_only | yes | PMID:19363290; PMCID:PMC2673873; Crossref:verified |
| `nakamura2009_jbc` | Nakamura et al., J Biol Chem, 2009 | 10.1074/jbc.M901488200 | 2009 | `background_mechanism` | abstract_only | yes | PMID:19332540; PMCID:PMC2685662; Crossref:verified |
| `cheng2009_natmed` | Cheng et al., Nat Med, 2009 | 10.1038/nm.2049 | 2009 | `background_mechanism` | abstract_only | yes | PMID:19838201; PMCID:PMC3994712; Crossref:verified |
| `ye2010_diabetes` | Ye et al., Diabetes, 2010 | 10.2337/db09-0755 | 2010 | `background_mechanism` | abstract_only | yes | PMID:19808896; PMCID:PMC2797945; Crossref:verified |
| `li2010_febslett` | Li et al., FEBS Lett, 2010 | 10.1016/j.febslet.2010.01.044 | 2010 | `background_mechanism` | abstract_only | yes | PMID:20102709; Crossref:verified |
| `gao2010_jbc` | Gao et al., J Biol Chem, 2010 | 10.1074/jbc.M110.128694 | 2010 | `background_mechanism` | abstract_only | yes | PMID:20647313; PMCID:PMC2943315; Crossref:verified |
| `li2011_cmet` | Li et al., Cell Metab, 2011 | 10.1016/j.cmet.2011.03.009 | 2011 | `background_mechanism` | abstract_only | yes | PMID:21459323; PMCID:PMC3132646; Crossref:verified |
| `yecies2011_cmet` | Yecies et al., Cell Metab, 2011 | 10.1016/j.cmet.2011.06.002 | 2011 | `background_mechanism` | abstract_only | yes | PMID:21723501; PMCID:PMC3132644; Crossref:verified |
| `li2013_endocrinology` | Li et al., Endocrinology, 2013 | 10.1210/en.2012-2127 | 2013 | `methods_reference` | abstract_only | yes | PMID:23885012; PMCID:PMC3781741; Crossref:verified |
| `zhang2013_plosone` | Zhang et al., PLoS One, 2013 | 10.1371/journal.pone.0080071 | 2013 | `background_mechanism` | abstract_only | yes | PMID:24244613; PMCID:PMC3828362; Crossref:verified; FLAG: cancer cells |
| `zhu2014_ajpendo` | Zhu et al., Am J Physiol Endocrinol Metab, 2014 | 10.1152/ajpendo.00579.2013 | 2014 | `sex_estrogen` | abstract_only | yes | PMID:24691030; PMCID:PMC4024403; Crossref:verified |
| `kimura2020_biomol` | Kimura et al., Biomolecules, 2020 | 10.3390/biom10101445 | 2020 | `review` | abstract_only | yes | PMID:33076386; PMCID:PMC7601959; Crossref:verified |
| `samanta2021_canres` | Samanta et al., Cancer Res, 2021 | 10.1158/0008-5472.CAN-20-1540 | 2021 | `methods_reference` | full_text_read | yes | PMID:33785501; PMCID:PMC8137563; Crossref:verified |
| `nasce2022_antiox` | Nascè et al., Antioxidants (Basel), 2022 | 10.3390/antiox11061131 | 2022 | `review` | full_text_read | yes | PMID:35740032; PMCID:PMC9220303; Crossref:verified |
| `pan2022_ijerph` | Pan et al., Int J Environ Res Public Health, 2022 | 10.3390/ijerph192315965 | 2022 | `review` | abstract_only | yes | PMID:36498048; PMCID:PMC9738090; Crossref:verified |
| `angelini2022_natcommun` | Angelini et al., Nat Commun, 2022 | 10.1038/s41467-022-35310-5 | 2022 | `background_mechanism` | abstract_only | yes | PMID:36513656; PMCID:PMC9747970; Crossref:verified |
| `depaoli2024_ijms` | De Paoli et al., Int J Mol Sci, 2024 | 10.3390/ijms25031816 | 2024 | `sex_estrogen` | abstract_only | yes | PMID:38339098; PMCID:PMC10855194; Crossref:verified |
| `alves2025_pathophys` | Alves et al., Pathophysiology, 2025 | 10.3390/pathophysiology32010001 | 2025 | `sex_estrogen` | abstract_only | yes | PMID:39846638; PMCID:PMC11755535; Crossref:verified; Numbers match |
| `depaoli2025_jes` | De Paoli et al., J Endocr Soc, 2025 | 10.1210/jendso/bvaf048 | 2025 | `sex_estrogen` | full_text_read | yes | PMID:40191018; PMCID:PMC11968335; Crossref:verified; Glucose numbers in Fig 1 |
| `lee2025_pnas` | Lee, Proc Natl Acad Sci U S A, 2025 | 10.1073/pnas.2412246122 | 2025 | `review` | abstract_only | yes | PMID:40699920; PMCID:PMC12318151; Crossref:verified |
| `yang2026_cells` | Yang et al., Cells, 2026 | 10.3390/cells15020109 | 2026 | `review` | abstract_only | yes | PMID:41597184; PMCID:PMC12838618; Crossref:verified |
| `franczak2026_biorxiv` | Franczak et al., bioRxiv, 2026 | 10.64898/2026.02.22.706993 | 2026 | `sex_estrogen` | full_text_read | yes | PMID:42124645; PMCID:PMC13160098; Crossref:verified; bioRxiv prefix 10.64898 |
| `li2026_theranostics` | Li et al., Theranostics, 2026 | 10.7150/thno.136060 | 2026 | `review` | full_text_read | yes | PMID:42370180; PMCID:PMC13294974; Crossref:verified |
| `monteillet2026_biorxiv` | Monteillet et al., bioRxiv, 2026 | 10.64898/2026.07.18.739339 | 2026 | `sex_estrogen` | full_text_read | yes | Crossref:verified; bioRxiv prefix 10.64898 |
| `cruzvillarreal2026_kp` | Cruz-Villarreal et al., Kinases Phosphatases, 2026 | 10.3390/kinasesphosphatases4030025 | 2026 | `review` | full_text_read | yes | Crossref:verified |
