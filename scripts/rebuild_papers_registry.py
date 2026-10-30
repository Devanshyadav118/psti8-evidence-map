#!/usr/bin/env python3
import csv

input_path = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/staging/thread3_registry_unverified.csv"
output_path = "/home/devansh/Downloads/Devansh projects/psti8-sex-bias-review/data/papers_registry.csv"

# Four open-access studies actually read in full text in this project
FULL_TEXT_READ_IDS = {
    "valicherla2018",
    "singh2020_heliyon",
    "valicherla2022_pk",
    "tshikudi2024_colitis"
}

REVIEWS = {
    "garg2023_review",
    "lu2025_fimmu",
    "maj2025_fimmu",
    "christoffersson2026_fcdhc"
}

with open(input_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

out_fieldnames = [
    "id",
    "citation",
    "doi",
    "year",
    "type",
    "thread",
    "access",
    "status",
    "role",
    "one_line_relevance",
    "source_url",
    "verified",
    "verification_note"
]

out_rows = []
for r in rows:
    pid = r["id"]
    
    # Determine status
    if pid in FULL_TEXT_READ_IDS:
        r["status"] = "full_text_read"
    else:
        r["status"] = "abstract_only"
        
    # Determine role
    if pid == "singla2026_jri":
        r["role"] = "context_only"
    elif pid in REVIEWS:
        r["role"] = "review"
    else:
        r["role"] = "primary_evidence"
        
    out_rows.append({k: r.get(k, "") for k in out_fieldnames})

with open(output_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

print(f"Rebuilt {len(out_rows)} rows in {output_path}")
