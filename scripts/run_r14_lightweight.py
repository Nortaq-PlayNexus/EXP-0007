#!/usr/bin/env python3
"""Retired static summary: this command cannot reproduce R14."""
import sys


def main():
    print(
        "R14 reproduction NOT RUN. The former lightweight command printed "
        "hard-coded historical values; it did not execute the optical model.\n"
        "Archived records remain in research_continuation/ and results/r14/.\n"
        "For a computation, configure EXP0007_PROJECT with the original "
        "optical sandbox and follow REPRODUCIBILITY.md.",
        file=sys.stderr,
    )
    return 2


if __name__ == "__main__":
    sys.exit(main())
