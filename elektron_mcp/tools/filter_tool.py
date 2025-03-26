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
            value (int): Attack time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the filter attack for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_attack(value)

    @mcp.tool()
    def set_multimode_filter_decay(value: int, track: int):
        """
        Set the decay time of the multi-mode filter envelope.

        Args:
            value (int): Decay time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 64.
            track (int): The track number to set the filter decay for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_decay(value)

    @mcp.tool()
    def set_multimode_filter_sustain(value: int, track: int):
        """
        Set the sustain level of the multi-mode filter envelope.

        Args:
            value (int): Sustain level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the filter sustain for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_sustain(value)

    @mcp.tool()
    def set_multimode_filter_release(value: int, track: int):
        """
        Set the release time of the multi-mode filter envelope.

        Args:
            value (int): Release time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 64.
            track (int): The track number to set the filter release for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_release(value)

    @mcp.tool()
    def set_multimode_filter_frequency(value: int, track: int):
        """
        Set the cutoff frequency of the multi-mode filter.

        Args:
            value (int): Cutoff frequency value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 127.
            track (int): The track number to set the filter frequency for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_frequency(value)

    @mcp.tool()
    def set_multimode_filter_resonance(value: int, track: int):
        """
        Set the resonance of the multi-mode filter.

        Args:
            value (int): Resonance value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 0.
            track (int): The track number to set the filter resonance for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_resonance(value)

    @mcp.tool()
    def set_multimode_filter_type(value: int, track: int):
        """
        Set the type of the multi-mode filter.

        Args:
            value (int): Filter type value ranging from 0 to 127.
                - 0   = Lowpass
                - 64  = EQ
                - 127 = Highpass
                Values between these points represent transitions between filter types.
                Display range: continuous.
                Default is 0 (Lowpass).
            track (int): The track number to set the filter type for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_type(value)

    @mcp.tool()
    def set_multimode_filter_envelope_depth(value: int, track: int):
        """
        Set the envelope depth of the multi-mode filter.

        Args:
            value (int): Envelope depth value ranging from 0 to 127.
                - 0 maps to -64
                - 64 maps to 0
                - 127 maps to +64
                Values in between are linearly mapped.
                Display range: -64 to +64.
                Default is 0.
            track (int): The track number to set the filter envelope depth for. 1-16
        """
        return MultiModeFilterController(
            digitone_config.multi_mode_filter.parameters, midi, track
        ).set_envelope_depth(value)
