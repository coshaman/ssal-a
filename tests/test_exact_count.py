from verification.exact_count import count_chordal_exact


def test_exact_count_reconstructs_nine_vertex_count():
    assert count_chordal_exact(9, 9, 3_000_000_000) == 2_192_816_760


def test_exact_count_reconstructs_multiple_small_known_counts():
    primes = tuple((p, 3) for p in (17, 19, 23, 29, 31, 37, 41, 43, 47))
    assert count_chordal_exact(6, 6, 2**16, primes) == 18_154
    assert count_chordal_exact(8, 8, 2**28, primes) == 30_888_596


def test_exact_count_rejects_prime_not_above_factorial_range():
    try:
        count_chordal_exact(9, 9, 3_000_000_000, ((7, 3),))
    except ValueError as exc:
        assert "greater than n" in str(exc)
    else:
        raise AssertionError("a prime not greater than n must be rejected")
