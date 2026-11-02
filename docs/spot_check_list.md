# Spot-Check Verification List: Batch 2 (Thread 3 Additions)

**Date:** 2026-11-02  
**Purpose:** Independent human verification of newly added data fields in [data/evidence_table.csv](../data/evidence_table.csv) and associated preprints against original primary manuscripts.

Below are 10 study rows from the newly verified Thread 3 literature additions to the master evidence table and registry. For each entry, key extracted values and their corresponding paper locators are provided for rapid audit against the source manuscript.

---

### 1. `gupta2019_dex` — Glucocorticoid Fatty Liver & AMPK Activation
* **Citation:** Gupta et al., *Biomed Pharmacother*, 2019; DOI: [10.1016/j.biopha.2019.108959](https://doi.org/10.1016/j.biopha.2019.108959)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 31108350)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) and HepG2 cells → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (abstract states "Twenty four mice were randomly divided into 4 groups" without specifying sex)*
  - `disease_model`: Dexamethasone-induced fatty liver disease / T2D → *Locator: Abstract*
  - `dose` & `route`: Acute 5 mg/kg, chronic 2 mg/kg, i.p. (DEX 1 mg/kg im) → *Locator: Abstract*
  - `key_result`: PSTi8 activates AMPK signaling via GRP78 and ameliorates glucocorticoid-induced fatty liver → *Locator: Abstract*

---

### 2. `valicherla2020_jpba` — LC-ESI-MS/MS Bioanalytical Assay & Pharmacokinetics
* **Citation:** Valicherla et al., *J Pharm Biomed Anal*, 2020; DOI: [10.1016/j.jpba.2019.113074](https://doi.org/10.1016/j.jpba.2019.113074)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 31891874)
* **Items to Verify:**
  - `species_strain`: Mouse plasma (healthy mice) → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (sex not stated in published abstract)*
  - `route`: Intravenous (IV) and intraperitoneal (IP) administration → *Locator: Abstract*
  - `key_endpoints`: Absolute bioavailability (52.74 ± 13.50%), SPE extraction recovery >55%, linearity 5–1000 ng/mL → *Locator: Abstract*
  - `interaction_tested`: `NOT_READ`

---

### 3. `singh2020_fetuina` — Fetuin-A Downregulation & Metformin Synergy
* **Citation:** Singh et al., *Heliyon*, 2020; DOI: [10.1016/j.heliyon.2020.e05133](https://doi.org/10.1016/j.heliyon.2020.e05133)
* **Access Level:** Full (Open Access PMC7533370)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) → *Locator: Section 2.2 ("Animals")*
  - `sex_male`: `yes` | `sex_female`: `no` → *Locator: Section 2.2 explicitly specifies "7–8 weeks old male C57BL/6 mice"*
  - `disease_model`: HFD (12 weeks) + STZ (100 mg/kg ip at wk 4) → *Locator: Section 2.3 & Figure 1*
  - `dose` & `n_per_group`: PSTi8 2 mg/kg alone, 1 mg/kg combo with Metformin 150 mg/kg; n=6 per group → *Locator: Section 2.3*
  - `key_result`: Combination of PSTi8 with metformin synergistically inhibited hepatic Fetuin-A and mitigated insulin resistance → *Locator: Abstract, Section 3.1–3.7*

---

### 4. `reza2021_mito` — Mitochondrial Dysfunction in Hepatic Steatosis
* **Citation:** Reza et al., *Life Sci*, 2021; DOI: [10.1016/j.lfs.2021.119905](https://doi.org/10.1016/j.lfs.2021.119905)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 34509503)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) and HepG2 cells → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (animal sex omitted in published abstract)*
  - `disease_model`: HFD-induced T2D and hepatic steatosis → *Locator: Abstract*
  - `key_endpoints`: Mitochondrial ROS, OCR, MMP, ATP, SREBP-1c, apoptosis, pro-inflammatory cytokines → *Locator: Abstract*
  - `interaction_tested`: `NOT_READ`

---

### 5. `goand2022_ssrn` — SSRN Preprint for Diet-Induced Obesity
* **Citation:** Goand et al., *SSRN Electronic Journal*, 2022; DOI: [10.2139/ssrn.4153464](https://doi.org/10.2139/ssrn.4153464)
* **Access Level:** Open Access Preprint (Elsevier SSRN)
* **Items to Verify:**
  - `type`: Preprint corresponding to published peer-reviewed journal article `goand2023_peptides` → *Locator: Title page*
  - `title`: Pancreastatin Inhibitor PSTi8 Balances Energy Homeostasis by Attenuating Adipose Tissue Inflammation in High Fat Diet Fed Mice → *Locator: Crossref / SSRN landing page*
  - `first_author`: Umesh K. Goand → *Locator: Author list*
  - `published_version_of`: Cross-linked to `goand2023_peptides` in master registry → *Locator: data/papers_registry.csv*

---

### 6. `goand2023_peptides` — Adipose Tissue Inflammation & M2 Polarization
* **Citation:** Goand et al., *Peptides*, 2023; DOI: [10.1016/j.peptides.2022.170902](https://doi.org/10.1016/j.peptides.2022.170902)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 36375661)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (animal sex omitted in published abstract)*
  - `disease_model`: Diet-induced obesity (DIO) in C57BL/6 mice → *Locator: Abstract*
  - `key_endpoints`: Body weight, eWAT adipocyte hypertrophy, SVF immunoprofiling (M1/M2 macrophages, Tregs), pAMPK, pAKT → *Locator: Abstract*
  - `key_result`: PSTi8 attenuated adipose inflammation, promoted M2 macrophage polarization, and restored mitochondrial function in DIO mice → *Locator: Abstract*

---

### 7. `goand2023_lifesci` — Continuous Osmotic Pump Delivery in Obesity
* **Citation:** Goand et al., *Life Sci*, 2023; DOI: [10.1016/j.lfs.2023.121415](https://doi.org/10.1016/j.lfs.2023.121415)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 36690282)
* **Items to Verify:**
  - `disease_model`: HFD diet-induced obesity / T2D in C57BL/6 mice → *Locator: Abstract*
  - `route` & `dose`: Subcutaneous Alzet osmotic minipump, release rate 2 mg/kg/day for 8 weeks → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (animal sex omitted in published abstract)*
  - `key_endpoints`: GTT, ITT, eWAT histology, mitochondrial ROS/MMP, Oroboros OCR, M1-to-M2 macrophage polarization → *Locator: Abstract*
  - `interaction_tested`: `NOT_READ`

---

### 8. `garg2023_ejp` — PST-Dependent and Independent Anti-Hyperglycemic Action
* **Citation:** Garg et al., *Eur J Pharmacol*, 2023; DOI: [10.1016/j.ejphar.2023.175559](https://doi.org/10.1016/j.ejphar.2023.175559)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 36681283)
* **Items to Verify:**
  - `species_strain`: Rat (streptozotocin-induced diabetic rats) and L6 / HepG2 cells → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (animal sex omitted in published abstract)*
  - `key_endpoints`: Blood glucose, plasma PST, insulin, glucagon, hepatic PEPCK/G6Pase, skeletal muscle P-Akt → *Locator: Abstract*
  - `key_result`: PSTi8 exhibited anti-hyperglycemic properties via both PST-dependent and independent pathways, enhancing muscle glucose disposal and reducing hepatic gluconeogenesis → *Locator: Abstract*

---

### 9. `garg2023_aminoacids` — Skeletal Muscle & Adipose Protection from FFA-Induced IR
* **Citation:** Garg et al., *Amino Acids*, 2023; DOI: [10.1007/s00726-023-03332-y](https://doi.org/10.1007/s00726-023-03332-y)
* **Access Level:** Abstract only (Springer paywall; PMID: 37721673)
* **Items to Verify:**
  - `species_strain`: Mouse (HFD-fed mice IR model) and 3T3-L1 / BMDM cells → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` → *Locator: Abstract (animal sex omitted in published abstract)*
  - `disease_model`: In vivo HFD-fed mice IR model + in vitro palmitate challenge → *Locator: Abstract*
  - `key_endpoints`: Glucose metabolism, skeletal muscle insulin sensitivity, adiposity, pro-inflammatory cytokines, BMDM M1 markers → *Locator: Abstract*
  - `interaction_tested`: `NOT_READ`

---

### 10. `tshikudi2024_jcag` — Colonic Mucosal Maintenance & Sex-Dependent Profiles
* **Citation:** Tshikudi et al., *J Can Assoc Gastroenterol*, 2024; DOI: [10.1093/jcag/gwad061.269](https://doi.org/10.1093/jcag/gwad061.269)
* **Access Level:** Open Access Conference Abstract Supplement (A269)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) → *Locator: Published abstract, Methods*
  - `sex_male`: `yes` | `sex_female`: `yes` → *Locator: Published abstract explicitly states "Male and female C57BL/6 mice were treated with PSTi8 (2.5mg/mL/kg, i.r.) or PBS for six days"*
  - `sex_analyzed_as_variable`: `yes (abstract-only)` → *Locator: Published abstract disaggregates findings by sex ("in females but not in male mice", "in both sexes")*
  - `interaction_tested`: `not_reported (abstract-only)` → *Locator: Published abstract (omnibus interaction test omitted)*
  - `key_result`: PSTi8 decreased epithelial proliferation in both sexes, but lowered differentiation and mucus while enhancing ER stress (CHOP) selectively in female mice → *Locator: Published abstract, Results & Conclusions*
