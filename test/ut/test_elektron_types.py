from elektron_mcp.elektron_types import (
    create_parameter,
    MidiMapping,
    ParameterGroup,
    elektron_config,
    ElektronParams,
)


def test_create_parameter():
    """Test the create_parameter helper function"""
    param = create_parameter(
        cc_msb="40",
        nrpn_lsb="1",
        nrpn_msb="73",
        max_midi=127,
        min_midi=0,
        max_val=60,
        min_val=-60,
        default=0,
    )

    assert param.midi.cc_msb == "40"
    assert param.midi.nrpn_lsb == "1"
    assert param.midi.nrpn_msb == "73"
    assert param.max_midi_value == 127
    assert param.min_midi_value == 0
    assert param.max_value == 60
    assert param.min_value == -60
    assert param.default_value == 0
    assert param.options is None

    # Test with options
    param_with_options = create_parameter(
        cc_msb="62",
        nrpn_lsb="1",
        nrpn_msb="95",
        max_midi=1,
        min_midi=0,
        max_val=1,
        min_val=0,
        default="off",
        options=["off", "on"],
    )

    assert param_with_options.options == ["off", "on"]
    assert param_with_options.default_value == "off"


def test_midi_mapping():
    """Test MidiMapping class"""
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")
    assert mapping.cc_msb == "40"
    assert mapping.nrpn_lsb == "1"
    assert mapping.nrpn_msb == "73"


def test_parameter():
    """Test Parameter class"""
    mapping = MidiMapping(cc_msb="40", nrpn_lsb="1", nrpn_msb="73")
    param = ElektronParams(
        midi=mapping,
        max_midi_value=127,
        min_midi_value=0,
        max_value=60,
        min_value=-60,
        default_value=0,
    )

    assert param.midi.cc_msb == "40"
    assert param.max_midi_value == 127
    assert param.min_midi_value == 0
    assert param.max_value == 60
    assert param.min_value == -60
    assert param.default_value == 0

    # Test with list values
    param_list = ElektronParams(
        midi=mapping,
        max_midi_value=127,
        min_midi_value=0,
        max_value=[60, 60],
        min_value=[-60, -60],
        default_value=[0, 0],
    )

    assert param_list.max_value == [60, 60]
    assert param_list.min_value == [-60, -60]
    assert param_list.default_value == [0, 0]


def test_parameter_group():
    """Test ParameterGroup class"""
    param = create_parameter("40", "1", "73", 127, 0, 60, -60, 0)
    group = ParameterGroup(parameters={"tune": param})

    assert group.parameters["tune"] == param

    # Test nested parameters
    nested_group = ParameterGroup(
        parameters={
            "A": {
                "atk": create_parameter("48", "1", "81", 127, 0, 127, 0, 0),
                "dec": create_parameter("49", "1", "82", 127, 0, 127, 0, 32),
            }
        }
    )

    assert nested_group.parameters["A"]["atk"].midi.cc_msb == "48"
    assert nested_group.parameters["A"]["dec"].default_value == 32


def test_config_structures():
    """Test that the major config structures were created correctly"""
    # Check fmdrum page structure
    assert "page_1" in elektron_config.fmdrum.pages
    assert "tune" in elektron_config.fmdrum.pages["page_1"].parameters

    # Check fmtone nested structure
    assert "page_2" in elektron_config.fmtone.pages
    assert "A" in elektron_config.fmtone.pages["page_2"].parameters
    assert "atk" in elektron_config.fmtone.pages["page_2"].parameters["A"]

    # Check filter parameters
    assert "FREQ" in elektron_config.multi_mode_filter.parameters

    # Check LFO parameters
    assert "lfo_1" in elektron_config.lfo.lfo_groups
    assert "SPD" in elektron_config.lfo.lfo_groups["lfo_1"]

    # Check AMP parameters
    assert "ATK" in elektron_config.amp_page.parameters

    # Check FX parameters
    assert "BR" in elektron_config.fx_page.parameters


def test_enum_values():
    """Test parameters with enum options"""
    param = elektron_config.multi_mode_filter.parameters.get("TYPE")
    assert param is not None

    mode_param = elektron_config.amp_page.parameters.get("MODE")
    assert mode_param is not None
    assert mode_param.options == ["AHD", "ADSR"]
    assert mode_param.default_value == "ADSR"

    wave_param = elektron_config.lfo.lfo_groups["lfo_1"]["WAVE"]
    assert wave_param.options == ["tri", "sine", "sqr", "saw", "expo", "ramp", "rand"]
    assert wave_param.default_value == "sine"
