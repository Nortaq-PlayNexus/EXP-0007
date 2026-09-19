# EXP-0007 — Zenodo Release Preparation

## 1. GitHub Repository Setup

1. Create repository at https://github.com/<username>/EXP-0007
2. Push this repository to GitHub
3. Enable GitHub Pages (optional, for documentation)
4. Create release tag: `v1.0.0-r14`

## 2. Zenodo Connection

1. Go to https://zenodo.org
2. Sign in with GitHub account
3. Authorize Zenodo to access your GitHub repositories
4. Zenodo automatically creates a DOI for each GitHub release

## 3. Version Release

1. Create git tag:
   ```powershell
   git tag v1.0.0-r14
   git push origin v1.0.0-r14
   ```
2. Zenodo will generate a DOI automatically
3. The DOI will be linked to this specific commit

## 4. DOI Generation

Zenodo will provide:
- DOI: 10.5281/zenodo.XXXXXXX
- DOI URL: https://doi.org/10.5281/zenodo.XXXXXXX
- Citation BibTeX (available on Zenodo page)

## 5. Metadata

Zenodo uses GitHub repository metadata:
- Repository name
- Description (from repository README)
- License (from LICENSE file)
- Contributors (from GitHub repository)
- Version (from git tag)

## 6. Linking DOI Back to GitHub

The DOI is automatically linked to:
- The specific git commit tagged
- The repository on GitHub
- The release notes on GitHub

## 7. Preserving the Exact Release Version

1. The DOI points to a specific git commit
2. Future changes do NOT affect the DOI
3. New versions get new DOIs
4. All versions are archived permanently by Zenodo

## Important: No Endorsement

**The DOI is an archival/citation mechanism only.**

Zenodo is operated by CERN/OpenAIRE infrastructure. A DOI from Zenodo does NOT imply:
- CERN endorsement
- Scientific review
- Validation of EXP-0007
- CERN approval

The DOI simply provides a persistent, citable link to this specific version of the repository.
