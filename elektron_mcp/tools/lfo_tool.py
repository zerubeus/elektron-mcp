"""
LFO tools for controlling LFO parameters on the Digitone.
"""

from elektron_mcp.digitone.controller.lfo_controller import (
    LFO1Controller,
    LFO2Controller,
)
from elektron_mcp.digitone.config.digitone_config import digitone_config


def register_lfo_tools(mcp, midi):
    """
    Register all LFO tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    # LFO1 tools
    @mcp.tool()
    def set_lfo1_speed(value: int, track: int):
        """
        Set the speed of LFO1.

        Args:
            value (int): Speed value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 48.
            track (int): The track number to set the LFO speed for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_speed(value)

    @mcp.tool()
    def set_lfo1_multiplier(value: int, track: int):
        """
        Set the multiplier of LFO1.

        Args:
            value (int): Multiplier value ranging from 0 to 11.
                - 0 maps to 1
                - 11 maps to 2000
                Display range: 1-2000.
                Default is 2.
            track (int): The track number to set the LFO multiplier for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_multiplier(value)

    @mcp.tool()
    def set_lfo1_fade(value: int, track: int):
        """
        Set the fade in/out of LFO1.

        Args:
            value (int): Fade value ranging from 0 to 127.
                - 0 maps to -64
                - 64 maps to 0
                - 127 maps to 63
                Display range: -64 to 63.
                Default is 0.
            track (int): The track number to set the LFO fade for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_fade(value)

    @mcp.tool()
    def set_lfo1_destination(value: int, track: int):
        """
        Set the destination of LFO1.

        Args:
            value (int): Destination value ranging from 0 to 99.
                - 0 = none (default)
                - 25 = wavetone_osc1_pitch
                - 26 = wavetone_osc1_waveform
                - 27 = wavetone_osc1_wavetable
                - 28 = wavetone_osc1_offset
                - 29 = wavetone_osc1_phase_distortion
                - 30 = wavetone_osc1_level
                - 31 = wavetone_osc2_pitch
                - 32 = wavetone_osc2_waveform
                - 33 = wavetone_osc2_wavetable
                - 34 = wavetone_osc2_offset
                - 35 = wavetone_osc2_phase_distortion
                - 36 = wavetone_osc2_level
                - 37 = wavetone_mode
                - 38 = wavetone_drift
                - 39 = wavetone_phase_reset
                - 40 = wavetone_noise_attack
                - 41 = wavetone_noise_hold
                - 42 = wavetone_noise_decay
                - 43 = wavetone_noise_level
                - 44 = wavetone_noise_base
                - 45 = wavetone_noise_width
                - 46 = wavetone_noise_type
                - 47 = wavetone_noise_character
                - 66 = filter_type
                - 67 = filter_freq
                - 69 = filter_envelope_depth
                - 70 = filter_envelope_delay
                - 71 = filter_envelope_attack
                - 72 = filter_envelope_decay
                - 73 = filter_envelope_sustain
                - 74 = filter_envelope_release
                - 75 = filter_reset
                - 76 = filter_base
                - 77 = filter_width
                - 78 = filter_bw_rt
                - 79 = filter_key_track
                - 81 = amp_attack
                - 82 = amp_hold
                - 83 = amp_decay
                - 84 = amp_sustain
                - 85 = amp_release
                - 86 = fx_delay_send
                - 87 = fx_reverb_send
                - 88 = fx_chorus_send
                - 89 = amp_pan
                - 90 = amp_volume
                - 95 = fx_bit_reduction
                - 96 = fx_srr
                - 97 = fx_srr_routing
                - 98 = fx_overdrive
                - 99 = fx_overdrive_routing
            track (int): The track number to set the LFO destination for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_destination(value)

    @mcp.tool()
    def set_lfo1_waveform(value: int, track: int):
        """
        Set the waveform of LFO1.

        Args:
            value (int): Waveform value ranging from 0 to 6.
                - 0 = "tri"
                - 1 = "sine"
                - 2 = "sqr"
                - 3 = "saw"
                - 4 = "expo"
                - 5 = "ramp"
                - 6 = "rand"
                Default is "sine" (1).
            track (int): The track number to set the LFO waveform for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_waveform(value)

    @mcp.tool()
    def set_lfo1_start_phase(value: int, track: int):
        """
        Set the start phase of LFO1.

        Args:
            value (int): Start phase value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO start phase for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_start_phase(value)

    @mcp.tool()
    def set_lfo1_trigger_mode(value: int, track: int):
        """
        Set the trigger mode of LFO1.

        Args:
            value (int): Trigger mode value ranging from 0 to 4.
                - 0 = "free"
                - 1 = "trig"
                - 2 = "hold"
                - 3 = "one"
                - 4 = "half"
                Default is "free" (0).
            track (int): The track number to set the LFO trigger mode for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_trigger_mode(value)

    @mcp.tool()
    def set_lfo1_depth(value: int, track: int):
        """
        Set the depth of LFO1.

        Args:
            value (int): Depth value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO depth for. 1-16
        """
        return LFO1Controller(
            digitone_config.lfo.lfo_groups["lfo_1"], midi, track
        ).set_depth(value)

    # LFO2 tools
    @mcp.tool()
    def set_lfo2_speed(value: int, track: int):
        """
        Set the speed of LFO2.

        Args:
            value (int): Speed value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 48.
            track (int): The track number to set the LFO speed for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_speed(value)

    @mcp.tool()
    def set_lfo2_multiplier(value: int, track: int):
        """
        Set the multiplier of LFO2.

        Args:
            value (int): Multiplier value ranging from 0 to 11.
                - 0 maps to 1
                - 11 maps to 2000
                Display range: 1-2000.
                Default is 2.
            track (int): The track number to set the LFO multiplier for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_multiplier(value)

    @mcp.tool()
    def set_lfo2_fade(value: int, track: int):
        """
        Set the fade in/out of LFO2.

        Args:
            value (int): Fade value ranging from 0 to 127.
                - 0 maps to -64
                - 64 maps to 0
                - 127 maps to 63
                Display range: -64 to 63.
                Default is 0.
            track (int): The track number to set the LFO fade for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_fade(value)

    @mcp.tool()
    def set_lfo2_destination(value: int, track: int):
        """
        Set the destination of LFO2.

        Args:
            value (int): Destination value ranging from 0 to 99.
                - 0 = none (default)
                - 1 = lfo1_speed
                - 2 = lfo1_multiplier
                - 3 = lfo1_fade
                - 5 = lfo1_wave
                - 6 = lfo1_start_phase
                - 7 = lfo1_mode
                - 8 = lfo1_depth
                - 25 = wavetone_osc1_pitch
                - 26 = wavetone_osc1_waveform
                - 27 = wavetone_osc1_wavetable
                - 28 = wavetone_osc1_offset
                - 29 = wavetone_osc1_phase_distortion
                - 30 = wavetone_osc1_level
                - 31 = wavetone_osc2_pitch
                - 32 = wavetone_osc2_waveform
                - 33 = wavetone_osc2_wavetable
                - 34 = wavetone_osc2_offset
                - 35 = wavetone_osc2_phase_distortion
                - 36 = wavetone_osc2_level
                - 37 = wavetone_mode
                - 38 = wavetone_drift
                - 39 = wavetone_phase_reset
                - 40 = wavetone_noise_attack
                - 41 = wavetone_noise_hold
                - 42 = wavetone_noise_decay
                - 43 = wavetone_noise_level
                - 44 = wavetone_noise_base
                - 45 = wavetone_noise_width
                - 46 = wavetone_noise_type
                - 47 = wavetone_noise_character
                - 66 = filter_type
                - 67 = filter_freq
                - 69 = filter_envelope_depth
                - 70 = filter_envelope_delay
                - 71 = filter_envelope_attack
                - 72 = filter_envelope_decay
                - 73 = filter_envelope_sustain
                - 74 = filter_envelope_release
                - 75 = filter_reset
                - 76 = filter_base
                - 77 = filter_width
                - 78 = filter_bw_rt
                - 79 = filter_key_track
                - 81 = amp_attack
                - 82 = amp_hold
                - 83 = amp_decay
                - 84 = amp_sustain
                - 85 = amp_release
                - 86 = fx_delay_send
                - 87 = fx_reverb_send
                - 88 = fx_chorus_send
                - 89 = amp_pan
                - 90 = amp_volume
                - 95 = fx_bit_reduction
                - 96 = fx_srr
                - 97 = fx_srr_routing
                - 98 = fx_overdrive
                - 99 = fx_overdrive_routing
            track (int): The track number to set the LFO destination for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_destination(value)

    @mcp.tool()
    def set_lfo2_waveform(value: int, track: int):
        """
        Set the waveform of LFO2.

        Args:
            value (int): Waveform value ranging from 0 to 6.
                - 0 = "tri"
                - 1 = "sine"
                - 2 = "sqr"
                - 3 = "saw"
                - 4 = "expo"
                - 5 = "ramp"
                - 6 = "rand"
                Default is "sine" (1).
            track (int): The track number to set the LFO waveform for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_waveform(value)

    @mcp.tool()
    def set_lfo2_start_phase(value: int, track: int):
        """
        Set the start phase of LFO2.

        Args:
            value (int): Start phase value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO start phase for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_start_phase(value)

    @mcp.tool()
    def set_lfo2_trigger_mode(value: int, track: int):
        """
        Set the trigger mode of LFO2.

        Args:
            value (int): Trigger mode value ranging from 0 to 4.
                - 0 = "free"
                - 1 = "trig"
                - 2 = "hold"
                - 3 = "one"
                - 4 = "half"
                Default is "free" (0).
            track (int): The track number to set the LFO trigger mode for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_trigger_mode(value)

    @mcp.tool()
    def set_lfo2_depth(value: int, track: int):
        """
        Set the depth of LFO2.

        Args:
            value (int): Depth value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO depth for. 1-16
        """
        return LFO2Controller(
            digitone_config.lfo.lfo_groups["lfo_2"], midi, track
        ).set_depth(value)
