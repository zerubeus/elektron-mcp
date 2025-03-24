from typing import Dict, List, Union, Optional
from pydantic import BaseModel, Field, model_validator


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
    return ElektronParams(
        midi=MidiMapping(cc_msb=cc_msb, nrpn_lsb=nrpn_lsb, nrpn_msb=nrpn_msb),
        max_midi_value=max_midi,
        min_midi_value=min_midi,
        max_value=max_val,
        min_value=min_val,
        default_value=default,
        options=options,
    )


# Create the elektron configuration using the more concise approach
elektron_config = ElektronConfig()

# FMDRUM
elektron_config.fmdrum.pages = {
    "page_1": ParameterGroup(
        parameters={
            "tune": create_parameter("40", "1", "73", 127, 0, 60, -60, 0),
            "stim": create_parameter("41", "1", "74", 127, 0, 127, 0, 0),
            "sdep": create_parameter("42", "1", "75", 127, 0, 127, 0, 0),
            "algo": create_parameter("43", "1", "76", 6, 0, 7, 1, 1),
            "OP.C": create_parameter("44", "1", "77", 127, 0, 127, 0, 0),
            "OP.AB": create_parameter("45", "1", "78", 127, 0, 127, 0, 0),
            "FDBK": create_parameter("46", "1", "79", 127, 0, 127, 0, 0),
            "FOLD": create_parameter("47", "1", "80", 127, 0, 127, 0, 0),
        }
    ),
    "page_2": ParameterGroup(
        parameters={
            "RATIO1": create_parameter("48", "1", "81", 127, 0, 31.75, 0.001, 0.500),
            "DEC1": create_parameter("49", "1", "82", 127, 0, 127, 0, 0),
            "END1": create_parameter("50", "1", "83", 127, 0, 127, 0, 0),
            "MOD1": create_parameter("51", "1", "84", 127, 0, 127, 0, 0),
            "RATIO2": create_parameter("52", "1", "85", 127, 0, 31.75, 0.001, 0.500),
            "DEC2": create_parameter("53", "1", "86", 127, 0, 127, 0, 0),
            "END2": create_parameter("54", "1", "87", 127, 0, 127, 0, 0),
            "MOD2": create_parameter("55", "1", "88", 127, 0, 127, 0, 0),
        }
    ),
    "page_3": ParameterGroup(
        parameters={
            "HOLD": create_parameter("56", "1", "89", 127, 0, 127, 0, 0),
            "DEC": create_parameter("57", "1", "90", 127, 0, 127, 0, 0),
            "PH.C": create_parameter("58", "1", "91", 91, 0, 91, 0, 0),
            "LEV": create_parameter("59", "1", "92", 127, 0, 127, 0, 0),
            "NRST": create_parameter("62", "1", "95", 1, 0, 1, 0, 0),
            "NRM": create_parameter("63", "1", "96", 1, 0, 1, 0, 0),
        }
    ),
    "page_4": ParameterGroup(
        parameters={
            "NHLD": create_parameter("70", "1", "97", 127, 0, 127, 0, 0),
            "NDEC": create_parameter("71", "1", "98", 127, 0, 127, 0, 0),
            "TRAN": create_parameter("72", "1", "99", 124, 0, 124, 0, 0),
            "TLEV": create_parameter("73", "1", "100", 127, 0, 127, 0, 0),
            "BASE": create_parameter("74", "1", "101", 127, 0, 127, 0, 0),
            "WDTH": create_parameter("75", "1", "102", 127, 0, 127, 0, 0),
            "GRAN": create_parameter("76", "1", "103", 127, 0, 127, 0, 0),
            "NLEV": create_parameter("77", "1", "104", 127, 0, 127, 0, 0),
        }
    ),
}

