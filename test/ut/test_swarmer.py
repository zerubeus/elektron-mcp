from elektron_mcp.digitone.digitone_params import digitone_config


def test_swarmer_page1_all_params():
    """Test all parameters in SWARMER page 1"""
    expected_params = {
        "TUNE": {
            "midi": {"cc_msb": "40", "nrpn_lsb": "1", "nrpn_msb": "73"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 60,
            "min_value": -60,
            "default_value": 0,
            "options": None,
        },
        "SWRM": {
            "midi": {"cc_msb": "41", "nrpn_lsb": "1", "nrpn_msb": "74"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 120,
            "min_value": 0,
            "default_value": 80,
            "options": None,
        },
        "DET": {
            "midi": {"cc_msb": "42", "nrpn_lsb": "1", "nrpn_msb": "75"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 70,
            "options": None,
        },
        "MIX": {
            "midi": {"cc_msb": "43", "nrpn_lsb": "1", "nrpn_msb": "76"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
            "options": None,
        },
        "M.OCT": {
            "midi": {"cc_msb": "44", "nrpn_lsb": "1", "nrpn_msb": "77"},
            "max_midi_value": 2,
            "min_midi_value": 0,
            "max_value": 2,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MAIN": {
            "midi": {"cc_msb": "45", "nrpn_lsb": "1", "nrpn_msb": "78"},
            "max_midi_value": 120,
            "min_midi_value": 0,
            "max_value": 120,
            "min_value": 0,
            "default_value": 80,
            "options": None,
        },
        "ANIM": {
            "midi": {"cc_msb": "46", "nrpn_lsb": "1", "nrpn_msb": "79"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 15,
            "options": None,
        },
        "N.MOD": {
            "midi": {"cc_msb": "47", "nrpn_lsb": "1", "nrpn_msb": "80"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 20,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.swarmer.pages["page_1"].parameters

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
