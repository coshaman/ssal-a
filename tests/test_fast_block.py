import random

from verification.transformed_fast.block import block_fast, block_naive
from verification.transformed_fast.fps import MOD


def test_fast_block_matches_scalar_transformed_recurrence():
    rng = random.Random(11)
    for _ in range(12):
        x, ell, z, K = rng.randrange(0, 4), rng.randrange(1, 4), rng.randrange(0, 4), 6
        z = min(z, x)
        g1 = {(r, q): rng.randrange(MOD) for r in range(1, x + ell) for q in range(1, K + 1)}
        lower = {(i, j): rng.randrange(MOD) for i in range(1, ell) for j in range(K + 1)}
        boundary = [rng.randrange(MOD) for _ in range(K + 1)]
        assert block_fast(x, ell, z, K, g1, lower, boundary) == block_naive(x, ell, z, K, g1, lower, boundary)
