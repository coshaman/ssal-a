# Global Complexity Proof

Fix `n`, `omega`, and a prime field. Let `s=x+ell`, `K=n-s`. Assume `M` is nondecreasing, `M(d)=Omega(d)`, and dominates the cost of each truncated-FPS primitive used by the solver, including any logarithmic factors.

## Accelerated blocks

For fixed `(t,x,z,ell)`, the `K+1` products `D_j(U)(1+U)^x` cost `O(K M(s))`. Forming `P` and the coefficient arrays costs `O(sK)`. The forcing series is computed as the sum of `s-1` univariate products `R_r B_r`, costing `O(s M(K))`; no dense `r,q,j` contraction is performed. The integrating-factor inverse, exponential, integration, and final products are included in `O(M(K))` by the definition of `M`.

For fixed `s`, there are `s(s+1)/2=O(s^2)` choices of `(x,ell,z)` with `x+ell=s` and `0<=z<=x`, and at most `n` values of `t`. Therefore `sum_s O(n s^2 ((n-s)M(s)+sM(n-s))) = O(n^5 M(n))`. The block cache charges this once per key, not once per requested `k`.

## Remaining families

Use the source-valid coarse domains `0<=t<=n`, `0<=z<=x<=n`, `ell>=1`, and total outside counter at most `n`; removing impossible states only decreases the charge.

| Family | State-index bound | Inner summation | Total |
|---|---:|---:|---:|
| `g, gt, gh` | `O(n^4)` each | `O(n^2)` for `gt,gh`, `O(n)` for `g` | `O(n^6)` |
| `g1, g2` | `O(n^3)` each | `O(n)` | `O(n^4)` |
| `f, ft` excluding accelerated block construction | `O(n^4)` each | `O(n)` | `O(n^5)` |
| `all_graphs` and connected extraction | `O(n^2)` / `O(n^3)` | `O(n)` or `O(n^2)` | `O(n^3)` / `O(n^5)` |
| accelerated `fh5` blocks | `O(n^4)` keys | `O(KM(s)+sM(K))` | `O(n^5M(n))` |

The `O(n^6)` scalar term is absorbed by `O(n^5M(n))` because `M(n)=Omega(n)`. Binomial tables cost `O(n^2)` scalar additions. Factorial and inverse-factorial tables cost `O(n)` inversions/multiplications when precomputed once per execution; per-block coefficient-array and input materialization costs `O(sK)` and is already included above. Dictionary hits are constant-time scalar accesses and are charged by the state/request counts. Hence one modular execution costs `O(n^5M(n))` field operations. Exact integer recovery repeats independent modular executions and CRT; prime generation and coefficient bit lengths are deliberately outside the field-operation theorem.
