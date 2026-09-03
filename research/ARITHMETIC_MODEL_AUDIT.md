# Arithmetic-Model Audit (preliminary)

The source theorem is explicitly an arithmetic-operation bound. The dissertation converts it to `O(n^9 log n)` RAM time because values have `O(n^2)` bits and integer multiplication is quasi-linear in the bit length (Chapter 2, p. 33). The proposed FPS method introduces factorial inverses, integration, inverse, and exponential operations, so it cannot inherit that RAM statement automatically.

## Models

1. **Characteristic zero / `Q`:** mathematically valid if divisions by factorials and ODE coefficients are represented as exact rationals. This is an algebraic-operation theorem, with coefficient growth unbounded unless separately analyzed.
2. **Finite field `F_p`:** valid for primes `p>n` (and, for all divisions used through truncation `K`, `p>K`) so factorials through `K` are invertible. A fast convolution backend requires a suitable field or extension field.
3. **Exact integers by CRT:** potentially valid after an a priori bound on the final and all intermediate values, enough pairwise-coprime primes, and a reconstruction argument. The required modulus size is not yet proved for the transformed intermediates.
4. **RAM/bit complexity:** not established. FFT/FPS costs, coefficient growth, modular reconstruction, and conversion overhead must all be bounded.

## Current conclusion

The strongest currently defensible core theorem is an algebraic-operation theorem over a field of characteristic larger than every truncation length used, combined with exact final-output CRT reconstruction. No unconditional apples-to-apples improvement over the source `O(n^9 log n)` RAM bound is claimed.

## Division-free possibility

The original binomial recurrence is division-free over the integers. The EGF representation is not division-free as written because it uses factorial inverses and formal integration. A ring-compatible alternative would need to store scaled coefficients and implement the ODE recurrence without dividing by nonunits; this remains open in this audit.

## CRT obligation

CRT is rigorous here because the final output is an integer count bounded by `2^{binom(n,2)}`, the recurrence is an integer identity reduced modulo each prime `p>n`, and no intermediate value is reconstructed. Choosing a product greater than twice the output bound gives unique recovery. The remaining question is total bit cost, handled separately in `research/BIT_COMPLEXITY_PROOF.md`.

## A valid coarse bound

Every counter entry is a count of a subclass of simple labeled graphs on at most `n` vertices, so it is at most

`B(n)=2^{binom(n,2)}`.

The same bound applies to the final all-graph count and connected count. Thus CRT reconstruction of a nonnegative final answer is unique once the combined modulus `P` satisfies `P>2B(n)`. This requires `log_2 P > n(n-1)/2+1` bits. The local `reconstruct_signed` utility implements the bounded uniqueness check.

The repository now includes a configurable modular backend and an exact-count driver that repeats the DP over selected primes and reconstructs once the product exceeds `2*bound`. A nine-vertex unrestricted count is reconstructed from two primes in a test. This establishes a rigorous small-instance modular-to-integer path, but not yet a complete asymptotic fast exact algorithm: the multiplication backend must be available over each selected field for arbitrary `n` (or an extension-field implementation must be specified), and the total cost of running enough primes must be charged. It also does not prove a better bit bound than the source algorithm.
