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
            value: int - The bit reduction amount to set. 0-127
            track: int - The track number to set the FX bit reduction for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_bit_reduction(value)

    @mcp.tool()
    def set_fx_overdrive(value: int, track: int):
        """
        Set the overdrive amount.

        Args:
            value: int - The overdrive amount to set. 0-127
            track: int - The track number to set the FX overdrive for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_overdrive(value)

    @mcp.tool()
    def set_fx_sample_rate_reduction(value: int, track: int):
        """
        Set the sample rate reduction amount.

        Args:
            value: int - The sample rate reduction amount to set. 0-127
            track: int - The track number to set the FX sample rate reduction for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_sample_rate_reduction(value)

    @mcp.tool()
    def set_fx_sample_rate_routing(value: int, track: int):
        """
        Set the sample rate reduction routing.

        Args:
            value: int - The sample rate routing to set. 0-1 (0="pre", 1="post")
            track: int - The track number to set the FX sample rate routing for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_sample_rate_routing(value)

    @mcp.tool()
    def set_fx_overdrive_routing(value: int, track: int):
        """
        Set the overdrive routing.

        Args:
            value: int - The overdrive routing to set. 0-1 (0="pre", 1="post")
            track: int - The track number to set the FX overdrive routing for. 1-16
        """
        return FXController(
            digitone_config.fx_page.parameters, midi, track
        ).set_overdrive_routing(value)

    @mcp.tool()
    def set_fx_delay(value: int, track: int):
        """
        Set the delay send amount.

        Args:
            value: int - The delay send amount to set. 0-127
            track: int - The track number to set the FX delay for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_delay(
            value
        )

    @mcp.tool()
    def set_fx_reverb(value: int, track: int):
        """
        Set the reverb send amount.

        Args:
            value: int - The reverb send amount to set. 0-127
            track: int - The track number to set the FX reverb for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_reverb(
            value
        )

    @mcp.tool()
    def set_fx_chorus(value: int, track: int):
        """
        Set the chorus send amount.

        Args:
            value: int - The chorus send amount to set. 0-127
            track: int - The track number to set the FX chorus for. 1-16
        """
        return FXController(digitone_config.fx_page.parameters, midi, track).set_chorus(
            value
        )
