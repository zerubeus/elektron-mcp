from elektron_mcp.elektron_types import (
    elektron_config,
)


# Original config dictionary
elektron_fn_to_midi = {
    "fmdrum": {
        "page_1": {
            "tune": {
                "midi": {"cc_msb": "40", "nrpn_lsb": "1", "nrpn_msb": "73"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 60,
                "min_value": -60,
                "default_value": 0,
            },
        }
    }
}


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
        assert hasattr(elektron_config, synth)

    # Check all filters exist
    for filter_type in expected_filters:
        assert hasattr(elektron_config, filter_type)

    # Check other sections exist
    for other in expected_others:
        assert hasattr(elektron_config, other)
