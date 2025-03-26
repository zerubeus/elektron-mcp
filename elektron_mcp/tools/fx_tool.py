"""
FX tools for controlling effects parameters on the Digitone.
"""

from elektron_mcp.digitone.controller.amp_fx_controller import FXController
from elektron_mcp.digitone.config.digitone_config import digitone_config


def register_fx_tools(mcp, midi):
    """
    Register all FX tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_fx_bit_reduction(value: int, track: int):
        """
        Set the bit reduction amount.

        Args:
            value (int): Bit reduction value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX bit reduction for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_bit_reduction(value)

    @mcp.tool()
    def set_fx_overdrive(value: int, track: int):
        """
        Set the overdrive amount.

        Args:
            value (int): Overdrive value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX overdrive for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_overdrive(value)

    @mcp.tool()
    def set_fx_sample_rate_reduction(value: int, track: int):
        """
        Set the sample rate reduction amount.

        Args:
            value (int): Sample rate reduction value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX sample rate reduction for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_sample_rate_reduction(value)

    @mcp.tool()
    def set_fx_sample_rate_routing(value: int, track: int):
        """
        Set the sample rate reduction routing.

        Args:
            value (int): Sample rate routing value ranging from 0 to 1.
                - 0 = "pre"
                - 1 = "post"
                Display range: discrete options.
                Default is "pre" (0).
            track (int): The track number to set the FX sample rate routing for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_sample_rate_routing(value)

    @mcp.tool()
    def set_fx_overdrive_routing(value: int, track: int):
        """
        Set the overdrive routing.

        Args:
            value (int): Overdrive routing value ranging from 0 to 1.
                - 0 = "pre"
                - 1 = "post"
                Display range: discrete options.
                Default is "pre" (0).
            track (int): The track number to set the FX overdrive routing for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_overdrive_routing(value)

    @mcp.tool()
    def set_fx_delay(value: int, track: int):
        """
        Set the delay send amount.

        Args:
            value (int): Delay send value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX delay for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_delay(
            value
        )

    @mcp.tool()
    def set_fx_reverb(value: int, track: int):
        """
        Set the reverb send amount.

        Args:
            value (int): Reverb send value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX reverb for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_reverb(
            value
        )

    @mcp.tool()
    def set_fx_chorus(value: int, track: int):
        """
        Set the chorus send amount.

        Args:
            value (int): Chorus send value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the FX chorus for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_chorus(
            value
        )
