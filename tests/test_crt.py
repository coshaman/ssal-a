from verification.exact_crt import reconstruct_nonnegative, reconstruct_signed
from verification.transformed_fast import dp


def test_crt_reconstructs_signed_integer_from_known_bound():
    value = 123456789
    residues = [(1000000007, value % 1000000007), (1000000009, value % 1000000009)]
    assert reconstruct_signed(residues, 200000000) == value


def test_crt_reconstructs_nonnegative_integer_from_one_sided_bound():
    value = 18154
    residues = [(17, value % 17), (19, value % 19), (23, value % 23), (29, value % 29)]
    assert reconstruct_nonnegative(residues, 2**16) == value


def test_fast_dp_can_supply_two_modular_residues():
    expected = 2192816760
    residues = []
    for prime in (998244353, 1004535809):
        dp.configure(prime)
        residues.append((prime, dp.count_chordal(9, 9)))
    assert reconstruct_signed(residues, 3_000_000_000) == expected
    dp.configure(998244353)
