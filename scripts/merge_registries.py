#!/usr/bin/env python3
"""
scripts/merge_registries.py

Merges verified literature staging registries (Thread 1, Thread 2, Thread 3, Thread 6)
into the master data/papers_registry.csv per instructions in prompts/07_merge_registries.md.

1. Backs up current data/papers_registry.csv to data/staging/papers_registry_pre_merge.csv.
2. Identifies and quarantines rows with verified=no or could_not_open to data/staging/rejected_rows.csv.
3. Deduplicates rows by normalized DOI (case-insensitive).
4. Maintains controlled role vocabulary.
5. Adds published_version_of column for preprints and published counterparts.
6. Preserves existing Thread 3 corrections and rows without overwriting.
7. Produces comprehensive audit data for docs/registry_merge_report.md.
"""

import os
import csv
import shutil
import re

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
MASTER_CSV_PATH = os.path.join(REPO_ROOT, "data", "papers_registry.csv")
BACKUP_CSV_PATH = os.path.join(REPO_ROOT, "data", "staging", "papers_registry_pre_merge.csv")
REJECTED_CSV_PATH = os.path.join(REPO_ROOT, "data", "staging", "rejected_rows.csv")

STAGING_FILES = [
    ("Thread 3", os.path.join(REPO_ROOT, "data", "papers_registry.csv")),  # master currently holds verified T3
    ("Thread 1", os.path.join(REPO_ROOT, "data", "staging", "thread1_registry_unverified.csv")),
    ("Thread 2", os.path.join(REPO_ROOT, "data", "staging", "thread2_registry_unverified.csv")),
    ("Thread 6", os.path.join(REPO_ROOT, "data", "staging", "thread6_registry_unverified.csv")),
]

CONTROLLED_ROLES = {
    "primary_evidence",
    "pst_chga_biology",
    "background_mechanism",
    "sex_estrogen",
    "methods_reference",
    "review",
    "context_only"
}

OUTPUT_FIELDNAMES = [
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
    "verification_note",
    "published_version_of"
]

REJECTED_FIELDNAMES = [
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
    "verification_note",
    "rejection_reason"
]

def clean_doi(doi_str):
    if not doi_str:
        return ""
    d = doi_str.strip().lower()
    d = re.sub(r"^https?://(dx\.)?doi\.org/", "", d)
    d = re.sub(r"^doi:", "", d)
    return d.strip()

