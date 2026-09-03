# Transformed-fast backend

`fps.py` provides modular NTT multiplication over `F_998244353`, Newton FPS inversion, derivative, integral, logarithm, and exponential. The NTT branch is tested against an independent Cauchy product. `dp.py` wires the blockwise EGF/FPS solver into the complete counter recurrence.

The fast DP matches the reference on all tested `n<=7` and `1<=omega<=n` modulo `998244353`. This validates correctness on small cases, but does not by itself certify the global asymptotic sum or exact integer reconstruction.
