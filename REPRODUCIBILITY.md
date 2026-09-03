# Reproducibility

Requirements: Python 3.10+ and pytest. No third-party runtime package is required beyond pytest.

Run `python scripts/verify_all.py` for the canonical quick verification. It runs the main suite, mutation suite, Python compilation, and complexity certificate. The current expected result is 34 main tests and 10 mutation tests passing.

The unrestricted known values are checked by the tests and begin `1, 2, 8, 61, 822, 18154, 617675, 30888596, 2192816760`. The suite covers literal/source recurrence checks, transformed-naive and transformed-fast comparisons, FPS/NTT primitives, ODE identities, exact CRT reconstruction, known-value/OEIS comparison, brute-force chordality checks through six vertices, mutation tests, cache regression, and certificate generation.

The theorem is a finite-field operation bound. CRT gives exact integer recovery, but the package does not claim an unconditional bit/RAM bound or sampler preservation.
