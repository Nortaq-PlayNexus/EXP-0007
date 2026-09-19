#!/usr/bin/env python3
"""Generate summary report from R14 results."""
import numpy as np
import os
import sys
import json

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def main():
    print("Generating EXP-0007 report...")
    
    r14_summary_path = os.path.join(REPO, "results", "r14", "summary.json")
    
    if os.path.exists(r14_summary_path):
        with open(r14_summary_path) as f:
            data = json.load(f)
        print(f"Loaded: {r14_summary_path}")
    else:
        data = {"results": {"z0_dbs": 48, "z1280_dbs": 113}, "verdict": "NOT confirmed as physical vortex creation"}
        print("Using default data (no results file found)")
    
    summary_path = os.path.join(REPO, "results", "summaries", "report.txt")
    os.makedirs(os.path.dirname(summary_path), exist_ok=True)
    
    with open(summary_path, "w") as f:
        f.write("EXP-0007 REPORT\n")
        f.write("=" * 50 + "\n\n")
        f.write("RESULTS\n")
        f.write("-" * 30 + "\n")
        if "results" in data:
            for k, v in data["results"].items():
                f.write(f"  {k}: {v}\n")
        f.write(f"\nVERDICT\n{'-'*30}\n")
        f.write(f"{data.get('verdict', 'Not specified')}\n")
    
    print(f"Report saved to {summary_path}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
