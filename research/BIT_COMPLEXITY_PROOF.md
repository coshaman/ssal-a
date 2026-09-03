# Exact bit-complexity audit

## Conditional bound

The final answer has at most `B = binom(n,2)+1 = O(n^2)` bits. By the prime number theorem, for sufficiently large `n` there are `Theta(n^3/log n)` primes in `(n,n^3]`; after handling finitely many small `n` separately, this supplies `R=O(n^2/log n)` distinct primes of `O(log n)` bits, enough for a product exceeding `2^B`. A deterministic implementation can scan the interval and test candidates with a polynomial-time primality test. This establishes existence and polynomial-time generation, though it is not the practical NTT-prime backend.

For one such prime, the algebraic algorithm uses `O(n^5 M(n))` field operations. With quasi-linear multiplication, this is `tilde O(n^6)` field operations. Arithmetic on `O(log n)`-bit residues costs `tilde O(log n)` bit operations, and the standard Newton FPS routines use only a constant number of polynomial multiplications per precision-doubling stage. Thus the modular runs total `tilde O(n^8)` bit operations over all `R` primes.

The CRT reconstruction handles `R` residues and an `O(n^2)`-bit result. A product-tree or balanced mixed-radix reconstruction costs `tilde O(n^2)` bit operations up to polylogarithmic factors, which is absorbed by `tilde O(n^8)`. Storing one modular DP run requires the state tables plus the block polynomials; the current implementation's cache representation is polynomial space, and rerunning primes sequentially avoids an `R`-fold space factor.

The argument applies to one fixed `omega`; computing all `omega` values multiplies the bound by at most `n`, giving `tilde O(n^9)` rather than the fixed-`omega` `tilde O(n^8)` estimate.

## Required caveat

The preceding paragraph is a conditional theorem, not yet a fully audited implementation-level bit bound. It assumes the standard arbitrary-finite-field fast multiplication and FPS algorithms have the stated uniform costs, and it does not provide a detailed deterministic prime-generation constant or a line-by-line bound for every auxiliary DP table. The project therefore retains the exact CRT theorem, but does **not** promote the `tilde O(n^8)` claim to the final strongest status without a specialist bit-complexity review.
