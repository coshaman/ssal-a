import random
from math import comb

from verification.transformed_naive.identity import compressed_sum, direct_sum
from verification.transformed_naive.ode import binomial_recurrence, solve_ode_egf


def test_compressed_sum_matches_literal_lemma_16_sum():
    rng = random.Random(7)
    for _ in range(20):
        x, ell, z, k = rng.randrange(0, 4), rng.randrange(1, 4), rng.randrange(0, 5), rng.randrange(1, 5)
        if z > x:
            z = x
        g1 = {(r, q): rng.randrange(-3, 4) for r in range(x + ell) for q in range(1, k + 1)}
        fp = {(i, j): rng.randrange(-3, 4) for i in range(1, ell) for j in range(k + 1)}
        gp = {j: rng.randrange(-3, 4) for j in range(k + 1)}
        current = {j: rng.randrange(-3, 4) for j in range(k + 1)}
        assert compressed_sum(x, ell, z, k, g1, fp, gp, current) == direct_sum(x, ell, z, k, g1, fp, gp, current)


def test_egf_ode_matches_binomial_recurrence():
    a = [None, 2, -1, 3, 1]
    h = {(q, j): (q + 1) * (j - 2) for q in range(1, 5) for j in range(4)}
    assert solve_ode_egf(a, h, 3) == binomial_recurrence(a, h, 3)


def test_q_factorial_mutation_is_detected():
    a = [None, 2, -1, 3]
    h = {(q, j): q + j + 1 for q in range(1, 4) for j in range(3)}
    expected = binomial_recurrence(a, h, 3)
    mutated = [0, 0, 0, 0]
    for k in range(1, 4):
        mutated[k] = sum(
            comb(k - 1, q - 1) * (a[q] * mutated[k - q] + h[q, k - q]) / q
            for q in range(1, k + 1)
        )
    assert mutated != expected
