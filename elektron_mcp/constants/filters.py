# Filter Parameters
MULTI_MODE_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20, "default": 127},
    "RESO": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "TYPE": {"cc_msb": 18, "nrpn_lsb": "1", "nrpn_msb": 22},
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}

LOWPASS_4_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20, "default": 127},
    "RESO": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}


EQUALIZER_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20, "default": 127},
    "GAIN": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "Q": {"cc_msb": 18, "nrpn_lsb": "1", "nrpn_msb": 22},
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}

BASE_WIDTH_FILTER_PARAMS = {
    "ENV.Delay": {"cc_msb": 19, "nrpn_lsb": "1", "nrpn_msb": 23},
    "KEY.Tracking": {"cc_msb": 26, "nrpn_lsb": "1", "nrpn_msb": 69},
    "BASE": {"cc_msb": 27, "nrpn_lsb": "1", "nrpn_msb": 24},
    "WDTH": {"cc_msb": 28, "nrpn_lsb": "1", "nrpn_msb": 25},
    "Env Reset": {
        "cc_msb": 25,
        "nrpn_lsb": "1",
        "nrpn_msb": 68,
        "max_midi": 1,
        "options": ["off", "on"],
        "default": "off",
    },
}


LEGACY_LP_HP_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20},
    "RESO": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "TYPE(lowpass/highpass)": {
        "cc_msb": 18,
        "nrpn_lsb": "1",
        "nrpn_msb": 22,
        "max_midi": 2,
        "options": ["lowpass", "highpass", "off"],
        "default": 0,
    },
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}

COMB_MINUS_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20, "default": 127},
    "FDBK": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "LPF": {"cc_msb": 18, "nrpn_lsb": "1", "nrpn_msb": 22, "default": 127},
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}

COMB_PLUS_FILTER_PARAMS = {
    "ATK": {"cc_msb": 20, "nrpn_lsb": "1", "nrpn_msb": 16},
    "DEC": {"cc_msb": 21, "nrpn_lsb": "1", "nrpn_msb": 17, "default": 64},
    "SUS": {"cc_msb": 22, "nrpn_lsb": "1", "nrpn_msb": 18},
    "REL": {"cc_msb": 23, "nrpn_lsb": "1", "nrpn_msb": 19, "default": 64},
    "FREQ": {"cc_msb": 16, "nrpn_lsb": "1", "nrpn_msb": 20, "default": 127},
    "FDBK": {"cc_msb": 17, "nrpn_lsb": "1", "nrpn_msb": 21},
    "LPF": {"cc_msb": 18, "nrpn_lsb": "1", "nrpn_msb": 22, "default": 127},
    "ENV.Depth": {
        "cc_msb": 24,
        "nrpn_lsb": "1",
        "nrpn_msb": 26,
        "max_val": 64,
        "min_val": -64,
    },
}
