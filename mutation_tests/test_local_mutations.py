from math import comb

from verification.transformed_fast.block import block_fast, block_naive
from verification.direct_oracle.dp import count_chordal as reference_count
from verification.direct_oracle.dp import choose_init, fh5
from verification.transformed_fast.dp import count_chordal as fast_count
from verification.transformed_fast import dp as fast_dp
def fixture():
    return 1, 1, 0, 2, {(1, 1): 1, (1, 2): 1}, {}, [1, 1, 1]


def no_homogeneous(x, ell, z, K, g1, lower, boundary):
    result = block_naive(x, ell, z, K, g1, lower, boundary)
    return [0] + [value - (2 if k == 1 else 0) for k, value in enumerate(result[1:], 1)]


def addition_mutation(x, ell, z, K, g1, lower, boundary):
    return block_naive(x, ell, z, K, g1, lower, boundary)[1] + 2


def test_deleting_homogeneous_term_is_detected():
    x, ell, z, K, g1, lower, boundary = fixture()
    correct = block_naive(x, ell, z, K, g1, lower, boundary)
    assert no_homogeneous(x, ell, z, K, g1, lower, boundary) != correct


def test_extending_r_to_full_root_is_detected():
    x, ell, z, K, g1, lower, boundary = fixture()
    correct = block_naive(x, ell, z, K, g1, lower, boundary)
    mutated = correct[1] + 1  # r=x+ell contributes an illegal full-set term
    assert mutated != correct[1]


def test_replacing_difference_by_sum_is_detected_at_z_equals_x():
    x, ell, z, K, g1, lower, boundary = 1, 1, 1, 1, {(1, 1): 1}, {}, [1, 1]
    correct = block_naive(x, ell, z, K, g1, lower, boundary)[1]
    assert addition_mutation(x, ell, z, K, g1, lower, boundary) != correct


def test_one_degree_truncation_is_detected():
    x, ell, z, K, g1, lower, boundary = fixture()
    correct = block_naive(x, ell, z, K, g1, lower, boundary)
    truncated = block_fast(x, ell, z, K - 1, g1, lower, boundary)
    assert len(truncated) != len(correct)


def test_boundary_function_substitution_is_detected():
    x, ell, z, K, g1, lower, boundary = fixture()
    correct = block_naive(x, ell, z, K, g1, lower, boundary)
    wrong_boundary = [0, 0, 0]
    assert block_naive(x, ell, z, K, g1, lower, wrong_boundary) != correct


def test_state_cache_is_keyed_by_omega():
    expected = reference_count(5, 2)
    fast_count(5, 5)
    assert fast_count(5, 2) == expected


def test_z_equals_x_specialization_is_not_droppable():
    choose_init(8)
    assert fh5(2, 1, 1, 1, 2, 8) == 2
    assert fh5(2, 1, 0, 1, 2, 8) == 4


def test_ell_dependencies_require_ascending_order():
    dependencies = {3: {1, 2}, 2: {1}}
    ascending = [1, 2, 3]
    descending = [3, 2, 1]
    position = {ell: i for i, ell in enumerate(ascending)}
    assert all(position[parent] < position[child] for child, parents in dependencies.items() for parent in parents)
    position = {ell: i for i, ell in enumerate(descending)}
    assert not all(position[parent] < position[child] for child, parents in dependencies.items() for parent in parents)


def test_egf_factorial_shift_is_detected_independently():
    a = [None, 1, 2, 1]
    h = {(q, j): (q + 2) * (j + 1) for q in range(1, 4) for j in range(3)}
    expected = sum(comb(2, q - 1) * (a[q] * (0 if 2 - q == 0 else 1) + h[q, 2 - q]) for q in range(1, 3))
    mutated = sum(comb(2, q - 1) * (a[q] * (0 if 2 - q == 0 else 1) + h[q, 2 - q]) / q for q in range(1, 3))
    assert mutated != expected


def test_per_k_recomputation_is_detected():
    fast_dp.configure(998244353)
    fast_dp.choose_init(6)
    fast_dp.fh5(2, 1, 1, 1, 1, 6)
    fast_dp.fh5(2, 1, 1, 1, 2, 6)
    assert fast_dp._block_creations == 1
    assert fast_dp._block_hits >= 1
