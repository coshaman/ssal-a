from verification.bruteforce import count_graphs
from verification.direct_oracle.dp import count_chordal


def test_bruteforce_chordality_matches_dp():
    assert [count_graphs(n) for n in range(1, 6)] == [1, 2, 8, 61, 822]
    assert [count_graphs(n) for n in range(1, 6)] == [count_chordal(n, n) for n in range(1, 6)]


def test_bruteforce_six_vertices():
    assert count_graphs(6) == 18154
