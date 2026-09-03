# Sampling Audit — intentionally out of scope

The source dissertation's Theorem 3 says that, after all counter functions are precomputed and accessible in constant time, exact uniform sampling of labeled (or connected) omega-colorable chordal graphs costs `O(n^4)` arithmetic operations per sample. The proof recursively samples according to the recurrence decompositions and uses the stored counter values.

The actual `Sample Fep With Z(t,x,ell,k,z)` pseudocode in §2.8 (pp. 100–101) chooses `(k',x',ell')` with probability equal to the literal Lemma 9/16 summand divided by `fep(t,x,ell,k,z)`, then calls `Sample Ge1` and either `Sample Fep` or `Sample Gep` at the `ell'=ell` boundary. Thus a representation that retains random-access values of all counter functions is sufficient for the branch probabilities; the sampler need not store `h` separately. Recomputing the literal triple sum for each call remains the source `O(n^4)` per-sample route.

For the proposed preprocessing replacement, the following would have to be checked before restoring that claim:

1. every counter value queried by the sampling procedures in dissertation §2.6/§2.8 is materialized or recoverable in the new representation;
2. the `h`/`D_j` decomposition supplies the exact branch weights needed by the `tilde f_p` sampler;
3. recovering a branch weight on demand does not add an uncharged polynomial/FPS computation;
4. the sampler's label-set and gluing operations remain within the source `O(n^4)` bound.

The fast DP currently retains random-access `fh5` block values modulo `998244353`. A local `branch_weights` implementation reproduces the literal Lemma 16 weights and verifies that they sum to the stored counter on representative states. No graph-construction sampler has been implemented. Therefore preservation of the source `O(n^4)` sampler remains plausible from the pseudocode but is not an accepted claim of this release. The counting theorem is independent of sampling and intentionally excludes it.
