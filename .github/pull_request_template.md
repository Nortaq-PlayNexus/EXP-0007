## Description

<!-- Describe what this PR changes and why -->

## Scientific Impact

<!-- What scientific claim does this PR make? Is it testable? What evidence supports it? -->

## Tests

- [ ] New tests added for new functionality
- [ ] All existing tests pass
- [ ] Regression tests for known bugs pass
- [ ] Reproducibility subset passes

```bash
pytest tests/
python scripts/run_r14.py --lightweight
```

## Reproducibility

<!-- Can someone reproduce your results? Include exact commands -->

## Data Changes

- [ ] Raw data modified (if yes, explain why in data/provenance/)
- [ ] Processed data updated
- [ ] Figures regenerated
- [ ] Metadata updated

## Documentation

- [ ] README updated if needed
- [ ] Methods documented
- [ ] Results documented
- [ ] CHANGELOG updated

## Checklist

- [ ] No hardcoded local paths (use relative paths or env vars)
- [ ] No secrets or credentials
- [ ] Configuration centralized in configs/
- [ ] Magic numbers removed from code
