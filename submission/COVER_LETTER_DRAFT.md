# Cover-letter draft

Dear Editors,

We submit “Faster Exact Counting of Labeled Chordal Graphs via Formal Power Series” for consideration as a regular research article. The paper gives a counting-only acceleration of the labeled chordal-graph dynamic program of Hébert-Johnson, Lokshtanov, and Vigoda. It retains the `r/h` regrouping already present in the authors' 2025 dissertation, then exposes a new coefficient-extraction convolution and an EGF/FPS linear-ODE formulation. The resulting blockwise algorithm computes the modular count in `O(n^5 M_p(n))` field operations, and a separate CRT corollary recovers the exact nonnegative integer count.

We state the computational model explicitly and do not claim an unconditional bit-complexity improvement or a sampler contribution. The manuscript includes independent recurrence implementations, brute-force checks, modular/FPS tests, CRT tests, mutation checks, and block-cache instrumentation. The accompanying reproducibility package contains the source, tests, audits, and bibliography.

JGAA is a strong fit because the contribution is an exact graph-counting algorithm with a concrete implementation and reproducibility package. Priority language is conservative: we claim only that no inspected source states this additional EGF/FPS acceleration, and we explicitly credit the dissertation's prior regrouping and discuss Matthew Sun's contemporary HLV-based work.

The authors have no conflicts of interest to report beyond any information supplied separately in the submission system. [Complete author and corresponding-author metadata before submission.]

Sincerely,

[Author names and affiliations]
