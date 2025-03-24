from elektron_mcp.digitone.digitone_params import digitone_config


def test_amp_all_params():
    """Test all parameters in the AMP page"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "84", "nrpn_lsb": "1", "nrpn_msb": "30"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 8,
            "options": None,
        },
        "HOLD": {
            "midi": {"cc_msb": "85", "nrpn_lsb": "1", "nrpn_msb": "31"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
            "options": None,
        },
        "DEC": {
            "midi": {"cc_msb": "86", "nrpn_lsb": "1", "nrpn_msb": "32"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 32,
            "options": None,
        },
        "SUS": {
            "midi": {"cc_msb": "87", "nrpn_lsb": "1", "nrpn_msb": "33"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 96,
            "options": None,
        },
        "REL": {
            "midi": {"cc_msb": "88", "nrpn_lsb": "1", "nrpn_msb": "34"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 24,
            "options": None,
        },
        "Env. RSET": {
            "midi": {"cc_msb": "92", "nrpn_lsb": "1", "nrpn_msb": "41"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "on",
            "options": ["off", "on"],
        },
        "MODE": {
            "midi": {"cc_msb": "91", "nrpn_lsb": "1", "nrpn_msb": "40"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "ADSR",
            "options": ["AHD", "ADSR"],
        },
        "PAN": {
            "midi": {"cc_msb": "89", "nrpn_lsb": "1", "nrpn_msb": "38"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
            "options": None,
        },
        "VOL": {
            "midi": {"cc_msb": "90", "nrpn_lsb": "1", "nrpn_msb": "39"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 110,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.amp_page.parameters

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
