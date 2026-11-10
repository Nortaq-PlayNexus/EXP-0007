# README claim and reproducibility review

Review date: 2026-11-10. Scope: documentation review only. No simulation or test suite was executed during this review.

## Items requiring scientific reconciliation

1. The README calls the 113 candidates "real phase singularities" but also reports that Method C found 0 of 20 at amplitude zeros. These statements need a precise operational definition and supporting data before the candidates are described as physical optical vortices. The overall README conclusion already rejects demonstrated physical vortex creation.
2. The historical 7,183 winding-number comparison is marked as affected by a sign or method bug. Keep this clearly identified as a superseded measurement wherever it appears in plots, graphics or abstracts.
3. The README labels reproducibility "Verified". Clarify whether that means the archived R14 run was reproduced previously, or whether a clean environment was independently reproduced. A badge alone does not establish current CI success.
4. The README's one-command reproduction instructions should be checked in a clean supported Python environment, with dependencies pinned and raw/processed data availability documented.

## Suggested verification protocol

- Record the exact commit, Python version, dependency lockfile, hardware assumptions and seed values.
- Run the documented lightweight validation and complete R14 runner in a clean environment.
- Confirm independent amplitude-zero, winding-number and charge-conservation definitions against saved outputs.
- Compare the generated figures and counts against the archived R14 tables.
- Preserve the original results and negative conclusion without retroactively rewriting measurements.
- Add a real CI badge only after verifying the actual workflow file and its execution.

This document is an editorial review checklist, not a new experimental finding.
