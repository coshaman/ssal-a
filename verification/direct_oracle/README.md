# Literal direct oracle

`dp.py` is a Python translation of the authors' published recurrence family, retaining the literal `(k',x',ell')` summation in `fh5` rather than using `r` compression. It uses exact Python integers and memoization.

Verified unrestricted outputs (`omega=n`):

| n | connected | all |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 1 | 2 |
| 3 | 4 | 8 |
| 4 | 35 | 61 |
| 5 | 541 | 822 |
| 6 | 13302 | 18154 |

These agree with OEIS A007134 (connected) and A058862 (all), whose current records list the same initial terms.
