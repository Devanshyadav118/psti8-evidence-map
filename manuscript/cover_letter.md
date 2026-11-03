# Cover Letter for Submission to *Biology of Sex Differences*

**Date:** November 3, 2026

**To:**  
The Editors-in-Chief and Editorial Board  
*Biology of Sex Differences*  
BioMed Central / Springer Nature  

**Subject:** Submission of Original Research Article: *"Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms"*

Dear Editors-in-Chief,

I am pleased to submit our original research manuscript entitled **"Targeting GRP78 with Pancreastatin Inhibitor PSTi8: A Systematic Evidence Audit of Preclinical Sex Bias and In Silico Structural Investigation of Binding Mechanisms"** for consideration as a Research Article in *Biology of Sex Differences*.

### Background & Rationale
Pancreastatin inhibitor PSTi8 (human chromogranin A residues 273–293-amide) is a promising peptide therapeutic developed to counter pancreastatin-driven insulin resistance, gluconeogenesis, and inflammatory macrophage polarization across metabolic indications. Despite extensive preclinical literature asserting its therapeutic potential via glucose-regulated protein 78 (GRP78/HSPA5) inhibition, the extent of compliance with the National Institutes of Health (NIH) Sex as a Biological Variable (SABV) mandate and the atomic-level structural mechanism of its receptor engagement have remained unaddressed.

### Key Findings & Fit with *Biology of Sex Differences*
Our study integrates a PRISMA-compliant systematic review, an ARRIVE 2.0 / SYRCLE risk-of-bias audit, mathematical factorial interaction power modeling, and full-length AlphaFold 3 neural co-folding (under physiological $\text{Mg}^{2+}$-ATP constraints). Our principal findings directly align with the core mission of *Biology of Sex Differences*:

1. **Systematic Preclinical Sex Segregation:** Auditing all 20 primary in vivo PSTi8 studies (within a broader 116-paper verified registry) revealed extreme disease-by-sex compartmentalization. Exactly 100% of primary type 2 diabetes and diet-induced obesity cohorts tested exclusively male rodents. Female rodents were evaluated exclusively in chemically or surgically induced reproductive failure models (PCOS and ovariectomy). Consequently, PSTi8 has never been evaluated in standard female models of type 2 diabetes.
2. **The Estrous Cycle Staging Deficit:** Across all female rodent cohorts, 0% (0/7 studies) performed baseline estrous cycle staging or synchronization, introducing uncharacterized cyclic hormonal variance into preclinical endpoints.
3. **The Subgroup Fallacy & Interaction Power Collapse:** In the three studies that evaluated both male and female animals, 0% (0/20) conducted a formal factorial $\text{Sex} \times \text{Treatment}$ interaction test. Non-central $t$-distribution modeling proves that standard preclinical sample sizes ($n = 6$ per group) possess $<19\%$ power to detect moderate interaction effects, demonstrating that published claims of sex-specific pharmacology reflect statistical noise rather than genuine sexual dimorphism.
4. **Refuting Active-Site Pocket Docking via AlphaFold 3:** Historical rigid-body docking claimed PSTi8 inserts into the catalytic nucleotide-binding domain (NBD) of GRP78. AlphaFold 3 quaternary co-folding refutes this model, demonstrating 0 contacts with the NBD. Instead, PSTi8 functions with high confidence (ipTM 0.81, min PAE 2.30 Å) as an allosteric steric wedge at the interdomain linker-hinge (Ile426) and $\text{SBD}\beta$ entrance (48 atomic contacts), uncoupling interdomain allostery without competing against millimolar cellular ATP.
5. **Resolution of the Gly297Ser Genetic Paradox:** We resolve why the human diabetogenic polymorphism Gly297Ser (rs9658664) collapses receptor binding (pairwise ipTM 0.28) while leaving the drug candidate intact: the substitution disrupts the hydrophobic $\text{SBD}\beta$ anchor, but because PSTi8 is truncated at residue 21, the inhibitor is structurally refractory to this common human risk allele.
6. **100% Cleft Interspecies Conservation:** The $\text{SBD}\beta$ binding pocket and linker exhibit 100.00% sequence identity between human, mouse, and rat, demonstrating that translational roadblocks stem from endocrine and methodological disparities rather than receptor sequence divergence.

### Declarations & Open Science Commitments
- **Originality:** This manuscript represents original work and is not under consideration for publication elsewhere in whole or in part.
- **Protocol Registration:** The study protocol was prospectively designed and registered on the Open Science Framework (OSF).
- **Open Data & Reproducibility:** In accordance with open-science principles, all curated datasets (evidence table, papers registry, dual-screening audit, SYRCLE/ARRIVE matrix, power modeling) and reproducible Python analysis scripts are publicly accessible under a Creative Commons Attribution 4.0 International license ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)) at:  
  `https://github.com/Devanshyadav118/psti8-evidence-map`
- **Conflicts of Interest:** The author declares no competing financial or commercial interests.
- **Funding:** No external financial support or commercial sponsorship was received for this work.

### Suggested Reviewers
We suggest the following independent experts with expertise in sex-as-a-biological-variable methodologies, preclinical reproducibility, and peptide-receptor biophysics:
1. **Natasha A. Karp, PhD** (Data Science and Quantitative Biology; Expert in Preclinical Sex Bias & Factorial Design; AstraZeneca / formerly Wellcome Sanger Institute)
2. **Franck Mauvais-Jarvis, MD, PhD** (Center for Sex-Based Biology & Medicine, Tulane University School of Medicine; Expert in Sexual Dimorphism in Diabetes and Metabolic Regulation)
3. **Malcolm R. Macleod, PhD, FRCP** (Centre for Clinical Brain Sciences, University of Edinburgh; Co-founder of CAMARADES; Expert in Preclinical Systematic Reviews & SYRCLE / ARRIVE Reporting Guidelines)
4. **Amy S. Lee, PhD** (Department of Biochemistry and Molecular Medicine, Keck School of Medicine, University of Southern California; World Authority on GRP78 / BiP Biology and Stress Signaling)

Thank you very much for your time, consideration, and editorial guidance. We look forward to receiving the reviewers' constructive feedback.

Sincerely,

**Devansh Pratap Singh**  
Lead Author & Corresponding Investigator  
Computational Structural Biology & Preclinical Methodology Framework  
Lucknow, Uttar Pradesh, India  
Email: devansh.research.repo@gmail.com  
Repository: [https://github.com/Devanshyadav118/psti8-evidence-map](https://github.com/Devanshyadav118/psti8-evidence-map)
