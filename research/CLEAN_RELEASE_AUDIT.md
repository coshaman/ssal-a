# Clean-release audit

Date: 2026-09-03.

## Verified

- `python -m pytest -q`: current rerun recorded in `results/FINAL_VERIFICATION.md`.
- `python -m compileall -q verification complexity_certificate mutation_tests`: passed.
- `FINAL_STATUS.md` begins with `PROOF_INCOMPLETE` pending specialist review.
- The manuscript separates modular complexity, exact CRT recovery, and conditional bit complexity.
- The manuscript credits HLV, the 2025 dissertation, Sun 2026, and OEIS.

## Release gates still open

The bundled `tectonic` executable compiles the manuscript and all eight rendered pages have passed visual inspection. The old selective-conference panel is historical; the current specialist-journal gate is still pending.

## Remaining human/editorial actions

- Specialist-journal review and final release audit remain open.
- The unconditional bit/RAM theorem and sampler remain intentionally out of scope.
- The unavailable Sun repository source/history remains a documented priority limitation.
