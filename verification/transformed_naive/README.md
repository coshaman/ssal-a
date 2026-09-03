# Transformed-naive oracle

`dp.py` duplicates the source counter family but rewrites the `tilde f_p` summation by `r=x'+ell'`, constructing `h` with the reconstructed `D_j` coefficients. It intentionally uses scalar loops rather than polynomial/FPS acceleration.

The implementation agrees with the literal oracle for all tested `n<=7` and `1<=omega<=n`.
