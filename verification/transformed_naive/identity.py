from math import comb


def direct_sum(x, ell, z, k, g1, fp, gp, current):
    total = 0
    for q in range(1, k + 1):
        for xp in range(x + 1):
            for ellp in range(ell + 1):
                r = xp + ellp
                if not 0 < r < x + ell:
                    continue
                weight = comb(x, xp) if ellp else comb(x, xp) - comb(z, xp)
                tail = fp[(ellp, k - q)] if ellp < ell and ellp else current[k - q]
                if ellp == ell:
                    tail = gp[k - q]
                total += comb(k - 1, q - 1) * comb(ell, ellp) * g1[(r, q)] * weight * tail
    return total


def compressed_sum(x, ell, z, k, g1, fp, gp, current):
    total = 0
    for q in range(1, k + 1):
        for r in range(1, x + ell):
            a = comb(x, r) - comb(z, r)
            for ellp in range(ell + 1):
                xp = r - ellp
                if not 0 <= xp <= x or not 0 <= ellp <= ell:
                    continue
                if ellp == 0:
                    tail = current[k - q]
                    weight = a
                elif ellp == ell:
                    tail = gp[k - q]
                    weight = comb(x, xp)
                else:
                    tail = fp[(ellp, k - q)]
                    weight = comb(x, xp)
                total += comb(k - 1, q - 1) * comb(ell, ellp) * g1[(r, q)] * weight * tail
    return total
