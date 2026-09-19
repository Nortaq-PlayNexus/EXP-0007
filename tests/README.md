# Test Suite — EXP-0007

## Running Tests

```powershell
# All tests
pytest tests/ -v

# Specific test categories
pytest tests/test_field_construction.py -v
pytest tests/test_propagation.py -v
pytest tests/test_winding.py -v
pytest tests/test_detector.py -v
pytest tests/test_reproducibility.py -v
```

## Test Categories

### test_field_construction.py
- ComplexField construction from amplitude and phase
- ComplexField.complex = amplitude × exp(1j×phase) (verified: max diff 2.22e-16)
- Phase range verification [-π, π]
- Vortex crystal field generation (48 design positions)

### test_propagation.py
- ASM propagation correctness
- Fresnel propagation (with known bug — documented test)
- Propagation reversibility (NCC = 1.0)
- FFT convention verification
- Independent ASM vs project propagation agreement

### test_winding.py
- winding_count on flat phase → 0
- winding_count on 1 vortex → 1 (regression test for double-np.angle bug)
- winding_count on 4 vortices → 4 (regression test)
- winding_count on lattice → 48 (at z=0)
- winding_count on lattice → 113 (at z=1280)
- MethodA vs MethodB (fixed) agreement
- Regression test: double-np.angle gives 127 on 1 vortex (documented)

### test_detector.py
- DBS on plane wave → 0 features
- DBS on known vortex → 1 (regression for detector overcount)
- DBS on known 4-vortex → 4
- DBS on random field → overcount documented
- Threshold behavior
- min_prominence dead parameter test

### test_reproducibility.py
- Deterministic: 3 trials give identical results
- Environment validation
- Configuration validation
- Data schema validation

### test_regression.py
- All known bugs documented with regression tests
- Double-np.angle bug (must NOT fix — test documents buggy behavior)
- Propagation sign bug
- Dead parameter behavior

### test_data_schema.py
- Raw data schema validation
- Processed data schema validation
- Metadata completeness
- Provenance chain verification

### test_config_validation.py
- Configuration parameter ranges
- Magic number detection
- Parameter consistency across scripts

## Regression Tests for Known Bugs

| Bug | Test | Expected Behavior | Documented |
|-----|------|-------------------|------------|
| Double-np.angle | test_winding.py::test_buggy_method | 1 vortex → 127 (BUGGY) | YES |
| Double-np.angle | test_winding.py::test_fixed_method | 1 vortex → 1 (FIXED) | YES |
| Propagation sign | test_propagation.py::test_fresnel_sign | NCC(+z,-z)=1.0 | YES |
| Dead parameter | test_detector.py::test_min_prominence_unused | Parameter never referenced | YES |

## Adding Tests

1. Create test file in `tests/`
2. Prefix with `test_`
3. Use pytest conventions
4. Include regression tests for any bug fixes
5. Run `pytest tests/` to verify all pass
6. Add to CI workflow
