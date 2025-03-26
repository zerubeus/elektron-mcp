"""
LFO tools for controlling LFO parameters on the Digitone.
"""

from elektron_mcp.digitone.controller.lfo_controller import (
    LFO1Controller,
    LFO2Controller,
    LFO3Controller,
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
            value (int): Destination value ranging from 0 to the number of available destinations.
                See the LFO1 destinations list in the constants.
                Default is "none" (0).
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
            value (int): Destination value ranging from 0 to the number of available destinations.
                See the LFO2 destinations list in the constants.
                Default is "none" (0).
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

    # LFO3 tools
    @mcp.tool()
    def set_lfo3_speed(value: int, track: int):
        """
        Set the speed of LFO3.

        Args:
            value (int): Speed value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 48.
            track (int): The track number to set the LFO speed for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_speed(value)

    @mcp.tool()
    def set_lfo3_multiplier(value: int, track: int):
        """
        Set the multiplier of LFO3.

        Args:
            value (int): Multiplier value ranging from 0 to 11.
                - 0 maps to 1
                - 11 maps to 2000
                Display range: 1-2000.
                Default is 2.
            track (int): The track number to set the LFO multiplier for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_multiplier(value)

    @mcp.tool()
    def set_lfo3_fade(value: int, track: int):
        """
        Set the fade in/out of LFO3.

        Args:
            value (int): Fade value ranging from 0 to 127.
                - 0 maps to -64
                - 64 maps to 0
                - 127 maps to 63
                Display range: -64 to 63.
                Default is 0.
            track (int): The track number to set the LFO fade for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_fade(value)

    @mcp.tool()
    def set_lfo3_destination(value: int, track: int):
        """
        Set the destination of LFO3.

        Args:
            value (int): Destination value ranging from 0 to the number of available destinations.
                See the LFO3 destinations list in the constants.
                Default is "none" (0).
            track (int): The track number to set the LFO destination for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_destination(value)

    @mcp.tool()
    def set_lfo3_waveform(value: int, track: int):
        """
        Set the waveform of LFO3.

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
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_waveform(value)

    @mcp.tool()
    def set_lfo3_start_phase(value: int, track: int):
        """
        Set the start phase of LFO3.

        Args:
            value (int): Start phase value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO start phase for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_start_phase(value)

    @mcp.tool()
    def set_lfo3_trigger_mode(value: int, track: int):
        """
        Set the trigger mode of LFO3.

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
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_trigger_mode(value)

    @mcp.tool()
    def set_lfo3_depth(value: int, track: int):
        """
        Set the depth of LFO3.

        Args:
            value (int): Depth value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
            track (int): The track number to set the LFO depth for. 1-16
        """
        return LFO3Controller(
            digitone_config.lfo.lfo_groups["lfo_3"], midi, track
        ).set_depth(value)
