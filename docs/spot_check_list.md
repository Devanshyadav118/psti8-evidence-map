# Spot-Check Verification List

**Date:** 2026-10-28  
**Purpose:** Independent human verification of extracted data fields in [data/evidence_table.csv](../data/evidence_table.csv) against original primary papers.

Below are 10 randomly sampled study rows from the master evidence table. For each entry, key extracted values and their corresponding paper locators are provided for rapid audit against the source manuscript.

---

### 1. `valicherla2018` — Discovery of PSTi8
* **Citation:** Valicherla et al., *Sci Rep*, 2018; DOI: [10.1038/s41598-018-27018-8](https://doi.org/10.1038/s41598-018-27018-8)
* **Access Level:** Full (PMC Open Access: PMC6008391)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6J, db/db) and Rat (Sprague Dawley) → *Locator: Methods, "Animals" section*
  - `sex_male`: `yes` | `sex_female`: `no` → *Locator: Methods, "Animals" section specifies male animals exclusively*
  - `n_per_group`: `n=6-8` → *Locator: Methods, "Animals" & Figure legends*
  - `dose` & `route`: `0.3, 1, 3 mg/kg` via `i.p.` for `28 days` → *Locator: Methods, "Treatment protocol"*
  - `sex_analyzed_as_variable`: `no` | `interaction_tested`: `not_applicable`

---

