# Experiment Overview — EXP-0007

## Summary

EXP-0007 investigated whether coherent optical propagation generates new vortex topological structures. The study found **no evidence of physical vortex creation**. The apparent 113-vortex population at z=+1280 is a systematic detector + grid-locking artifact.

## Parameters

| Parameter | Value |
|-----------|-------|
| Grid | 256 × 256 pixels |
| Pixel size | 1 µm |
| Wavelength | 694.3 nm |
| Lattice | 6 rows × 8 cols = 48 design vortices |
| Propagation | 0 → 1280 µm |
| Detector | DeepBeamScan (DBS) |
| Random seed | 42 |

## Key Numbers

| Measurement | Value |
|-------------|-------|
| DBS at z=0 | 48 |
| DBS at z=+1280 | 113 |
| Independent winding (fixed) | 113 = DBS (verified) |
| Independent winding (buggy) | 7,183 (double-np.angle bug) |
| Random field count | ~21,670 |
| Lattice/Random ratio | 0.0052 (191× deficit) |

## Pipeline

```
vortex_crystal_field → propagate_fresnel → DeepBeamScan.find_features → feature count
```

## Conclusion

**No propagation-generated topological structure creation was demonstrated.** The 113 features at z=+1280 are reproducible but detector-dependent, grid-locked, and threshold-sensitive.

## Raw Data Location

- Original research data: `research_continuation/`
- Structured data: `data/raw/`, `data/processed/`
- Results: `results/r14/`, `results/figures/`, `results/tables/`
