# Exact reconstruction proof

Let `C(n,omega)` be the number of labeled chordal graphs on `[n]` whose clique number is at most `omega`. Since these are simple graphs,

`0 <= C(n,omega) <= 2^(n choose 2)`.

Choose pairwise distinct primes `p_i > n` and run the transformed algorithm over each `F_{p_i}`. The condition `p_i > n` makes every factorial and every integer denominator used by the EGF normalization through degree `n` invertible. The recurrence is an identity over the integers; reducing its integer coefficients and applying the field operations therefore computes the reduction of the same integer DP value modulo every such prime. Intermediate DP values need not be reconstructed.

If `P = product_i p_i > 2^(n choose 2)+1`, then two integers in the interval `[0,2^(n choose 2)]` cannot be congruent modulo `P`: their difference has absolute value less than `P` and is divisible by `P`, hence is zero. CRT therefore reconstructs the unique nonnegative answer in that interval from the residues `C(n,omega) mod p_i`.

The implementation uses convenient NTT primes as one backend. That is an implementation choice, not a restriction of the theorem: the abstract field-operation theorem may use any standard fast polynomial-multiplication algorithm over finite fields, provided the required FPS inverse, exponential, derivative, and integral routines are charged in terms of `M(d)` and the primes exceed `n`.

This proves exact integer recovery provided the prime product and modular executions are supplied. It does not by itself prove a bit-complexity bound for prime generation, modular arithmetic, or CRT.
