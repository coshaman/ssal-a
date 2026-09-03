from verification.transformed_fast import dp
from verification.transformed_fast.fps import MOD


def collect(n, omega):
    dp.configure(MOD)
    value = dp.count_chordal(n, omega)
    functions = (dp.g, dp.gt, dp.gh, dp.g1, dp.g2, dp.f, dp.ft, dp.fh5, dp.all_graphs)
    return {
        "status": "instrumented",
        "n": n,
        "omega": omega,
        "modulus": MOD,
        "result_mod_p": value,
        "blocks": len(dp._blocks),
        "block_creations": dp._block_creations,
        "block_hits": dp._block_hits,
        "states_by_type": {fn.__name__: fn.cache_info().currsize for fn in functions},
        "block_truncation_lengths": sorted({dp._N - x - ell for _, _, _, x, _, ell, _ in dp._blocks}),
        "global_bound_bits": n * (n - 1) // 2 + 1,
        "notes": ["The creation count is the number of distinct block keys materialized in this run; hits are later k-queries served by an existing block. This is an implementation certificate, not by itself a proof of the asymptotic theorem."]
    }
