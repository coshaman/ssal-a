from functools import cache
from math import comb


def count_connected(n, omega):
    choose_init(n)
    return sum(C(n, ell) * f(t, 0, ell, n - ell, omega) for t in range(1, n + 1) for ell in range(1, n + 1))


def count_chordal(n, omega):
    choose_init(n)
    return all_graphs(n, omega)


_choose = []


def choose_init(n):
    global _choose
    if len(_choose) >= n + 1:
        return
    _choose = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        _choose[i][0] = _choose[i][i] = 1
        for j in range(1, i):
            _choose[i][j] = _choose[i - 1][j - 1] + _choose[i - 1][j]
    for fn in (g, gt, gh, g1, g2, f, ft, fh5, all_graphs):
        fn.cache_clear()


def C(n, k):
    return _choose[n][k] if 0 <= k <= n < len(_choose) else 0


@cache
def all_graphs(n, omega):
    if n == 0:
        return 1
    return sum(C(n - 1, k - 1) * count_connected(k, omega) * all_graphs(n - k, omega) for k in range(1, n + 1))


@cache
def g(t, x, z, k, omega):
    if t == 0:
        return int(k == 0)
    if x == 0:
        return 0
    return sum(C(k, q) * gt(t, x, z, q, omega) * g(t - 1, x, z, k - q, omega) for q in range(k + 1))


@cache
def gt(t, x, z, k, omega):
    if k == 0:
        return 1
    if t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * (C(x, u) - C(z, u)) * g1(t, u, q, omega) * gt(t, x, z, k - q, omega) for q in range(1, k + 1) for u in range(1, x + 1))


@cache
def gh(t, x, z, k, omega):
    if k == 0:
        return 1
    if t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * (C(x, u) - C(z, u)) * g1(t, u, q, omega) * gh(t, x, z, k - q, omega) for q in range(1, k + 1) for u in range(1, x))


@cache
def g1(t, x, k, omega):
    if k == 0 or t == 0 or x == 0:
        return 0
    return sum(C(k, ell) * f(t, x, ell, k - ell, omega) for ell in range(1, k + 1))


@cache
def g2(t, x, k, omega):
    if k == 0 or t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * g1(t, x, q, omega) * (g1(t, x, k - q, omega) + g2(t, x, k - q, omega)) for q in range(1, k))


@cache
def f(t, x, ell, k, omega):
    if x + ell > omega or t == 0:
        return 0
    if t == 1:
        return int(k == 0)
    if k == 0:
        return 0
    return sum(C(k, q) * ft(t, x, ell, q, omega) * g(t - 2, x + ell, x, k - q, omega) for q in range(1, k + 1))


@cache
def ft(t, x, ell, k, omega):
    if t <= 1 or k == 0:
        return 0
    ans = fh5(t, x, x, ell, k, omega)
    ans += sum(C(k, q) * g1(t - 1, x + ell, q, omega) * fh5(t, x, x, ell, k - q, omega) for q in range(1, k))
    ans += sum(C(k, q) * g2(t - 1, x + ell, q, omega) * gh(t - 1, x + ell, x, k - q, omega) for q in range(1, k + 1))
    return ans


@cache
def fh5(t, x, z, ell, k, omega):
    if t <= 1 or k == 0:
        return 0
    ans = 0
    for q in range(1, k + 1):
        for u in range(x + 1):
            for i in range(ell + 1):
                if not 0 < u + i < x + ell:
                    continue
                weight = C(x, u) if i else C(x, u) - C(z, u)
                tail = fh5(t, x + i, z, ell - i, k - q, omega) if i < ell else gh(t - 1, x + i, z, k - q, omega)
                ans += C(k - 1, q - 1) * C(ell, i) * weight * g1(t - 1, u + i, q, omega) * tail
    return ans
