from . import exact_crt
from .transformed_fast import dp


DEFAULT_PRIMES = ((998244353, 3), (1004535809, 3), (469762049, 3))


def count_chordal_exact(n, omega, bound, primes=DEFAULT_PRIMES):
    residues = []
    modulus = 1
    try:
        for prime, root in primes:
            if prime <= n:
                raise ValueError("all reconstruction primes must be greater than n")
            dp.configure(prime, root)
            residues.append((prime, dp.count_chordal(n, omega)))
            modulus *= prime
            if modulus > bound:
                return exact_crt.reconstruct_nonnegative(residues, bound)
    finally:
        dp.configure(998244353, 3)
    raise ValueError("supplied prime product is too small for the bound")
