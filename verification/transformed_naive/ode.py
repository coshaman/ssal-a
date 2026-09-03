from fractions import Fraction
from math import comb, factorial


def binomial_recurrence(a, h, K):
    out = [0] * (K + 1)
    for k in range(1, K + 1):
        out[k] = sum(
            comb(k - 1, q - 1) * (a[q] * out[k - q] + h[q, k - q])
            for q in range(1, k + 1)
        )
    return out


def solve_ode_egf(a, h, K):
    p = [Fraction(0) for _ in range(K)]
    qpoly = [Fraction(0) for _ in range(K)]
    for q in range(1, K + 1):
        p[q - 1] += Fraction(a[q], factorial(q - 1))
        for j in range(K - q + 1):
            qpoly[q + j - 1] += Fraction(h[q, j], factorial(q - 1) * factorial(j))

    f = [Fraction(0) for _ in range(K + 1)]
    for n in range(K):
        f[n + 1] = (qpoly[n] + sum(p[i] * f[n - i] for i in range(n) if i < len(p))) / (n + 1)
    return [int(value * factorial(k)) for k, value in enumerate(f)]
