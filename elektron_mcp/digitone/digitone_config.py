from .constants.filters import (
    MULTI_MODE_FILTER_PARAMS,
    LOWPASS_4_FILTER_PARAMS,
    LEGACY_LP_HP_FILTER_PARAMS,
    COMB_PLUS_FILTER_PARAMS,
    COMB_MINUS_FILTER_PARAMS,
    EQUALIZER_FILTER_PARAMS,
    BASE_WIDTH_FILTER_PARAMS,
)

from .constants.fm_drum import FM_DRUM_PARAMS
from .constants.fm_tone import FM_TONE_PARAMS
from .constants.swarmer import SWARMER_PARAMS
from .constants.wavetone import WAVETONE_PARAMS
from .constants.lfo import LFO1_PARAMS, LFO2_PARAMS, LFO3_PARAMS
from .models.models import DigitoneConfig
from .utils.parameter_utils import (
    create_lfo_params,
    create_parameter_group,
    setup_filter_parameters,
    create_parameter,
)

# Create the elektron configuration
digitone_config = DigitoneConfig()

# Set up LFO groups
digitone_config.lfo.lfo_groups = {
    "lfo_1": create_lfo_params(LFO1_PARAMS),
    "lfo_2": create_lfo_params(LFO2_PARAMS),
    "lfo_3": create_lfo_params(LFO3_PARAMS),
}

# Set up FMDRUM parameters
digitone_config.fmdrum.pages = {
    page: create_parameter_group(params) for page, params in FM_DRUM_PARAMS.items()
}

# Set up FMTONE parameters
digitone_config.fmtone.pages = {
    page: create_parameter_group(params) for page, params in FM_TONE_PARAMS.items()
}

# Set up SWARMER parameters
digitone_config.swarmer.pages = {
    page: create_parameter_group(params) for page, params in SWARMER_PARAMS.items()
}

# Set up WAVETONE parameters
digitone_config.wavetone.pages = {
    page: create_parameter_group(params) for page, params in WAVETONE_PARAMS.items()
}


# Set up filter parameters
setup_filter_parameters(digitone_config.multi_mode_filter, MULTI_MODE_FILTER_PARAMS)
setup_filter_parameters(digitone_config.lowpass_4_filter, LOWPASS_4_FILTER_PARAMS)
setup_filter_parameters(digitone_config.legacy_lp_hp_filter, LEGACY_LP_HP_FILTER_PARAMS)
setup_filter_parameters(digitone_config.comb_minus_filter, COMB_MINUS_FILTER_PARAMS)
setup_filter_parameters(digitone_config.comb_plus_filter, COMB_PLUS_FILTER_PARAMS)
setup_filter_parameters(digitone_config.equalizer_filter, EQUALIZER_FILTER_PARAMS)
setup_filter_parameters(digitone_config.base_width_filter, BASE_WIDTH_FILTER_PARAMS)

# AMP page
digitone_config.amp_page.parameters = {
    "ATK": create_parameter("84", "1", "30", 127, 0, 127, 0, 8),
    "HOLD": create_parameter("85", "1", "31", 127, 0, 127, 0, 127),
    "DEC": create_parameter("86", "1", "32", 127, 0, 127, 0, 32),
    "SUS": create_parameter("87", "1", "33", 127, 0, 127, 0, 96),
    "REL": create_parameter("88", "1", "34", 127, 0, 127, 0, 24),
    "Env. RSET": create_parameter("92", "1", "41", 1, 0, 1, 0, "on", ["off", "on"]),
    "MODE": create_parameter("91", "1", "40", 1, 0, 1, 0, "ADSR", ["AHD", "ADSR"]),
    "PAN": create_parameter("89", "1", "38", 127, 0, 64, -64, 0),
    "VOL": create_parameter("90", "1", "39", 127, 0, 127, 0, 110),
}

# FX page
digitone_config.fx_page.parameters = {
    "BR": create_parameter("78", "1", "5", 127, 0, 127, 0, 0),
    "OVER": create_parameter("81", "1", "8", 127, 0, 127, 0, 0),
    "SRR": create_parameter("79", "1", "6", 127, 0, 127, 0, 0),
    "SR.RT(pre/post)": create_parameter(
        "80", "1", "7", 1, 0, 1, 0, "pre", ["pre", "post"]
    ),
    "OD.RT(pre/post)": create_parameter(
        "82", "1", "9", 1, 0, 1, 0, "pre", ["pre", "post"]
    ),
    "DEL": create_parameter("30", "1", "36", 127, 0, 127, 0, 0),
    "REV": create_parameter("31", "1", "37", 127, 0, 127, 0, 0),
    "CHR": create_parameter("29", "1", "35", 127, 0, 127, 0, 0),
}
