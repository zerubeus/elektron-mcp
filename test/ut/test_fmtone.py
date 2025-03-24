from elektron_mcp.elektron_params import elektron_config


def test_fmtone_page1_all_params():
    """Test all parameters in FMTONE page 1"""
    expected_params = {
        "ALGO": {
            "midi": {"cc_msb": "40", "nrpn_lsb": "1", "nrpn_msb": "73"},
            "max_midi_value": 7,
            "min_midi_value": 0,
            "max_value": 8,
            "min_value": 1,
            "default_value": 1,
            "options": None,
        },
        "C": {
            "midi": {"cc_msb": "41", "nrpn_lsb": "1", "nrpn_msb": "74"},
            "max_midi_value": 18,
            "min_midi_value": 0,
            "max_value": 16,
            "min_value": 0.25,
            "default_value": 1.0,
            "options": None,
        },
        "A": {
            "midi": {"cc_msb": "42", "nrpn_lsb": "1", "nrpn_msb": "75"},
            "max_midi_value": 35,
            "min_midi_value": 0,
            "max_value": 16,
            "min_value": 0.25,
            "default_value": 1.0,
            "options": None,
        },
        "B": {
            "midi": {"cc_msb": "43", "nrpn_lsb": "1", "nrpn_msb": "76"},
            "max_midi_value": 3,
            "min_midi_value": 0,
            "max_value": [16, 16],
            "min_value": [0.25, 0.25],
            "default_value": [1.0, 1.0],
            "options": None,
        },
        "HARM": {
            "midi": {"cc_msb": "44", "nrpn_lsb": "1", "nrpn_msb": "77"},
            "max_midi_value": 37,
            "min_midi_value": 90,
            "max_value": 26,
            "min_value": -26,
            "default_value": 0.0,
            "options": None,
        },
        "DTUN": {
            "midi": {"cc_msb": "45", "nrpn_lsb": "1", "nrpn_msb": "78"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "FDBK": {
            "midi": {"cc_msb": "46", "nrpn_lsb": "1", "nrpn_msb": "79"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MIX": {
            "midi": {"cc_msb": "47", "nrpn_lsb": "1", "nrpn_msb": "80"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 63,
            "min_value": -63,
            "default_value": -63,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmtone.pages["page_1"].parameters

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

    # Verify no extra parameters exist
    assert set(actual_params.keys()) == set(
        expected_params.keys()
    ), "Extra parameters found"


def test_fmtone_page2_all_params():
    """Test all parameters in FMTONE page 2"""
    expected_params = {
        "A": {
            "atk": {
                "midi": {"cc_msb": "48", "nrpn_lsb": "1", "nrpn_msb": "81"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
                "options": None,
            },
            "dec": {
                "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 32,
                "options": None,
            },
            "end": {
                "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 127,
                "options": None,
            },
            "lev": {
                "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
                "options": None,
            },
        },
        "B": {
            "atk": {
                "midi": {"cc_msb": "48", "nrpn_lsb": "1", "nrpn_msb": "81"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
                "options": None,
            },
            "dec": {
                "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 32,
                "options": None,
            },
            "end": {
                "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 127,
                "options": None,
            },
            "lev": {
                "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
                "options": None,
            },
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmtone.pages["page_2"].parameters

    # Verify all expected parameters exist
    for param_name, expected_values in expected_params.items():
        assert param_name in actual_params, f"Missing parameter: {param_name}"
        param = actual_params[param_name]

        # For nested parameters
        for nested_name, nested_expected in expected_values.items():
            assert (
                nested_name in param
            ), f"Missing nested parameter: {nested_name} in {param_name}"
            nested_param = param[nested_name]

            # Verify all fields match
            assert (
                nested_param.midi.cc_msb == nested_expected["midi"]["cc_msb"]
            ), f"Mismatch in {param_name}.{nested_name} cc_msb"
            assert (
                nested_param.midi.nrpn_lsb == nested_expected["midi"]["nrpn_lsb"]
            ), f"Mismatch in {param_name}.{nested_name} nrpn_lsb"
            assert (
                nested_param.midi.nrpn_msb == nested_expected["midi"]["nrpn_msb"]
            ), f"Mismatch in {param_name}.{nested_name} nrpn_msb"
            assert (
                nested_param.max_midi_value == nested_expected["max_midi_value"]
            ), f"Mismatch in {param_name}.{nested_name} max_midi_value"
            assert (
                nested_param.min_midi_value == nested_expected["min_midi_value"]
            ), f"Mismatch in {param_name}.{nested_name} min_midi_value"
            assert (
                nested_param.max_value == nested_expected["max_value"]
            ), f"Mismatch in {param_name}.{nested_name} max_value"
            assert (
                nested_param.min_value == nested_expected["min_value"]
            ), f"Mismatch in {param_name}.{nested_name} min_value"
            assert (
                nested_param.default_value == nested_expected["default_value"]
            ), f"Mismatch in {param_name}.{nested_name} default_value"

    # Verify no extra parameters exist
    assert set(actual_params.keys()) == set(
        expected_params.keys()
    ), "Extra parameters found"
