from verification.direct_oracle.dp import count_chordal, count_connected


def test_source_dp_matches_small_known_counts():
    assert count_connected(1, 1) == 1
    assert count_connected(2, 2) == 1
    assert count_connected(3, 3) == 4
    assert count_chordal(3, 3) == 8
