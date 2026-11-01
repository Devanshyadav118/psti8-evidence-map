# Thread 2 Literature Audit Addendum: Established Claims, GRP78 Conflict, Sex Reporting & One-Liner Audit

**Audit Date:** 2026-10-31 (Updated: 2026-11-01)  
**Scope:** Read-only audit of [docs/thread2_verification.md](thread2_verification.md) and [data/staging/thread2_registry_unverified.csv](../data/staging/thread2_registry_unverified.csv) cross-referenced against raw Gemini 4 Argon output ([data/staging/thread2_argon_raw.md](../data/staging/thread2_argon_raw.md)) and raw API payloads ([data/staging/thread2_raw_api_responses.json](../data/staging/thread2_raw_api_responses.json)).  
**Status:** Completed  

---

## 1. Audit of Established Knowledge Summary Bullets & Laboratory Independence

In [data/staging/thread2_argon_raw.md](../data/staging/thread2_argon_raw.md) (Section C, lines 95–106), there are **9 distinct bullets** marked under the headline `Established` (lines 98–106). Each bullet was mapped to its cited registry papers and evaluated for laboratory independence:

| # | Knowledge Summary Bullet Title | Line Range in `thread2_argon_raw.md` | Cited Verified Papers (Registry IDs) | Independent Laboratories / Research Groups | Multi-Lab or Single-Lab? |
|---|---|---|---|---|---|
| **1** | Endoplasmic reticulum stress and GRP78/UPR in obesity and insulin resistance | Line 98 | `ozcan2004_science`, `samanta2021_canres`, `li2026_theranostics`, `kammoun2009_jci` | **3 independent primary labs** (Gökhan S. Hotamisligil, Harvard; Fabienne Foufelle / Pascal Ferré, INSERM Paris; Pinku Mukherjee, UNC Charlotte) + 1 review (Zun-Nan Li, Sun Yat-sen Univ) | **Multi-Lab** |
| **2** | Cell-surface and circulating GRP78 as a signaling receptor and metabolic driver | Line 99 | `zhang2013_plosone`, `angelini2022_natcommun`, `lee2025_pnas`, `li2026_theranostics`, `pan2022_ijerph` | **2 primary labs** (`zhang2013_plosone`: Amy S. Lee, USC; `angelini2022_natcommun`: Geltrude Mingrone, King's College London / Rome) + 3 reviews/perspectives | **Single-Lab for metabolic disease** (circulating GRP78 infusion and antibody reversal rests entirely on Geltrude Mingrone's lab); **Single-Lab for cancer cell surface** (Amy S. Lee lab) |
| **3** | GRP78 structure, post-translational modifications, and ATPase inhibitors | Line 100 | `samanta2021_canres`, `pan2022_ijerph`, `li2026_theranostics` | **1 primary lab** (`samanta2021_canres`: Pinku Mukherjee, UNC Charlotte) + 2 reviews | **Single-Lab** for small-molecule SBD-binding ATPase inhibition (YUM70 rests entirely on Mukherjee lab) |
| **4** | Hepatic insulin receptor and IRS1/2–PI3K–AKT–FoxO1 signaling | Line 101 | `dong2006_jci`, `kubota2008_cmet`, `cheng2009_natmed`, `cruzvillarreal2026_kp`, `yang2026_cells` | **2 independent primary lab networks** (Morris F. White, Joslin Diabetes Center/Harvard; Takashi Kadowaki / Naoto Kubota, Univ of Tokyo) + 2 reviews | **Multi-Lab** |
| **5** | GSK-3$\beta$ vs. GSK-3$\alpha$ and hepatic glycogen regulation | Line 102 | `mcmanus2005_emboj`, `dong2006_jci`, `patel2008_mcb` | **3 independent primary genetic knockin/knockout labs** (Dario R. Alessi, Univ of Dundee; Morris F. White, Joslin/Harvard; Jim R. Woodgett, Lunenfeld-Tanenbaum/Univ of Toronto) | **Multi-Lab** |
| **6** | PKC isoforms ($\text{PKC}\lambda/\zeta$, $\text{PKC}\varepsilon$, $\text{PKC}\delta$) and SREBP-1c in selective hepatic insulin resistance | Line 103 | `matsumoto2003_jci`, `taniguchi2006_cmet`, `yecies2011_cmet`, `nasce2022_antiox`, `cruzvillarreal2026_kp` | **2 independent primary lab networks** (C. Ronald Kahn network [Matsumoto, Taniguchi], Joslin Diabetes Center; Brendan D. Manning, Harvard) + 2 reviews | **Multi-Lab** |
| **7** | Oxidative stress, NOX3, and mitochondrial ROS in JNK-mediated hepatic insulin resistance | Line 104 | `nakamura2009_jbc`, `li2010_febslett`, `gao2010_jbc`, `nasce2022_antiox` | **2 primary labs** (`nakamura2009_jbc`: Takashi Kadowaki / Shinsuke Nakamura, Univ of Tokyo; `li2010_febslett` and `gao2010_jbc`: Jian Li, Hunan Normal Univ) + 1 review | **Single-Lab for NOX3** (The claim that NOX3 specifically produces ROS in hepatocytes rests exclusively on Jian Li's group; `nakamura2009_jbc` attributed ROS to mitochondrial $\beta$-oxidation) |
| **8** | AMPK and $G_{q/11}$/PLC signaling in hepatic glucose and lipid control | Line 105 | `li2011_cmet`, `li2013_endocrinology`, `kimura2020_biomol`, `cruzvillarreal2026_kp` | **2 primary labs** (`li2011_cmet`: Ming-Hui Zou, Univ of Oklahoma; `li2013_endocrinology`: Jürgen Wess, NIDDK/NIH) + 2 reviews | **Single-Lab for in vivo hepatocyte $G_q$ chemogenetics** (Transgenic `Hep-Rq` / `Hep-GqD` model and $V_{1b}$ antagonism rests exclusively on Jürgen Wess's lab) |
| **9** | Sex differences and estrogen ($\text{E}_2$ / $\text{ER}\alpha$) regulation of UPR and hepatic insulin signaling | Line 106 | `zhu2014_ajpendo`, `depaoli2024_ijms`, `alves2025_pathophys`, `depaoli2025_jes`, `franczak2026_biorxiv`, `monteillet2026_biorxiv` | **5 independent primary research groups** (Franck Mauvais-Jarvis, Tulane Univ; Robin E. De Paoli, Memorial Univ of Newfoundland; Eduardo R. Ropelle, UNICAMP Brazil; R. Scott Rector / Victoria J. Vieira-Potter, Univ of Missouri; Mathieu Bourret / Sylvie Cardin, Univ of Montreal) | **Multi-Lab** |

### Bullets Resting on One Lab or One Lab Network

1. **Bullet 7 (NOX3-specific ROS generation in hepatocytes):**  
   - *Key finding:* The mechanistic attribution of FFA/TNF-$\alpha$-induced hepatocyte ROS specifically to NADPH oxidase 3 (NOX3) and subsequent rescue by NOX3 siRNA knockdown rests exclusively on **a single laboratory: Jian Li's group at Hunan Normal University / Central South University, Changsha, China** (`li2010_febslett` and `gao2010_jbc`).  
   - *Corroboration status:* The third cited primary paper (`nakamura2009_jbc` from Tokyo) attributed palmitate-induced ROS to mitochondrial electron transport chain flux rather than NOX3. The review `nasce2022_antiox` explicitly notes that primary hepatocyte expression of NOX3 remains unverified outside the HepG2 cell line.
2. **Bullet 8 (In vivo hepatocyte $G_{q/11}$ chemogenetic activation and vasopressin $V_{1b}$ signaling):**  
   - *Key finding:* The in vivo evidence establishing that hepatocyte $G_q$ GPCR signaling acutely triggers gluconeogenesis matching the hyperglycemic magnitude of glucagon via `Hep-Rq` designer receptors rests entirely on **a single laboratory: Jürgen Wess's group at the Molecular Signaling Section, NIDDK, National Institutes of Health, Bethesda, MD** (`li2013_endocrinology` and reviewed in `kimura2020_biomol`).
3. **Bullet 2 (Circulating GRP78/HSP70 infusion inducing NASH and T2D in vivo):**  
   - *Key finding:* The finding that continuous peripheral infusion of recombinant extracellular GRP78 and HSP70 drives hepatic and systemic insulin resistance, hyperglycemia, and NASH in rodents—and that monoclonal neutralizing antibodies against GRP78/HSP70 reverse diet-induced NASH—rests on **a single laboratory network: Geltrude Mingrone's lab at King's College London and the Catholic University of the Sacred Heart, Rome** (`angelini2022_natcommun`). In cancer biology, cell-surface GRP78 complexing with p85 rests on **Amy S. Lee's lab at USC** (`zhang2013_plosone`, `lee2025_pnas`).
4. **Bullet 3 (Allosteric GRP78 ATPase inhibition by YUM70):**  
   - *Key finding:* The discovery, structural docking to the C-terminal substrate-binding domain, and in vivo characterization of the small-molecule GRP78 inhibitor YUM70 rests entirely on **a single laboratory: Pinku Mukherjee's group at the University of North Carolina at Charlotte** (`samanta2021_canres`).

---

## 2. Dedicated Entry: The GRP78 Mechanistic Paradox in Metabolic Disease

### Prior Documentation Status
- In [data/staging/thread2_argon_raw.md](../data/staging/thread2_argon_raw.md), the conflict is briefly noted in narrative prose under Section C "Contested" (line 109) and Section D "Contradictions" (line 122).
- In [docs/thread2_verification.md](thread2_verification.md), Section 3D (lines 79–81) verified the individual substantive claims of `kammoun2009_jci`, `ye2010_diabetes`, and `angelini2022_natcommun`.
- However, prior project documentation lacked a dedicated, structured conflict analysis with paraphrased abstract claims and mechanistic reconciliation. This entry formalizes that paradox.

### Structured Conflict Analysis

| Study Registry ID | Full Citation & DOI | Experimental Manipulation | Model / System | Abstract-Level Finding (Paraphrase & Quote < 15 Words) | Direction of Effect on Insulin Sensitivity & Steatosis |
|---|---|---|---|---|---|
| **`kammoun2009_jci`** | Kammoun et al., *J Clin Invest*, 2009<br>DOI: [10.1172/JCI37007](https://doi.org/10.1172/JCI37007) | Adenoviral **overexpression** of GRP78 chaperone in liver | *ob/ob* obese mice | Adenoviral GRP78 expression in obese mouse liver lowered ER stress and blocked SREBP-1c cleavage, noting *"hepatic triglyceride and cholesterol contents were reduced, and insulin sensitivity improved"* (11 words), mediated by IRS-2 restoration. | **Protective:** Increasing GRP78 folding capacity in the ER lumen rescues insulin signaling and resolves steatosis. |
| **`ye2010_diabetes`** | Ye et al., *Diabetes*, 2010<br>DOI: [10.2337/db09-0755](https://doi.org/10.2337/db09-0755) | Whole-body heterozygous **gene deletion** (`Grp78+/-`, ~50% reduction) | Male *Grp78(+/-)* mice on high-fat diet (HFD) | Partial GRP78 gene deletion in high-fat-diet mice elevated energy expenditure, demonstrating that *"Grp78(+/-) mice are resistant to diet-induced hyperinsulinemia, liver steatosis"* (8 words) and hyperglycemia via adaptive UPR and EDEM upregulation. | **Protective:** Partial loss of GRP78 gene dosage triggers an adaptive/hormetic UPR that resists obesity, steatosis, and insulin resistance. |
| **`angelini2022_natcommun`** | Angelini et al., *Nat Commun*, 2022<br>DOI: [10.1038/s41467-022-35310-5](https://doi.org/10.1038/s41467-022-35310-5) | Continuous systemic **protein infusion** of recombinant GRP78 / HSP70 vs. neutralizing monoclonal antibodies | Chow-fed vs. HFD-fed rats; human NASH patient sera | Prolonged systemic delivery of GRP78/HSP70 in rats triggered metabolic pathology, showing *"infusion of Heat-Shock-Protein70 and Glucose-Regulated Protein78 caused insulin-resistance, hyperglycemia, and non-alcoholic steato-hepatitis"* (13 words), whereas neutralizing antibodies reversed phenotypes in HFD rats. | **Pathogenic:** Extracellular/circulating GRP78 acts as a causal driver of insulin resistance and NASH; antibody neutralization is therapeutic. |

### Mechanistic Reconciliation
[Inference] The apparent contradiction between GRP78 gain-of-function (`kammoun2009_jci`) and loss-of-function (`ye2010_diabetes`) resolving insulin resistance, contrasted with circulating GRP78 provoking disease (`angelini2022_natcommun`), can be reconciled across three distinct biological dimensions:
1. **Cellular Compartmentalization (Intracellular vs. Extracellular):** [Inference] Intracellular ER-luminal GRP78 acts as an essential chaperone maintaining protein folding and suppressing IRE1$\alpha$/PERK stress kinases (`kammoun2009_jci`). [Inference] Under severe chronic ER stress, GRP78 escapes to the cell surface and is secreted into circulation, where extracellular GRP78 acts as a pathogenic paracrine/endocrine driver of hepatic insulin resistance and steatohepatitis (`angelini2022_natcommun`).
2. **Hormetic Genetic Compensation (Gene Dosage Thresholds):** [Inference] A 50% partial reduction in GRP78 gene dosage (`Grp78+/-`) does not cause proteotoxic collapse; instead, it triggers a compensatory "adaptive UPR" via ATF6 upregulation and EDEM induction in white adipose tissue, enhancing overall ER quality control and energy expenditure (`ye2010_diabetes`).
3. **Relevance to PSTi8 Pharmacology:** [Inference] Pancreastatin inhibitor PSTi8 is proposed to bind GRP78 at the cell membrane or intracellularly. [Inference] Because complete GRP78 inhibition could trigger apoptotic UPR (CHOP) while circulating GRP78 neutralization is beneficial, PSTi8's therapeutic efficacy depends critically on whether it acts as an extracellular neutralizing agent, an allosteric chaperone modulator, or an inhibitor of cell-surface GRP78 signaling complexes.

> [!NOTE]
> [Inference] This mechanistic reconciliation represents a hypothetical model to test in future studies rather than an established empirical finding.

---

## 3. Systematic Audit of Biological Sex Reporting in Abstracts (`sex=NOT_READ`)

> [!IMPORTANT]
> **Sex Provenance Rule:** MeSH indexing is an interpretive bibliographic hint only and must never be used as an authoritative source to fill animal sex fields in `data/evidence_table.csv`. In accordance with AGENTS.md, biological sex must be verified directly from the published abstract or open full-text methods, or coded `sex=NOT_READ`.

Following AGENTS.md Rule 1 ("never guess or fill from memory"), each paper was audited strictly against its published abstract. Of the 32 verified records, exactly **25 rows do NOT state animal or subject sex in the abstract** and are coded `sex=NOT_READ`:

| ID | Citation | DOI | Study Type | Stated System in Abstract | Audit of Abstract & Basis for `sex=NOT_READ` | Sex Provenance (For Context) |
|:---|:---|:---|:---:|:---|:---|:---|
| `matsumoto2003_jci` | Matsumoto et al., 2003 | 10.1172/JCI18816 | primary | "L-lambdaKO mice" | Abstract states only "mice"; no sex specified. `sex=NOT_READ` | Full-text read: male (PMC193669, Methods Section 2.1) |
| `ozcan2004_science` | Ozcan et al., 2004 | 10.1126/science.1103160 | primary | "diet-induced and genetic obesity" | Abstract states only "mice"; no sex specified. `sex=NOT_READ` | not checked |
| `mcmanus2005_emboj` | McManus et al., 2005 | 10.1038/sj.emboj.7600633 | primary | "homozygous knockin mice" | Abstract states "knockin mice"; no sex specified. `sex=NOT_READ` | not checked |
| `dong2006_jci` | Dong et al., 2006 | 10.1172/JCI25735 | primary | "LKO::Irs1-/- mice" | Abstract states only "mice"; no sex specified. `sex=NOT_READ` | not checked |
| `taniguchi2006_cmet` | Taniguchi et al., 2006 | 10.1016/j.cmet.2006.04.005 | primary | "mouse liver" | Abstract states "mouse liver"; no sex specified. `sex=NOT_READ` | not checked |
| `kubota2008_cmet` | Kubota et al., 2008 | 10.1016/j.cmet.2008.05.007 | primary | "Irs1- and Irs2-deficient mice" | Abstract states only "mice"; no sex specified. `sex=NOT_READ` | not checked |
| `patel2008_mcb` | Patel et al., 2008 | 10.1128/MCB.00763-08 | primary | "mice lacking GSK-3beta" | Abstract states "mice lacking GSK-3beta"; no sex specified. `sex=NOT_READ` | not checked |
| `kammoun2009_jci` | Kammoun et al., 2009 | 10.1172/JCI37007 | primary | "ob/ob mice" | Abstract states "ob/ob mice"; no sex specified. `sex=NOT_READ` | MeSH-indexed: Male |
| `nakamura2009_jbc` | Nakamura et al., 2009 | 10.1074/jbc.M901488200 | primary | "H4IIEC3 cells" | In vitro rat hepatoma cell line; no animal sex in abstract. `sex=NOT_READ` | not checked |
| `cheng2009_natmed` | Cheng et al., 2009 | 10.1038/nm.2049 | primary | "mice with insulin resistance" | Abstract states "mice"; no sex specified. `sex=NOT_READ` | not checked |
| `li2010_febslett` | Li et al., 2010 | 10.1016/j.febslet.2010.01.044 | primary | "HepG2 cells" | In vitro human hepatoma cell line; no sex in abstract. `sex=NOT_READ` | not checked |
| `gao2010_jbc` | Gao et al., 2010 | 10.1074/jbc.M110.128694 | primary | "db/db mouse livers & HepG2" | Abstract states "db/db mouse livers"; no sex specified. `sex=NOT_READ` | not checked |
| `li2011_cmet` | Li et al., 2011 | 10.1016/j.cmet.2011.03.009 | primary | "insulin-resistant mice" | Abstract states "insulin-resistant mice"; no sex specified. `sex=NOT_READ` | MeSH-indexed: Male |
| `yecies2011_cmet` | Yecies et al., 2011 | 10.1016/j.cmet.2011.06.002 | primary | "LTsc1KO mice" | Abstract states "LTsc1KO mice"; no sex specified. `sex=NOT_READ` | MeSH-indexed: Male |
| `li2013_endocrinology` | Li et al., 2013 | 10.1210/en.2012-2127 | primary | "Hep-Rq mice" | Abstract states "Hep-Rq mice" & "ob/ob mice"; no sex specified. `sex=NOT_READ` | MeSH-indexed: Male, Female |
| `zhang2013_plosone` | Zhang et al., 2013 | 10.1371/journal.pone.0080071 | primary | "breast and prostate cancer cells" | In vitro human cell lines (MCF-7, LNCaP); no animal sex in abstract. `sex=NOT_READ` | not checked |
| `kimura2020_biomol` | Kimura et al., 2020 | 10.3390/biom10101445 | review | "hepatocyte GPCRs" | Review article; no animal sex specified in abstract. `sex=NOT_READ` | not checked |
| `samanta2021_canres` | Samanta et al., 2021 | 10.1158/0008-5472.CAN-20-1540 | primary | "in vivo preclinical models" | Abstract states "in vivo preclinical models"; no sex specified. `sex=NOT_READ` | Full-text read: female (PMC8137563 Methods) |
| `nasce2022_antiox` | Nascè et al., 2022 | 10.3390/antiox11061131 | review | "hepatic redox homeostasis" | Review article; no animal sex specified in abstract. `sex=NOT_READ` | Full-text read: review / not applicable |
| `pan2022_ijerph` | Pan et al., 2022 | 10.3390/ijerph192315965 | review | "GRP78 in lipid metabolism" | Review article; no animal sex specified in abstract. `sex=NOT_READ` | not checked |
| `angelini2022_natcommun` | Angelini et al., 2022 | 10.1038/s41467-022-35310-5 | primary | "rats on high-fat / chow diet" | Abstract states "rats" and "patients"; no sex specified. `sex=NOT_READ` | not checked |
| `lee2025_pnas` | Lee, 2025 | 10.1073/pnas.2412246122 | review | "GRP78/BiP translocation" | Perspective / review article; no animal sex specified in abstract. `sex=NOT_READ` | not checked |
| `yang2026_cells` | Yang et al., 2026 | 10.3390/cells15020109 | review | "Foxo1 research" | Review article; no animal sex specified in abstract. `sex=NOT_READ` | not checked |
| `li2026_theranostics` | Li et al., 2026 | 10.7150/thno.136060 | review | "GRP78 structure & targeting" | Comprehensive review; no animal sex specified in abstract. `sex=NOT_READ` | Full-text read: review / not applicable |
| `cruzvillarreal2026_kp` | Cruz-Villarreal et al., 2026 | 10.3390/kinasesphosphatases4030025 | review | "PKC isoforms in metabolic syndrome" | Review article; no animal sex specified in abstract. `sex=NOT_READ` | Full-text read: review / not applicable |

### The 7 Rows with Sex Explicitly Stated in Abstract
For completeness, biological sex was stated in the abstract for only 7 rows:
1. `ye2010_diabetes`: **Male** (*"Male Grp78(+/-) mice and their wild-type littermates"*).
2. `zhu2014_ajpendo`: **Male** (*"liver ERalpha-knockout (LKO) male mice"*).
3. `depaoli2024_ijms`: **Male & Ovariectomized Female** (*"ovariectomized female and male ApoE-/-:Ins2+/Akita mice"*).
4. `alves2025_pathophys`: **Male** (*"Methods: Male C57BL/6J mice were divided into four groups"*).
5. `depaoli2025_jes`: **Male & Female / Ovariectomized Female** (*"Male TALLYHO/JngJ mice... while females remain normoglycemic... Ovariectomized female mice..."*).
6. `franczak2026_biorxiv`: **Female / Ovariectomized Female** (*"middle-aged female mice (36-40 weeks) following ovariectomy"*).
7. `monteillet2026_biorxiv`: **Male & Female** (*"both NCK1betaKO male and female mice... only males showed improved insulin secretion"* — 11 words).

---

## 4. Statements to Downgrade from Established to Contested (single-lab)

Based on the laboratory independence audit in Section 1, the following four statements in Section C ("Established", lines 98–106) of [data/staging/thread2_argon_raw.md](../data/staging/thread2_argon_raw.md) rest on only one laboratory or laboratory network and are designated for downgrade:

| Bullet # | Stated Biological Claim (Paraphrase) | Originating Laboratory Network | Target Label |
|:---:|---|---|:---:|
| **Bullet 2** | Continuous systemic infusion of recombinant GRP78/HSP70 protein induces hyperglycemia, insulin resistance, and NASH in rodents, reversed by monoclonal antibody neutralization. | **Geltrude Mingrone's laboratory** (King's College London / Catholic University of the Sacred Heart, Rome; `angelini2022_natcommun`). *(Cell-surface GRP78-p85 complexing in cancer cells likewise rests on Amy S. Lee's laboratory, `zhang2013_plosone`).* | `Contested (single-lab)` |
| **Bullet 3** | The hydroxyquinoline compound YUM70 binds allosterically to the GRP78 substrate-binding domain ($\text{IC}_{50} = 1.5\ \mu\text{M}$) to inhibit ATPase activity and trigger pro-apoptotic ER stress. | **Pinku Mukherjee's laboratory** (University of North Carolina at Charlotte; `samanta2021_canres`). | `Contested (single-lab)` |
| **Bullet 7** | Palmitate and TNF-$\alpha$ selectively upregulate NADPH oxidase 3 (NOX3) to produce ROS driving JNK activation and hepatic insulin resistance, preventable by NOX3 siRNA knockdown. | **Jian Li's laboratory** (Hunan Normal University / Central South University, Changsha, China; `li2010_febslett` and `gao2010_jbc`). | `Contested (single-lab)` |
| **Bullet 8** | Hepatocyte-selective chemogenetic $G_q$ activation via transgenic `Hep-Rq` designer receptors acutely stimulates gluconeogenesis equaling glucagon's glycemic response, and endogenous vasopressin $V_{1\text{b}}$ antagonism reduces glucose excursions in *ob/ob* mice. | **Jürgen Wess's laboratory** (Molecular Signaling Section, NIDDK, National Institutes of Health, Bethesda, MD; `li2013_endocrinology`, `kimura2020_biomol`). | `Contested (single-lab)` |

*(Note: In accordance with project instructions, `data/staging/thread2_argon_raw.md` remains unmodified as originally generated; these downgrades govern downstream synthesis in Phase 1 topic notes).*

---

## 5. Audit of One-Line Relevance Going Beyond Abstract Claims

Each row in [data/staging/thread2_registry_unverified.csv](../data/staging/thread2_registry_unverified.csv) marked `verified: yes` was audited against its published abstract to detect quantitative parameters, experimental group sizes, or comparative claims that exceed the abstract text. All quoted passages are strictly **under 15 words**:

| ID | Verified | Quoted Passage Exceeding Abstract (< 15 Words) | Word Count | Exact Source Locator & Nature of Extension |
|---|:---:|---|:---:|---|
| **`matsumoto2003_jci`** | yes | `"male mice have ~50% lower refeeding-induced hepatic Srebp1c mRNA"` | 9 words | **Fig 2B & Methods Section 2.1.** The abstract only states induction was "inhibited" and refers to "mice"; the "~50%" figure is derived from Figure 2B bar graphs, and "male" is from Methods. |
| **`depaoli2025_jes`** | yes | `"fasting glucose 27.55 vs 7.9 mmol/L in females"` | 8 words | **Fig 1 Caption (`PMC11968335`).** The abstract only states that blood glucose exceeded the `>15 mM` threshold; the specific numerical values `27.55` and `7.9` appear verbatim only in Figure 1 caption. |
| **`samanta2021_canres`** | yes | `"IC50 = 1.5 +/- 0.3 uM (vs VER-155008 IC50 = 0.7 +/- 0.3 uM)"` | 13 words | **Full-Text Results (Section 'Identification of YUM70', `PMC8137563`).** The abstract states YUM70 binds and inhibits GRP78 ATPase activity, but omits IC50 values and the head-to-head VER-155008 comparator. |
| **`li2013_endocrinology`** | yes | `"equaling glucagon's hyperglycemic magnitude"` | 4 words | **Full-Text Discussion / Fig 1.** The abstract states CNO induced "pronounced increases in blood glucose levels"; the comparative equivalence to maximal glucagon is made in the full-text body. |
| **`zhang2013_plosone`** | yes | `"sGRP78 complexes with the p85 subunit of PI3K"` | 8 words | **Abstract Context Omission.** While the binding claim is verbatim, the one-liner omitted the essential disease limitation stated in the abstract: *"In hormonal therapy-resistant breast and prostate cancer cells"*, implying a general hepatocyte mechanism. |
| **`monteillet2026_biorxiv`** | yes | `"~50% lower CyclinA/B mRNA"` | 4 words | **Preprint Full-Text Fig 4.** The abstract reports that females exhibited "altered PERK pathway activation and increased numbers of small islets"; the specific `~50% lower CyclinA/B` figure is from Fig 4. |
| **`nasce2022_antiox`** | yes | `"noting ~56% NAFLD prevalence in T2D"` | 6 words | **Review Full-Text Section 3.** The abstract describes hepatic redox and NADPH oxidases; the exact epidemiological statistic `~56%` is from the narrative review text. |
| **`franczak2026_biorxiv`** | yes | `"n=9-11/group"` | 1 word | **Preprint Methods Section.** The abstract describes female ovariectomized mice (36–40 weeks), but group sample sizes `n=9-11/group` are specified only in Methods. |

*(Note on `alves2025_pathophys`: All five quantitative percentages—`28% body fat`, `19% basal`, `34% maximal respiration`, `43% triglycerides`, and `145% insulin sensitivity`—are present verbatim in the published publisher abstract on MDPI and PMC (`PMC11755535`), and therefore do not exceed the abstract.)*
