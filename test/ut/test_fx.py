from elektron_mcp.digitone.digitone_params import digitone_config


def test_fx_all_params():
    """Test all parameters in the FX page"""
    expected_params = {
        "BR": {
            "midi": {"cc_msb": "78", "nrpn_lsb": "1", "nrpn_msb": "5"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "OVER": {
            "midi": {"cc_msb": "81", "nrpn_lsb": "1", "nrpn_msb": "8"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "SRR": {
            "midi": {"cc_msb": "79", "nrpn_lsb": "1", "nrpn_msb": "6"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "SR.RT(pre/post)": {
            "midi": {"cc_msb": "80", "nrpn_lsb": "1", "nrpn_msb": "7"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "pre",
            "options": ["pre", "post"],
        },
        "OD.RT(pre/post)": {
            "midi": {"cc_msb": "82", "nrpn_lsb": "1", "nrpn_msb": "9"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "pre",
            "options": ["pre", "post"],
        },
        "DEL": {
            "midi": {"cc_msb": "30", "nrpn_lsb": "1", "nrpn_msb": "36"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "REV": {
            "midi": {"cc_msb": "31", "nrpn_lsb": "1", "nrpn_msb": "37"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "CHR": {
            "midi": {"cc_msb": "29", "nrpn_lsb": "1", "nrpn_msb": "35"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.fx_page.parameters

    # Verify all expected parameters exist
    for param_name, expected_values in expected_params.items():
        assert param_name in actual_params, f"Missing parameter: {param_name}"
        param = actual_params[param_name]

        # Verify all fields match
        assert (
            param.midi.cc_msb == expected_values["midi"]["cc_msb"]
        ), f"Mismatch in {param_name} cc_msb"
        assert (
            param.midi.nrpn_lsb == expected_values["midi"]["nrpn_lsb"]
        ), f"Mismatch in {param_name} nrpn_lsb"
        assert (
            param.midi.nrpn_msb == expected_values["midi"]["nrpn_msb"]
        ), f"Mismatch in {param_name} nrpn_msb"
        assert (
            param.max_midi_value == expected_values["max_midi_value"]
        ), f"Mismatch in {param_name} max_midi_value"
        assert (
            param.min_midi_value == expected_values["min_midi_value"]
        ), f"Mismatch in {param_name} min_midi_value"
        assert (
            param.max_value == expected_values["max_value"]
        ), f"Mismatch in {param_name} max_value"
        assert (
            param.min_value == expected_values["min_value"]
        ), f"Mismatch in {param_name} min_value"
        assert (
            param.default_value == expected_values["default_value"]
        ), f"Mismatch in {param_name} default_value"
        if expected_values["options"] is not None:
            assert (
                param.options == expected_values["options"]
            ), f"Mismatch in {param_name} options"

    # Verify no extra parameters exist
    assert set(actual_params.keys()) == set(
        expected_params.keys()
    ), "Extra parameters found"