# FMTONE
elektron_config.fmtone.pages = {
    "page_1": ParameterGroup(
        parameters={
            "ALGO": create_parameter("40", "1", "73", 7, 0, 8, 0, 0),
            "C": create_parameter("41", "1", "74", 18, 0, 16, 0.25, 1.00),
            "A": create_parameter("42", "1", "75", 35, 0, 16, 0.25, 1.00),
            "B": create_parameter(
                "43", "1", "76", 3, 0, [16, 16], [0.25, 0.25], [1.00, 1.00]
            ),
            "HARM": create_parameter("44", "1", "77", 37, 90, 26, -26, 0.00),
            "DTUN": create_parameter("45", "1", "78", 127, 0, 127, 0, 0),
            "FDBK": create_parameter("46", "1", "79", 127, 0, 127, 0, 0),
            "MIX": create_parameter("47", "1", "80", 127, 0, 63, -63, -63),
        }
    ),
    "page_2": ParameterGroup(
        parameters={
            "A": {
                "atk": create_parameter("48", "1", "81", 127, 0, 127, 0, 0),
                "dec": create_parameter("49", "1", "82", 127, 0, 127, 0, 32),
                "end": create_parameter("50", "1", "83", 127, 0, 127, 0, 127),
                "lev": create_parameter("51", "1", "84", 127, 0, 127, 0, 0),
            },
            "B": {
                "atk": create_parameter("48", "1", "81", 127, 0, 127, 0, 0),
                "dec": create_parameter("49", "1", "82", 127, 0, 127, 0, 32),
                "end": create_parameter("50", "1", "83", 127, 0, 127, 0, 127),
                "lev": create_parameter("51", "1", "84", 127, 0, 127, 0, 0),
            },
        }
    ),
    "page_3": ParameterGroup(
        parameters={
            "ADEL": create_parameter("56", "1", "89", 127, 0, 127, 0, 0),
            "ATRG": create_parameter("57", "1", "90", 1, 0, 1, 0, 1),
            "ARST": create_parameter("58", "1", "91", 1, 0, 1, 0, 1),
            "PHRT": create_parameter(
                "59", "1", "92", 4, 0, 4, 0, "all", ["off", "all", "c", "a+b", "a+b2"]
            ),
            "BDEL": create_parameter("60", "1", "93", 127, 0, 127, 0, 0),
            "BTRG": create_parameter("61", "1", "94", 1, 0, 1, 0, 1),
            "BRST": create_parameter("62", "1", "95", 1, 0, 1, 0, 1),
        }
    ),
    "page_4": ParameterGroup(
        parameters={
            "Ratio_Offset": {
                "C": create_parameter("70", "1", "97", 127, 0, +0.999, -1.00, 0.00),
                "A": create_parameter("71", "1", "98", 127, 0, +0.999, -1.00, 0.00),
                "B1": create_parameter("72", "1", "99", 127, 0, +0.999, -1.00, 0.00),
                "B2": create_parameter("73", "1", "100", 127, 0, +0.999, -1.00, 0.00),
            },
            "Key_Track": {
                "A": create_parameter("75", "1", "102", 127, 0, 127, 0, 0),
                "B1": create_parameter("76", "1", "103", 127, 0, 127, 0, 0),
                "B2": create_parameter("77", "1", "104", 127, 0, 127, 0, 0),
            },
        }
    ),
}

# SWARMER
elektron_config.swarmer.pages = {
    "page_1": ParameterGroup(
        parameters={
            "TUNE": create_parameter("40", "1", "73", 127, 0, 60, -60, 0),
            "SWRM": create_parameter("41", "1", "74", 127, 0, 120, 0, 80),
            "DET": create_parameter("42", "1", "75", 127, 0, 127, 0, 70),
            "MIX": create_parameter("43", "1", "76", 127, 0, 127, 0, 127),
            "M.OCT": create_parameter("44", "1", "77", 2, 0, 2, 0, 0),
            "MAIN": create_parameter("45", "1", "78", 120, 0, 120, 0, 80),
            "ANIM": create_parameter("46", "1", "79", 127, 0, 127, 0, 15),
            "N.MOD": create_parameter("47", "1", "80", 127, 0, 127, 0, 20),
        }
    ),
}

