from typing import Dict, List, Union, Optional
from pydantic import BaseModel, Field, model_validator

from elektron_mcp.constants.filters import (
    MULTI_MODE_FILTER_PARAMS,
    LOWPASS_4_FILTER_PARAMS,
    LEGACY_LP_HP_FILTER_PARAMS,
    COMB_PLUS_FILTER_PARAMS,
    COMB_MINUS_FILTER_PARAMS,
    EQUALIZER_FILTER_PARAMS,
    BASE_WIDTH_FILTER_PARAMS,
)
from elektron_mcp.constants.fm_drum import FM_DRUM_PARAMS
from elektron_mcp.constants.fm_tone import FM_TONE_PARAMS
from elektron_mcp.constants.swarmer import SWARMER_PARAMS
from elektron_mcp.constants.wavetone import WAVETONE_PARAMS
from elektron_mcp.constants.lfo import LFO1_PARAMS, LFO2_PARAMS, LFO3_PARAMS


class MidiMapping(BaseModel):
    cc_msb: str
    nrpn_lsb: str
    nrpn_msb: str


class ElektronParams(BaseModel):
    midi: MidiMapping
    max_midi_value: int
    min_midi_value: int
    max_value: Union[int, float, List[Union[int, float]]]
    min_value: Union[int, float, List[Union[int, float]]]
    default_value: Union[int, float, str, List[Union[int, float]]]
    options: Optional[List[str]] = None

    @model_validator(mode="after")
    def validate_values(self):
        """Validate parameter values"""
        # Check options
        if self.options is not None and isinstance(self.default_value, str):
            if self.default_value not in self.options:
                raise ValueError(
                    f"Default value '{self.default_value}' not in options list {self.options}"
                )

        # Check numeric range for numeric values (when not using options)
        if self.options is None:
            if (
                isinstance(self.default_value, (int, float))
                and isinstance(self.max_value, (int, float))
                and isinstance(self.min_value, (int, float))
            ):
                if (
                    self.default_value > self.max_value
                    or self.default_value < self.min_value
                ):
                    raise ValueError(
                        f"Default value {self.default_value} outside valid range [{self.min_value}, {self.max_value}]"
                    )

            # Check list values
            if (
                isinstance(self.default_value, list)
                and isinstance(self.max_value, list)
                and isinstance(self.min_value, list)
            ):
                if len(self.default_value) != len(self.max_value) or len(
                    self.default_value
                ) != len(self.min_value):
                    raise ValueError(
                        "Inconsistent length for default, min, and max value lists"
                    )

                for idx, val in enumerate(self.default_value):
                    if val > self.max_value[idx] or val < self.min_value[idx]:
                        raise ValueError(
                            f"Default value at index {idx} outside valid range"
                        )

        return self


class ParameterGroup(BaseModel):
    """Represents a group of parameters, like page_1, page_2, etc."""

    parameters: Dict[str, Union[ElektronParams, Dict[str, ElektronParams]]] = Field(
        default_factory=dict
    )


class SynthParameters(BaseModel):
    """Represents all parameters for a synth type (fmdrum, fmtone, etc.)"""

    pages: Dict[str, ParameterGroup] = Field(default_factory=dict)


class FilterParameters(BaseModel):
    """Represents filter parameters"""

    parameters: Dict[str, ElektronParams] = Field(default_factory=dict)


class LfoParameters(BaseModel):
    """Represents LFO parameters"""

    lfo_groups: Dict[str, Dict[str, ElektronParams]] = Field(default_factory=dict)


class AmpParameters(BaseModel):
    """Represents amp parameters"""

    parameters: Dict[str, ElektronParams] = Field(default_factory=dict)


class FxParameters(BaseModel):
    """Represents fx parameters"""

    parameters: Dict[str, ElektronParams] = Field(default_factory=dict)


class ElektronConfig(BaseModel):
    """Top level configuration for Elektron synths"""

    fmdrum: SynthParameters = Field(default_factory=SynthParameters)
    fmtone: SynthParameters = Field(default_factory=SynthParameters)
    swarmer: SynthParameters = Field(default_factory=SynthParameters)
    wavetone: SynthParameters = Field(default_factory=SynthParameters)
    multi_mode_filter: FilterParameters = Field(default_factory=FilterParameters)
    lowpass_4_filter: FilterParameters = Field(default_factory=FilterParameters)
    legacy_lp_hp_filter: FilterParameters = Field(default_factory=FilterParameters)
    comb_minus_filter: FilterParameters = Field(default_factory=FilterParameters)
    comb_plus_filter: FilterParameters = Field(default_factory=FilterParameters)
    equalizer_filter: FilterParameters = Field(default_factory=FilterParameters)
    base_width_filter: FilterParameters = Field(default_factory=FilterParameters)
    amp_page: AmpParameters = Field(default_factory=AmpParameters)
    fx_page: FxParameters = Field(default_factory=FxParameters)
    lfo: LfoParameters = Field(default_factory=LfoParameters)

    def model_dump_json(self, **kwargs) -> str:
        """Serialize to JSON"""
        return super().model_dump_json(**kwargs)

    @classmethod
    def model_validate_json(cls, json_data: str, **kwargs) -> "ElektronConfig":
        """Deserialize from JSON"""
        return super().model_validate_json(json_data, **kwargs)


