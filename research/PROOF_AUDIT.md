# Proof Audit

## Scope

This audit derives the proposed compression directly from ESA 2023 Lemma 16. It does not rely on an absent supplied derivation. The notation below uses `i=ell'`, `u=x'`, `r=u+i`, `q=k'`, and `j=k-q`.

## Exact regrouping

The source summand is

`binom(k-1,q-1) binom(ell,i) tilde g_1(t-1,r,q) W(u,i,z) T_i(j)`,

subject to `0<=u<=x`, `0<=i<=ell`, and `0<r=u+i<x+ell`. Here

- if `i=0`, `W=binom(x,u)-binom(z,u)` and `T_0(j)=F_j`, the current `tilde f_p(t,x,ell,j)` sequence;
- if `0<i<ell`, `W=binom(x,u)` and `T_i(j)=tilde f_p(t,x+i,ell-i,j)`;
- if `i=ell`, `W=binom(x,u)` and `T_ell(j)=tilde g_p(t-1,x+ell,j,z)`.

For fixed `r`, the `i=0` term has `u=r`, hence its coefficient is exactly

`a_r = binom(x,r)-binom(z,r)`.

Every other contribution has `i>0`; grouping all such terms defines

`b_r(j) = sum_{i=1..ell-1} binom(ell,i) binom(x,r-i) F^{(i)}_j + binom(x,r-ell) G_j`,

where `F^{(i)}_j=tilde f_p(t,x+i,ell-i,j)` and `G_j=tilde g_p(t-1,x+ell,j,z)`, with out-of-range binomial coefficients interpreted as zero. Therefore

`F_k = sum_{q=1..k} sum_{r=1..x+ell-1} binom(k-1,q-1) G_{r,q}(a_r F_{k-q}+b_r(k-q))`,

where `G_{r,q}=tilde g_1(t-1,r,q)`. The factor `binom(ell,i)` belongs inside `b_r` (and inside the `a_r` contribution only with `i=0`, where it equals one). The standalone identity oracle tests this equivalence directly.

## Dependency order

For `0<i<ell`, the recursive state has second free-layer parameter `ell-i<ell`, so increasing `ell` is a valid topological order for fixed compatible outer parameters. For `i=ell`, the source calls `tilde g_p`, exactly as required; replacing it with an ordinary `tilde f_p` changes both the function family and its domain and is not justified.

## Polynomial identity

Define

`D_j(U) = sum_{i=1..ell-1} binom(ell,i) F^{(i)}_j U^i + G_j U^ell`.

Then

`[U^r] D_j(U)(1+U)^x`
`= sum_{i=1..ell-1} binom(ell,i) F^{(i)}_j binom(x,r-i) + G_j binom(x,r-ell)`
`= b_r(j)`.

This also proves the `i=ell` boundary is included in `D_j` without treating it as an `f_p` state.

## EGF normalization

Set

`A_q = sum_r G_{r,q} a_r`,
`H_{q,j} = sum_r G_{r,q} b_r(j)`,
`F(Y)=sum_{k>=0} F_k Y^k/k!`,
`P(Y)=sum_{q>=1} A_q Y^{q-1}/(q-1)!`,
`Q(Y)=sum_{q>=1,j>=0} H_{q,j} Y^{q+j-1}/((q-1)!j!)`.

The coefficient of `Y^{k-1}` in `P(Y)F(Y)` is

`sum_{q+j=k-1} A_q /((q-1)!j!) F_j`
`= 1/(k-1)! sum_{q=1..k} binom(k-1,q-1) A_q F_{k-q}`.

The same factorial calculation gives the corresponding inhomogeneous term from `Q`. Thus `F'=PF+Q`, `F(0)=0`, coefficient-by-coefficient. The `(q-1)!` is forced by the derivative shift; using `q!` produces an extra factor `1/q` and is a valid mutation.

Over a field where `0!,...,K!` are invertible, the recurrence determines `F_k` successively, so the truncated formal solution is unique. The integrating-factor expression follows by formal differentiation because `E(0)=1` and `E'=PE`.

## Edge audit

- `r=1`: all terms with `i>1` vanish; `i=0` and possibly `i=1` are handled separately by the coefficient extraction.
- `r=x+ell-1`: the forbidden full-set case `r=x+ell` is excluded; coefficients with impossible `u` or `i` vanish.
- `x=0`: `u=0` only; the `i=0` coefficient is `1-1=0` when `z=0`, and all valid contributions have `i>0`.
- `ell=1`: there are no interior `f_p` dependencies; `D_j(U)=G_jU`.
- `z=0`: `a_r=binom(x,r)`.
- `z=x`: `a_r=0` for every `r`; the source footnote specifically permits skipping the `i=0` calls because their coefficient vanishes.
- `K=0`: no `q` satisfies `1<=q<=0`, so the convolution sum is empty; the source base case is used.

## Current qualification

The algebra above validates the natural transformation induced by Lemma 16. It does not yet prove the global state-cost bound, the complete DP agreement, or the claimed fast implementation. Those remain separate gates.
