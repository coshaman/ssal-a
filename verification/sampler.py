from verification.direct_oracle import dp


def branch_weights(t, x, z, ell, k, omega):
    """Return literal Lemma 16 sampler weights and their counter total."""
    dp.choose_init(max(x + ell + k, omega))
    branches = []
    for q in range(1, k + 1):
        for u in range(x + 1):
            for i in range(ell + 1):
                if not 0 < u + i < x + ell:
                    continue
                weight_set = dp.C(x, u) if i else dp.C(x, u) - dp.C(z, u)
                tail = dp.fh5(t, x + i, z, ell - i, k - q, omega) if i < ell else dp.gh(t - 1, x + i, z, k - q, omega)
                weight = dp.C(k - 1, q - 1) * dp.C(ell, i) * weight_set * dp.g1(t - 1, u + i, q, omega) * tail
                if weight:
                    branches.append(((q, u, i), weight))
    return branches, dp.fh5(t, x, z, ell, k, omega)
