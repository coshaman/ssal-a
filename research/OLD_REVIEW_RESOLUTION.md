# Old Review Resolution

The six-reviewer panel recorded in `research/INDEPENDENT_REVIEW_PANEL.md` assessed an earlier manuscript version. This map checks those objections against the current post-revision manuscript; it does not infer acceptance.

| Historical objection | Resolution | Current evidence |
|---|---|---|
| Full HLV state vocabulary and source recurrence were omitted. | RESOLVED | Section 2, pp. 2–3, defines the accelerated state, domains, base cases, exact recurrence, proper-subset range, and the `i=0`, `0<i<ell`, and `i=ell` cases. |
| The `r=x'+ell'` regrouping and helper were not credited precisely. | RESOLVED | Sections 1–3, pp. 1–3, identify the regrouping as dissertation prior art and isolate the present coefficient-extraction step. |
| The forcing term appeared to require a dense contraction. | RESOLVED | Section 3, p. 3, states that `H` is only an algebraic abbreviation; Section 4, pp. 3–4, computes `Q=sum_r R_r B_r` as univariate products. |
| The coefficient-extraction identity lacked a full accounting of binomial and boundary terms. | RESOLVED | Section 3, p. 3, gives the coefficient ranges, weights, endpoint term, and correspondence `u=r-i`. |
| The EGF factorial shift and `q=0` issue were unclear. | RESOLVED | Section 4, pp. 3–4, uses `q=1..K`, defines `F_0=0`, derives coefficients, and explains `(q-1)!` explicitly. |
| Formal ODE uniqueness and truncation were asserted. | RESOLVED | Section 4, p. 4, gives the integrating-factor solution and coefficient-by-coefficient uniqueness in the truncated ring. |
| The all-`k` block invariant and hidden extra-`n` factor were not established. | RESOLVED | Section 5, p. 4, states one vector solve per `(t,x,ell,z,omega)`, gives the cache key, and charges the global block sum. |
| Auxiliary-family costs were merely asserted. | RESOLVED | Sections 5 and 9, pp. 4 and 6–7, give coarse family charges and the auxiliary recurrence ledger. |
| Exact CRT and bit complexity were conflated. | RESOLVED | Section 6, p. 5, separates the finite-field theorem from CRT recovery and explicitly limits the bit/RAM claim. |
| The paper was too compressed and not reproducible. | RESOLVED | Sections 2–9, pp. 2–7, now contain the proof machinery, recurrence ledger, implementation checks, and repository reproduction entry points. |
| Novelty and prior-art positioning were too broad. | RESOLVED | Section 8, p. 6, narrows the claim to the post-dissertation coefficient-extraction/EGF/FPS acceleration and uses conservative priority language. |

Remaining non-scientific release gates are handled separately in the current final release audit: independent fresh review, clean-package synchronization, and final remote verification.
