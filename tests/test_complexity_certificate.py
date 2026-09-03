from complexity_certificate.generate import collect


def test_certificate_reports_fast_state_and_block_counts():
    report = collect(6, 6)
    assert report["n"] == 6
    assert report["blocks"] > 0
    assert "states_by_type" in report
