from elektron_mcp.digitone.models.models import (
    MidiMapping,
    DigitoneParams,
    ParameterGroup,
)


def _extract_param_values(param_dict):
    """Helper function to extract parameter values with common defaults from a dictionary"""
    return {
        "cc_msb": str(param_dict.get("cc_msb", param_dict.get("cc", ""))),
        "nrpn_lsb": param_dict.get("nrpn_lsb", 1),
        "nrpn_msb": param_dict.get("nrpn_msb", param_dict.get("nrpn", 0)),
        "max_midi": param_dict.get("max_midi", 127),
        "min_midi": param_dict.get("min_midi", 0),
        "max_val": param_dict.get("max_val", 127),
        "min_val": param_dict.get("min_val", 0),
        "default": param_dict.get("default", 0),
        "options": param_dict.get("options", None),
    }


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
    # Convert only CC MSB to string, keep NRPN values as integers
    cc_msb_str = str(cc_msb) if isinstance(cc_msb, (int, float)) else cc_msb

    # Don't convert NRPN values to strings - they should be integers
    nrpn_lsb_int = int(nrpn_lsb) if isinstance(nrpn_lsb, (str, float)) else nrpn_lsb
    nrpn_msb_int = int(nrpn_msb) if isinstance(nrpn_msb, (str, float)) else nrpn_msb

    mapping = MidiMapping(
        cc_msb=cc_msb_str, nrpn_lsb=nrpn_lsb_int, nrpn_msb=nrpn_msb_int
    )
    return DigitoneParams(
        midi=mapping,
        max_midi_value=max_midi,
        min_midi_value=min_midi,
        max_value=max_val,
        min_value=min_val,
        default_value=default,
        options=options,
    )


def create_param_from_dict(param_dict):
    """Create a parameter from a dictionary with standard keys"""
    values = _extract_param_values(param_dict)
    return create_parameter(
        cc_msb=values["cc_msb"],
        nrpn_lsb=values["nrpn_lsb"],
        nrpn_msb=values["nrpn_msb"],
        max_midi=values["max_midi"],
        min_midi=values["min_midi"],
        max_val=values["max_val"],
        min_val=values["min_val"],
        default=values["default"],
        options=values["options"],
    )


def create_lfo_params(params_config):
    """Create LFO parameters with explicit CC and NRPN values."""
    return {
        name: create_param_from_dict(param) for name, param in params_config.items()
    }


def create_parameter_group(params_dict):
    """Helper function to create a parameter group from a dictionary"""
    parameters = {}
    for key, value in params_dict.items():
        if isinstance(value, dict) and ("cc" in value or "cc_msb" in value):
            # This is a parameter definition
            parameters[key] = create_param_from_dict(value)
        elif isinstance(value, dict):
            # This is a nested dictionary of parameters
            nested_params = {}
            for nested_key, nested_value in value.items():
                nested_params[nested_key] = create_param_from_dict(nested_value)
            parameters[key] = nested_params
    return ParameterGroup(parameters=parameters)


def setup_filter_parameters(filter_obj, params_dict):
    """Helper function to set up filter parameters to avoid code duplication"""
    filter_obj.parameters = {
        name: create_param_from_dict(param) for name, param in params_dict.items()
    }
