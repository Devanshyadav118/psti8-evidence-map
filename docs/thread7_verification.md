# Literature Audit & Verification Report: Thread 7 — Target Engagement & Biophysical Evidence

**Audit Date:** 2026-11-03  
**Auditor:** Antigravity (Gemini 3.8 Flash High)  
**Input:** Gemini 4 Argon Thread 7 Raw Staging Output ([data/staging/thread7_argon_raw.md](../data/staging/thread7_argon_raw.md))  
**Primary Standards:** Official PubMed/MEDLINE, Crossref, and PubMed Central (PMC) full-text records  
**Related Vault Assets:** [data/papers_registry.csv](../data/papers_registry.csv), [docs/gap_map.md](gap_map.md), [docs/tool_usage_log.md](tool_usage_log.md), [data/structures/3d_models/af3_interface_contacts.csv](../data/structures/3d_models/af3_interface_contacts.csv)

---

## 1. Executive Summary & Verification of 8 Candidate Papers

Argon presented 8 literature records in [data/staging/thread7_argon_raw.md](../data/staging/thread7_argon_raw.md). Each candidate was audited against PubMed, Crossref, and PMC:

1. **Mapping to Existing Registry Entries (No Duplicate IDs):**
   * All 8 candidate papers were already catalogued in [data/papers_registry.csv](../data/papers_registry.csv):
     * `biswas2014_plosone` (DOI: `10.1371/journal.pone.0084132`) $\rightarrow$ Pre-existing record `biswas2014_plosone` (Thread 1); thread updated to `Thread 1, Thread 7`.
     * `allu2014_jbc` (DOI: `10.1074/jbc.M113.520916`) $\rightarrow$ Pre-existing record `allu2014_jbc` (Thread 1); thread updated to `Thread 1, Thread 7`, status upgraded to `full_text_read`.
     * `valicherla2018_scirep` (DOI: `10.1038/s41598-018-27018-8`) $\rightarrow$ Pre-existing record `valicherla2018` (Thread 3); thread updated to `Thread 3, Thread 7`.
     * `gupta2019_biopha` (DOI: `10.1016/j.biopha.2019.108959`) $\rightarrow$ Pre-existing record `gupta2019_dex` (Thread 3); thread updated to `Thread 3, Thread 7`.
     * `allu2022_diabetes` (DOI: `10.2337/db21-0289`) $\rightarrow$ Pre-existing record `allu2022_diabetes` (Thread 1); thread updated to `Thread 1, Thread 7`.
     * `garg2023_review` (DOI: `10.1007/s00726-023-03252-x`) $\rightarrow$ Pre-existing record `garg2023_review` (Thread 3); thread updated to `Thread 3, Thread 7`.
     * `garg2023_aminoacids` (DOI: `10.1007/s00726-023-03332-y`) $\rightarrow$ Pre-existing record `garg2023_aminoacids` (Thread 3); thread updated to `Thread 3, Thread 7`.
     * `tshikudi2024_ijms` (DOI: `10.3390/ijms252312757`) $\rightarrow$ Pre-existing record `tshikudi2024_colitis` (Thread 3); thread updated to `Thread 3, Thread 7`.
   * **Result:** 0 duplicate rows created. All 8 rows now carry the `Thread 7` tag in [data/papers_registry.csv](../data/papers_registry.csv).

