from mcp.server.fastmcp import FastMCP

from elektron_mcp.digitone.controller.amp_fx_controller import (
    AmpController,
    FXController,
)
from elektron_mcp.digitone.controller.filter_controller import MultiModeFilterController
from elektron_mcp.digitone.controller.wavetone_controller import WavetoneController
from elektron_mcp.midi.digitone_midi import DigitoneMIDI
from elektron_mcp.digitone.config.digitone_config import digitone_config


mcp = FastMCP("Digitone 2")
midi = DigitoneMIDI()

wavetone_pages = digitone_config.wavetone.pages


@mcp.tool()
def set_wavetone_osc1_pitch(value: int):
    """
    Set the pitch of oscillator one.

    Value range for midi: 0 to 127
    Display range: -60 to +60
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_pitch(value)


@mcp.tool()
def set_wavetone_osc1_waveform(value: int):
    """
    Set the waveform of oscillator one.

    Value range for midi: 0 to 127
    Display range: 0 to 120
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_waveform(value)


@mcp.tool()
def set_wavetone_osc1_phase_distortion(value: int):
    """
    Set the phase distortion of oscillator one.

    Value range for midi: 0 to 127
    Display range: 0 to 100
    Default: 50
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_phase_distortion(value)


@mcp.tool()
def set_wavetone_osc1_level(value: int):
    """
    Set the level of oscillator one.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 100
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_level(value)


@mcp.tool()
def set_wavetone_osc1_offset(value: int):
    """
    Set the offset of oscillator one.

    Value range for midi: 0 to 127
    Display range: -10 to +10
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_offset(value)


@mcp.tool()
def set_wavetone_osc1_table(value: int):
    """
    Set the table of oscillator one.

    Value range for midi: 0 to 1
    Display options: "prim" (0), "harm" (1)
    Default: "prim"
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc1_table(value)


@mcp.tool()
def set_wavetone_osc2_pitch(value: int):
    """
    Set the pitch of oscillator two.

    Value range for midi: 0 to 127
    Display range: -60 to +60
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_pitch(value)


@mcp.tool()
def set_wavetone_osc2_waveform(value: int):
    """
    Set the waveform of oscillator two.

    Value range for midi: 0 to 127
    Display range: 0 to 120
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_waveform(value)


@mcp.tool()
def set_wavetone_osc2_phase_distortion(value: int):
    """
    Set the phase distortion of oscillator two.

    Value range for midi: 0 to 127
    Display range: 0 to 100
    Default: 50
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_phase_distortion(value)


@mcp.tool()
def set_wavetone_osc2_level(value: int):
    """
    Set the level of oscillator two.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 100
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_level(value)


@mcp.tool()
def set_wavetone_osc2_offset(value: int):
    """
    Set the offset of oscillator two.

    Value range for midi: 0 to 127
    Display range: -10 to +10
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_offset(value)


@mcp.tool()
def set_wavetone_osc2_table(value: int):
    """
    Set the table of oscillator two.

    Value range for midi: 0 to 1
    Display options: "prim" (0), "harm" (1)
    Default: "prim"
    """
    return WavetoneController(wavetone_pages, midi, 1).set_osc2_table(value)


@mcp.tool()
def set_wavetone_mod_type(value: int):
    """
    Set the modulation type.

    Value range for midi: 0 to 3
    Display options: "off" (0), "ring mod" (1), "ring mod fixed" (2), "hard sync" (3)
    Default: "off"
    """
    return WavetoneController(wavetone_pages, midi, 1).set_mod_type(value)


@mcp.tool()
def set_wavetone_reset_mode(value: int):
    """
    Set the oscillator reset mode.

    Value range for midi: 0 to 2
    Display options: "off" (0), "on" (1), "random" (2)
    Default: "on"
    """
    return WavetoneController(wavetone_pages, midi, 1).set_reset_mode(value)


@mcp.tool()
def set_wavetone_drift(value: int):
    """
    Set the drift amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_drift(value)


@mcp.tool()
def set_wavetone_attack(value: int):
    """
    Set the attack time.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_attack(value)


@mcp.tool()
def set_wavetone_hold(value: int):
    """
    Set the hold time.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 127
    """
    return WavetoneController(wavetone_pages, midi, 1).set_hold(value)


@mcp.tool()
def set_wavetone_decay(value: int):
    """
    Set the decay time.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 127
    """
    return WavetoneController(wavetone_pages, midi, 1).set_decay(value)


@mcp.tool()
def set_wavetone_noise_level(value: int):
    """
    Set the noise level.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_noise_level(value)


@mcp.tool()
def set_wavetone_noise_base(value: int):
    """
    Set the noise base frequency.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_noise_base(value)


@mcp.tool()
def set_wavetone_noise_width(value: int):
    """
    Set the noise width.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 127
    """
    return WavetoneController(wavetone_pages, midi, 1).set_noise_width(value)


@mcp.tool()
def set_wavetone_noise_type(value: int):
    """
    Set the noise type.

    Value range for midi: 0 to 2
    Display options: "grain noise" (0), "tuned noise" (1), "sample and hold noise" (2)
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_noise_type(value)


