"""
Wavetone tools for controlling oscillator parameters on the Digitone.
"""

from elektron_mcp.digitone.services.wavetone_controller import WavetoneController
from elektron_mcp.digitone.config.config import digitone_config

wavetone_pages = digitone_config.wavetone.pages


def register_wavetone_tools(mcp, midi):
    """
    Register all wavetone tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_wavetone_osc1_pitch(value: int, track: int):
        """
        Set the pitch of oscillator one.

        Args:
            value (int): MIDI pitch value ranging from 0 to 127.
                - 0 maps to -5
                - 64 maps to 0
                - 127 maps to +5
                Values in between are linearly mapped.
                Display range: -5 to +5.
                Default is 0.
            track (int): The track number to set the pitch for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_pitch(value)

    @mcp.tool()
    def set_wavetone_osc1_waveform(value: int, track: int):
        """
        Set the waveform of oscillator one for a specific track.

        Args:
            value (int): Waveform value to set, ranging from 0 to 127.
                - 0   = Sine
                - 40  = Triangle
                - 80  = Saw
                - 3   = Square
                Values between these points represent transitions between waveforms.
                (Display range: 0–120)

            track (int): Track number to set the waveform for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_waveform(value)

    @mcp.tool()
    def set_wavetone_osc1_phase_distortion(value: int, track: int):
        """
        Set the phase distortion of oscillator one.

        Args:
            value (int): Phase distortion value ranging from 0 to 127.
                - 0 maps to 0%
                - 64 maps to 50%
                - 127 maps to 100%
                Values in between are linearly mapped.
                Display range: 0-100%.
                Default is 50%.
            track (int): The track number to set the phase distortion for. 1-16
        """
        return WavetoneController(
            wavetone_pages, midi, track
        ).set_osc1_phase_distortion(value)

    @mcp.tool()
    def set_wavetone_osc1_level(value: int, track: int):
        """
        Set the level of oscillator one.

        Args:
            value (int): Level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 100.
            track (int): The track number to set the level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_level(value)

    @mcp.tool()
    def set_wavetone_osc1_offset(value: int, track: int):
        """
        Set the offset of oscillator one.

        Args:
            value (int): Offset value ranging from 0 to 127.
                - 0 maps to -10
                - 64 maps to 0
                - 127 maps to +10
                Values in between are linearly mapped.
                Display range: -10 to +10.
                Default is 0.
            track (int): The track number to set the offset for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_offset(value)

    @mcp.tool()
    def set_wavetone_osc1_wavetable(value: int, track: int):
        """
        Selects the wavetable for oscillator 1's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

        Args:
            value (int): wavetable value ranging from 0 to 1.
                - 0 = "prim"
                - 1 = "harm"
                Display range: discrete options.
                Default is "prim".
            track (int): The track number to set the wavetable for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_table(value)

    @mcp.tool()
    def set_wavetone_osc2_pitch(value: int, track: int):
        """
        Set the pitch of oscillator two.

        Args:
            value (int): MIDI pitch value ranging from 0 to 127.
                - 0 maps to -5
                - 64 maps to 0
                - 127 maps to +5
                Values in between are linearly mapped.
                Display range: -5 to +5.
                Default is 0.
            track (int): The track number to set the pitch for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_pitch(value)

    @mcp.tool()
    def set_wavetone_osc2_waveform(value: int, track: int):
        """
        Set the waveform of oscillator two.

        Args:
            value (int): Waveform value to set, ranging from 0 to 127.
                - 0   = Sine
                - 40  = Triangle
                - 80  = Saw
                - 3   = Square
                Values between these points represent transitions between waveforms.
                Display range: 0-120.
                Default is 0.
            track (int): The track number to set the waveform for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_waveform(value)

    @mcp.tool()
    def set_wavetone_osc2_phase_distortion(value: int, track: int):
        """
        Set the phase distortion of oscillator two.

        Args:
            value (int): Phase distortion value ranging from 0 to 127.
                - 0 maps to 0%
                - 64 maps to 50%
                - 127 maps to 100%
                Values in between are linearly mapped.
                Display range: 0-100%.
                Default is 50%.
            track (int): The track number to set the phase distortion for. 1-16
        """
        return WavetoneController(
            wavetone_pages, midi, track
        ).set_osc2_phase_distortion(value)

    @mcp.tool()
    def set_wavetone_osc2_level(value: int, track: int):
        """
        Set the level of oscillator two.

        Args:
            value (int): Level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 100.
            track (int): The track number to set the level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_level(value)

    @mcp.tool()
    def set_wavetone_osc2_offset(value: int, track: int):
        """
        Set the offset of oscillator two.

        Args:
            value (int): Offset value ranging from 0 to 127.
                - 0 maps to -10
                - 64 maps to 0
                - 127 maps to +10
                Values in between are linearly mapped.
                Display range: -10 to +10.
                Default is 0.
            track (int): The track number to set the offset for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_offset(value)

    @mcp.tool()
    def set_wavetone_osc2_wavetable(value: int, track: int):
        """
        Selects the wavetable for oscillator 2's WAVE parameter. Options include PRIM (basic waves like Sin, Tri, Saw, Square) and HARM (a range of harmonic combinations)

        Args:
            value (int): Table value ranging from 0 to 1.
                - 0 = "prim"
                - 1 = "harm"
                Display range: discrete options.
                Default is "prim".
            track (int): The track number to set the table for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_table(value)

    @mcp.tool()
    def set_wavetone_mod_type(value: int, track: int):
        """
        MOD Oscillator Modulation selects how the two oscillators interact. The options are OFF, RING MOD (Oscillator 2 modulates Oscillator 1), RING MODE FIXED (Oscillator 2 modulates Oscillator 1, but its pitch doesn't track note values), and HARD SYNC (Oscillator 1's phase resets with each new cycle of Oscillator 2)

        Args:
            value (int): Modulation type value ranging from 0 to 3.
                - 0 = "off"
                - 1 = "ring mod"
                - 2 = "ring mod fixed"
                - 3 = "hard sync"
                Display range: discrete options.
                Default is "off".
            track (int): The track number to set the modulation type for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_mod_type(value)

    @mcp.tool()
    def set_wavetone_reset_mode(value: int, track: int):
        """
        RSET Oscillator Phase Reset determines if and how the oscillators' wave phases reset when a note is played. Options are OFF (no reset), ON (reset to the start of the waveform), and RAND (reset to a random position)

        Args:
            value (int): Reset mode value ranging from 0 to 2.
                - 0 = "off"
                - 1 = "on"
                - 2 = "random"
                Display range: discrete options.
                Default is "on".
            track (int): The track number to set the reset mode for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_reset_mode(value)

    @mcp.tool()
    def set_wavetone_drift(value: int, track: int):
        """
        Set the drift amount.

        Args:
            value (int): Drift value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the drift for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_drift(value)

    @mcp.tool()
    def set_wavetone_attack(value: int, track: int):
        """
        Set the attack time.

        Args:
            value (int): Attack time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the attack for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_attack(value)

    @mcp.tool()
    def set_wavetone_hold(value: int, track: int):
        """
        Set the hold time.

        Args:
            value (int): Hold time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 127.
            track (int): The track number to set the hold for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_hold(value)

    @mcp.tool()
    def set_wavetone_decay(value: int, track: int):
        """
        Set the decay time.

        Args:
            value (int): Decay time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 127.
            track (int): The track number to set the decay for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_decay(value)

    @mcp.tool()
    def set_wavetone_noise_level(value: int, track: int):
        """
        Set the noise level.

        Args:
            value (int): Noise level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the noise level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_level(value)

    @mcp.tool()
    def set_wavetone_noise_base(value: int, track: int):
        """
        Set the noise base frequency.

        Args:
            value (int): Noise base frequency value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the noise base for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_base(value)

    @mcp.tool()
    def set_wavetone_noise_width(value: int, track: int):
        """
        Set the noise width.

        Args:
            value (int): Noise width value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 127.
            track (int): The track number to set the noise width for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_width(value)

    @mcp.tool()
    def set_wavetone_noise_type(value: int, track: int):
        """
        Set the noise type.

        Args:
            value (int): Noise type value ranging from 0 to 2.
                - 0 = "grain noise"
                - 1 = "tuned noise"
                - 2 = "sample and hold noise"
                Display range: discrete options.
                Default is "grain noise" (0).
            track (int): The track number to set the noise type for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_type(value)

    @mcp.tool()
    def set_wavetone_noise_character(value: int, track: int):
        """
        Set the noise character.

        Args:
            value (int): Noise character value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the noise character for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_character(
            value
        )
