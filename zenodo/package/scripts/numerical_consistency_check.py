"""Search repository for numerical consistency of key values."""
import json
import os
import re

KEY_VALUES = [48, 113, 47, 328, 1328, 5742, 21670, 21608, 7183, 127, 609, 4612, 7844, 15598, 711]

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def search_files():
    findings = {}
    for key in KEY_VALUES:
        findings[key] = []
    
    for root, dirs, files in os.walk(REPO):
        dirs_to_skip = {'.git', '__pycache__', '.venv', 'node_modules', 'archive/superseded', 'archive/bugs'}
        dirs[:] = [d for d in dirs if d not in dirs_to_skip]
        
        for fname in files:
            if fname.endswith(('.py', '.json', '.jsonl', '.md', '.txt', '.csv')):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, 'r', errors='ignore') as f:
                        content = f.read()
                    for key in KEY_VALUES:
                        if str(key) in content:
                            findings[key].append(fpath.replace(REPO, '.'))
                except Exception:
                    pass
    
    return findings

def check_markdown_consistency():
    """Check markdown files for consistency of key numbers."""
    issues = []
    for root, dirs, files in os.walk(REPO):
        dirs[:] = [d for d in dirs if d not in {'.git', '__pycache__'}]
        for fname in files:
            if fname.endswith('.md'):
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath) as f:
                        content = f.read()
                    if '98.4%' in content:
                        issues.append(f"STALE: {fpath} still references 98.4% undercount (INVALIDATED)")
                    if '7,183' in content and 'BUG' not in content.upper() and 'INVALID' not in content.upper():
                        issues.append(f"CHECK: {fpath} references 7,183 without bug context")
                    if '7844' in content and 'BUG' not in content.upper() and 'CORRECTED' not in content.upper():
                        issues.append(f"CHECK: {fpath} references 7844 without correction context")
                except Exception:
                    pass
    return issues

def main():
    print("NUMERICAL CONSISTENCY CHECK")
    print("=" * 50)
    
    findings = search_files()
    for key, locations in findings.items():
        print(f"\n{key}: found in {len(locations)} files")
        if len(locations) <= 5:
            for loc in locations:
                print(f"  - {loc}")
    
    print("\n\nCONSISTENCY ISSUES")
    print("=" * 50)
    issues = check_markdown_consistency()
    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("  No issues found")
    
    print("\n\nCHECK COMPLETE")

if __name__ == "__main__":
    main()
