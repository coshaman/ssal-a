# Matthew Sun 2026 priority audit

Audit date: 2026-09-03.

The public repository page describes `assemble.py` as “the labeled HLV DP, used as the base case” for the equivariant/unlabeled program. Its README describes the new contribution as a divisor-bundle/Burnside method and reports labeled values as validation data. The 2026 paper likewise states that the identity-permutation instance is exactly the earlier labeled recurrence and gives the earlier labeled theorem as its Theorem 2; its new asymptotic theorem is sub-exponential for the unlabeled Burnside computation, not a faster polynomial labeled counter.

The repository URL was not fetchable from the current GitHub endpoint during this audit: a read-only `git clone https://github.com/msun170/chordal-counting.git` returned “Repository not found.” The cached repository page exposed the file listing and README but not the source body or commit diffs. Therefore the following code-level questions cannot be certified from the current endpoint: whether `assemble.py` contains the dissertation's `r/h` regrouping, whether it contains polynomial convolution or factorial-normalized EGF/FPS code, and the detailed history of changes to that file.

What is established from the available primary sources:

1. Sun's paper treats the labeled identity case as the HLV recurrence, not as a newly stated EGF/FPS acceleration.
2. Sun's stated structural contribution is equivariant divisor-bundle decomposition, with a sub-exponential unlabeled bound.
3. OEIS A058862 attributes extensions `a(16)`–`a(18)` to Sun on 2026-06-26 and links the unlabeled paper; it does not describe an asymptotically faster labeled algorithm.
4. No available source states the proposed `O(n^5 M(n))` labeled EGF/FPS acceleration.

Conclusion: Sun is important contemporary computational/sequence prior art and must be cited, but the available evidence does not show that his work contains the proposed acceleration. Because the repository source and history were unavailable, this does not establish priority or justify a “first” claim.
