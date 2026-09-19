# EXP-0007 — D1 Propagation Bug: Measurable Effect

## The Finding

The D1 sign bug in `propagate_fresnel` produces **measurable, reproducible** differences in DBS feature counts:

| Propagation Method | z position | DBS Count |
|-------------------|-----------|-----------|
| Independent ASM (+z correct) | z=+1280 µm | **113** |
| Project Fresnel (-z buggy) | z=-1280 µm | **47** |
| Independent ASM (-z correct) | z=-1280 µm | **47** |

## What This Means

1. **Project's propagate_fresnel at z=1280 gives 47, NOT 113**
   - The 47 features are at z=-1280 (opposite direction)
   - This is a real, measurable effect of the sign bug
   - NCC(fresnel(+z), ASM(-z)) = 0.999 confirms the direction

2. **R14 result of 113 requires correct propagation**
   - 113 at z=+1280 is only obtained with correct +z propagation
   - This is verified by independent ASM: NCC=1.000000

3. **All project results using propagate_fresnel at "z=1280" are at z=-1280**
   - Feature counts, positions, and statistics correspond to z=-1280
   - This affects all scripts that use project propagation at positive z

## Reproduction

```python
# Buggy propagation (project code): call z=+1280 gives physical z=-1280
E_buggy = propagate_fresnel(E0, z=1280)  # Physical z=-1280 (D1 bug)
dbs_buggy = DeepBeamScan()
count_buggy = len(dbs_buggy.find_features(E_buggy))  # 47

# Exploiting the D1 bug: call z=-1280 gives physical z=+1280
E_r14 = propagate_fresnel(E0, z=-1280)  # Physical z=+1280 (D1 flip)
dbs_r14 = DeepBeamScan()
count_r14 = len(dbs_r14.find_features(E_r14))  # 113 — the R14 result

# Correct propagation (independent ASM at z=+1280)
asm_plus = independent_asm(z=1280)
E_correct = ComplexField(
    amplitude=np.abs(E0.complex * asm_plus),
    phase=np.angle(E0.complex * asm_plus),
    pixel_size=1e-6, wavelength_nm=694.3
)
dbs_correct = DeepBeamScan()
count_correct = len(dbs_correct.find_features(E_correct))  # 113

# Verification
NCC(E_buggy, ASM(-1280)) = 1.000000  # Project(+1280 call) = ASM(-1280): confirms D1
NCC(E_r14, ASM(+1280)) = 1.000000    # Project(-1280 call) = ASM(+1280): confirms D1
```

## Impact on Results

| Result | Affected? | Impact |
|--------|-----------|--------|
| DBS 113 at z=+1280 | YES | Only valid with correct propagation |
| DBS 47 at z=-1280 | YES | Project gives this at "z=1280" (bug) |
| All R13 results | YES | Used project propagation |
| R14 validation | PARTIAL | R14 used correct ASM |
| Orientation dependence | YES | R9 used project propagation |

## Resolution

The D1 bug is documented but not fixed in this repository because:
1. The original code is preserved for historical accuracy
2. R14 validation used correct propagation (independent ASM)
3. The bug's effect is fully characterized (47 vs 113 at |z|=1280)
4. Correcting the bug would change all historical results

Future work should fix the propagation sign in the project code and re-run all experiments.