2. **Systematic PMC ID Hallucinations by Argon:**
   * Argon cited three incorrect PMC identifiers:
     * Cited `PMC5993748` for `valicherla2018` (PMC5993748 is a paper on CDK7 in hepatocellular carcinoma). The authentic PMC identifier is **PMC5992141**.
     * Cited `PMC3924308` for `allu2014_jbc` (PMC3924308 is a paper on hyaluronan in vascular cells). The authentic PMC identifier is **PMC3924307**.
     * Cited `PMC11641510` for `tshikudi2024_colitis` (PMC11641510 is a clinical study on Parkinson's disease). The authentic PMC identifier is **PMC11641590** (and PubMed Central index PMC11641973).

---

## 2. Direct Full-Text Audit of Open-Access Literature (Items 2a–2d)

### 2A. Biswas 2014 ATPase $\text{IC}_{50}$ Value(s) (`PMC3896336`)
* **Argon Claim:** Claimed an $\text{IC}_{50} \sim 5.2\ \mu\text{M}$ with specific sub-values: "$6\ \mu\text{M} \pm 8.9\%$ for native GRP78 and $5.4\ \mu\text{M} \pm 4.3\%$ for 6xHis-GRP78".
* **Direct Full-Text Inspection:**
  * In Section "PST unexpectedly inhibits the ATPase enzymatic activity of GRP78...", the authors state:
    > "The IC50 for this inhibition was estimated at ~5.2 µM"
  * In Figure 4B legend, the authors explicitly state:
    > "IC50 of PST inhibition (by interpolation)"
  * Figure 4B displays inhibition points at $1\ \mu\text{M}$ (~25% inhibition) and $10\ \mu\text{M}$ (~60% inhibition).
* **Verdict:** Argon hallucinated the separate values "$6\ \mu\text{M} \pm 8.9\%$" and "$5.4\ \mu\text{M} \pm 4.3\%$". The actual text provides only a single interpolated estimate of $\sim 5.2\ \mu\text{M}$.

### 2B. Allu 2014 Helix Residues and % Helicity (`PMC3924307` / DOI `10.1074/jbc.M113.520916`)
* **Argon Claim:** Claimed $\alpha$-helicity in water of $\sim 13.5\%$ vs $\sim 5.1\%$, and a 7-residue helix spanning residues 282–288 (`HSQQKEE`).
* **Direct Full-Text Inspection:**
  * Circular dichroism (CD) spectra in water:
    * PST-WT: **$\sim 5.1\%$** $\alpha$-helix (increases to **$10.6\%$** in 30% trifluoroethanol [TFE]).
    * PST-287K: **$\sim 7.9\%$** $\alpha$-helix in water.
    * PST-297S: **$\sim 13.5\%$** $\alpha$-helix in water (increases to **$19.7\%$** in 30% TFE).
  * 200-ns explicit-solvent molecular dynamics (MD) simulations identified stable helical segments:
    * PST-WT: Glu280 to Met291 (12 residues).
    * PST-287K: Glu280 to Val293 (14 residues).
    * PST-297S: Gly275 to Val293 (19 residues).
  * Within the simulation trajectory, the core central segment `HSQQKEE` (residues 282–288) maintained persistent helical secondary structure and intra-peptide salt bridges (`Lys276–Glu284`, `Lys285–Glu289`).
* **Verdict:** Confirmed CD values ($\sim 13.5\%$ vs $\sim 5.1\%$ in water, rising to $19.7\%$ vs $10.6\%$ in TFE) and the core 7-residue helical segment (residues 282–288).

### 2C. Hossain 2018 GRP78 Docking Residues and Structure Numbering (`PMC5992141`)
* **Argon Claim:** Claimed Hossain 2018 docked onto PDB 5E84 and provided a "Table 1" detailing hydrogen bonds with Asp391, Asp390, Glu392, Leu443, Thr434, Tyr63, Glu427, Lys447.
* **Direct Full-Text Inspection:**
  * **Table 1 Content:** Table 1 in Hossain et al. (2018) is titled:
    > "AUC of GTT, ITT and PTT in high fat, high fructose and db/db mice"
    Table 1 contains zero docking data.
  * **Actual Docking Section & Figure:** Docking is reported in Section "PSTi8 competes with PST on GRP78 receptor binding" and illustrated in Figure 6.
  * **Target Structure & Numbering:** The Methods section specifies:
    > "docking studies of GRP78 (PDB ID: 3LDP)... performed using GRAMM-X"
    PDB 3LDP is the human GRP78 Nucleotide-Binding Domain (NBD, residues 26–407). PDB 3LDP utilizes canonical UniProt P11021 numbering.
  * **Reported Contact Residues:**
    * The text and Figure 6a–c report:
      > "PST and PSTi8 involved in making hydrogen bonds with Glu293, Ser300"
    * For PSTi8, the paper notes:
      > "makes few more hydrogen bonds with Tyr39, Asn55 and Arg60"
    * All five residues (Tyr39, Asn55, Arg60, Glu293, Ser300) reside within the NBD catalytic ATPase cleft.
* **Verdict:** Argon fabricated both PDB 5E84 and the docking table. The real paper used PDB 3LDP (canonical numbering, NBD) and reported residues Tyr39, Asn55, Arg60, Glu293, and Ser300 in Figure 6.

### 2D. Tshikudi 2024 Sex $\times$ Treatment Interaction vs Separate Analysis (`PMC11641590`)
* **Argon Claim:** Claimed Tshikudi 2024 analysed sexes separately without an omnibus interaction test.
* **Direct Full-Text Inspection:**
  * In Section 4.11 ("Statistical Analysis"):
    > "One-way ANOVA followed by Bonferroni or Tukey-post hoc analysis was performed"
  * In Figure 1 legend:
    > "Red significance signs compare conditions between female mice, whereas black signs compare conditions between male mice."
  * No two-way ANOVA, factorial ANOVA, or mixed-effects model testing an interaction term ($\text{Sex} \times \text{Treatment}$) was conducted.
* **Verdict:** Confirmed. Male and female cohorts were analyzed in isolation by one-way ANOVA per sex; no formal $\text{Sex} \times \text{Treatment}$ statistical interaction was evaluated.

---

## 3. Independent Audit of Argon's Absence Claims (15 Exa Searches)

Argon made three broad absence assertions: "no GRP78 knockdown", "no SPR/ITC", and "no AlphaFold model". Following the Tool Usage Policy, each assertion was evaluated with 5 targeted Exa semantic searches (15 searches total; logged in [docs/tool_usage_log.md](tool_usage_log.md); 0 Firecrawl credits consumed).

Per strict reporting rules, outcomes are phrased as "not found in $N$ searches":

1. **Claim 1: "No GRP78 (`HSPA5`) knockdown (`siRNA`/`shRNA`) or knockout in PST/PSTi8 studies":**
   * *Searches Conducted:*
     1. `GRP78 siRNA knockdown pancreastatin PSTi8 insulin resistance rescue`
     2. `HSPA5 shRNA silencing blocks pancreastatin or PSTi8 effect on glucose uptake`
     3. `BiP knockdown eliminates pancreastatin inhibitory action in hepatocytes`
     4. `GRP78 CRISPR knockout primary hepatocytes pancreastatin resistance PSTi8`
     5. `siRNA against GRP78 HSPA5 abolishes PSTi8 activation of AMPK or Akt`
   * *Finding:* Genetic knockdown or knockout of GRP78 demonstrating abolishment of PSTi8 activity was **not found in 5 searches**. Literature relies on correlative Western blot/qPCR and ATPase enzyme inhibition/mimicry (`VER-155008`, ADP).

2. **Claim 2: "No direct biophysical binding kinetics (SPR / ITC) for PST or PSTi8 with GRP78":**
   * *Searches Conducted:*
     1. `pancreastatin GRP78 surface plasmon resonance SPR binding affinity Kd`
     2. `PSTi8 HSPA5 isothermal titration calorimetry ITC binding thermodynamics`
     3. `surface plasmon resonance purified BiP GRP78 binding pancreastatin inhibitor`
     4. `isothermal titration calorimetry GRP78 pancreastatin PST Kd binding constant`
     5. `Biacore SPR binding kinetics of PSTi8 with recombinant human GRP78`
   * *Finding:* Quantitative biophysical affinity ($K_d$) or thermodynamic parameters ($\Delta H$, $\Delta S$) from surface plasmon resonance (SPR) or isothermal titration calorimetry (ITC) for PST or PSTi8 binding to purified GRP78 were **not found in 5 searches**. Binding evidence is limited to ligand-affinity pull-down (`biswas2014_plosone`) and whole-cell fluorescent competition (`valicherla2018`).

3. **Claim 3: "No published AlphaFold / AlphaFold-Multimer models of PST or PSTi8 bound to GRP78":**
   * *Searches Conducted:*
     1. `AlphaFold model of pancreastatin bound to GRP78 HSPA5`
     2. `AlphaFold-Multimer structure of PSTi8 complexed with GRP78 BiP`
     3. `AlphaFold 3 prediction of pancreastatin inhibitor PSTi8 receptor complex`
     4. `AlphaFold docking GRP78 pancreastatin CHGA co-folding structure`
     5. `in silico AlphaFold structure of GRP78 with pancreastatin variant Gly297Ser`
   * *Finding:* Peer-reviewed or preprint publications presenting AlphaFold, AlphaFold-Multimer, or AlphaFold 3 co-folded structures of GRP78 complexed with PST or PSTi8 were **not found in 5 searches**. Prior published in silico modeling was restricted to rigid-body GRAMM-X docking onto isolated domains (`valicherla2018`).

---

## 4. AlphaFold 3 Numbering Fix (+18 Offset) & Canonical Domain Boundaries

### 4A. Derivation of Canonical Coordinates
* **UniProt P11021 Precursor:** 654 amino acids.
* **Signal Peptide:** Residues 1–18 (cleaved in ER lumen).
* **Mature GRP78 Construct:** Residues 19–654 (636 amino acids).
* **AF3 Numbering Offset:** In the AlphaFold 3 mature receptor chain (Chain A, 1–636), residue index $i$ corresponds to UniProt canonical coordinate $i + 18$:
  $$\text{UniProt Canonical Coordinate} = \text{AF3 Chain Residue Number} + 18$$

### 4B. Standard Domain Boundaries (Re-Derived from 3LDL, 5EVZ, and P11021)
* **NBD (Nucleotide-Binding Domain):** UniProt residues 26–407 (crystal structures 3LDL residues 26–406; 5EVZ residues 26–407; mature chain residues 8–389).
* **Interdomain Linker:** UniProt residues 408–426 (mature chain residues 390–408; core linker `411-VGGSTRIPKIQQLVK-425` plus hinge residue `Ile426`).
* **$\text{SBD}\beta$ (Substrate-Binding Domain $\beta$-sandwich):** UniProt residues 427–537 (mature chain residues 409–519).
* **$\text{SBD}\alpha$ (Helical Lid Domain):** UniProt residues 538–633 (mature chain residues 520–615).
* **C-terminal Tail (KDEL):** UniProt residues 634–654 (mature chain residues 616–636).

### 4C. Recalibrated Contact Summary (Model 0, Contacts $< 4.0\ \text{Å}$)

| Peptide | Canonical GRP78 Residues Contacted | Domain Breakdown (Canonical) | Total Contacts |
|:---|:---|:---|:---:|
| **PSTi8** | `ILE426`, `GLU427`, `THR428`, `VAL429`, `THR434`, `PHE451`, `SER452`, `THR453`, `ALA454`, `GLN458`, `VAL461`, `GLY493`, `GLN496` | Linker: 1 residue (`ILE426`)<br>$\text{SBD}\beta$: 12 residues (`GLU427`–`GLN496`)<br>NBD: **0 residues** | 48 |
| **WT PST-29** | `MET196`, `ARG197`, `GLN401`, `LEU405`, `LEU416`, `LEU417`, `ILE426`, `GLU427`–`LYS516` (25 residues) | NBD: 4 residues (`MET196`–`LEU405`)<br>Linker: 3 residues (`LEU416`, `LEU417`, `ILE426`)<br>$\text{SBD}\beta$: 25 residues (`GLU427`–`LYS516`) | 140 |
| **E287K PST-29** | `MET196`, `ARG197`, `LEU405`, `LEU416`, `LEU417`, `ILE426`, `GLU427`–`VAL499` (20 residues) | NBD: 3 residues (`MET196`, `ARG197`, `LEU405`)<br>Linker: 3 residues (`LEU416`, `LEU417`, `ILE426`)<br>$\text{SBD}\beta$: 20 residues (`GLU427`–`VAL499`) | 137 |
| **G297S PST-29** | `ILE426`, `GLU427`–`VAL499` (19 residues) | Linker: 1 residue (`ILE426`)<br>$\text{SBD}\beta$: 19 residues (`GLU427`–`VAL499`)<br>NBD: **0 residues** | 79 |

---

## 5. Cross-Platform Comparison: AF3 Predicted Contacts vs Hossain 2018 Docking

A rigorous comparison between the contact residues reported by Hossain et al. (2018) from rigid-body docking onto isolated NBD (PDB 3LDP) and the contacts predicted across all 5 AF3 seeds (20 models in total) reveals:

* **Hossain 2018 Docking Residues (NBD Catalytic Pocket):** Tyr39, Asn55, Arg60, Glu293, Ser300 (UniProt canonical numbering 26–407).
* **AF3 Predictions across All 5 Seeds:**
  * **PSTi8 Complex (5 seeds):** In all 5 models, AF3 predicts PSTi8 engages the $\text{SBD}\beta$ cleft (UniProt 427–496) and interdomain linker hinge (`ILE426`), making **0 contacts with the NBD**. Overlap with Hossain 2018 docking residues is **0 residues (0% overlap)**.
  * **WT PST-29 Complex (5 seeds):** AF3 predicts extensive engagement of the $\text{SBD}\beta$ cavity (UniProt 427–516) and the interdomain linker (411–426), with contacts to the outer linker-adjacent surface of NBD (UniProt 196–198, 401, 405). Across all 5 seeds, AF3 predicts **0 contacts** with the catalytic ATPase cleft residues (39, 55, 60, 293, 300). Overlap with Hossain 2018 docking residues is **0 residues (0% overlap)**.
  * **E287K and G297S Complexes (5 seeds each):** In all 10 models, contacts are concentrated in $\text{SBD}\beta$ and the linker, with 0 contacts to catalytic pocket residues. Overlap is **0 residues (0% overlap)**.
* **Comparative Interpretation:** AF3 predicts an alternative, full-length binding mode in which peptides engage the client-binding $\text{SBD}\beta$ groove and interdomain linker rather than the catalytic nucleotide pocket. The observation that isolated NBD docking and full-length quaternary co-folding predict different binding loci highlights the necessity of experimental biophysical mapping (e.g., cross-linking mass spectrometry or point-mutant binding assays) to definitively resolve target engagement.

---

## 6. Audit Trail & File Synchronizations

The following vault files were updated to reflect this verification:
- [data/papers_registry.csv](../data/papers_registry.csv): Mapped all 8 Thread 7 papers; updated thread designations and `allu2014_jbc` status.
- [docs/tool_usage_log.md](tool_usage_log.md): Logged the 15 Exa semantic searches.
- [scripts/analyze_af3_complexes.py](../scripts/analyze_af3_complexes.py): Corrected domain annotation to use canonical UniProt coordinates ($+18$ offset).
- [data/structures/3d_models/af3_interface_contacts.csv](../data/structures/3d_models/af3_interface_contacts.csv): Regenerated with canonical UniProt numbering and accurate domain designations.
- [docs/structural_data_inventory.md](structural_data_inventory.md): Corrected AF3 chain-to-UniProt coordinates and domain breakdowns.
- [docs/gap_map.md](gap_map.md): Corrected AF3 contact coordinates and added Section "Target-Engagement Evidence & Cross-Platform Comparison".
- [notes/topics/06_structural_biophysics_and_variants.md](../notes/topics/06_structural_biophysics_and_variants.md): Corrected Section 5.5 coordinates and domain annotations.
