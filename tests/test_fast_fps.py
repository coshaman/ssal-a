from verification.transformed_fast.fps import exp, inverse, mul
from verification.transformed_fast.fps import MOD


def test_ntt_multiplication_matches_small_cauchy_product():
    assert mul([1, 2, 3], [4, 5], 5) == [4, 13, 22, 15]


def test_ntt_branch_matches_cauchy_product():
    a = list(range(20))
    b = list(range(17, 37))
    expected = [sum(a[i] * b[j] for i in range(len(a)) for j in range(len(b)) if i + j == k) % MOD for k in range(25)]
    assert mul(a, b, 25) == expected


def test_fps_inverse_and_exp():
    assert mul([1, 1], inverse([1, 1], 3), 3) == [1, 0, 0]
    assert exp([0, 1], 5) == [1, 1, 499122177, 166374059, 291154603]
