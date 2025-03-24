import pytest
import sys
import os
import json
from pydantic import ValidationError

from elektron_mcp.elektron_types import (
    MidiMapping,
    ElektronConfig,
    create_parameter,
    ParameterGroup,
    ElektronParams,
)


def test_midi_mapping_validation():
    """Test that MidiMapping validates its values"""
    # Valid values should pass
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")
    assert mapping.cc_msb == "40"

    # Invalid types should raise validation errors
    with pytest.raises(ValidationError):
        MidiMapping(cc_msb=40, nrpn_lsb="1", nrpn_msb="73")  # Integer instead of string

    with pytest.raises(ValidationError):
        MidiMapping(cc_msb="40", nrpn_lsb=1, nrpn_msb="73")  # Integer instead of string


def test_parameter_option_validation():
    """Test Parameter validation for options"""
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")

    # Test options validation - valid default value
    param = ElektronParams(
        midi=mapping,
        max_midi_value=127,
        min_midi_value=0,
        max_value=127,
        min_value=0,
        default_value="on",
        options=["on", "off"],
    )
    assert param.default_value == "on"

    # Test options validation - invalid default value
    with pytest.raises(ValueError):
        ElektronParams(
            midi=mapping,
            max_midi_value=127,
            min_midi_value=0,
            max_value=127,
            min_value=0,
            default_value="invalid",
            options=["on", "off"],
        )


def test_parameter_numeric_validation():
    """Test Parameter validation for numeric ranges"""
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")

    # Valid numeric value within range
    param = ElektronParams(
        midi=mapping,
        max_midi_value=127,
        min_midi_value=0,
        max_value=60,
        min_value=-60,
        default_value=0,
    )
    assert param.default_value == 0

    # Invalid numeric value - above max
    with pytest.raises(ValueError):
        ElektronParams(
            midi=mapping,
            max_midi_value=127,
            min_midi_value=0,
            max_value=60,
            min_value=-60,
            default_value=70,
        )

    # Invalid numeric value - below min
    with pytest.raises(ValueError):
        ElektronParams(
            midi=mapping,
            max_midi_value=127,
            min_midi_value=0,
            max_value=60,
            min_value=-60,
            default_value=-70,
        )


def test_parameter_list_validation():
    """Test Parameter validation for list values"""
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")

    # Valid list within range
    param = ElektronParams(
        midi=mapping,
        max_midi_value=127,
        min_midi_value=0,
        max_value=[60, 60],
        min_value=[-60, -60],
        default_value=[0, 0],
    )
    assert param.default_value == [0, 0]

    # Invalid - inconsistent list lengths
    with pytest.raises(ValueError):
        ElektronParams(
            midi=mapping,
            max_midi_value=127,
            min_midi_value=0,
            max_value=[60, 60, 60],
            min_value=[-60, -60],
            default_value=[0, 0],
        )

    # Invalid - value outside range
    with pytest.raises(ValueError):
        ElektronParams(
            midi=mapping,
            max_midi_value=127,
            min_midi_value=0,
            max_value=[60, 60],
            min_value=[-60, -60],
            default_value=[0, 70],  # Second value is outside range
        )


def test_json_serialization():
    """Test JSON serialization and deserialization"""
    # Create a simple config
    config = ElektronConfig()

    # Add a simple parameter
    param = create_parameter("40", "1", "73", 127, 0, 60, -60, 0)
    group = ParameterGroup(parameters={"test_param": param})
    config.fmdrum.pages["test_page"] = group

    # Serialize to JSON
    json_data = config.model_dump_json()
    assert json_data is not None
    assert isinstance(json_data, str)

    # Parse the JSON string to ensure it's valid
    parsed_json = json.loads(json_data)
    assert parsed_json is not None

    # Deserialize from JSON
    new_config = ElektronConfig.model_validate_json(json_data)
    assert new_config is not None

    # Verify data is preserved
    assert "test_page" in new_config.fmdrum.pages
    test_param = new_config.fmdrum.pages["test_page"].parameters["test_param"]
    assert test_param.midi.cc_msb == "40"
    assert test_param.max_value == 60
    assert test_param.min_value == -60
