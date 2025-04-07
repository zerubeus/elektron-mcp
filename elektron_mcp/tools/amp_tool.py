"""
Amp tools for controlling amplitude and envelope parameters on the Digitone.
"""

from elektron_mcp.digitone.services.amp_fx_controller import AmpController
from elektron_mcp.digitone.config.config import digitone_config


def register_amp_tools(mcp, midi):
    """
    Register all amp tools with the MCP server.

    Args:
        mcp: The MCP server instance
        midi: The MIDI interface
    """

    @mcp.tool()
    def set_amp_attack(value: int, track: int):
        """
        Set the attack time of the amplitude envelope.

        Args:
            value (int): Attack time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 8.
            track (int): The track number to set the amp attack for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_attack(value)

    @mcp.tool()
    def set_amp_hold(value: int, track: int):
        """
        Set the hold time of the amplitude envelope.

        Args:
            value (int): Hold time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 127.
            track (int): The track number to set the amp hold for. 1-16
        """
        return AmpController(digitone_config.amp_page.parameters, midi, track).set_hold(
            value
        )

    @mcp.tool()
    def set_amp_decay(value: int, track: int):
        """
        Set the decay time of the amplitude envelope.

        Args:
            value (int): Decay time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 32.
            track (int): The track number to set the amp decay for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_decay(value)

    @mcp.tool()
    def set_amp_sustain(value: int, track: int):
        """
        Set the sustain level of the amplitude envelope.

        Args:
            value (int): Sustain level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 96.
            track (int): The track number to set the amp sustain for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_sustain(value)

    @mcp.tool()
    def set_amp_release(value: int, track: int):
        """
        Set the release time of the amplitude envelope.

        Args:
            value (int): Release time value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 24.
            track (int): The track number to set the amp release for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_release(value)

    @mcp.tool()
    def set_amp_envelope_reset(value: int, track: int):
        """
        Set the envelope reset mode.

        Args:
            value (int): Envelope reset mode value ranging from 0 to 1.
                - 0 = "off"
                - 1 = "on"
                Display range: discrete options.
                Default is "on" (1).
            track (int): The track number to set the amp envelope reset for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_envelope_reset(value)

    @mcp.tool()
    def set_amp_envelope_mode(value: int, track: int):
        """
        Set the envelope mode.

        Args:
            value (int): Envelope mode value ranging from 0 to 1.
                - 0 = "AHD"
                - 1 = "ADSR"
                Display range: discrete options.
                Default is "ADSR" (1).
            track (int): The track number to set the amp envelope mode for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_envelope_mode(value)

    @mcp.tool()
    def set_amp_pan(value: int, track: int):
        """
        Set the stereo panning position.

        Args:
            value (int): Pan position value ranging from 0 to 127.
                - 0 maps to -64
                - 64 maps to 0
                - 127 maps to +64
                Values in between are linearly mapped.
                Display range: -64 to +64.
                Default is 0 (center).
            track (int): The track number to set the amp pan for. 1-16
        """
        return AmpController(digitone_config.amp_page.parameters, midi, track).set_pan(
            value
        )

    @mcp.tool()
    def set_amp_volume(value: int, track: int):
        """
        Set the overall volume level.

        Args:
            value (int): Volume level value ranging from 0 to 127.
                - 0 maps to 0
                - 127 maps to 127
                Display range: 0-127.
                Default is 110.
            track (int): The track number to set the amp volume for. 1-16
        """
        return AmpController(
            digitone_config.amp_page.parameters, midi, track
        ).set_volume(value)
