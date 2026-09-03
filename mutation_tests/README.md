# Mutation-test matrix

The complete mutation suite is gated on the full reference DP. The current standalone transformation suite covers the mathematically local mutations that can be exercised before that DP exists:

| Mutation | Local test status | Full-DP smallest detector |
|---|---|---|
| `q!` for `(q-1)!` | covered by EGF coefficient test design | pending |
| delete `a_r F_j` | covered by `test_local_mutations.py` | pending full-DP smallest case |
| extend `r` through `x+ell` | covered by `test_local_mutations.py` | pending full-DP smallest case |
| use `tilde f_p` at `ell'=ell` | local boundary substitution covered | pending full-DP smallest case |
| add instead of subtract `binom(z,r)` | covered at `z=x` by `test_local_mutations.py` | pending full-DP smallest case |
| wrong `ell` order | dependency-order detector covered | pending full-DP schedule mutation |
| drop `z=x` special behavior | covered by direct `fh5` contrast | pending full-DP smallest case |
| wrong EGF normalization | covered by EGF coefficient test design | pending |
| truncate `P,Q,E,F` incorrectly | local output-length mutation covered | pending full-DP smallest case |
| reuse an uncomputed state | cache-key regression covered for `omega` | pending schedule mutation |

No mutation is reported as fully killed until a test demonstrates a failing mutated implementation and records the smallest detecting input.