### 2. `tshikudi2024_colitis` — Colitis & Sex-Dependent Epithelial Profile
* **Citation:** Tshikudi, Hutchison & Ghia, *Int J Mol Sci*, 2024; DOI: [10.3390/ijms252312757](https://doi.org/10.3390/ijms252312757)
* **Access Level:** Full (MDPI Open Access)
* **Items to Verify:**
  - `sex_male`: `yes` | `sex_female`: `yes` → *Locator: Section 4.1 ("Animals")*
  - `disease_model`: 5% DSS-induced colitis + steady-state homeostasis → *Locator: Section 4.2*
  - `route` & `dose`: Intrarectal, `10 µg/mouse (~2.5 mg/kg)` daily → *Locator: Section 4.3*
  - `key_result`: PSTi8 protective in males, deleterious in females → *Locator: Abstract, Section 2.1, Figure 1*
  - `estrous_controlled`: `NOT_READ` (verify if estrous staging is absent in Section 4.1)
  - `interaction_tested`: `NOT_READ` (verify if two-way ANOVA interaction term p-value is omitted in Section 4.9 & Results)

---

### 3. `valicherla2022_pk` — Pharmacokinetics in Rats
* **Citation:** Valicherla et al., *Molecules*, 2022; DOI: [10.3390/molecules27020339](https://doi.org/10.3390/molecules27020339)
* **Access Level:** Full (MDPI Open Access)
* **Items to Verify:**
  - `species_strain`: Rat (Sprague Dawley) → *Locator: Section 4.2 ("Animals")*
  - `sex_male`: `yes` | `sex_female`: `yes` (both sexes tested) → *Locator: Section 4.2 & Section 4.5*
  - `sex_analyzed_as_variable`: `yes` (PK parameters reported by sex) → *Locator: Tables 4 and 5*
  - `key_result`: Bioavailability ~95% IP and ~78% SC; no significant sex differences in PK → *Locator: Abstract, Section 2.5*
  - `interaction_tested`: `no`

---

### 4. `singh2020_heliyon` — Perimenopausal Steatohepatitis & ER Stress
* **Citation:** Singh et al., *Heliyon*, 2020; DOI: [10.1016/j.heliyon.2020.e05826](https://doi.org/10.1016/j.heliyon.2020.e05826)
* **Access Level:** Full (Heliyon Open Access: PMC7779780)
* **Items to Verify:**
  - `sex_male`: `no` | `sex_female`: `yes` → *Locator: Section 2.2 ("Female Wistar/SD rats")*
  - `disease_model`: VCD perimenopause + high-fructose diet (HFrD) → *Locator: Section 2.2*
  - `estrous_controlled`: `yes` (daily vaginal cytology monitoring) → *Locator: Section 2.3*
  - `dose` & `route`: PSTi8 1 mg/kg alone, 0.5 mg/kg with metformin, i.p. → *Locator: Section 2.2*

---

### 5. `yadav2024_pcos_let` — PCOS Letrozole Model
* **Citation:** Yadav et al., *Steroids*, 2024; DOI: [10.1016/j.steroids.2024.109558](https://doi.org/10.1016/j.steroids.2024.109558)
* **Access Level:** Abstract only (Elsevier paywall)
* **Items to Verify:**
  - `disease_model`: Letrozole (2 mg/kg) + 60% HFD-induced PCOS in rats → *Locator: Abstract*
  - `sex_male`: `no` | `sex_female`: `yes` → *Locator: Abstract (female-only disorder)*
  - `estrous_controlled`: `yes` (cyclicity monitored and restored) → *Locator: Abstract*
  - `dose` & `n_per_group`: `NOT_READ` (verify absence in abstract)

---

### 6. `yadav2025_pcos_dhea` — PCOS DHEA Model
* **Citation:** Yadav et al., *JPET*, 2025; DOI: [10.1016/j.jpet.2025.103765](https://doi.org/10.1016/j.jpet.2025.103765)
* **Access Level:** Abstract only (ASPET paywall)
* **Items to Verify:**
  - `disease_model`: DHEA (60 mg/kg s.c. × 21 d) + HFD-induced PCOS → *Locator: Abstract*
  - `dose`: PSTi8 10 mg/kg; metformin 300 mg/kg → *Locator: Abstract*
  - `sex_male`: `no` | `sex_female`: `yes` → *Locator: Abstract*
  - `estrous_controlled`: `yes` (cyclicity tracked as endpoint) → *Locator: Abstract*

---

### 7. `gupta2019_obesity` — Obesity & Hyperinsulinemia
* **Citation:** Gupta et al., *Eur J Pharmacol*, 2019; DOI: [10.1016/j.ejphar.2019.172723](https://doi.org/10.1016/j.ejphar.2019.172723)
* **Access Level:** Abstract only (Elsevier paywall; PMID: 31586632)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6) → *Locator: Abstract*
  - `disease_model`: Mini-osmotic insulin pump hyperinsulinemia for 4 weeks → *Locator: Abstract*
  - `dose`, `route`, `n_per_group`: `NOT_READ` (verify absence in abstract)
  - `key_endpoints`: MAPK/NOX3-JNK, adipokines, body weight → *Locator: Abstract*

---

### 8. `singh2019_menopause` — Perimenopausal Insulin Resistance
* **Citation:** Valicherla/Singh et al., *Peptides*, 2019; DOI: [10.1016/j.peptides.2019.170147](https://doi.org/10.1016/j.peptides.2019.170147)
* **Access Level:** Abstract only (Elsevier paywall)
* **Items to Verify:**
  - `first_author`: Check whether indexed under Valicherla GR vs Singh → *Locator: Header / Citation*
  - `disease_model`: VCD + OVX + HFD rat model → *Locator: Abstract*
  - `sex_male`: `no` | `sex_female`: `yes` (implied by OVX model) → *Locator: Abstract*
  - `dose`, `route`, `duration`: `NOT_READ` (verify absence in abstract)

---

### 9. `reza2022_lfs` — Hepatic Oxidative Stress & JNK
* **Citation:** Reza et al., *Life Sci*, 2022; DOI: [10.1016/j.lfs.2021.120221](https://doi.org/10.1016/j.lfs.2021.120221)
* **Access Level:** Abstract only (Elsevier paywall)
* **Items to Verify:**
  - `species_strain`: Mouse (C57BL/6J) in vivo + HepG2 in vitro → *Locator: Abstract*
  - `dose`: 1 mg/kg in vivo; 200 nM in vitro → *Locator: Abstract*
  - `duration`: 21 days → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` (verify if sex is omitted in abstract)

---

### 10. `dadge2023_nash` / `goand2023_nash` — NASH MCD Model
* **Citation:** Goand et al. (Dadge et al.), *Cytokine*, 2023; DOI: [10.1016/j.cyto.2023.156354](https://doi.org/10.1016/j.cyto.2023.156354)
* **Access Level:** Abstract only (Elsevier paywall)
* **Items to Verify:**
  - `first_author`: Verify first author is Goand UK (Dadge key retained for repository tracking) → *Locator: Article title page*
  - `disease_model`: MCD diet-induced NASH in C57BL/6 mice → *Locator: Abstract*
  - `sex_male` & `sex_female`: `NOT_READ` (verify omission in abstract)
  - `key_endpoints`: M1/M2 macrophages, fibrosis (α-SMA), ALT/AST → *Locator: Abstract*
