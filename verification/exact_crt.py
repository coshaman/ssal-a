from math import gcd


def reconstruct_nonnegative(residues, bound):
    """Reconstruct the unique integer in [0,bound] from CRT residues."""
    if bound < 0 or not residues:
        raise ValueError("a nonnegative bound and at least one residue are required")
    x, modulus = 0, 1
    for prime, residue in residues:
        if prime <= 1 or gcd(modulus, prime) != 1:
            raise ValueError("moduli must be pairwise coprime integers greater than one")
        residue %= prime
        step = ((residue - x) * pow(modulus, -1, prime)) % prime
        x += modulus * step
        modulus *= prime
    if modulus <= bound or x > bound:
        raise ValueError("combined modulus is too small for the supplied bound")
    return x


def reconstruct_signed(residues, bound):
    """Reconstruct the unique integer in [-bound,bound] from CRT residues."""
    if bound < 0 or not residues:
        raise ValueError("a nonnegative bound and at least one residue are required")
    x, modulus = 0, 1
    for prime, residue in residues:
        if prime <= 1 or gcd(modulus, prime) != 1:
            raise ValueError("moduli must be pairwise coprime integers greater than one")
        residue %= prime
        step = ((residue - x) * pow(modulus, -1, prime)) % prime
        x += modulus * step
        modulus *= prime
    candidate = x if x <= modulus // 2 else x - modulus
    if abs(candidate) > bound:
        raise ValueError("combined modulus is too small for the supplied bound")
    return candidate