@mcp.tool()
def set_wavetone_noise_character(value: int):
    """
    Set the noise character.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return WavetoneController(wavetone_pages, midi, 1).set_noise_character(value)


# Multi Mode Filter tools
@mcp.tool()
def set_multimode_filter_attack(value: int):
    """
    Set the attack time of the multi-mode filter envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_attack(value)


@mcp.tool()
def set_multimode_filter_decay(value: int):
    """
    Set the decay time of the multi-mode filter envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 64
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_decay(value)


@mcp.tool()
def set_multimode_filter_sustain(value: int):
    """
    Set the sustain level of the multi-mode filter envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_sustain(value)


@mcp.tool()
def set_multimode_filter_release(value: int):
    """
    Set the release time of the multi-mode filter envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 64
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_release(value)


@mcp.tool()
def set_multimode_filter_frequency(value: int):
    """
    Set the cutoff frequency of the multi-mode filter.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 127
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_frequency(value)


@mcp.tool()
def set_multimode_filter_resonance(value: int):
    """
    Set the resonance of the multi-mode filter.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_resonance(value)


@mcp.tool()
def set_multimode_filter_type(value: int):
    """
    Set the type of the multi-mode filter.

    Value range for midi: 0 to 127
    Display options: Various filter types (LP2, LP4, BP2, BP4, HP2, HP4, etc.)
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_type(value)


@mcp.tool()
def set_multimode_filter_envelope_depth(value: int):
    """
    Set the envelope depth of the multi-mode filter.

    Value range for midi: 0 to 127
    Display range: -64 to +64
    """
    return MultiModeFilterController(
        digitone_config.multi_mode_filter.parameters, midi, 1
    ).set_envelope_depth(value)


# Amp tools
@mcp.tool()
def set_amp_attack(value: int):
    """
    Set the attack time of the amplitude envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 8
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_attack(value)


@mcp.tool()
def set_amp_hold(value: int):
    """
    Set the hold time of the amplitude envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 127
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_hold(value)


@mcp.tool()
def set_amp_decay(value: int):
    """
    Set the decay time of the amplitude envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 32
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_decay(value)


@mcp.tool()
def set_amp_sustain(value: int):
    """
    Set the sustain level of the amplitude envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 96
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_sustain(
        value
    )


@mcp.tool()
def set_amp_release(value: int):
    """
    Set the release time of the amplitude envelope.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 24
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_release(
        value
    )


@mcp.tool()
def set_amp_envelope_reset(value: int):
    """
    Set the envelope reset mode.

    Value range for midi: 0 to 1
    Display options: "off" (0), "on" (1)
    Default: "on"
    """
    return AmpController(
        digitone_config.amp_page.parameters, midi, 1
    ).set_envelope_reset(value)


@mcp.tool()
def set_amp_envelope_mode(value: int):
    """
    Set the envelope mode.

    Value range for midi: 0 to 1
    Display options: "AHD" (0), "ADSR" (1)
    Default: "ADSR"
    """
    return AmpController(
        digitone_config.amp_page.parameters, midi, 1
    ).set_envelope_mode(value)


@mcp.tool()
def set_amp_pan(value: int):
    """
    Set the stereo panning position.

    Value range for midi: 0 to 127
    Display range: -64 to +64
    Default: 0 (center)
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_pan(value)


@mcp.tool()
def set_amp_volume(value: int):
    """
    Set the overall volume level.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 110
    """
    return AmpController(digitone_config.amp_page.parameters, midi, 1).set_volume(value)


# FX tools
@mcp.tool()
def set_fx_bit_reduction(value: int):
    """
    Set the bit reduction amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(digitone_config.fx_page.parameters, midi, 1).set_bit_reduction(
        value
    )


@mcp.tool()
def set_fx_overdrive(value: int):
    """
    Set the overdrive amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(digitone_config.fx_page.parameters, midi, 1).set_overdrive(
        value
    )


@mcp.tool()
def set_fx_sample_rate_reduction(value: int):
    """
    Set the sample rate reduction amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(
        digitone_config.fx_page.parameters, midi, 1
    ).set_sample_rate_reduction(value)


@mcp.tool()
def set_fx_sample_rate_routing(value: int):
    """
    Set the sample rate reduction routing.

    Value range for midi: 0 to 1
    Display options: "pre" (0), "post" (1)
    Default: "pre"
    """
    return FXController(
        digitone_config.fx_page.parameters, midi, 1
    ).set_sample_rate_routing(value)


@mcp.tool()
def set_fx_overdrive_routing(value: int):
    """
    Set the overdrive routing.

    Value range for midi: 0 to 1
    Display options: "pre" (0), "post" (1)
    Default: "pre"
    """
    return FXController(
        digitone_config.fx_page.parameters, midi, 1
    ).set_overdrive_routing(value)


@mcp.tool()
def set_fx_delay(value: int):
    """
    Set the delay send amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(digitone_config.fx_page.parameters, midi, 1).set_delay(value)


@mcp.tool()
def set_fx_reverb(value: int):
    """
    Set the reverb send amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(digitone_config.fx_page.parameters, midi, 1).set_reverb(value)


@mcp.tool()
def set_fx_chorus(value: int):
    """
    Set the chorus send amount.

    Value range for midi: 0 to 127
    Display range: 0 to 127
    Default: 0
    """
    return FXController(digitone_config.fx_page.parameters, midi, 1).set_chorus(value)
