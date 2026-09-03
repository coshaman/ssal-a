# Faster Exact Counting of Labeled Chordal Graphs

This repository contains a counting-only research package for accelerating the labeled chordal-graph dynamic program of Hébert-Johnson, Lokshtanov, and Vigoda.

## Result

For any suitable finite-field multiplication/FPS backend, the abstract blockwise EGF/FPS algorithm computes the number of `omega`-colorable labeled chordal graphs on `[n]` in `O(n^5 M_p(n))` field operations. The supplied implementation uses admissible NTT primes and rejects unsupported transform lengths. Running over sufficiently many pairwise-coprime admissible primes and applying canonical nonnegative CRT recovers the exact count. The unrestricted case is `omega=n`.

The package does not claim a sampler or an unconditional improved bit/RAM bound. The `r/h` regrouping is credited to the 2025 dissertation; the present claim concerns the further coefficient-extraction and EGF/FPS acceleration. Priority language is conservative.

## Reproduce

Requires Python 3 and pytest. Run `python scripts/verify_all.py` for the canonical verification suite. Run `python -m compileall -q verification complexity_certificate mutation_tests tests scripts` for syntax checks. Run `python -m complexity_certificate.generate` to regenerate the machine-readable block-cache certificate. The unrestricted sequence reproduced by the package begins `1, 2, 8, 61, 822, 18154, 617675, 30888596, 2192816760`. The paper is in `paper/main.tex` (with the working copy in `manuscript/main.tex`); verification and research details are under `research/`.

Current status: `PROOF_INCOMPLETE` for the specialist-journal continuation. The counting-only theorem is locally verified, but the full dependency/complexity proof and specialist-journal review are still in progress.
