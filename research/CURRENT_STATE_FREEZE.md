# Current State Freeze

Date: 2026-09-03.

## Current theorem under review

For fixed `n` and `1 <= omega <= n`, the abstract blockwise algorithm over a suitable finite field computes `C(n, omega)` in `O(n^5 M_p(n))` field operations. The supplied transformed-fast implementation realizes this with admissible NTT primes and rejects unsupported transform lengths. Independent admissible primes whose product exceeds the graph-count bound recover the exact nonnegative integer by canonical CRT. The specialization `omega=n` counts all labeled chordal graphs.

The sampler and an unconditional bit/RAM theorem are not part of the claim. The HLV recurrence and the dissertation's `r=x'+ell'` regrouping/six-argument helper are prior art. The candidate contribution is the additional coefficient extraction, EGF-to-linear-ODE conversion, and all-`k` blockwise FPS solve.

## Proof obligations closed in this continuation

- The source dependency graph and topological order are recorded in `research/FULL_DEPENDENCY_PROOF.md`.
- Every counter family has a domain, state count, inner-loop charge, and global sum in `research/GLOBAL_COMPLEXITY_PROOF.md`.
- The block cache is scoped by `(n, p, omega)` and keyed by `(t,x,z,ell,omega)` within that scope; its all-`k` invariant is stated and instrumented.
- The reproducibility entry point is `python scripts/verify_all.py`; expected results are in `REPRODUCIBILITY.md`.

These documents close presentation and accounting obligations; they do not upgrade the result to a bit-complexity theorem or establish absolute priority.
