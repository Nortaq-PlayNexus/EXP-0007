# Methodology — EXP-0007

## Experimental Design

### Field Generation
- `vortex_crystal_field(shape=(256,256), rows=6, cols=8, pixel_size=1e-6, wavelength_nm=694.3)`
- Creates a 2D periodic array of phase singularities
- 48 design vortex positions at z=0

### Propagation
- `propagate_fresnel(E, z=1280, pixel_size=1e-6)`
- Buggy sign (D1): propagates -z instead of +z
- Independent ASM used for validation: NCC=1.000000

### Feature Detection
- `DeepBeamScan().find_features(E)`
- Winding-number topology method
- Dead min_prominence parameter (D2)

### Independent Verification Methods
- MethodA: DBS find_features (validated on synthetic cases)
- MethodB: winding_count with np.mod (validated AFTER bug fix)
- MethodC: zero-amplitude search (fails: 0/20 confirmed)
- Independent ASM: from-scratch numpy implementation

## Statistical Framework

### Controls
- D01: Random phase null (completeness)
- D02: Matched-spectrum null (decisive)
- Known vortices: Synthetic 1, 2, 4, 10, 100 vortex fields
- Random noise: 100 trials for null distribution

### Significance Testing
- Per-seed p-values with Bonferroni correction
- Chi-square tests for distribution comparison
- Bootstrap confidence intervals

## Data Processing Pipeline

```
RAW FIELD (vortex_crystal_field)
→ ComplexField (amplitude × exp(1j*phase))
→ propagate_fresnel (z=1280)
→ DeepBeamScan.find_features
→ Feature list (position, charge, intensity, type)
→ Statistical analysis
→ Publication figures
```

## Validation Protocol

1. **Reproduce**: Run R14 exactly (3 trials minimum)
2. **Cross-validate**: MethodA vs MethodB (fixed) vs MethodC
3. **Null test**: Compare with random field distribution
4. **Sensitivity**: Test threshold, resolution, orientation dependence
5. **Document**: All parameters, seeds, versions recorded

## Quality Controls

- NCC(ASM(+z), ASM(-z)) = 1.000000 (propagation consistency)
- NCC(phase attr, np.angle(complex)) = 2.22e-16 (field construction)
- Deterministic: 3 trials give identical results
- Reproducible: Full script available for every figure