def create_parameter(
    cc_msb,
    nrpn_lsb,
    nrpn_msb,
    max_midi,
    min_midi,
    max_val,
    min_val,
    default,
    options=None,
):
    """Helper function to create a parameter with midi mapping"""
    # Convert numeric values to strings for MIDI parameters
    cc_msb_str = str(cc_msb) if isinstance(cc_msb, (int, float)) else cc_msb
    nrpn_lsb_str = str(nrpn_lsb) if isinstance(nrpn_lsb, (int, float)) else nrpn_lsb
    nrpn_msb_str = str(nrpn_msb) if isinstance(nrpn_msb, (int, float)) else nrpn_msb

    mapping = MidiMapping(
        cc_msb=cc_msb_str, nrpn_lsb=nrpn_lsb_str, nrpn_msb=nrpn_msb_str
    )
    return ElektronParams(
        midi=mapping,
        max_midi_value=max_midi,
        min_midi_value=min_midi,
        max_value=max_val,
        min_value=min_val,
        default_value=default,
        options=options,
    )


def create_lfo_params(params_config):
    """Create LFO parameters with explicit CC and NRPN values."""
    return {
        name: create_parameter(
            cc_msb=str(param.get("cc_msb", param.get("cc"))),
            nrpn_lsb="1",
            nrpn_msb=str(param.get("nrpn_msb", param.get("nrpn"))),
            max_midi=param.get("max_midi", 127),
            min_midi=param.get("min_midi", 0),
            max_val=param.get("max_val", 127),
            min_val=param.get("min_val", 0),
            default=param.get("default", 0),
            options=param.get("options", None),
        )
        for name, param in params_config.items()
    }


def create_parameter_group(params_dict):
    """Helper function to create a parameter group from a dictionary"""
    parameters = {}
    for key, value in params_dict.items():
        if isinstance(value, dict) and ("cc" in value or "cc_msb" in value):
            # This is a parameter definition
            parameters[key] = create_parameter(
                cc_msb=str(value.get("cc_msb", value.get("cc"))),
                nrpn_lsb=str(value.get("nrpn_lsb", "1")),  # Default value
                nrpn_msb=str(value.get("nrpn_msb", value.get("nrpn"))),
                max_midi=value.get("max_midi", 127),
                min_midi=value.get("min_midi", 0),
                max_val=value.get("max_val", 127),
                min_val=value.get("min_val", 0),
                default=value.get("default", 0),
                options=value.get("options", None),
            )
        elif isinstance(value, dict):
            # This is a nested dictionary of parameters
            nested_params = {}
            for nested_key, nested_value in value.items():
                nested_params[nested_key] = create_parameter(
                    cc_msb=str(nested_value.get("cc_msb", nested_value.get("cc"))),
                    nrpn_lsb=str(nested_value.get("nrpn_lsb", "1")),  # Default value
                    nrpn_msb=str(
                        nested_value.get("nrpn_msb", nested_value.get("nrpn"))
                    ),
                    max_midi=nested_value.get("max_midi", 127),
                    min_midi=nested_value.get("min_midi", 0),
                    max_val=nested_value.get("max_val", 127),
                    min_val=nested_value.get("min_val", 0),
                    default=nested_value.get("default", 0),
                    options=nested_value.get("options", None),
                )
            parameters[key] = nested_params
    return ParameterGroup(parameters=parameters)


def setup_filter_parameters(filter_obj, params_dict):
    """Helper function to set up filter parameters to avoid code duplication"""
    filter_obj.parameters = {
        name: create_parameter(
            cc_msb=str(param.get("cc_msb", param.get("cc"))),
            nrpn_lsb="1",
            nrpn_msb=str(param.get("nrpn_msb", param.get("nrpn"))),
            max_midi=param.get("max_midi", 127),
            min_midi=param.get("min_midi", 0),
            max_val=param.get("max_val", 127),
            min_val=param.get("min_val", 0),
            default=param.get("default", 0),
            options=param.get("options", None),
        )
        for name, param in params_dict.items()
    }


# Create the elektron configuration
elektron_config = ElektronConfig()

# Set up LFO groups
elektron_config.lfo.lfo_groups = {
    "lfo_1": create_lfo_params(LFO1_PARAMS),
    "lfo_2": create_lfo_params(LFO2_PARAMS),
    "lfo_3": create_lfo_params(LFO3_PARAMS),
}

# Set up FMDRUM parameters
elektron_config.fmdrum.pages = {
    page: create_parameter_group(params) for page, params in FM_DRUM_PARAMS.items()
}

# Set up FMTONE parameters
elektron_config.fmtone.pages = {
    page: create_parameter_group(params) for page, params in FM_TONE_PARAMS.items()
}

# Set up SWARMER parameters
elektron_config.swarmer.pages = {
    page: create_parameter_group(params) for page, params in SWARMER_PARAMS.items()
}

# Set up WAVETONE parameters
elektron_config.wavetone.pages = {
    page: create_parameter_group(params) for page, params in WAVETONE_PARAMS.items()
}


# Set up filter parameters
setup_filter_parameters(elektron_config.multi_mode_filter, MULTI_MODE_FILTER_PARAMS)
setup_filter_parameters(elektron_config.lowpass_4_filter, LOWPASS_4_FILTER_PARAMS)
setup_filter_parameters(elektron_config.legacy_lp_hp_filter, LEGACY_LP_HP_FILTER_PARAMS)
setup_filter_parameters(elektron_config.comb_minus_filter, COMB_MINUS_FILTER_PARAMS)
setup_filter_parameters(elektron_config.comb_plus_filter, COMB_PLUS_FILTER_PARAMS)
setup_filter_parameters(elektron_config.equalizer_filter, EQUALIZER_FILTER_PARAMS)
setup_filter_parameters(elektron_config.base_width_filter, BASE_WIDTH_FILTER_PARAMS)

# AMP page
elektron_config.amp_page.parameters = {
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
elektron_config.fx_page.parameters = {
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
