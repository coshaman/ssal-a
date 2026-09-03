# Verification report — authoritative current state

Date: 2026-09-03 (Asia/Seoul).

## Passed

- Source recurrence and domains transcribed from ESA 2023 and independently audited.
- Literal, transformed-naive, and transformed-fast implementations agree on tested domains through `n=8`.
- Modular FPS/NTT primitives, block solver, ODE identities, coefficient extraction, and mutation checks pass.
- Exact CRT recovery passes for multiple small known counts and unrestricted `n=9`.
- Brute-force chordality agrees through six vertices.
- Block instrumentation proves one all-`k` block vector is created once and reused; the `n=8,omega=8` certificate records 406 creations and 722 hits.
- Latest canonical run: 34 main tests and 10 mutation tests passed via `python scripts/verify_all.py`.
- `python -m compileall -q verification complexity_certificate mutation_tests`: passed.

## Deliberate scope limits

- The unconditional bit/RAM improvement is not claimed; the `tilde O(n^8)` discussion is conditional.
- The sampler is out of scope.
- Absolute priority is not claimed; the Sun repository source/history and author responses remain unavailable.
- PDF compilation succeeded with the bundled `tectonic` executable; all eight rendered pages were visually inspected. Remaining diagnostics are the known fontconfig warning and the existing `lineno.sty` invalid-byte warning; neither caused a compile failure or visible layout defect.

## Current judgment

The counting-only result is ready for independent specialist-journal review, subject to the final three-reviewer gate and release audit.
