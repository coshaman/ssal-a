# Source Recurrence Audit

## Result so far

The authoritative ESA paper confirms the critical domain quoted in the handoff:

`tilde f_p(t,x,ell,k,z)` has domain `t >= 2`, `x >= 0`, `ell >= 1`, `z <= x` (ESA 2023, Definition 7(8), p. 6, PDF lines 338–340).

The source recurrence is Lemma 16, p. 12 (PDF lines 680–732):

`tilde f_p(t,x,ell,k,z)` equals the sum over `k'=1..k`, `0<=x'<=x`, `0<=ell'<=ell`, and `0 < x'+ell' < x+ell` of

`binom(k-1,k'-1) binom(ell,ell') tilde g_1(t-1,x'+ell',k') * W(x,x',ell',z) * R(t,x,ell,k,k',ell')`,

where

`W = binom(x,x')` if `ell'>0`, and `W = binom(x,x') - binom(z,x')` otherwise;

`R = tilde f_p(t,x+ell',ell-ell',k-k')` if `ell'<ell`, and
`R = tilde g_p(t-1,x+ell',k-k',z)` if `ell'=ell`.

This is a literal transcription with notation normalized from the PDF typography.

## Symbol-by-symbol comparison with the handoff

| Item | Authoritative source | Handoff | Audit |
|---|---|---|---|
| `t` domain | `t >= 2` | explicitly required | MATCH |
| `x` domain | `x >= 0` | explicitly required | MATCH |
| `ell` domain | `ell >= 1` | explicitly required | MATCH |
| `z` domain | `z <= x` | explicitly required | MATCH |
| `k'` range | `1..k` | required literal oracle | MATCH |
| `x'` range | `0..x` | required literal oracle | MATCH |
| `ell'` range | `0..ell` | required literal oracle | MATCH |
| proper-subset condition | `0 < x'+ell' < x+ell` | proposed `r=1..x+ell-1` | EQUIVALENT after `r=x'+ell'` |
| coefficient | `binom(k-1,k'-1) binom(ell,ell')` | binomial convolution target | source supports target form, transformation unverified |
| `ell'=0` weight | `binom(x,x')-binom(z,x')` | `a_r=binom(x,r)-binom(z,r)` candidate | plausible only after proving `r=x'` and all residual terms |
| `ell'>0` weight | `binom(x,x')` | polynomial identity candidate | not yet proved |
| `ell'<ell` recursive target | `tilde f_p(t,x+ell',ell-ell',k-k',z)` | strictly smaller `ell` claimed | source confirms |
| `ell'=ell` target | `tilde g_p(t-1,x+ell',k-k',z)` | boundary must be `tilde g_p` | MATCH |
| `z=x` behavior | source footnote: zero coefficient for `ell'=0`, so calls need not be evaluated | required mutation test | MATCH |

## Other source facts relevant to implementation

Definition 7 states `f(t,x,ell,k)` has `t>=1,x>=0,ell>=1`; `tilde f` has `t>=2,x>=0,ell>=1`; and the five-argument `tilde f_p` has the `z<=x` restriction. Lemma 15 identifies the four-argument `tilde f_p` with its `z=x` specialization. The published base cases include `tilde f_p=0` when `t=1` or `k=0`, and the paper explains that the control flow terminates because either `t` or the vertex count decreases.

## Priority-relevant correction

The dissertation does not leave the `r=x'+ell'` compression as an unmade suggestion. Chapter 2, §2.5.4, pp. 66–68, independently reorders Lemma 9 by `r`, defines the six-argument helper `h(t,x,ell,z,r,k)`, and obtains its Equation (2.1), followed by the `O(n^7)` analysis. Thus the `r` regrouping itself is already explicitly present in the authors' 2025 dissertation. Any novelty claim must be limited to a further acceleration of the resulting `h`/`tilde f_p` evaluation, not to discovering `r`-compression.

The dissertation also states that sampling uses the precomputed counter tables with constant-time access and that the per-sample cost is `O(n^4)` (Chapter 2, §2.6, Theorem 3, pp. 68–69). This supports auditing whether a new preprocessing representation can still provide the same table values, but does not by itself establish that it can.

## Current fatal limitation

The handoff does not contain the actual proposed research derivation, `D_j(U)`, `P(Y)`, `Q(Y)`, or a complete transformed implementation specification. Consequently, no honest proof of the proposed transformation or end-to-end implementation can be claimed from the supplied material. This is a missing-input blocker, not evidence that the theorem is false.

## Sources

- Hébert-Johnson, Lokshtanov, Vigoda, ESA 2023, Definition 7 and Lemmas 8–16, pp. 6–12: <https://drops.dagstuhl.de/storage/00lipics/lipics-vol274-esa2023/LIPIcs.ESA.2023.58/LIPIcs.ESA.2023.58.pdf>
- arXiv full version: <https://arxiv.org/abs/2308.09703>
- implementation: <https://github.com/uhebertj/chordal>
- dissertation, Chapter 2, §2.5.4 and §2.6: <https://escholarship.org/content/qt9646w20k/qt9646w20k_noSplash_a999d89b7bf506c1036ca826b9719acc.pdf>
