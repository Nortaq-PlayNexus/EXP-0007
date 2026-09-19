# EXP-0007 Data Provenance

## Data Classification

### RAW DATA
Original experimental outputs, unmodified:
- `research_continuation/` — All original R1-R14 JSON/CSV outputs
- `research_continuation/r14_summary.json`
- `research_continuation/CONTINUATION_FINAL.json`
- `research_continuation/FINAL_MANIFEST.json`
- `corpus/` — File inventories, hash manifests, evidence manifests

### PROCESSED DATA
Derived from raw data with documented transformation:
- `results/r14/` — R14 phase results (derived from research_continuation/)
- `metadata.json` — Project metadata (derived from FINAL_MANIFEST.json)

### DERIVED RESULTS
Statistical analyses and summaries:
- `results/tables/` — Comparison tables
- `results/summaries/` — Summary reports
- `docs/r14-validation.md` — R14 documentation (derived from R14 phases)

### FIGURES
Publication-quality plots:
- `results/figures/` — Generated from scripts/reproduce_figures.py

### REPORTS
Final interpretations:
- `README.md` — Master report
- `docs/experiment-overview.md` — Experiment summary
- `CHANGELOG.md` — Change history

## Provenance Chain

```
vortex_crystal_field (raw simulation)
→ propagate_fresnel / ASM (simulation)
→ DeepBeamScan.find_features (detection)
→ Feature counts (raw data)
→ Statistical analysis (processed)
→ R14 validation (derived)
→ Documentation (reports)
→ Figures (visualization)
```

## Data Integrity

| Check | Method | Status |
|-------|--------|--------|
| Determinism | 3 trials identical | PASS |
| Raw data preserved | archive/raw_data/ | PASS |
| Original research data | research_continuation/ | PASS |
| Bug artifacts preserved | archive/bugs/ | PASS |
| Superseded documents | archive/superseded/ | PASS |

## Data Sources (Original)

All original data from `C:\Users\natha\AI_RESEARCH\EXP-0007-SWARM-AUDIT/`:
- `research_continuation/` — 67 files (R1-R14 experiments)
- `corpus/` — 19 files (inventories, manifests)
- `FIRST_PASS/` — 12 agent reports
- `FINAL_MANIFEST.json` — Master file manifest
- All reports and analysis documents
