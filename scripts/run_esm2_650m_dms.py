#!/usr/bin/env python3
"""
scripts/run_esm2_650m_dms.py

Full GPU/CPU-accelerated ESM-2 650M deep mutational scan (DMS) on human
Pancreastatin (PST-29) in the context of full-length human Chromogranin A
(UniProt P10645).

Model: facebook/esm2_t33_650M_UR50D (33 layers, 1280 hidden, 650M params).
Method: masked marginal log-likelihood ratio per variant:
    LLR = log P(mutant_aa | context) - log P(wt_aa | context)
Context: full-length human CHGA (457 aa, P10645). Mature PST-29 occupies
preprotein coordinates 291-319 (mature CHGA coordinates 273-301).
Scan: all 29 PST positions x 20 amino acids = 580 variants.
Output: data/structures/1d_sequences/esm2_650m_dms_scores.csv
    columns: position, wt_aa, mut_aa, llr_score, domain_region
    position = mature PST position (1-29); domain_region follows the
    Prompt 17 convention (N_Terminal_Polar_Head 1-13,
    Poly_Glu_Electrostatic_Latch 14-21, Cleaved_C_Terminal_Octapeptide 22-29).

Hardware note (Prompt 23): this VM has no GPU and no CUDA. The script uses
CUDA when available, otherwise CPU with bfloat16 weights (AVX512-BF16) and
low_cpu_mem_usage. Device/dtype actually used are printed and recorded.
"""

import os
import sys
import csv
import time
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
DIR_1D = os.path.join(REPO_ROOT, "data", "structures", "1d_sequences")
OUT_CSV = os.path.join(DIR_1D, "esm2_650m_dms_scores.csv")

MODEL_NAME = os.environ.get(
    "ESM2_MODEL_PATH", "facebook/esm2_t33_650M_UR50D")
AMINO_ACIDS = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L',
               'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

PST29_WT = "PEGKGEQEHSQQKEEEEEMAVVPQGLFRG"
PST_START_PREPROTEIN = 291  # 1-based preprotein coordinate of PST pos 1


def region_for(pos_1based):
    if pos_1based <= 13:
        return "N_Terminal_Polar_Head"
    if 14 <= pos_1based <= 21:
        return "Poly_Glu_Electrostatic_Latch"
    return "Cleaved_C_Terminal_Octapeptide"


def load_chga_full():
    fasta_path = os.path.join(DIR_1D, "P10645_CHGA_HUMAN.fasta")
    with open(fasta_path, "r") as f:
        lines = [line.strip() for line in f if not line.startswith(">")]
    seq = "".join(lines)
    assert len(seq) == 457, f"Expected 457 aa CHGA, got {len(seq)}"
    assert seq[PST_START_PREPROTEIN - 1:PST_START_PREPROTEIN - 1 + 29] == PST29_WT, \
        "PST-29 substring mismatch at preprotein 291-319"
    return seq


def main():
    os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
    torch.set_num_threads(max(1, os.cpu_count() or 4))

    print("=== GPU Environment Audit (Prompt 23, step 2) ===")
    print(f"torch version: {torch.__version__}")
    print(f"torch.cuda.is_available(): {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"device name: {torch.cuda.get_device_name(0)}")
        print(f"total memory (GB): {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f}")
        device = torch.device("cuda")
        dtype = torch.float16
    else:
        print("device name: none (no CUDA device on this machine)")
        print("total memory (GB): n/a - CPU-only host")
        device = torch.device("cpu")
        dtype = torch.bfloat16
    print(f"selected device: {device}, dtype: {dtype}")

    print(f"\nLoading {MODEL_NAME} ...")
    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForMaskedLM.from_pretrained(
        MODEL_NAME, dtype=dtype, low_cpu_mem_usage=True)
    model.to(device)
    model.eval()
    print(f"Model loaded in {time.time() - t0:.1f}s "
          f"({sum(p.numel() for p in model.parameters()) / 1e6:.0f}M params)")

    chga_full = load_chga_full()
    print(f"Full CHGA context: {len(chga_full)} aa (P10645)")

    # Pre-tokenize the unmasked full sequence once; each position is masked
    # in a cloned copy. ESM tokenizer: token 0 is <cls>, residue i (1-based)
    # sits at index i.
    base_inputs = tokenizer(chga_full, return_tensors="pt")
    base_ids = base_inputs["input_ids"].to(device)

    rows = []
    highlights = {}
    t_start = time.time()
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["position", "wt_aa", "mut_aa", "llr_score", "domain_region"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for pos_idx in range(len(PST29_WT)):
            pos_1based = pos_idx + 1
            wt_aa = PST29_WT[pos_idx]
            chga_pos = PST_START_PREPROTEIN + pos_idx  # 1-based preprotein
            region = region_for(pos_1based)
            token_idx = chga_pos  # <cls> offset
            assert chga_full[chga_pos - 1] == wt_aa

            masked_ids = base_ids.clone()
            masked_ids[0, token_idx] = tokenizer.mask_token_id
            with torch.no_grad():
                logits = model(masked_ids).logits
                log_probs = torch.log_softmax(
                    logits[0, token_idx].float(), dim=-1)

            wt_tok = tokenizer.convert_tokens_to_ids(wt_aa)
            wt_logp = log_probs[wt_tok].item()
            for mut_aa in AMINO_ACIDS:
                if mut_aa == wt_aa:
                    llr = 0.0
                else:
                    mut_tok = tokenizer.convert_tokens_to_ids(mut_aa)
                    llr = log_probs[mut_tok].item() - wt_logp
                row = {"position": pos_1based, "wt_aa": wt_aa,
                       "mut_aa": mut_aa, "llr_score": f"{llr:+.4f}",
                       "domain_region": region}
                writer.writerow(row)
                rows.append(row)
                if (pos_1based, mut_aa) in ((25, "S"), (15, "K")):
                    highlights[(pos_1based, mut_aa)] = llr
            f.flush()
            print(f"pos {pos_1based:2d} ({wt_aa}, CHGA {chga_pos}): "
                  f"{time.time() - t_start:.1f}s elapsed", flush=True)

    print(f"\nSaved {len(rows)} DMS rows to {OUT_CSV} "
          f"in {time.time() - t_start:.1f}s total")

    # Highlights (means over the 19 non-wild-type substitutions per position).
    def mean_llr(positions):
        vals = [float(r["llr_score"]) for r in rows
                if r["position"] in positions and r["mut_aa"] != r["wt_aa"]]
        return sum(vals) / len(vals)

    g297s = highlights.get((25, "S"))
    e287k = highlights.get((15, "K"))
    latch_mean = mean_llr(set(range(14, 22)))
    anchor_mean = mean_llr(set(range(22, 30)))
    print("\n=== Highlights (ESM-2 650M, full CHGA context) ===")
    print(f"Gly297Ser (rs9658664; PST pos 25 G->S): LLR = {g297s:+.4f}")
    print(f"Glu287Lys (rs140089514; PST pos 15 E->K): LLR = {e287k:+.4f}")
    print(f"Mean LLR, poly-Glu latch (pos 14-21, non-WT): {latch_mean:+.4f}")
    print(f"Mean LLR, C-terminal anchor (pos 22-29, non-WT): {anchor_mean:+.4f}")


if __name__ == "__main__":
    main()