def run_merge():
    # 1. Back up current papers_registry.csv
    print(f"Backing up {MASTER_CSV_PATH} to {BACKUP_CSV_PATH}...")
    shutil.copyfile(MASTER_CSV_PATH, BACKUP_CSV_PATH)
    
    # Read existing master (Thread 3)
    with open(BACKUP_CSV_PATH, "r", encoding="utf-8") as f:
        master_rows = list(csv.DictReader(f))
    print(f"Master baseline: {len(master_rows)} rows (Thread 3)")

    seen_dois = {} # clean_doi -> index in final_rows
    final_rows = []
    rejected_rows = []
    thread_stats = {
        "Thread 3": {"staged": len(master_rows), "yes": 0, "partial": 0, "no": 0, "merged": 0, "rejected": 0, "duplicates": 0},
        "Thread 1": {"staged": 0, "yes": 0, "partial": 0, "no": 0, "merged": 0, "rejected": 0, "duplicates": 0},
        "Thread 2": {"staged": 0, "yes": 0, "partial": 0, "no": 0, "merged": 0, "rejected": 0, "duplicates": 0},
        "Thread 6": {"staged": 0, "yes": 0, "partial": 0, "no": 0, "merged": 0, "rejected": 0, "duplicates": 0},
    }

    # Step 1: Ingest Thread 3 (master rows) first
    for r in master_rows:
        v = r.get("verified", "").strip().lower()
        if v == "yes":
            thread_stats["Thread 3"]["yes"] += 1
        elif v == "partial":
            thread_stats["Thread 3"]["partial"] += 1
        else:
            thread_stats["Thread 3"]["no"] += 1

        c_doi = clean_doi(r.get("doi", ""))
        seen_dois[c_doi] = len(final_rows)
        r_out = {k: r.get(k, "") for k in OUTPUT_FIELDNAMES}
        r_out["published_version_of"] = ""
        final_rows.append(r_out)
        thread_stats["Thread 3"]["merged"] += 1

    # Step 2: Ingest other threads
    other_threads = [
        ("Thread 1", STAGING_FILES[1][1]),
        ("Thread 2", STAGING_FILES[2][1]),
        ("Thread 6", STAGING_FILES[3][1]),
    ]

    for thread_name, file_path in other_threads:
        with open(file_path, "r", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        thread_stats[thread_name]["staged"] = len(rows)

        for r in rows:
            v = r.get("verified", "").strip().lower()
            if v == "yes":
                thread_stats[thread_name]["yes"] += 1
            elif v == "partial":
                thread_stats[thread_name]["partial"] += 1
            else:
                thread_stats[thread_name]["no"] += 1

            # Quarantine check
            if v in ("no", "could_not_open"):
                thread_stats[thread_name]["rejected"] += 1
                rej_row = {k: r.get(k, "") for k in REJECTED_FIELDNAMES}
                rej_row["rejection_reason"] = r.get("verification_note", "Unverified or fabricated metadata")
                rejected_rows.append(rej_row)
                continue

            # Deduplication check by DOI
            c_doi = clean_doi(r.get("doi", ""))
            if c_doi in seen_dois:
                thread_stats[thread_name]["duplicates"] += 1
                idx = seen_dois[c_doi]
                existing_threads = final_rows[idx]["thread"].split(", ")
                if thread_name not in existing_threads:
                    existing_threads.append(thread_name)
                    final_rows[idx]["thread"] = ", ".join(existing_threads)
                print(f"Duplicate DOI found for {r['id']} ({c_doi}): merged threads to {final_rows[idx]['thread']}")
                continue

            # Add new row
            seen_dois[c_doi] = len(final_rows)
            r_out = {k: r.get(k, "") for k in OUTPUT_FIELDNAMES}
            r_out["published_version_of"] = ""

            # Validate role
            role = r_out.get("role", "")
            if role not in CONTROLLED_ROLES:
                raise ValueError(f"Invalid role '{role}' in {r['id']}")

            final_rows.append(r_out)
            thread_stats[thread_name]["merged"] += 1

    # Step 3: Handle published_version_of cross-referencing
    # Find preprints and published counterparts
    # goand2022_ssrn <-> goand2023_peptides
    # muntjewerff2025_biorxiv <-> muntjewerff2025_commbiol
    id_to_idx = {r["id"]: i for i, r in enumerate(final_rows)}

    pairs = [
        ("goand2022_ssrn", "goand2023_peptides"),
        ("muntjewerff2025_biorxiv", "muntjewerff2025_commbiol")
    ]

    for preprint_id, published_id in pairs:
        if preprint_id in id_to_idx and published_id in id_to_idx:
            p_idx = id_to_idx[preprint_id]
            pub_idx = id_to_idx[published_id]
            # Link bidirectionally
            final_rows[p_idx]["published_version_of"] = published_id
            final_rows[pub_idx]["published_version_of"] = preprint_id
            print(f"Linked preprint pair: {preprint_id} <-> {published_id}")

    # Write data/staging/rejected_rows.csv
    print(f"Writing {len(rejected_rows)} quarantined rows to {REJECTED_CSV_PATH}...")
    with open(REJECTED_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=REJECTED_FIELDNAMES)
        writer.writeheader()
        writer.writerows(rejected_rows)

    # Write data/papers_registry.csv
    print(f"Writing {len(final_rows)} merged rows to {MASTER_CSV_PATH}...")
    with open(MASTER_CSV_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=OUTPUT_FIELDNAMES)
        writer.writeheader()
        writer.writerows(final_rows)

    print("\n=== SUMMARY STATS ===")
    for t, s in thread_stats.items():
        print(f"{t}: staged={s['staged']}, yes={s['yes']}, partial={s['partial']}, no={s['no']}, merged={s['merged']}, rejected={s['rejected']}, duplicates={s['duplicates']}")
    print(f"Total merged in master: {len(final_rows)}")
    print(f"Total rejected: {len(rejected_rows)}")

if __name__ == "__main__":
    run_merge()
