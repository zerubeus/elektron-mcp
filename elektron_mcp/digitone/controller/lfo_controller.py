from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController
import logging

logger = logging.getLogger(__name__)


class BaseLFOController(BaseSynthController):
    """Base controller for LFO parameters."""

    def set_lfo_parameter(self, param_name: str, value: int) -> bool:
        """
        Set an LFO parameter value using the improved base controller method.

        Args:
            param_name: The LFO parameter name
            value: The value to set (0-127)

        Returns:
            bool: True if successful, False if failed

        Raises:
            ValueError: If the parameter doesn't exist
        """
        # Use the direct parameter access in the base class
        return self.set_direct_parameter(param_name, value)


class LFO1Controller(BaseLFOController):
    """Controller for LFO1 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO1."""
        return self.set_lfo_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO1."""
        return self.set_lfo_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO1."""
        return self.set_lfo_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO1."""
        return self.set_lfo_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO1."""
        return self.set_lfo_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO1."""
        return self.set_lfo_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO1."""
        return self.set_lfo_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO1."""
        return self.set_lfo_parameter("DEP", value)


class LFO2Controller(BaseLFOController):
    """Controller for LFO2 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO2."""
        return self.set_lfo_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO2."""
        return self.set_lfo_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO2."""
        return self.set_lfo_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO2."""
        return self.set_lfo_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO2."""
        return self.set_lfo_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO2."""
        return self.set_lfo_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO2."""
        return self.set_lfo_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO2."""
        return self.set_lfo_parameter("DEP", value)


class LFO3Controller(BaseLFOController):
    """Controller for LFO3 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO3."""
        return self.set_lfo_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO3."""
        return self.set_lfo_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO3."""
        return self.set_lfo_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO3."""
        return self.set_lfo_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO3."""
        return self.set_lfo_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO3."""
        return self.set_lfo_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO3."""
        return self.set_lfo_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO3."""
        return self.set_lfo_parameter("DEP", value)
