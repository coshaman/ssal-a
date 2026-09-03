MOD = 998244353
PRIMITIVE_ROOT = 3


def configure(mod, primitive_root=3):
    global MOD, PRIMITIVE_ROOT
    MOD, PRIMITIVE_ROOT = mod, primitive_root


def _ntt(a, invert):
    n = len(a)
    j = 0
    for i in range(1, n):
        bit = n >> 1
        while j & bit:
            j ^= bit
            bit >>= 1
        j ^= bit
        if i < j:
            a[i], a[j] = a[j], a[i]
    length = 2
    while length <= n:
        wlen = pow(PRIMITIVE_ROOT, (MOD - 1) // length, MOD)
        if invert:
            wlen = pow(wlen, MOD - 2, MOD)
        for start in range(0, n, length):
            w = 1
            half = length // 2
            for i in range(start, start + half):
                u, v = a[i], a[i + half] * w % MOD
                a[i], a[i + half] = (u + v) % MOD, (u - v) % MOD
                w = w * wlen % MOD
        length <<= 1
    if invert:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD


def mul(a, b, limit=None):
    if limit is None:
        limit = len(a) + len(b) - 1
    if not a or not b or limit <= 0:
        return []
    need = min(limit, len(a) + len(b) - 1)
    if min(len(a), len(b)) <= 16:
        out = [0] * need
        for i, x in enumerate(a):
            for j, y in enumerate(b[: need - i]):
                out[i + j] = (out[i + j] + x * y) % MOD
        return out
    size = 1
    while size < len(a) + len(b) - 1:
        size <<= 1
    if (MOD - 1) % size:
        raise ValueError("configured modulus does not support the required NTT length")
    root = pow(PRIMITIVE_ROOT, (MOD - 1) // size, MOD)
    if pow(root, size, MOD) != 1 or (size > 1 and pow(root, size // 2, MOD) == 1):
        raise ValueError("configured primitive root does not provide the required NTT root")
    fa = list(a) + [0] * (size - len(a))
    fb = list(b) + [0] * (size - len(b))
    _ntt(fa, False)
    _ntt(fb, False)
    for i in range(size):
        fa[i] = fa[i] * fb[i] % MOD
    _ntt(fa, True)
    return fa[:need]


def derivative(a):
    return [(i + 1) * a[i + 1] % MOD for i in range(max(0, len(a) - 1))]


def integral(a):
    out = [0] * (len(a) + 1)
    for i, value in enumerate(a):
        out[i + 1] = value * pow(i + 1, MOD - 2, MOD) % MOD
    return out


def inverse(a, n):
    if not a or a[0] == 0:
        raise ValueError("FPS inverse requires a nonzero constant term")
    g = [pow(a[0], MOD - 2, MOD)]
    m = 1
    while m < n:
        m2 = min(2 * m, n)
        ag = mul(a[:m2], g, m2)
        correction = [(MOD - value) % MOD for value in ag]
        correction[0] = (correction[0] + 2) % MOD
        g = mul(g, correction, m2)
        m = m2
    return g[:n]


def _log(a, n):
    out = integral(mul(derivative(a[:n]), inverse(a, n), n - 1))
    return out + [0] * (n - len(out))


def exp(a, n):
    if a and a[0] % MOD:
        raise ValueError("FPS exponential requires zero constant term")
    g = [1]
    m = 1
    while m < n:
        m2 = min(2 * m, n)
        lg = _log(g, m2) if len(g) < m2 else _log(g, m2)
        target = list(a[:m2]) + [0] * (m2 - len(a[:m2]))
        correction = [(target[i] - lg[i]) % MOD for i in range(m2)]
        correction[0] = (correction[0] + 1) % MOD
        g = mul(g, correction, m2)
        m = m2
    return g[:n]
