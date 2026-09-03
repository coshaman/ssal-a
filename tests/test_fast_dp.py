from verification.transformed_fast.dp import count_chordal, count_connected


def test_fast_dp_rejects_unsupported_ntt_length():
    import verification.transformed_fast.dp as fast_dp
    fast_dp.configure(101)
    try:
        fast_dp.fps.mul([1] * 17, [1] * 17)
    except ValueError:
        pass
    else:
        raise AssertionError("unsupported NTT length was accepted")
    fast_dp.configure(998244353)


def test_fast_dp_clears_state_when_n_decreases():
    import verification.transformed_fast.dp as fast_dp
    fast_dp.configure(998244353)
    fast_dp.count_chordal(8, 8)
    fast_dp.count_chordal(5, 5)
    assert fast_dp._N == 5


def test_fast_dp_matches_reference_mod_prime():
    assert [count_connected(n, n) for n in range(1, 6)] == [1, 1, 4, 35, 541]
    assert [count_chordal(n, n) for n in range(1, 6)] == [1, 2, 8, 61, 822]


def test_fast_unrestricted_values_match_exact_counts_below_modulus():
    assert [count_chordal(n, n) for n in range(1, 9)] == [1, 2, 8, 61, 822, 18154, 617675, 30888596]


def test_fh5_block_is_created_once_then_reused():
    import verification.transformed_fast.dp as fast_dp
    from verification.transformed_fast.fps import MOD

    fast_dp.configure(MOD)
    fast_dp.choose_init(6)
    first = fast_dp.fh5(3, 1, 1, 2, 1, 6)
    creations = fast_dp._block_creations
    second = fast_dp.fh5(3, 1, 1, 2, 2, 6)
    assert first >= 0 and second >= 0
    assert fast_dp._block_creations == creations
    assert fast_dp._block_hits >= 1