# WAVETONE
elektron_config.wavetone.pages = {
    "page_1": ParameterGroup(
        parameters={
            "TUN1": create_parameter("40", "1", "73", 127, 0, 60, -60, 0),
            "WAV1": create_parameter("41", "1", "74", 127, 0, 120, 0, 0),
            "PD1": create_parameter("42", "1", "75", 127, 0, 100, 0, 50),
            "LEV1": create_parameter("43", "1", "76", 127, 0, 127, 0, 100),
            "TUN2": create_parameter("44", "1", "77", 127, 0, 60, -60, 0),
            "WAV2": create_parameter("45", "1", "78", 127, 0, 120, 0, 0),
            "PD2": create_parameter("46", "1", "79", 127, 0, 100, 0, 50),
            "LEV2": create_parameter("47", "1", "80", 127, 0, 127, 0, 100),
        }
    ),
    "page_2": ParameterGroup(
        parameters={
            "OFS1": create_parameter("48", "1", "81", 127, 0, 10, -10, 0),
            "TBL1": create_parameter(
                "49", "1", "82", 1, 0, 1, 0, "prim", ["prim", "harm"]
            ),
            "MOD": create_parameter(
                "50",
                "1",
                "83",
                3,
                0,
                3,
                0,
                "off",
                ["off", "ring mod", "ring mod fixed", "hard sync"],
            ),
            "RSET": create_parameter(
                "51", "1", "84", 2, 0, 2, 0, "on", ["off", "on", "random"]
            ),
            "OFS2": create_parameter("52", "1", "85", 127, 0, 10, -10, 0),
            "TBL2": create_parameter(
                "53", "1", "86", 1, 0, 1, 0, "prim", ["prim", "harm"]
            ),
            "DRIF": create_parameter("55", "1", "88", 127, 0, 127, 0, 0),
        }
    ),
    "page_3": ParameterGroup(
        parameters={
            "ATK": create_parameter("56", "1", "89", 127, 0, 127, 0, 0),
            "HOLD": create_parameter("57", "1", "90", 127, 0, 127, 0, 127),
            "DEC": create_parameter("58", "1", "91", 127, 0, 127, 0, 127),
            "NLEV": create_parameter("59", "1", "92", 127, 0, 127, 0, 0),
            "BASE": create_parameter("60", "1", "93", 127, 0, 127, 0, 0),
            "WDTH": create_parameter("61", "1", "94", 127, 0, 127, 0, 127),
            "TYPE": create_parameter(
                "62",
                "1",
                "95",
                2,
                0,
                2,
                0,
                "grain nose",
                ["grain nose", "tuned noise", "sample and hold noise"],
            ),
            "CHAR": create_parameter("63", "1", "96", 127, 0, 127, 0, 0),
        }
    ),
}

# FILTERS
elektron_config.multi_mode_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 127),
    "RESO": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "TYPE": create_parameter("18", "1", "22", 127, 0, 127, 0, 0),
    "ENV Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.lowpass_4_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 0),
    "RESO": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "ENV.Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.legacy_lp_hp_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 0),
    "RESO": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "TYPE(lowpass/highpass)": create_parameter(
        "18", "1", "22", 2, 0, 2, 0, 0, ["lowpass", "highpass", "off"]
    ),
    "ENV.Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.comb_minus_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 127),
    "FDBK": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "LPF": create_parameter("18", "1", "22", 127, 0, 127, 0, 127),
    "ENV.Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.comb_plus_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 127),
    "FDBK": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "LPF": create_parameter("18", "1", "22", 127, 0, 127, 0, 127),
    "ENV.Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.equalizer_filter.parameters = {
    "ATK": create_parameter("20", "1", "16", 127, 0, 127, 0, 0),
    "DEC": create_parameter("21", "1", "17", 127, 0, 127, 0, 64),
    "SUS": create_parameter("22", "1", "18", 127, 0, 127, 0, 0),
    "REL": create_parameter("23", "1", "19", 127, 0, 127, 0, 64),
    "FREQ": create_parameter("16", "1", "20", 127, 0, 127, 0, 127),
    "GAIN": create_parameter("17", "1", "21", 127, 0, 127, 0, 0),
    "Q": create_parameter("18", "1", "22", 127, 0, 127, 0, 0),
    "ENV.Depth": create_parameter("24", "1", "26", 127, 0, 64, -64, 0),
}

