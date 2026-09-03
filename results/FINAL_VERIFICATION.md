# Final Verification

Date: 2026-09-03.

## Code

- `python -m pytest -q`: 29 passed in 4.12 seconds.
- `python -m compileall -q verification complexity_certificate mutation_tests tests`: passed.
- `python -m complexity_certificate.generate`: passed; certificate records 406 block creations and 722 cache hits for the instrumented sample.

## Mathematical and artifact checks

- Literal, transformed-naive, and transformed-fast recurrences agree on the tested cases.
- Modular FPS/NTT, ODE coefficient, CRT, mutation, block-cache, and brute-force chordality checks passed.
- The scientific freeze, complexity proof, arithmetic-model audit, exact-reconstruction proof, Sun audit, venue report, and artifact-consistency audit are present.
- The sampler remains explicitly out of scope; no sampler claim is used in the manuscript.

## PDF

- `manuscript/main.tex` compiled with `tectonic` and produced `manuscript/main.pdf`.
- All eight rendered pages were visually inspected in `manuscript/manuscript/.pdf-render-final-4f95c1a4`.
- No clipping, missing equations, or broken page boundaries were found. TeX emitted only the known `lineno` UTF-8 warning and minor overfull prose boxes.

## Limits

The confirmed author block is present. The fresh six-reviewer panel did not unanimously return STRONG ACCEPT; all six rejected the release gate. The unconditional bit/RAM theorem, sampler preservation, and absolute priority claim remain unmade.
