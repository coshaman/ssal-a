from verification.sampler import branch_weights


def test_literal_sampler_branch_weights_sum_to_counter():
    branches, total = branch_weights(2, 1, 1, 1, 2, 8)
    assert sum(weight for _, weight in branches) == total == 2
    branches, total = branch_weights(2, 1, 0, 1, 2, 8)
    assert sum(weight for _, weight in branches) == total == 4
