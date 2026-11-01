---
prompt_id: 04
slug: argon_search_template
status: TEMPLATE (Threads 1, 2, 3 DONE; Threads 4, 5, 6 not run)
tool: Google AI Studio
model: Gemini 4 Argon
legacy_name: "Prompt 3"
---
# 04 Argon literature-search template (one thread per chat)

**Model:** Gemini 4 Argon in Google AI Studio.
**Settings:** Grounding with Google Search ON, URL context ON, no system instructions, JSON mode OFF. New chat for every thread.
**Output:** copy the whole answer into `data/staging/threadN_argon_raw.md` in the repo.
**Rule:** Argon's output is a lead list, not evidence. Everything goes through prompt 03 (verification) before use.
**Note:** The scope blocks used for Threads 1 and 3 were not saved. Their results are in `sources/argon_raw/`.

## Prompt (fill in [SCOPE BLOCK])

```text
You are a research assistant doing a literature review for a computational biology project on PSTi8 (pancreastatin inhibitor peptide), the pancreastatin/CHGA pathway, and type 2 diabetes. Use Google Search and URL context. Do not answer from memory.

First open these files so you know what is already catalogued:
https://raw.githubusercontent.com/Devanshyadav118/psti8-evidence-map/main/data/evidence_table.csv
https://raw.githubusercontent.com/Devanshyadav118/psti8-evidence-map/main/data/papers_registry.csv
https://raw.githubusercontent.com/Devanshyadav118/psti8-evidence-map/main/data/staging/thread2_registry_unverified.csv

THREAD FOR THIS RUN: [SCOPE BLOCK]

Output plain text and one CSV code block, not JSON. Do not show your thinking.

RULES
- Run at least 10 different searches (PubMed, Europe PMC, bioRxiv/medRxiv). Include 2024-2026 work and label preprints. List every query.
- Find 20-30 papers: primary studies first, then systematic reviews, then narrative reviews.
- Include a paper only if you saw it in a search result or opened it this session. Give its own page URL (PubMed, DOI, publisher, or PMC), never an author profile. If you cannot confirm the DOI, write UNVERIFIED. Never fill in authors, years, DOIs, numbers or findings from memory.
- verified may be "yes" ONLY if you opened the paper's own page with URL context and title and DOI matched; otherwise "no".
- status must be honest: abstract_only / full_text_read / not_read.
- The registry row count must match the counts you state in LIMITS. Count the rows before you write LIMITS.
- Every summary bullet cites registry ids; every number must match the cited paper. Call a finding "Established" only if two or more independent labs support it (a lab network counts as one); otherwise label it "single-lab" and put it under Contested.
- Paraphrase; quotes under 15 words.

OUTPUT: A. SEARCH LOG (query | source | relevant hits). B. REGISTRY as one CSV block with columns id,citation,doi,year,type,thread,access,status,one_line_relevance,source_url,verified. C. KNOWLEDGE SUMMARY (Established, Contested, Unknown). D. CONTRADICTIONS (real disagreements only). E. OPEN QUESTIONS (marked as inference). F. LIMITS (what was not opened or verified, with exact counts).
```

(The earlier version listed only evidence_table.csv and thread3_registry_unverified.csv as the "already catalogued" files. The version above adds the master registry and Thread 2 so Argon does not repeat those papers. Thread 1 raw rows are also in the repo; add its staging CSV once prompt 02 has produced it.)

## Scope blocks

**Thread 2, signaling mechanisms (RUN, 32 rows returned, verified):**
"Thread 2, signaling mechanisms. Cover: pancreastatin and PSTi8 signaling through GRP78/HSPA5 and the unfolded protein response; GRP78 ATPase activity and insulin signaling; IRS1/2-PI3K-AKT-GSK3beta-FoxO1 in liver; PKC (including PKClambda/zeta) and SREBP-1c; NOX3-JNK oxidative stress; AMPK activation; Galpha q/11-PLCbeta-PKC signaling; hepatic gluconeogenic genes (PEPCK, G6Pase); sex hormone and estrogen effects on these pathways (estrogen receptor signaling, ER stress and AMPK in females); any evidence that GRP78 overexpression or Grp78 haploinsufficiency changes insulin sensitivity. Do not repeat papers already in the catalogued files."

**Thread 4, disease context (NOT RUN):**
"Thread 4, disease context. Cover: type 2 diabetes pathophysiology focused on hepatic insulin resistance and hepatic glucose production; MASLD/NASH and T2D; PCOS and insulin resistance; menopause, estrogen loss and metabolic risk; the current T2D drug landscape (metformin, GLP-1 receptor agonists, SGLT2 inhibitors, others) and unmet needs; peptide therapeutics in metabolic disease; sex differences in T2D prevalence, complications and drug response."

**Thread 5, related and competing approaches (NOT RUN):**
"Thread 5, related and competing approaches. Cover: other chromogranin A-derived peptide approaches (catestatin, vasostatin, PSTv1); other pancreastatin-pathway inhibitors; other GRP78/HSPA5 modulators studied in metabolic disease; peptides or small molecules aimed at hepatic gluconeogenesis; any patents, clinical trials or translational reports on PSTi8 or pancreastatin inhibitors; independent-lab replications. Do not repeat papers already in the catalogued files."

**Thread 6, methods and reporting standards (NOT RUN; the one that matters most for Direction 1):**
"Thread 6, methods and reporting standards. Cover: ARRIVE 2.0; NIH sex-as-a-biological-variable policy; published audits of sex inclusion and sex-based analysis in preclinical or metabolic animal research; SYRCLE risk-of-bias tool; methodology of systematic reviews of animal studies; power and sample size for sex-by-treatment interaction tests; estrous-cycle reporting; PRISMA 2020 and PRISMA-S; protocol registration options for animal-study reviews (PROSPERO, PreclinicalTrials.eu, OSF); validation of LLM-assisted screening and data extraction in systematic reviews."
