# Claim Freeze

## Provenance

This freeze is extracted from the supplied handoff at `C:\Users\owner\.codex\attachments\8978b6f0-26f5-47ec-881d-91c695ba3f85\pasted-text-1.txt`. It is a statement of the claim under audit, not an assertion that the claim is true.

## Candidate theorem

The number of labeled `omega`-colorable chordal graphs on `[n]` can be computed modulo suitable finite-field primes using `O(n^5 M(n))` field operations after replacing the `tilde f_p` bottleneck in the Hébert–Johnson–Lokshtanov–Vigoda dynamic program by polynomial convolution in the `r` direction and a formal-power-series linear ODE in the `k` direction. Exact integer recovery follows by CRT when enough primes `p>n` are used.

The handoff also proposes the shorthand `O(n^5 M(n)) = tilde O(n^6)`, where `M(d)` is polynomial-multiplication complexity. The equality is provisional and must be audited under an explicit multiplication model.

## Frozen definitions and domains to verify

- `n`: number of labeled vertices, with labels `[n]`.
- `omega`: colorability parameter; the precise source definition is to be transcribed.
- `p,t,x,ell,z,k,q,r`: DP/state and summation parameters; exact meanings and ranges are not supplied completely by the handoff and must be recovered from the authoritative recurrence.
- `M(d)`: polynomial-multiplication complexity on degree/length scale `d`.
- Required source-domain check for five-argument `tilde f_p`: `t >= 2`, `x >= 0`, `ell >= 1`, `z <= x`.
- Proposed compressed variable: `r = x' + ell'`.
- Proposed fixed-state size: `s = x + ell`, `K = n - s`.

## Frozen transformation claims

For fixed `(t,x,ell,z)`, the proposed recurrence is intended to have the form

`F_k = sum_{q=1}^k sum_{r=1}^{x+ell-1} binom(k-1,q-1) G_{r,q} h_{r,k-q}`.

The proposed decomposition is `h_{r,j} = a_r F_j + b_r(j)`, with

`a_r = binom(x,r) - binom(z,r)`

and a proposed polynomial formula for `b_r(j)` that remains to be recovered and verified from the handoff/source derivation.

The `a_r F_j` contribution is claimed to arise exactly from `ell' = 0`; all `0 < ell' < ell` dependencies should have strictly smaller `ell`; and `ell' = ell` should be a `tilde g_p` boundary term, not another `tilde f_p` state.

The handoff does not provide `D_j`; independent reconstruction from source Lemma 16 gives `D_j(U)=sum_{i=1..ell-1} binom(ell,i)F^{(i)}_jU^i+G_jU^ell`, subject to proof and implementation audits.

The proposed EGF reduction is `F'(Y) = P(Y)F(Y) + Q(Y)`, `F(0)=0`, with formal solution

`F(Y) = E(Y) integral(E(Y)^(-1) Q(Y) dY)`, `E(Y)=exp(integral P(Y)dY)`.

## Frozen output claims

- Exact counting: intended count for labeled chordal graphs, with the precise `omega`-restricted and unrestricted relationship to be confirmed.
- Uniform sampling: intended preservation of the source sampling-to-counting result.
- Preprocessing: proposed `O(n^5 M(n))` algebraic operations.
- Per-sample: proposed `O(n^4)`.

## Arithmetic model boundary

The principal claim is frozen as an algebraic-complexity claim only until the audit distinguishes: characteristic-zero rational/algebraic operations; finite fields of characteristic `p > n`; exact integer reconstruction by CRT; and actual RAM/bit complexity. No bit-complexity improvement is frozen as a claim.

## Explicit non-claims

The handoff explicitly forbids silently strengthening the result to a RAM/bit-complexity theorem, forbids assuming the derivation is correct, forbids claiming priority merely because searches are empty, and forbids manuscript promotion while a fatal issue remains. Routine FPS algorithms are not to be presented as original contributions.

## Gate status

`COUNTING-ONLY`: the modular theorem and exact CRT recovery argument are closed at the stated abstraction level. A stronger bit-complexity claim, complete mutation engineering, and priority/publication claims remain separately gated.
