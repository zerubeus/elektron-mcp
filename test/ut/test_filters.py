from elektron_mcp.digitone.config.config import digitone_config


def test_multi_mode_filter():
    """Test parameters in the multi-mode filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "RESO": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "TYPE": {
            "midi": {"cc_msb": "18", "nrpn_lsb": "1", "nrpn_msb": "22"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.multi_mode_filter.parameters

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


def test_lowpass_4_filter():
    """Test parameters in the lowpass 4 filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "RESO": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.lowpass_4_filter.parameters

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


def test_legacy_lp_hp_filter():
    """Test parameters in the legacy LP/HP filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "RESO": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "TYPE(lowpass/highpass)": {
            "midi": {"cc_msb": "18", "nrpn_lsb": "1", "nrpn_msb": "22"},
            "max_midi_value": 2,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": ["lowpass", "highpass", "off"],
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.legacy_lp_hp_filter.parameters

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
        if "options" in expected_values:
            assert (
                param.options == expected_values["options"]
            ), f"Mismatch in {param_name} options"

    # Verify no extra parameters exist
    assert set(actual_params.keys()) == set(
        expected_params.keys()
    ), "Extra parameters found"


def test_comb_minus_filter():
    """Test parameters in the comb minus filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "FDBK": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "LPF": {
            "midi": {"cc_msb": "18", "nrpn_lsb": "1", "nrpn_msb": "22"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.comb_minus_filter.parameters

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


def test_comb_plus_filter():
    """Test parameters in the comb plus filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "FDBK": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "LPF": {
            "midi": {"cc_msb": "18", "nrpn_lsb": "1", "nrpn_msb": "22"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.comb_plus_filter.parameters

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


def test_equalizer_filter():
    """Test parameters in the equalizer filter"""
    expected_params = {
        "ATK": {
            "midi": {"cc_msb": "20", "nrpn_lsb": "1", "nrpn_msb": "16"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "DEC": {
            "midi": {"cc_msb": "21", "nrpn_lsb": "1", "nrpn_msb": "17"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "SUS": {
            "midi": {"cc_msb": "22", "nrpn_lsb": "1", "nrpn_msb": "18"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "REL": {
            "midi": {"cc_msb": "23", "nrpn_lsb": "1", "nrpn_msb": "19"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 64,
        },
        "FREQ": {
            "midi": {"cc_msb": "16", "nrpn_lsb": "1", "nrpn_msb": "20"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 127,
        },
        "GAIN": {
            "midi": {"cc_msb": "17", "nrpn_lsb": "1", "nrpn_msb": "21"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "Q": {
            "midi": {"cc_msb": "18", "nrpn_lsb": "1", "nrpn_msb": "22"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "ENV.Depth": {
            "midi": {"cc_msb": "24", "nrpn_lsb": "1", "nrpn_msb": "26"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 64,
            "min_value": -64,
            "default_value": 0,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.equalizer_filter.parameters

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


def test_base_width_filter():
    """Test parameters in the base/width filter"""
    expected_params = {
        "ENV.Delay": {
            "midi": {"cc_msb": "19", "nrpn_lsb": "1", "nrpn_msb": "23"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "KEY.Tracking": {
            "midi": {"cc_msb": "26", "nrpn_lsb": "1", "nrpn_msb": "69"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "BASE": {
            "midi": {"cc_msb": "27", "nrpn_lsb": "1", "nrpn_msb": "24"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "WDTH": {
            "midi": {"cc_msb": "28", "nrpn_lsb": "1", "nrpn_msb": "25"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
        },
        "Env Reset": {
            "midi": {"cc_msb": "25", "nrpn_lsb": "1", "nrpn_msb": "68"},
            "max_midi_value": 1,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": "off",
            "options": ["off", "on"],
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.base_width_filter.parameters

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
        if "options" in expected_values:
            assert (
                param.options == expected_values["options"]
            ), f"Mismatch in {param_name} options"

    # Verify no extra parameters exist
    assert set(actual_params.keys()) == set(
        expected_params.keys()
    ), "Extra parameters found"
