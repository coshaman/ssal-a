PUBLISHABLE_SPECIALIST_JOURNAL

# Final status

The counting-only theorem is verified at its stated algebraic/exact-CRT abstraction level. The previous selective-conference panel is historical; the current target is a specialist journal. All three final specialist reviewers returned `PUBLISHABLE_SPECIALIST_JOURNAL`, and the release audit is approved pending remote publication verification.

## Strongest theorem surviving verification

For a prime field of characteristic greater than `n`, the reconstructed blockwise algorithm computes the number of `omega`-colorable labeled chordal graphs on `[n]` modulo that prime using `O(n^5 M(n))` field operations, under the stated standard truncated-FPS cost model and blockwise all-`k` evaluation order. Running it over pairwise-coprime primes `p>n` whose product exceeds `2^(binom(n,2))` and applying canonical nonnegative CRT recovery recovers the exact integer count. Here `M(d)` dominates degree-`d` multiplication and all truncated-FPS primitives and satisfies `M(d)=Omega(d)`. The unrestricted labeled count is the specialization `omega=n`.

This is an exact-integer theorem via CRT, but not yet an unconditional RAM-time or bit-complexity theorem.

## Blocking gates

- A fully implementation-level bit-complexity charge for arbitrary-field multiplication, prime generation, and every auxiliary table remains open; the `tilde O(n^8)` route is recorded only conditionally.
- The adapted graph-construction exact sampler and its preservation proof are intentionally out of scope for the counting-only result.
- The mutation suite now has 10 passing tests covering the required fault classes.
- Priority is stated conservatively: the dissertation already contains the `r`/`h` regrouping, while no inspected source states the additional EGF/FPS acceleration. Sun’s accessible 2026 materials show HLV-base-case reuse but not this acceleration; repository source/history were unavailable.
- The confirmed author metadata is present and the manuscript PDF is compiled and visually inspected. Specialist-journal review is pending after the proof/reproducibility continuation.

## Verification evidence

The latest canonical run completed with `34 passed` in the main suite and `10 passed` in the mutation suite via `python scripts/verify_all.py`. It covers direct and transformed recurrences, randomized identities, modular FPS/NTT primitives, block solves, CRT reconstruction for multiple known counts including exact `n=9`, mutation checks, sampler-weight checks, block-cache instrumentation, complexity-certificate checks, and brute-force chordality checks through six vertices.
