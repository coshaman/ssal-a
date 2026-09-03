from verification.transformed_naive.dp import count_chordal, count_connected


def test_transformed_dp_matches_reference_counts():
    assert [count_connected(n, n) for n in range(1, 6)] == [1, 1, 4, 35, 541]
    assert [count_chordal(n, n) for n in range(1, 6)] == [1, 2, 8, 61, 822]
