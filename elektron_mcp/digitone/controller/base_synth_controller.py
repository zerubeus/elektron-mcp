from elektron_mcp.digitone.models.models import ParameterGroup
from elektron_mcp.midi.digitone_midi import DigitoneMIDI


class BaseSynthController:
    """Base class for synth parameter controllers."""

    def __init__(
        self,
        config: dict[str, ParameterGroup],
        digitone_midi: DigitoneMIDI,
        midi_channel: int,
    ):
        self.config = config
        self.digitone_midi = digitone_midi
        self.midi_channel = midi_channel

    def set_parameter(self, page: str, param_name: str, value: int) -> bool:
        """
        Generic method to set any synth parameter.

        Args:
            page: The parameter page (e.g., 'page_1', 'page_2', etc.)
            param_name: The parameter name
            value: The value to set (0-127)

        Returns:
            bool: True if successful, False if failed

        Raises:
            ValueError: If the page or parameter doesn't exist
        """
        if page not in self.config:
            raise ValueError(f"Invalid page: {page}")

        if param_name not in self.config[page].parameters:
            raise ValueError(f"Invalid parameter: {param_name} on {page}")

        param = self.config[page].parameters[param_name]

        # Convert cc_msb to int before sending
        cc_msb = int(param.midi.cc_msb)

        result = self.digitone_midi.send_cc(
            self.midi_channel,
            cc_msb,
            value,
        )

        if result is None:
            raise Exception(f"Failed to set {param_name} on {page}")

        return result
