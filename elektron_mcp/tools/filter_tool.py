"""
Filter tools for controlling the multi-mode filter parameters on the Digitone.
"""

from elektron_mcp.digitone.controller.filter_controller import MultiModeFilterController
from elektron_mcp.digitone.config.digitone_config import digitone_config


def register_filter_tools(mcp, midi):
    """
    Register all filter tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_multimode_filter_attack(value: int, track: int):
        """
        Set the attack time of the multi-mode filter envelope.

        Args:
            value: int - The attack time to set. 0-127
            track: int - The track number to set the filter attack for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_attack(value)

    @mcp.tool()
    def set_multimode_filter_decay(value: int, track: int):
        """
        Set the decay time of the multi-mode filter envelope.

        Args:
            value: int - The decay time to set. 0-127
            track: int - The track number to set the filter decay for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_decay(value)

    @mcp.tool()
    def set_multimode_filter_sustain(value: int, track: int):
        """
        Set the sustain level of the multi-mode filter envelope.

        Args:
            value: int - The sustain level to set. 0-127
            track: int - The track number to set the filter sustain for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_sustain(value)

    @mcp.tool()
    def set_multimode_filter_release(value: int, track: int):
        """
        Set the release time of the multi-mode filter envelope.

        Args:
            value: int - The release time to set. 0-127
            track: int - The track number to set the filter release for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_release(value)

    @mcp.tool()
    def set_multimode_filter_frequency(value: int, track: int):
        """
        Set the cutoff frequency of the multi-mode filter.

        Args:
            value: int - The cutoff frequency to set. 0-127
            track: int - The track number to set the filter frequency for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_frequency(value)

    @mcp.tool()
    def set_multimode_filter_resonance(value: int, track: int):
        """
        Set the resonance of the multi-mode filter.

        Args:
            value: int - The resonance value to set. 0-127
            track: int - The track number to set the filter resonance for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_resonance(value)

    @mcp.tool()
    def set_multimode_filter_type(value: int, track: int):
        """
        Set the type of the multi-mode filter.

        Args:
            value: int - The filter type to set. 0-127 (Various filter types: LP2, LP4, BP2, BP4, HP2, HP4, etc.)
            track: int - The track number to set the filter type for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_type(value)

    @mcp.tool()
    def set_multimode_filter_envelope_depth(value: int, track: int):
        """
        Set the envelope depth of the multi-mode filter.

        Args:
            value: int - The envelope depth to set. 0-127 (display range: -64 to +64)
            track: int - The track number to set the filter envelope depth for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_envelope_depth(value)
