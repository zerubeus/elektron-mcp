from elektron_mcp.digitone.data.filters import (
    MULTI_MODE_FILTER_PARAMS,
    LOWPASS_4_FILTER_PARAMS,
    LEGACY_LP_HP_FILTER_PARAMS,
    COMB_PLUS_FILTER_PARAMS,
    COMB_MINUS_FILTER_PARAMS,
    EQUALIZER_FILTER_PARAMS,
    BASE_WIDTH_FILTER_PARAMS,
)

from elektron_mcp.digitone.data.fm_drum import FM_DRUM_PARAMS
from elektron_mcp.digitone.data.fm_tone import FM_TONE_PARAMS
from elektron_mcp.digitone.data.swarmer import SWARMER_PARAMS
from elektron_mcp.digitone.data.wavetone import WAVETONE_PARAMS
from elektron_mcp.digitone.data.lfo import LFO1_PARAMS, LFO2_PARAMS, LFO3_PARAMS
from elektron_mcp.digitone.data.amp import AMP_PARAMS_DATA
from elektron_mcp.digitone.data.fx import FX_PARAMS_DATA
from elektron_mcp.digitone.models.models import DigitoneConfig
from elektron_mcp.digitone.utils.parameter_utils import (
    create_lfo_params,
    create_parameter_group,
    setup_filter_parameters,
    create_param_from_dict,
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
    name: create_param_from_dict(param) for name, param in AMP_PARAMS_DATA.items()
}

# FX page
digitone_config.fx_page.parameters = {
    name: create_param_from_dict(param) for name, param in FX_PARAMS_DATA.items()
}
