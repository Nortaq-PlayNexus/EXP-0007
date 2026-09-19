#!/usr/bin/env python3
"""Create Zenodo-ready release package."""
import os
import shutil
import json
import zipfile
import datetime

REPO = r'C:\Users\natha\AI_RESEARCH\EXP-0007'
ZENODO = os.path.join(REPO, 'zenodo')
PACKAGE = os.path.join(ZENODO, 'package')

def main():
    print("EXP-0007 Zenodo Package Generator")
    print("=" * 50)

    # Clean and create package directory
    if os.path.exists(PACKAGE):
        shutil.rmtree(PACKAGE)
    os.makedirs(PACKAGE)

    # Data files to include
    data_dirs = [
        ('results/r14', 'data/results'),
        ('research_continuation', 'data/research'),
    ]

    for src, dst in data_dirs:
        src_path = os.path.join(REPO, src)
        dst_path = os.path.join(PACKAGE, dst)
        if os.path.exists(src_path):
            os.makedirs(dst_path, exist_ok=True)
            for f in os.listdir(src_path):
                src_file = os.path.join(src_path, f)
                dst_file = os.path.join(dst_path, f)
                if os.path.isfile(src_file):
                    shutil.copy2(src_file, dst_file)
                    print(f"  Copied: {src} -> {dst}/{f}")

    # Copy documentation files
    docs_dir = os.path.join(PACKAGE, 'docs')
    os.makedirs(docs_dir, exist_ok=True)
    for f in ['bug-history.md', 'd1-bug-effect.md', 'final-interpretation.md',
               'what-we-know-dont-know.md', 'r14-validation.md',
               'propagation-implementation.md', 'propagation-features-analysis.md',
               'future-experiments.md', 'detector-improvement.md',
               'definitive-test-proposal.md', 'mathematical-background.md',
               'detector-analysis.md', 'experiment-overview.md']:
        src = os.path.join(REPO, 'docs', f)
        dst = os.path.join(docs_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: docs/{f}")

    # Copy scripts
    scripts_dir = os.path.join(PACKAGE, 'scripts')
    os.makedirs(scripts_dir, exist_ok=True)
    for f in ['run_r14.py', 'run_r14_lightweight.py', 'validate_environment.py',
               'qa_check.py', 'numerical_consistency_check.py']:
        src = os.path.join(REPO, 'scripts', f)
        dst = os.path.join(scripts_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: scripts/{f}")

    # Copy tests
    tests_dir = os.path.join(PACKAGE, 'tests')
    os.makedirs(tests_dir, exist_ok=True)
    for f in ['test_field_construction.py', 'test_propagation.py', 'test_winding.py',
               'test_detector.py', 'test_reproducibility.py', 'test_regression.py']:
        src = os.path.join(REPO, 'tests', f)
        dst = os.path.join(tests_dir, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: tests/{f}")

    # Copy core files
    for f in ['README.md', 'METHODS.md', 'RESULTS.md', 'CHANGELOG.md',
               'REPRODUCIBILITY.md', 'LIMITATIONS.md', 'metadata.json',
               'requirements.txt', 'pyproject.toml', 'environment.yml',
               'CITATION.cff', 'LICENSE', '.gitignore']:
        src = os.path.join(REPO, f)
        dst = os.path.join(PACKAGE, f)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"  Copied: {f}")

    # Create package manifest
    manifest = {
        "created": datetime.datetime.now().isoformat(),
        "repo_commit": "1ef180d",
        "zenodo_upload_type": "dataset",
        "files": [],
        "total_size_bytes": 0,
        "total_files": 0,
    }

    for root, dirs, files in os.walk(PACKAGE):
        for f in files:
            path = os.path.join(root, f)
            rel = os.path.relpath(path, PACKAGE)
            size = os.path.getsize(path)
            manifest["files"].append({
                "path": rel,
                "size_bytes": size,
            })
            manifest["total_size_bytes"] += size
            manifest["total_files"] += 1

    manifest_path = os.path.join(PACKAGE, 'manifest.json')
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    print(f"\nManifest created: {manifest['total_files']} files, {manifest['total_size_bytes'] / 1024:.1f} KB")

    # Create zip package
    zip_path = os.path.join(ZENODO, 'EXP-0007-zenodo-package.zip')
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(PACKAGE):
            for f in files:
                path = os.path.join(root, f)
                arcname = os.path.relpath(path, PACKAGE)
                zf.write(path, arcname)
    zip_size = os.path.getsize(zip_path)
    print(f"Zip package created: {zip_size / 1024:.1f} KB")

    # Create upload list
    upload_list = os.path.join(ZENODO, 'upload-list.txt')
    with open(upload_list, 'w') as f:
        for item in manifest["files"]:
            f.write(item["path"] + "\n")
    print(f"Upload list created: {len(manifest['files'])} files")

    print("\nPackage generation complete!")
    print(f"Package directory: {PACKAGE}")
    print(f"Zip file: {zip_path}")
    print(f"Upload list: {upload_list}")
    print(f"\nTo upload to Zenodo:")
    print(f"1. Go to https://zenodo.org/upload")
    print(f"2. Select 'Dataset' as upload type")
    print(f"3. Fill metadata from zenodo/doi-registration.md")
    print(f"4. Upload all files from zenodo/data/ directory")
    print(f"5. Or upload the zip: {zip_path}")

if __name__ == "__main__":
    main()
