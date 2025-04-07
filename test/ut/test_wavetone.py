from elektron_mcp.digitone.config.config import digitone_config


def test_wavetone_page1_all_params():
    """Test all parameters in WAVETONE page 1"""
    expected_params = {
        "TUN1": {
            "midi": {"cc_msb": "40", "nrpn_lsb": "1", "nrpn_msb": "73"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 5,
            "min_value": -5,
            "default_value": 0,
            "options": None,
        },
        "WAV1": {
            "midi": {"cc_msb": "41", "nrpn_lsb": "1", "nrpn_msb": "74"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 120,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "PD1": {
            "midi": {"cc_msb": "42", "nrpn_lsb": "1", "nrpn_msb": "75"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 100,
            "min_value": 0,
            "default_value": 50,
            "options": None,
        },
        "LEV1": {
            "midi": {"cc_msb": "43", "nrpn_lsb": "1", "nrpn_msb": "76"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 100,
            "options": None,
        },
        "TUN2": {
            "midi": {"cc_msb": "44", "nrpn_lsb": "1", "nrpn_msb": "77"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 5,
            "min_value": -5,
            "default_value": 0,
            "options": None,
        },
        "WAV2": {
            "midi": {"cc_msb": "45", "nrpn_lsb": "1", "nrpn_msb": "78"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 120,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "PD2": {
            "midi": {"cc_msb": "46", "nrpn_lsb": "1", "nrpn_msb": "79"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 100,
            "min_value": 0,
            "default_value": 50,
            "options": None,
        },
        "LEV2": {
            "midi": {"cc_msb": "47", "nrpn_lsb": "1", "nrpn_msb": "80"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 100,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.wavetone.pages["page_1"].parameters

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


def test_wavetone_page2_all_params():
    """Test all parameters in WAVETONE page 2"""
    expected_params = {
        "OFS1": {
            "midi": {"cc_msb": "48", "nrpn_lsb": "1", "nrpn_msb": "81"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 10,
            "min_value": -10,
            "default_value": 0,
            "options": None,
        },
        "TBL1": {
            "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "prim",
            "options": ["prim", "harm"],
        },
        "MOD": {
            "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
            "max_midi_value": 3,
            "min_midi_value": 0,
            "max_value": 3,
            "min_value": 0,
            "default_value": "off",
            "options": ["off", "ring mod", "ring mod fixed", "hard sync"],
        },
        "RSET": {
            "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
            "max_midi_value": 2,
            "min_midi_value": 0,
            "max_value": 2,
            "min_value": 0,
            "default_value": "on",
            "options": ["off", "on", "random"],
        },
        "OFS2": {
            "midi": {"cc_msb": "52", "nrpn_lsb": "1", "nrpn_msb": "85"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 10,
            "min_value": -10,
            "default_value": 0,
            "options": None,
        },
        "TBL2": {
            "midi": {"cc_msb": "53", "nrpn_lsb": "1", "nrpn_msb": "86"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": "prim",
            "options": ["prim", "harm"],
        },
        "DRIF": {
            "midi": {"cc_msb": "55", "nrpn_lsb": "1", "nrpn_msb": "88"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.wavetone.pages["page_2"].parameters

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


def test_wavetone_page3_all_params():
    """Test all parameters in WAVETONE page 3"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "56", "nrpn_lsb": "1", "nrpn_msb": "89"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "HOLD": {
            "midi": {"cc_msb": "57", "nrpn_lsb": "1", "nrpn_msb": "90"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
            "options": None,
        },
        "DEC": {
            "midi": {"cc_msb": "58", "nrpn_lsb": "1", "nrpn_msb": "91"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
            "options": None,
        },
        "NLEV": {
            "midi": {"cc_msb": "59", "nrpn_lsb": "1", "nrpn_msb": "92"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "BASE": {
            "midi": {"cc_msb": "60", "nrpn_lsb": "1", "nrpn_msb": "93"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "WDTH": {
            "midi": {"cc_msb": "61", "nrpn_lsb": "1", "nrpn_msb": "94"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
            "options": None,
        },
        "TYPE": {
            "midi": {"cc_msb": "62", "nrpn_lsb": "1", "nrpn_msb": "95"},
            "max_midi_value": 2,
            "min_midi_value": 0,
            "max_value": 2,
            "min_value": 0,
            "default_value": 0,
            "options": ["grain nose", "tuned noise", "sample and hold noise"],
        },
        "CHAR": {
            "midi": {"cc_msb": "63", "nrpn_lsb": "1", "nrpn_msb": "96"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.wavetone.pages["page_3"].parameters

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
