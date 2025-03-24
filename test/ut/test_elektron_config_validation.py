from elektron_mcp.elektron_types import elektron_config

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


def test_fmdrum_page1_tune():
    """Test the FMDRUM page 1 tune parameter configuration"""
    # Get the parameter from the config
    param = elektron_config.fmdrum.pages["page_1"].parameters["tune"]

    # Get the expected values from the original config
    expected = elektron_fn_to_midi["fmdrum"]["page_1"]["tune"]

    # Verify all fields match
    assert param.midi.cc_msb == expected["midi"]["cc_msb"]
    assert param.midi.nrpn_lsb == expected["midi"]["nrpn_lsb"]
    assert param.midi.nrpn_msb == expected["midi"]["nrpn_msb"]
    assert param.max_midi_value == expected["max_midi_value"]
    assert param.min_midi_value == expected["min_midi_value"]
    assert param.max_value == expected["max_value"]
    assert param.min_value == expected["min_value"]
    assert param.default_value == expected["default_value"]


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
    actual_params = elektron_config.fmdrum.pages["page_1"].parameters

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
            "default_value": 0.500,
        },
        "DEC1": {
            "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "END1": {
            "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "MOD1": {
            "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "RATIO2": {
            "midi": {"cc_msb": "52", "nrpn_lsb": "1", "nrpn_msb": "85"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 31.75,
            "min_value": 0.001,
            "default_value": 0.500,
        },
        "DEC2": {
            "midi": {"cc_msb": "53", "nrpn_lsb": "1", "nrpn_msb": "86"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "END2": {
            "midi": {"cc_msb": "54", "nrpn_lsb": "1", "nrpn_msb": "87"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "MOD2": {
            "midi": {"cc_msb": "55", "nrpn_lsb": "1", "nrpn_msb": "88"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmdrum.pages["page_2"].parameters

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
        },
        "DEC": {
            "midi": {"cc_msb": "57", "nrpn_lsb": "1", "nrpn_msb": "90"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "PH.C": {
            "midi": {"cc_msb": "58", "nrpn_lsb": "1", "nrpn_msb": "91"},
            "max_midi_value": 91,
            "min_midi_value": 0,
            "max_value": 91,
            "min_value": 0,
            "default_value": 0,
        },
        "LEV": {
            "midi": {"cc_msb": "59", "nrpn_lsb": "1", "nrpn_msb": "92"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "NRST": {
            "midi": {"cc_msb": "62", "nrpn_lsb": "1", "nrpn_msb": "95"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 0,
        },
        "NRM": {
            "midi": {"cc_msb": "63", "nrpn_lsb": "1", "nrpn_msb": "96"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmdrum.pages["page_3"].parameters

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
        },
        "NDEC": {
            "midi": {"cc_msb": "71", "nrpn_lsb": "1", "nrpn_msb": "98"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "TRAN": {
            "midi": {"cc_msb": "72", "nrpn_lsb": "1", "nrpn_msb": "99"},
            "max_midi_value": 124,
            "min_midi_value": 0,
            "max_value": 124,
            "min_value": 0,
            "default_value": 0,
        },
        "TLEV": {
            "midi": {"cc_msb": "73", "nrpn_lsb": "1", "nrpn_msb": "100"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "BASE": {
            "midi": {"cc_msb": "74", "nrpn_lsb": "1", "nrpn_msb": "101"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "WDTH": {
            "midi": {"cc_msb": "75", "nrpn_lsb": "1", "nrpn_msb": "102"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "GRAN": {
            "midi": {"cc_msb": "76", "nrpn_lsb": "1", "nrpn_msb": "103"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "NLEV": {
            "midi": {"cc_msb": "77", "nrpn_lsb": "1", "nrpn_msb": "104"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmdrum.pages["page_4"].parameters

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
        },
        "C": {
            "midi": {"cc_msb": "41", "nrpn_lsb": "1", "nrpn_msb": "74"},
            "max_midi_value": 18,
            "min_midi_value": 0,
            "max_value": 16,
            "min_value": 0.25,
            "default_value": 1.00,
        },
        "A": {
            "midi": {"cc_msb": "42", "nrpn_lsb": "1", "nrpn_msb": "75"},
            "max_midi_value": 35,
            "min_midi_value": 0,
            "max_value": 16,
            "min_value": 0.25,
            "default_value": 1.00,
        },
        "B": {
            "midi": {"cc_msb": "43", "nrpn_lsb": "1", "nrpn_msb": "76"},
            "max_midi_value": 3,
            "min_midi_value": 0,
            "max_value": [16, 16],
            "min_value": [0.25, 0.25],
            "default_value": [1.00, 1.00],
        },
        "HARM": {
            "midi": {"cc_msb": "44", "nrpn_lsb": "1", "nrpn_msb": "77"},
            "max_midi_value": 37,
            "min_midi_value": 90,
            "max_value": 26,
            "min_value": -26,
            "default_value": 0.00,
        },
        "DTUN": {
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
        "MIX": {
            "midi": {"cc_msb": "47", "nrpn_lsb": "1", "nrpn_msb": "80"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 63,
            "min_value": -63,
            "default_value": -63,
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
            },
            "dec": {
                "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 32,
            },
            "end": {
                "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 127,
            },
            "lev": {
                "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
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
            },
            "dec": {
                "midi": {"cc_msb": "49", "nrpn_lsb": "1", "nrpn_msb": "82"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 32,
            },
            "end": {
                "midi": {"cc_msb": "50", "nrpn_lsb": "1", "nrpn_msb": "83"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 127,
            },
            "lev": {
                "midi": {"cc_msb": "51", "nrpn_lsb": "1", "nrpn_msb": "84"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
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


def test_fmtone_page3_all_params():
    """Test all parameters in FMTONE page 3"""
    expected_params = {
        "ADEL": {
            "midi": {"cc_msb": "56", "nrpn_lsb": "1", "nrpn_msb": "89"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "ATRG": {
            "midi": {"cc_msb": "57", "nrpn_lsb": "1", "nrpn_msb": "90"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 1,
        },
        "ARST": {
            "midi": {"cc_msb": "58", "nrpn_lsb": "1", "nrpn_msb": "91"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 1,
        },
        "PHRT": {
            "midi": {"cc_msb": "59", "nrpn_lsb": "1", "nrpn_msb": "92"},
            "max_midi_value": 4,
            "min_midi_value": 0,
            "options": ["off", "all", "c", "a+b", "a+b2"],
            "default_value": "all",
        },
        "BDEL": {
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "BTRG": {
            "midi": {"cc_msb": "61", "nrpn_lsb": "1", "nrpn_msb": "94"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 1,
        },
        "BRST": {
            "midi": {"cc_msb": "62", "nrpn_lsb": "1", "nrpn_msb": "95"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 1,
            "min_value": 0,
            "default_value": 1,
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmtone.pages["page_3"].parameters

    # Verify all expected parameters exist
    for param_name, expected_values in expected_params.items():
        assert param_name in actual_params, f"Missing parameter: {param_name}"
        param = actual_params[param_name]

        # Verify all fields match
        if "midi" in expected_values:
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
        if "options" in expected_values:
            assert (
                param.options == expected_values["options"]
            ), f"Mismatch in {param_name} options"
        else:
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


def test_fmtone_page4_all_params():
    """Test all parameters in FMTONE page 4"""
    expected_params = {
        "Ratio_Offset": {
            "C": {
                "midi": {"cc_msb": "70", "nrpn_lsb": "1", "nrpn_msb": "97"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 0.999,
                "min_value": -1.00,
                "default_value": 0.00,
            },
            "A": {
                "midi": {"cc_msb": "71", "nrpn_lsb": "1", "nrpn_msb": "98"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 0.999,
                "min_value": -1.00,
                "default_value": 0.00,
            },
            "B1": {
                "midi": {"cc_msb": "72", "nrpn_lsb": "1", "nrpn_msb": "99"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 0.999,
                "min_value": -1.00,
                "default_value": 0.00,
            },
            "B2": {
                "midi": {"cc_msb": "73", "nrpn_lsb": "1", "nrpn_msb": "100"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 0.999,
                "min_value": -1.00,
                "default_value": 0.00,
            },
        },
        "Key_Track": {
            "A": {
                "midi": {"cc_msb": "75", "nrpn_lsb": "1", "nrpn_msb": "102"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
            },
            "B1": {
                "midi": {"cc_msb": "76", "nrpn_lsb": "1", "nrpn_msb": "103"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
            },
            "B2": {
                "midi": {"cc_msb": "77", "nrpn_lsb": "1", "nrpn_msb": "104"},
                "max_midi_value": 127,
                "min_midi_value": 0,
                "max_value": 127,
                "min_value": 0,
                "default_value": 0,
            },
        },
    }

    # Get all parameters from the config
    actual_params = elektron_config.fmtone.pages["page_4"].parameters

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
