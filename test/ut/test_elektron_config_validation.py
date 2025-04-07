from elektron_mcp.digitone.config.config import digitone_config


def test_config_structure():
    """Test that all expected synth types are present"""
    expected_synths = ["fmdrum", "fmtone", "swarmer", "wavetone"]

    expected_filters = [
        "multi_mode_filter",
        "lowpass_4_filter",
        "legacy_lp_hp_filter",
        "comb_minus_filter",
        "comb_plus_filter",
        "equalizer_filter",
        "base_width_filter",
    ]

    expected_others = ["amp_page", "fx_page", "lfo"]

    # Check all synths exist
    for synth in expected_synths:
        assert hasattr(digitone_config, synth)

    # Check all filters exist
    for filter_type in expected_filters:
        assert hasattr(digitone_config, filter_type)

    # Check other sections exist
    for other in expected_others:
        assert hasattr(digitone_config, other)
