from functools import cache

from .block import block_fast
from . import fps

_choose, _N = [], 0
_blocks = {}
_block_creations = 0
_block_hits = 0
_execution_active = False


def configure(mod, primitive_root=3):
    global _choose, _N, _block_creations, _block_hits, _execution_active
    fps.configure(mod, primitive_root)
    _choose, _N = [], 0
    _blocks.clear()
    _block_creations = _block_hits = 0
    _execution_active = False
    for fn in (g, gt, gh, g1, g2, f, ft, fh5, all_graphs):
        fn.cache_clear()


def C(n, k):
    return _choose[n][k] if 0 <= k <= n < len(_choose) else 0


def choose_init(n):
    global _choose, _N, _block_creations, _block_hits
    if _N == n:
        return
    _N = n
    _choose = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        _choose[i][0] = _choose[i][i] = 1
        for j in range(1, i):
            _choose[i][j] = _choose[i - 1][j - 1] + _choose[i - 1][j]
    _blocks.clear()
    _block_creations = _block_hits = 0
    for fn in (g, gt, gh, g1, g2, f, ft, fh5, all_graphs):
        fn.cache_clear()


def count_connected(n, omega):
    if not _execution_active and _N != n:
        choose_init(n)
    return sum(C(n, ell) * f(t, 0, ell, n - ell, omega) for t in range(1, n + 1) for ell in range(1, n + 1)) % fps.MOD


def count_chordal(n, omega):
    global _execution_active
    choose_init(n)
    _execution_active = True
    try:
        return all_graphs(n, omega)
    finally:
        _execution_active = False


@cache
def all_graphs(n, omega):
    if n == 0:
        return 1
    return sum(C(n - 1, k - 1) * count_connected(k, omega) * all_graphs(n - k, omega) for k in range(1, n + 1)) % fps.MOD


@cache
def g(t, x, z, k, omega):
    if t == 0:
        return int(k == 0)
    if x == 0:
        return 0
    return sum(C(k, q) * gt(t, x, z, q, omega) * g(t - 1, x, z, k - q, omega) for q in range(k + 1)) % fps.MOD


@cache
def gt(t, x, z, k, omega):
    if k == 0:
        return 1
    if t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * (C(x, u) - C(z, u)) * g1(t, u, q, omega) * gt(t, x, z, k - q, omega) for q in range(1, k + 1) for u in range(1, x + 1)) % fps.MOD


@cache
def gh(t, x, z, k, omega):
    if k == 0:
        return 1
    if t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * (C(x, u) - C(z, u)) * g1(t, u, q, omega) * gh(t, x, z, k - q, omega) for q in range(1, k + 1) for u in range(1, x)) % fps.MOD


@cache
def g1(t, x, k, omega):
    if k == 0 or t == 0 or x == 0:
        return 0
    return sum(C(k, ell) * f(t, x, ell, k - ell, omega) for ell in range(1, k + 1)) % fps.MOD


@cache
def g2(t, x, k, omega):
    if k == 0 or t == 0 or x == 0:
        return 0
    return sum(C(k - 1, q - 1) * g1(t, x, q, omega) * (g1(t, x, k - q, omega) + g2(t, x, k - q, omega)) for q in range(1, k)) % fps.MOD


@cache
def f(t, x, ell, k, omega):
    if x + ell > omega or t == 0:
        return 0
    if t == 1:
        return int(k == 0)
    if k == 0:
        return 0
    return sum(C(k, q) * ft(t, x, ell, q, omega) * g(t - 2, x + ell, x, k - q, omega) for q in range(1, k + 1)) % fps.MOD


@cache
def ft(t, x, ell, k, omega):
    if t <= 1 or k == 0:
        return 0
    ans = fh5(t, x, x, ell, k, omega)
    ans += sum(C(k, q) * g1(t - 1, x + ell, q, omega) * fh5(t, x, x, ell, k - q, omega) for q in range(1, k))
    ans += sum(C(k, q) * g2(t - 1, x + ell, q, omega) * gh(t - 1, x + ell, x, k - q, omega) for q in range(1, k + 1))
    return ans % fps.MOD


@cache
def fh5(t, x, z, ell, k, omega):
    global _block_creations, _block_hits
    if t <= 1 or k == 0:
        return 0
    key = (_N, fps.MOD, t, x, z, ell, omega)
    if key not in _blocks:
        _block_creations += 1
        K = _N - x - ell
        gvalues = {(r, q): g1(t - 1, r, q, omega) for r in range(1, x + ell) for q in range(1, K + 1)}
        lower = {(i, j): fh5(t, x + i, z, ell - i, j, omega) for i in range(1, ell) for j in range(K + 1)}
        boundary = [gh(t - 1, x + ell, z, j, omega) for j in range(K + 1)]
        _blocks[key] = block_fast(x, ell, z, K, gvalues, lower, boundary)
    else:
        _block_hits += 1
    values = _blocks[key]
    return values[k] if k < len(values) else 0
