# EXP-0007 R14 — Final Report

## Experiment Summary

**EXP-0007** investigated whether coherent optical propagation generates novel topological structure (vortices).

**Result: No evidence of physical vortex creation was found.** The apparent 113-vortex population at z=+1280 is a systematic detector + grid-locking artifact.

## Key Numbers

| Metric | Value |
|--------|-------|
| DBS at z=0 | 48 |
| DBS at z=+1280 | 113 |
| Independent verification | 113 = 113 ✓ |
| Random field count | ~21,670 |
| Lattice/Random | 0.0052 (191× deficit) |
| Orientation range | 8.65× (corrected) |

## R14 Verdict

The 113 candidates are real phase singularities but:
- NOT at amplitude zeros (MethodC: 0/20)
- NOT resolution-convergent (328→5,742)
- NOT stable across z (7 discontinuities)
- NOT preserved by reversal (113→48)
- NOT beyond detector capability (9-19× overcount)
- NOT above null distribution (0th percentile)

## Scientific Conclusion

All EXP-0007 claims are **Level 1** (quantitatively measurable, designed/inherited). No Level 2 or Level 3 claims are supportable. No propagation-generated structure creation was demonstrated.

## Reproduction

```powershell
python scripts/run_r14.py
```

## Limitations

- 65 propagation-generated features uncharacterized
- R11/R12 need re-run with corrected MethodB
- No physical experimental validation
- D02 measurement method unverified

## Files

| Location | Content |
|----------|---------|
| `docs/` | All documentation |
| `results/r14/` | R14 results |
| `research_continuation/` | Preserved raw data |
| `archive/` | Historical and bug artifacts |
| `scripts/` | Reproduction scripts |
| `tests/` | Test suite |
