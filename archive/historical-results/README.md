# Archive: Historical Results

This directory preserves all original research outputs before correction.

## Contents

### Original R13 Results (Buggy)
- `DEFINITIVE_DBS_TEST.json` — Original: 113/150/7183/4067
- `r9_orientation.json` — Original: 7,844→15,598 (inflated)
- `r11_dbs_fix.json` — Original: 7,844→6,558 (inflated)
- `r12_exp3_null.json` — Original counts (inflated MethodB)
- `r13_forensic_results.json` — Original forensic results
- `r13_forensic_results.csv` — Original forensic CSV

### Corrected Versions
See `../results/r14/` for all corrected numerical values.

## Preservation Policy

All raw numerical outputs are preserved here. No results are deleted.
Corrections are documented alongside originals.

## Key Corrections

| Original | Corrected | Bug |
|----------|-----------|-----|
| 7,183 | 113 | Double-np.angle in winding_count |
| 98.4% undercount | No discrepancy | Bug invalidated comparison (98.4% was comparing valid MethodA vs buggy MethodB) |
| 2.0× orientation | 6.3× orientation | MethodB corrected |
| 8× lattice/D02 | 191× | MethodA corrected |
