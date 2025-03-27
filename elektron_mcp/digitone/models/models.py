from typing import Dict, List, Union, Optional
from pydantic import BaseModel, Field, model_validator


class MidiMapping(BaseModel):
    cc_msb: str
    nrpn_lsb: int
    nrpn_msb: int


class DigitoneParams(BaseModel):
    midi: MidiMapping
    max_midi_value: int
    min_midi_value: int
    max_value: Union[int, float, List[Union[int, float]]]
    min_value: Union[int, float, List[Union[int, float]]]
    default_value: Union[int, float, str, List[Union[int, float]]]
    options: Optional[Union[List[str], Dict[str, int]]] = None

    @model_validator(mode="after")
    def validate_values(self):
        """Validate parameter values"""
        # Check options
        if self.options is not None and isinstance(self.default_value, str):
            if (
                isinstance(self.options, list)
                and self.default_value not in self.options
            ):
                raise ValueError(
                    f"Default value '{self.default_value}' not in options list {self.options}"
                )
            elif (
                isinstance(self.options, dict)
                and self.default_value not in self.options
            ):
                raise ValueError(
                    f"Default value '{self.default_value}' not in options dict {self.options}"
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

    parameters: Dict[str, Union[DigitoneParams, Dict[str, DigitoneParams]]] = Field(
        default_factory=dict
    )


class SynthParameters(BaseModel):
    """Represents all parameters for a synth type (fmdrum, fmtone, etc.)"""

    pages: Dict[str, ParameterGroup] = Field(default_factory=dict)


class FilterParameters(BaseModel):
    """Represents filter parameters"""

    parameters: Dict[str, DigitoneParams] = Field(default_factory=dict)


class LfoParameters(BaseModel):
    """Represents LFO parameters"""

    lfo_groups: Dict[str, Dict[str, DigitoneParams]] = Field(default_factory=dict)


class AmpParameters(BaseModel):
    """Represents amp parameters"""

    parameters: Dict[str, DigitoneParams] = Field(default_factory=dict)


class FxParameters(BaseModel):
    """Represents fx parameters"""

    parameters: Dict[str, DigitoneParams] = Field(default_factory=dict)


class DigitoneConfig(BaseModel):
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
    def model_validate_json(cls, json_data: str, **kwargs):
        """Deserialize from JSON"""
        return super().model_validate_json(json_data, **kwargs)
