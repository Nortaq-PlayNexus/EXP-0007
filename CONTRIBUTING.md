# Contributing to EXP-0007

## Issue Reporting

1. Check existing issues before reporting
2. Use the bug report template for bugs
3. Use the scientific question template for research questions
4. Include:
   - Expected behavior
   - Observed behavior
   - Steps to reproduce
   - Environment details
   - Relevant data/figures

## Reproduction Requirements

All contributions must include:

1. **Reproducible evidence**: New scientific claims must include commands to reproduce
2. **Test coverage**: New features must include tests (see `tests/`)
3. **Documentation**: New methods must be documented in `docs/`
4. **Data provenance**: New results must trace from raw data → script → result

## Pull Requests

PRs must include:

- [ ] Tests pass (`pytest tests/`)
- [ ] Reproducibility subset passes (`python scripts/run_r14.py --lightweight`)
- [ ] Scientific impact documented
- [ ] Data changes documented
- [ ] Documentation changes included
- [ ] No hardcoded local paths
- [ ] No secrets or credentials

## Adding Experiments

1. Create experiment directory: `experiments/rXX/`
2. Add README.md with purpose, method, parameters, results
3. Add raw data to `data/raw/`
4. Add processed data to `data/processed/`
5. Update `configs/experiment_config.json`
6. Add to `results/` with figures and summaries
7. Document in `docs/research-timeline.md`

## Modifying Analysis Code

1. Check `src/` for existing implementations
2. Add tests in `tests/` for any behavior change
3. Verify regression tests pass
4. Update documentation if parameters change
5. Run `python scripts/validate_environment.py` before committing

## Updating Results

1. Never overwrite raw results in `data/raw/`
2. Derive new results in `data/processed/`
3. Update provenance metadata
4. Update `results/` with new figures and summaries
5. Update CHANGELOG.md

## Code Style

- Follow PEP 8
- Type hints where practical
- Docstrings for public functions
- No hardcoded paths (use relative or env vars)
- No hardcoded magic numbers (use `configs/`)