elektron_config.base_width_filter.parameters = {
    "ENV.Delay": create_parameter("19", "1", "23", 127, 0, 127, 0, 0),
    "KEY.Tracking": create_parameter("26", "1", "69", 127, 0, 127, 0, 0),
    "BASE": create_parameter("27", "1", "24", 127, 0, 127, 0, 0),
    "WDTH": create_parameter("28", "1", "25", 127, 0, 127, 0, 0),
    "Env Reset": create_parameter("25", "1", "68", 1, 0, 1, 0, "off", ["off", "on"]),
}

# LFO
elektron_config.lfo.lfo_groups = {
    "lfo_1": {
        "SPD": create_parameter("102", "1", "42", 127, 0, 127, 0, 48),
        "MULT": create_parameter("103", "1", "43", 11, 0, 2000, 1, 2),
        "FADE": create_parameter("104", "1", "44", 127, 0, 63, -64, 0),
        "DEST": create_parameter(
            "105",
            "1",
            "45",
            50,
            25,
            50,
            25,
            "none",
            [
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
        ),
        "WAVE": create_parameter(
            "106",
            "1",
            "46",
            6,
            0,
            6,
            0,
            "sine",
            ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        ),
        "SPH": create_parameter("107", "1", "47", 127, 0, 127, 0, 0),
        "MODE": create_parameter(
            "108",
            "1",
            "48",
            4,
            0,
            4,
            0,
            "free",
            ["free", "trig", "hold", "one", "half"],
        ),
        "DEP": create_parameter("109", "1", "49", 127, 0, 127, 0, 0),
    },
    "lfo_2": {
        "SPD": create_parameter("111", "1", "50", 127, 0, 127, 0, 48),
        "MULT": create_parameter("112", "1", "51", 11, 0, 2000, 1, 2),
        "FADE": create_parameter("113", "1", "52", 127, 0, 63, -64, 0),
        "DEST": create_parameter(
            "114",
            "1",
            "53",
            50,
            25,
            50,
            25,
            "none",
            [
                "none",
                "LFO1: Speed",
                "LFO1: Multiplier",
                "LFO1: Fade In/Out",
                "LFO1: Waveform",
                "LFO1: Start Phase",
                "LFO1: Trig Mode",
                "LFO1: Depth",
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
        ),
        "WAVE": create_parameter(
            "115",
            "1",
            "54",
            6,
            0,
            6,
            0,
            "sine",
            ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        ),
        "SPH": create_parameter("116", "1", "55", 127, 0, 127, 0, 0),
        "Trig MODE": create_parameter(
            "117",
            "1",
            "56",
            4,
            0,
            4,
            0,
            "free",
            ["free", "trig", "hold", "one", "half"],
        ),
        "DEP": create_parameter("118", "1", "57", 127, 0, 127, 0, 0),
    },
    "lfo_3": {
        "SPD": create_parameter("121", "1", "58", 127, 0, 127, 0, 48),
        "MULT": create_parameter("122", "1", "59", 11, 0, 2000, 1, 2),
        "FADE": create_parameter("123", "1", "60", 127, 0, 63, -64, 0),
        "DEST": create_parameter(
            "124",
            "1",
            "61",
            50,
            25,
            50,
            25,
            "none",
            [
                "none",
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
        ),
        "WAVE": create_parameter(
            "125",
            "1",
            "62",
            6,
            0,
            6,
            0,
            "sine",
            ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"],
        ),
        "SPH": create_parameter("126", "1", "70", 127, 0, 127, 0, 0),
        "Trig MODE": create_parameter(
            "127",
            "1",
            "71",
            4,
            0,
            4,
            0,
            "free",
            ["free", "trig", "hold", "one", "half"],
        ),
        "DEP": create_parameter("128", "1", "72", 127, 0, 127, 0, 0),
    },
}

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
