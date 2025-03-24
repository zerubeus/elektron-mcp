from elektron_mcp.digitone.digitone_params import digitone_config


def test_lfo1_all_params():
    """Test all parameters in LFO1"""
    expected_params = {
        "SPD": {
            "midi": {"cc_msb": "102", "nrpn_lsb": "1", "nrpn_msb": "42"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 48,
            "options": None,
        },
        "MULT": {
            "midi": {"cc_msb": "103", "nrpn_lsb": "1", "nrpn_msb": "43"},
            "max_midi_value": 11,
            "min_midi_value": 0,
            "max_value": 2000,
            "min_value": 1,
            "default_value": 2,
            "options": None,
        },
        "FADE": {
            "midi": {"cc_msb": "104", "nrpn_lsb": "1", "nrpn_msb": "44"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 63,
            "min_value": -64,
            "default_value": 0,
            "options": None,
        },
        "DEST": {
            "midi": {"cc_msb": "105", "nrpn_lsb": "1", "nrpn_msb": "45"},
            "max_midi_value": 50,
            "min_midi_value": 25,
            "max_value": 50,
            "min_value": 25,
            "default_value": "none",
            "options": [
                "none",
                "FILTER: Base",
                "FILTER: Width",
                "FILTER: Env. Reset",
                "AMP: Attack Time",
                "AMP: Hold Time",
                "AMP: Decay Time",
                "AMP: Sustain Level",
                "AMP: Release Time",
                "AMP: Pan",
                "AMP: Volume",
                "FX: Delay Send",
                "FX: Reverb Send",
                "FX: Chorus Send",
                "FX: Bit Reduction",
                "FX: SRR",
                "FX: SRR Routing",
                "FX: Overdrive",
                "SYN: Data entry knob A, page 1–4",
                "SYN: Data entry knob B, page 1–4",
                "SYN: Data entry knob C, page 1–4",
                "SYN: Data entry knob D, page 1–4",
                "SYN: Data entry knob E, page 1–4",
                "SYN: Data entry knob F, page 1–4",
                "SYN: Data entry knob G, page 1–4",
                "SYN: Data entry knob H, page 1–4",
                "SYN: Pitch Bend",
                "SYN: Aftertouch",
                "SYN: Mod Wheel",
                "SYN: Breath Controller",
                "CC: CC1–16 Values",
                "FILTER: Attack Time",
                "FILTER: Decay Time",
                "FILTER: Sustain Level",
                "FILTER: Release Time",
                "FILTER: Frequency",
                "FILTER: Data entry knob F",
                "FILTER: Data entry knob G",
                "FILTER: Envelope Depth",
                "FILTER: Env. Delay",
                "FILTER: Key Tracking",
            ],
        },
        "WAVE": {
            "midi": {"cc_msb": "106", "nrpn_lsb": "1", "nrpn_msb": "46"},
            "max_midi_value": 6,
            "min_midi_value": 0,
            "max_value": 6,
            "min_value": 0,
            "default_value": "sine",
            "options": ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        },
        "SPH": {
            "midi": {"cc_msb": "107", "nrpn_lsb": "1", "nrpn_msb": "47"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MODE": {
            "midi": {"cc_msb": "108", "nrpn_lsb": "1", "nrpn_msb": "48"},
            "max_midi_value": 4,
            "min_midi_value": 0,
            "max_value": 4,
            "min_value": 0,
            "default_value": "free",
            "options": ["free", "trig", "hold", "one", "half"],
        },
        "DEP": {
            "midi": {"cc_msb": "109", "nrpn_lsb": "1", "nrpn_msb": "49"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.lfo.lfo_groups["lfo_1"]

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


def test_lfo2_all_params():
    """Test all parameters in LFO2"""
    expected_params = {
        "SPD": {
            "midi": {"cc_msb": "111", "nrpn_lsb": "1", "nrpn_msb": "50"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 48,
            "options": None,
        },
        "MULT": {
            "midi": {"cc_msb": "112", "nrpn_lsb": "1", "nrpn_msb": "51"},
            "max_midi_value": 11,
            "min_midi_value": 0,
            "max_value": 2000,
            "min_value": 1,
            "default_value": 2,
            "options": None,
        },
        "FADE": {
            "midi": {"cc_msb": "113", "nrpn_lsb": "1", "nrpn_msb": "52"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 63,
            "min_value": -64,
            "default_value": 0,
            "options": None,
        },
        "DEST": {
            "midi": {"cc_msb": "114", "nrpn_lsb": "1", "nrpn_msb": "53"},
            "max_midi_value": 50,
            "min_midi_value": 25,
            "max_value": 50,
            "min_value": 25,
            "default_value": "none",
            "options": [
                "LFO1: Speed",
                "LFO1: Multiplier",
                "LFO1: Fade In/Out",
                "LFO1: Waveform",
                "LFO1: Start Phase",
                "LFO1: Trig Mode",
                "LFO1: Depth",
                "none",
                "FILTER: Base",
                "FILTER: Width",
                "FILTER: Env. Reset",
                "AMP: Attack Time",
                "AMP: Hold Time",
                "AMP: Decay Time",
                "AMP: Sustain Level",
                "AMP: Release Time",
                "AMP: Pan",
                "AMP: Volume",
                "FX: Delay Send",
                "FX: Reverb Send",
                "FX: Chorus Send",
                "FX: Bit Reduction",
                "FX: SRR",
                "FX: SRR Routing",
                "FX: Overdrive",
                "SYN: Data entry knob A, page 1–4",
                "SYN: Data entry knob B, page 1–4",
                "SYN: Data entry knob C, page 1–4",
                "SYN: Data entry knob D, page 1–4",
                "SYN: Data entry knob E, page 1–4",
                "SYN: Data entry knob F, page 1–4",
                "SYN: Data entry knob G, page 1–4",
                "SYN: Data entry knob H, page 1–4",
                "SYN: Pitch Bend",
                "SYN: Aftertouch",
                "SYN: Mod Wheel",
                "SYN: Breath Controller",
                "CC: CC1–16 Values",
                "FILTER: Attack Time",
                "FILTER: Decay Time",
                "FILTER: Sustain Level",
                "FILTER: Release Time",
                "FILTER: Frequency",
                "FILTER: Data entry knob F",
                "FILTER: Data entry knob G",
                "FILTER: Envelope Depth",
                "FILTER: Env. Delay",
                "FILTER: Key Tracking",
            ],
        },
        "WAVE": {
            "midi": {"cc_msb": "115", "nrpn_lsb": "1", "nrpn_msb": "54"},
            "max_midi_value": 6,
            "min_midi_value": 0,
            "max_value": 6,
            "min_value": 0,
            "default_value": "sine",
            "options": ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        },
        "SPH": {
            "midi": {"cc_msb": "116", "nrpn_lsb": "1", "nrpn_msb": "55"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MODE": {
            "midi": {"cc_msb": "117", "nrpn_lsb": "1", "nrpn_msb": "56"},
            "max_midi_value": 4,
            "min_midi_value": 0,
            "max_value": 4,
            "min_value": 0,
            "default_value": "free",
            "options": ["free", "trig", "hold", "one", "half"],
        },
        "DEP": {
            "midi": {"cc_msb": "118", "nrpn_lsb": "1", "nrpn_msb": "57"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.lfo.lfo_groups["lfo_2"]

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


def test_lfo3_all_params():
    """Test all parameters in LFO3"""
    expected_params = {
        "SPD": {
            "midi": {"cc_msb": "121", "nrpn_lsb": "1", "nrpn_msb": "58"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 48,
            "options": None,
        },
        "MULT": {
            "midi": {"cc_msb": "122", "nrpn_lsb": "1", "nrpn_msb": "59"},
            "max_midi_value": 11,
            "min_midi_value": 0,
            "max_value": 2000,
            "min_value": 1,
            "default_value": 2,
            "options": None,
        },
        "FADE": {
            "midi": {"cc_msb": "123", "nrpn_lsb": "1", "nrpn_msb": "60"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 63,
            "min_value": -64,
            "default_value": 0,
            "options": None,
        },
        "DEST": {
            "midi": {"cc_msb": "124", "nrpn_lsb": "1", "nrpn_msb": "61"},
            "max_midi_value": 50,
            "min_midi_value": 25,
            "max_value": 50,
            "min_value": 25,
            "default_value": "none",
            "options": [
                "LFO1: Speed",
                "LFO1: Multiplier",
                "LFO1: Fade In/Out",
                "LFO1: Waveform",
                "LFO1: Start Phase",
                "LFO1: Trig Mode",
                "LFO1: Depth",
                "LFO2: Speed",
                "LFO2: Multiplier",
                "LFO2: Fade In/Out",
                "LFO2: Waveform",
                "LFO2: Start Phase",
                "LFO2: Trig Mode",
                "LFO2: Depth",
                "none",
                "FILTER: Base",
                "FILTER: Width",
                "FILTER: Env. Reset",
                "AMP: Attack Time",
                "AMP: Hold Time",
                "AMP: Decay Time",
                "AMP: Sustain Level",
                "AMP: Release Time",
                "AMP: Pan",
                "AMP: Volume",
                "FX: Delay Send",
                "FX: Reverb Send",
                "FX: Chorus Send",
                "FX: Bit Reduction",
                "FX: SRR",
                "FX: SRR Routing",
                "FX: Overdrive",
                "SYN: Data entry knob A, page 1–4",
                "SYN: Data entry knob B, page 1–4",
                "SYN: Data entry knob C, page 1–4",
                "SYN: Data entry knob D, page 1–4",
                "SYN: Data entry knob E, page 1–4",
                "SYN: Data entry knob F, page 1–4",
                "SYN: Data entry knob G, page 1–4",
                "SYN: Data entry knob H, page 1–4",
                "SYN: Pitch Bend",
                "SYN: Aftertouch",
                "SYN: Mod Wheel",
                "SYN: Breath Controller",
                "CC: CC1–16 Values",
                "FILTER: Attack Time",
                "FILTER: Decay Time",
                "FILTER: Sustain Level",
                "FILTER: Release Time",
                "FILTER: Frequency",
                "FILTER: Data entry knob F",
                "FILTER: Data entry knob G",
                "FILTER: Envelope Depth",
                "FILTER: Env. Delay",
                "FILTER: Key Tracking",
            ],
        },
        "WAVE": {
            "midi": {"cc_msb": "125", "nrpn_lsb": "1", "nrpn_msb": "62"},
            "max_midi_value": 6,
            "min_midi_value": 0,
            "max_value": 6,
            "min_value": 0,
            "default_value": "sine",
            "options": ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        },
        "SPH": {
            "midi": {"cc_msb": "126", "nrpn_lsb": "1", "nrpn_msb": "70"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
        "MODE": {
            "midi": {"cc_msb": "127", "nrpn_lsb": "1", "nrpn_msb": "71"},
            "max_midi_value": 4,
            "min_midi_value": 0,
            "max_value": 4,
            "min_value": 0,
            "default_value": "free",
            "options": ["free", "trig", "hold", "one", "half"],
        },
        "DEP": {
            "midi": {"cc_msb": "128", "nrpn_lsb": "1", "nrpn_msb": "72"},
            "max_midi_value": 127,
            "min_midi_value": 0,
            "max_value": 127,
            "min_value": 0,
            "default_value": 0,
            "options": None,
        },
    }

    # Get all parameters from the config
    actual_params = digitone_config.lfo.lfo_groups["lfo_3"]

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
