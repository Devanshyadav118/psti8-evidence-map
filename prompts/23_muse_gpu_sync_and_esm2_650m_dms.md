---
prompt_id: 23
slug: muse_gpu_sync_and_esm2_650m_dms
target: "Meta Muse"
status: running
date: 2026-11-03
---

Step 0: Save this prompt verbatim to prompts/23_muse_gpu_sync_and_esm2_650m_dms.md (front matter: prompt_id: 23, slug: muse_gpu_sync_and_esm2_650m_dms, target: "Meta Muse", status: running, date: 2026-11-03). When the run ends, update status to done and record the git commit hash.

Read AGENTS.md, STATE.md, and docs/audit_report.md.

Task: (1) reconcile the 14 paywalled studies and sync the latest main branch, (2) benchmark GPU hardware capabilities, and (3) execute a full GPU-accelerated ESM-2 650M deep mutational scan (DMS) on Pancreastatin.

1. Literature Status & Repo Sync:
   - Regarding the 14 paywalled studies: keep them marked honestly as abstract_only in all registries and evidence tables. Leave unstated methodological parameters (sample size, exact sex, estrous staging) strictly as NOT_READ. Do not infer or impute missing data from disease models or MeSH terms. This paywall constraint is formally documented as a systematic review limitation under PRISMA 2020 in docs/audit_report.md and manuscript/manuscript.md.
   - Run `git pull origin main` to ensure your local clone is up to date with the latest commits (through da0e20d, including manuscript/manuscript.md, manuscript/cover_letter.md, and figures/).

2. GPU Environment Audit:
   - Check and display GPU resources via Python/PyTorch:
     * torch.cuda.is_available(), torch.cuda.get_device_name(0), and torch.cuda.get_device_properties(0).total_memory / 1e9.
   - Confirm whether CUDA drivers and PyTorch GPU support are active.

3. ESM-2 650M Deep Mutational Scan (scripts/run_esm2_650m_dms.py):
   - Load the full 650M parameter protein language model `facebook/esm2_t33_650M_UR50D` onto CUDA.
   - Target sequence: Full mature WT human PST-29 (PEGKGEQEHSQQKEEEEEMAVVPQGLFRG) in the context of full-length human Chromogranin A (UniProt P10645, mature coordinates 273-301).
   - Perform a complete in silico deep mutational scan across all 29 positions (29 positions x 20 amino acids = 580 variants).
   - For each variant, compute the masked marginal log-likelihood ratio:
     LLR = log P(mutant_aa | context) - log P(wt_aa | context)
   - Specifically extract and highlight the scores for:
     a. Gly297Ser (rs9658664; mature PST pos 25, precursor CHGA pos 315)
     b. Glu287Lys (rs140089514; mature PST pos 15, precursor CHGA pos 305)
     c. Mean evolutionary tolerance of the penta-glutamate latch (EEEEEMAV, positions 14-21) vs. the C-terminal anchor (VPQGLFRG, positions 22-29).
   - Save the full dataset (position, wt_aa, mut_aa, llr_score, domain_region) to data/structures/1d_sequences/esm2_650m_dms_scores.csv.

4. Update STATE.md, INDEX.md, and prompts/INDEX.md. Run ./scripts/sync.sh and report:
   - GPU device name and allocated VRAM.
   - Confirmation of clean `git pull`.
   - Top-line ESM-2 650M LLR scores for Gly297Ser and Glu287Lys, and mean LLR for the poly-Glu latch vs C-terminal octapeptide.
