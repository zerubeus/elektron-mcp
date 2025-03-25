"""
Wavetone tools for controlling oscillator parameters on the Digitone.
"""

from elektron_mcp.digitone.controller.wavetone_controller import WavetoneController
from elektron_mcp.digitone.config.digitone_config import digitone_config

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
            value: int - The pitch value to set. 0-127
            track: int - The track number to set the pitch for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_pitch(value)

    @mcp.tool()
    def set_wavetone_osc1_waveform(value: int, track: int):
        """
        Set the waveform of oscillator one.

        Args:
            value: int - The waveform value to set. 0-127 (display range: 0-120)
            track: int - The track number to set the waveform for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_waveform(value)

    @mcp.tool()
    def set_wavetone_osc1_phase_distortion(value: int, track: int):
        """
        Set the phase distortion of oscillator one.

        Args:
            value: int - The phase distortion value to set. 0-127 (display range: 0-100)
            track: int - The track number to set the phase distortion for. 1-16
        """
        return WavetoneController(
            wavetone_pages, midi, track
        ).set_osc1_phase_distortion(value)

    @mcp.tool()
    def set_wavetone_osc1_level(value: int, track: int):
        """
        Set the level of oscillator one.

        Args:
            value: int - The level value to set. 0-127
            track: int - The track number to set the level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_level(value)

    @mcp.tool()
    def set_wavetone_osc1_offset(value: int, track: int):
        """
        Set the offset of oscillator one.

        Args:
            value: int - The offset value to set. 0-127 (display range: -10 to +10)
            track: int - The track number to set the offset for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_offset(value)

    @mcp.tool()
    def set_wavetone_osc1_table(value: int, track: int):
        """
        Set the table of oscillator one.

        Args:
            value: int - The table value to set. 0-1 (0="prim", 1="harm")
            track: int - The track number to set the table for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc1_table(value)

    @mcp.tool()
    def set_wavetone_osc2_pitch(value: int, track: int):
        """
        Set the pitch of oscillator two.

        Args:
            value: int - The pitch value to set. 0-127 (display range: -60 to +60)
            track: int - The track number to set the pitch for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_pitch(value)

    @mcp.tool()
    def set_wavetone_osc2_waveform(value: int, track: int):
        """
        Set the waveform of oscillator two.

        Args:
            value: int - The waveform value to set. 0-127 (display range: 0-120)
            track: int - The track number to set the waveform for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_waveform(value)

    @mcp.tool()
    def set_wavetone_osc2_phase_distortion(value: int, track: int):
        """
        Set the phase distortion of oscillator two.

        Args:
            value: int - The phase distortion value to set. 0-127 (display range: 0-100)
            track: int - The track number to set the phase distortion for. 1-16
        """
        return WavetoneController(
            wavetone_pages, midi, track
        ).set_osc2_phase_distortion(value)

    @mcp.tool()
    def set_wavetone_osc2_level(value: int, track: int):
        """
        Set the level of oscillator two.

        Args:
            value: int - The level value to set. 0-127
            track: int - The track number to set the level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_level(value)

    @mcp.tool()
    def set_wavetone_osc2_offset(value: int, track: int):
        """
        Set the offset of oscillator two.

        Args:
            value: int - The offset value to set. 0-127 (display range: -10 to +10)
            track: int - The track number to set the offset for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_offset(value)

    @mcp.tool()
    def set_wavetone_osc2_table(value: int, track: int):
        """
        Set the table of oscillator two.

        Args:
            value: int - The table value to set. 0-1 (0="prim", 1="harm")
            track: int - The track number to set the table for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_osc2_table(value)

    @mcp.tool()
    def set_wavetone_mod_type(value: int, track: int):
        """
        Set the modulation type.

        Args:
            value: int - The modulation type to set. 0-3 (0="off", 1="ring mod", 2="ring mod fixed", 3="hard sync")
            track: int - The track number to set the modulation type for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_mod_type(value)

    @mcp.tool()
    def set_wavetone_reset_mode(value: int, track: int):
        """
        Set the oscillator reset mode.

        Args:
            value: int - The reset mode to set. 0-2 (0="off", 1="on", 2="random")
            track: int - The track number to set the reset mode for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_reset_mode(value)

    @mcp.tool()
    def set_wavetone_drift(value: int, track: int):
        """
        Set the drift amount.

        Args:
            value: int - The drift amount to set. 0-127
            track: int - The track number to set the drift for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_drift(value)

    @mcp.tool()
    def set_wavetone_attack(value: int, track: int):
        """
        Set the attack time.

        Args:
            value: int - The attack time to set. 0-127
            track: int - The track number to set the attack for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_attack(value)

    @mcp.tool()
    def set_wavetone_hold(value: int, track: int):
        """
        Set the hold time.

        Args:
            value: int - The hold time to set. 0-127
            track: int - The track number to set the hold for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_hold(value)

    @mcp.tool()
    def set_wavetone_decay(value: int, track: int):
        """
        Set the decay time.

        Args:
            value: int - The decay time to set. 0-127
            track: int - The track number to set the decay for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_decay(value)

    @mcp.tool()
    def set_wavetone_noise_level(value: int, track: int):
        """
        Set the noise level.

        Args:
            value: int - The noise level to set. 0-127
            track: int - The track number to set the noise level for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_level(value)

    @mcp.tool()
    def set_wavetone_noise_base(value: int, track: int):
        """
        Set the noise base frequency.

        Args:
            value: int - The noise base frequency to set. 0-127
            track: int - The track number to set the noise base for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_base(value)

    @mcp.tool()
    def set_wavetone_noise_width(value: int, track: int):
        """
        Set the noise width.

        Args:
            value: int - The noise width to set. 0-127
            track: int - The track number to set the noise width for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_width(value)

    @mcp.tool()
    def set_wavetone_noise_type(value: int, track: int):
        """
        Set the noise type.

        Args:
            value: int - The noise type to set. 0-2 (0="grain noise", 1="tuned noise", 2="sample and hold noise")
            track: int - The track number to set the noise type for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_type(value)

    @mcp.tool()
    def set_wavetone_noise_character(value: int, track: int):
        """
        Set the noise character.

        Args:
            value: int - The noise character to set. 0-127
            track: int - The track number to set the noise character for. 1-16
        """
        return WavetoneController(wavetone_pages, midi, track).set_noise_character(
            value
        )
