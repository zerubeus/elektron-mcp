from elektron_mcp.digitone.config.config import digitone_config


def test_fmdrum_page1_all_params():
    """Test all parameters in FMDRUM page 1"""
    expected_params = {
        "tune": {
            "midi": {"cc_msb": "40", "nrpn_lsb": "1", "nrpn_msb": "73"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 60,
            "min_value": -60,
            "default_value": 0,
        },
        "stim": {
            "midi": {"cc_msb": "41", "nrpn_lsb": "1", "nrpn_msb": "74"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "sdep": {
            "midi": {"cc_msb": "42", "nrpn_lsb": "1", "nrpn_msb": "75"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "algo": {
            "midi": {"cc_msb": "43", "nrpn_lsb": "1", "nrpn_msb": "76"},
            "max_midi_value": 6,
            "min_midi_value": 0,
            "max_value": 7,
            "min_value": 1,
            "default_value": 1,
        },
        "OP.C": {
            "midi": {"cc_msb": "44", "nrpn_lsb": "1", "nrpn_msb": "77"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "OP.AB": {
            "midi": {"cc_msb": "45", "nrpn_lsb": "1", "nrpn_msb": "78"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "FDBK": {
            "midi": {"cc_msb": "46", "nrpn_lsb": "1", "nrpn_msb": "79"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "FOLD": {
            "midi": {"cc_msb": "47", "nrpn_lsb": "1", "nrpn_msb": "80"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.fmdrum.pages["page_1"].parameters

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


def test_fmdrum_page2_all_params():
    """Test all parameters in FMDRUM page 2"""
    expected_params = {
        "RATIO1": {
            "midi": {"cc_msb": "48", "nrpn_lsb": "1", "nrpn_msb": "81"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 31.75,
            "min_value": 0.001,
            "default_value": 0.5,
            "options": None,
        },
        "DEC1": {
            "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "END1": {
            "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MOD1": {
            "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "RATIO2": {
            "midi": {"cc_msb": "52", "nrpn_lsb": "1", "nrpn_msb": "85"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 31.75,
            "min_value": 0.001,
            "default_value": 0.5,
            "options": None,
        },
        "DEC2": {
            "midi": {"cc_msb": "53", "nrpn_lsb": "1", "nrpn_msb": "86"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "END2": {
            "midi": {"cc_msb": "54", "nrpn_lsb": "1", "nrpn_msb": "87"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MOD2": {
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
    actual_params = digitone_config.fmdrum.pages["page_2"].parameters

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


def test_fmdrum_page3_all_params():
    """Test all parameters in FMDRUM page 3"""
    expected_params = {
        "HOLD": {
            "midi": {"cc_msb": "56", "nrpn_lsb": "1", "nrpn_msb": "89"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "DEC": {
            "midi": {"cc_msb": "57", "nrpn_lsb": "1", "nrpn_msb": "90"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "PH.C": {
            "midi": {"cc_msb": "58", "nrpn_lsb": "1", "nrpn_msb": "91"},
            "max_midi_value": 91,
            "min_midi_value": 0,
            "max_value": 91,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "LEV": {
            "midi": {"cc_msb": "59", "nrpn_lsb": "1", "nrpn_msb": "92"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "NRST": {
            "midi": {"cc_msb": "62", "nrpn_lsb": "1", "nrpn_msb": "95"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "NRM": {
            "midi": {"cc_msb": "63", "nrpn_lsb": "1", "nrpn_msb": "96"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.fmdrum.pages["page_3"].parameters

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


def test_fmdrum_page4_all_params():
    """Test all parameters in FMDRUM page 4"""
    expected_params = {
        "NHLD": {
            "midi": {"cc_msb": "70", "nrpn_lsb": "1", "nrpn_msb": "97"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "NDEC": {
            "midi": {"cc_msb": "71", "nrpn_lsb": "1", "nrpn_msb": "98"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "TRAN": {
            "midi": {"cc_msb": "72", "nrpn_lsb": "1", "nrpn_msb": "99"},
            "max_midi_value": 124,
            "min_midi_value": 0,
            "max_value": 124,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "TLEV": {
            "midi": {"cc_msb": "73", "nrpn_lsb": "1", "nrpn_msb": "100"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "BASE": {
            "midi": {"cc_msb": "74", "nrpn_lsb": "1", "nrpn_msb": "101"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "WDTH": {
            "midi": {"cc_msb": "75", "nrpn_lsb": "1", "nrpn_msb": "102"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "GRAN": {
            "midi": {"cc_msb": "76", "nrpn_lsb": "1", "nrpn_msb": "103"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "NLEV": {
            "midi": {"cc_msb": "77", "nrpn_lsb": "1", "nrpn_msb": "104"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.fmdrum.pages["page_4"].parameters

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
