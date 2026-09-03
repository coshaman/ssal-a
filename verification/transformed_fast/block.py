from math import comb, factorial

from . import fps
from .fps import exp, integral, inverse, mul


def _c(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def block_naive(x, ell, z, K, g1, lower, boundary):
    out = [0] * (K + 1)
    for k in range(1, K + 1):
        for q in range(1, k + 1):
            for r in range(1, x + ell):
                h = 0
                for i in range(max(0, r - x), min(r, ell) + 1):
                    u = r - i
                    if i == 0:
                        tail, weight = out[k - q], _c(x, r) - _c(z, r)
                    elif i == ell:
                        tail, weight = boundary[k - q], _c(x, u)
                    else:
                        tail, weight = lower[i, k - q], _c(x, u)
                    h += _c(ell, i) * weight * tail
                out[k] = (out[k] + _c(k - 1, q - 1) * g1[r, q] * h) % fps.MOD
    return out


def block_fast(x, ell, z, K, g1, lower, boundary):
    s = x + ell
    binom_x = [(_c(x, i) % fps.MOD) for i in range(s)]
    b = [[0] * (K + 1) for _ in range(s)]
    for j in range(K + 1):
        d = [0] * (ell + 1)
        for i in range(1, ell):
            d[i] = _c(ell, i) * lower[i, j] % fps.MOD
        d[ell] = boundary[j] % fps.MOD
        coeffs = mul(d, binom_x, s)
        for r in range(1, s):
            b[r][j] = coeffs[r] % fps.MOD

    p = [0] * (K + 1)
    qpoly = [0] * (K + 1)
    for q in range(1, K + 1):
        invfac = pow(factorial(q - 1), fps.MOD - 2, fps.MOD)
        for r in range(1, s):
            p[q - 1] = (p[q - 1] + g1[r, q] * (_c(x, r) - _c(z, r)) * invfac) % fps.MOD
    for r in range(1, s):
        gp = [g1[r, q] * pow(factorial(q - 1), fps.MOD - 2, fps.MOD) % fps.MOD for q in range(1, K + 1)]
        bp = [b[r][j] * pow(factorial(j), fps.MOD - 2, fps.MOD) % fps.MOD for j in range(K + 1)]
        product = mul(gp, bp, K)
        qpoly[:len(product)] = [(qpoly[i] + product[i]) % fps.MOD for i in range(len(product))]

    e = exp(integral(p), K + 1)
    ei = inverse(e, K + 1)
    integral_part = integral(mul(ei, qpoly, K))
    fseries = mul(e, integral_part, K + 1)
    return [fseries[k] * factorial(k) % fps.MOD for k in range(K + 1)]
