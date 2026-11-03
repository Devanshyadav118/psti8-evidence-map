#!/usr/bin/env python3
"""
scripts/generate_dual_screening_sheet.py

Generates reproducible dual-screening and data extraction verification audit sheet
(data/dual_screening_audit.csv) across all 20 primary PSTi8 in vivo studies in
accordance with PRISMA-P and SYRCLE guidelines.

Screener 1 fields are pre-populated from the master evidence table and raw API records;
Screener 2 fields are set to 'pending' for independent secondary verification.
"""

import os
import csv
import json

def get_year_from_record(cite_str, raw_info):
    """Extract 4-digit publication year from citation string or raw metadata."""
    for part in cite_str.split(","):
        part = part.strip()
        if part.isdigit() and len(part) == 4:
            return part
    pubdate = raw_info.get("pubdate", "")
    for p in pubdate.split():
        if p.isdigit() and len(p) == 4:
            return p
    return "UNKNOWN"

def determine_sex_extracted(row):
    """Determine Screener 1 extracted sex: male, female, both, or not_read."""
    sm = row.get("sex_male", "").strip().lower()
    sf = row.get("sex_female", "").strip().lower()
    
    if sm == "yes" and sf == "yes":
        return "both"
    elif sm == "yes" and sf == "no":
        return "male"
    elif sm == "no" and sf == "yes":
        return "female"
    else:
        return "not_read"

def determine_interaction_status(row):
    """
    Determine Screener 1 interaction status: confirmed_absent vs unreported.
    Confirmed absent applies to dual-sex studies read in full text where statistical
    tests omit interaction testing (valicherla2022_pk, tshikudi2024_colitis).
    """
    it = row.get("interaction_tested", "").strip().lower()
    if it == "no":
        return "confirmed_absent"
    else:
        return "unreported"

def generate_reconciliation_note(pid, row, sex_val, it_val):
    """Generate comprehensive audit rationale for Screener 1 extraction."""
    access = row.get("access", "").strip()
    disease = row.get("disease_model", "").strip()
    sex_src = row.get("sex_source", "").strip()
    
    notes = []
    if access == "full":
        notes.append("Open full-text audited")
    elif access == "abstract":
        notes.append("Abstract-only audited (paywalled)")
    else:
        notes.append(f"Access tier: {access}")
        
    if sex_val == "both":
        notes.append(f"Dual-sex cohort in {disease}")
        if it_val == "confirmed_absent":
            notes.append("Factorial Sex x Treatment interaction testing confirmed absent in published statistics")
        else:
            notes.append("Omnibus interaction test statistics unreported")
    elif sex_val == "male":
        notes.append(f"Male-only cohort ({sex_src})")
    elif sex_val == "female":
        notes.append(f"Female-only cohort ({sex_src})")
    else:
        notes.append(f"Sex unstated in abstract; marked not_read per provenance rule (MeSH ignored)")
        
    return "; ".join(notes)

def main():
    repo_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    evidence_csv = os.path.join(repo_dir, "data", "evidence_table.csv")
    raw_json_path = os.path.join(repo_dir, "data", "staging", "all_26_verified_raw.json")
    output_csv = os.path.join(repo_dir, "data", "dual_screening_audit.csv")

    if not os.path.exists(evidence_csv):
        raise FileNotFoundError(f"Missing master evidence table: {evidence_csv}")
    
    raw_metadata = {}
    if os.path.exists(raw_json_path):
        with open(raw_json_path, "r", encoding="utf-8") as f:
            raw_metadata = json.load(f)

    audit_rows = []
    with open(evidence_csv, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            pid = row["paper_id"]
            raw_info = raw_metadata.get(pid, {})
            
            title = raw_info.get("title", "").strip().replace("\n", " ").replace("  ", " ")
            if not title:
                title = row.get("key_result", "").strip()
                
            first_author = raw_info.get("first_author", "").strip()
            if not first_author:
                first_author = row.get("citation", "").split()[0].replace(",", "")
                
            year = get_year_from_record(row.get("citation", ""), raw_info)
            doi = row.get("doi", "").strip()
            
            sex_extracted = determine_sex_extracted(row)
            interaction_status = determine_interaction_status(row)
            recon_note = generate_reconciliation_note(pid, row, sex_extracted, interaction_status)
            
            audit_rows.append({
                "study_id": pid,
                "doi": doi,
                "title": title,
                "first_author": first_author,
                "year": year,
                "screener1_inclusion": "included",
                "screener1_sex_extracted": sex_extracted,
                "screener1_interaction_status": interaction_status,
                "screener2_inclusion": "pending",
                "screener2_sex_extracted": "pending",
                "screener2_interaction_status": "pending",
                "agreement_status": "pending",
                "reconciliation_notes": recon_note
            })

    fieldnames = [
        "study_id",
        "doi",
        "title",
        "first_author",
        "year",
        "screener1_inclusion",
        "screener1_sex_extracted",
        "screener1_interaction_status",
        "screener2_inclusion",
        "screener2_sex_extracted",
        "screener2_interaction_status",
        "agreement_status",
        "reconciliation_notes"
    ]

    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(audit_rows)

    print(f"Generated dual-screening audit sheet with {len(audit_rows)} studies at: {output_csv}")

if __name__ == "__main__":
    main()
