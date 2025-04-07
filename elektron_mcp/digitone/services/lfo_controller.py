from elektron_mcp.digitone.services.base_synth_controller import BaseSynthController


class LFO1Controller(BaseSynthController):
    """Controller for LFO1 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO1."""
        return self.set_direct_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO1."""
        return self.set_direct_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO1."""
        return self.set_direct_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO1."""
        return self.set_direct_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO1."""
        return self.set_direct_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO1."""
        return self.set_direct_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO1."""
        return self.set_direct_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO1."""
        return self.set_direct_parameter("DEP", value)


class LFO2Controller(BaseSynthController):
    """Controller for LFO2 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO2."""
        return self.set_direct_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO2."""
        return self.set_direct_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO2."""
        return self.set_direct_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO2."""
        return self.set_direct_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO2."""
        return self.set_direct_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO2."""
        return self.set_direct_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO2."""
        return self.set_direct_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO2."""
        return self.set_direct_parameter("DEP", value)


class LFO3Controller(BaseSynthController):
    """Controller for LFO3 parameters."""

    def set_speed(self, value: int) -> bool:
        """Set the speed of LFO3."""
        return self.set_direct_parameter("SPD", value)

    def set_multiplier(self, value: int) -> bool:
        """Set the multiplier of LFO3."""
        return self.set_direct_parameter("MULT", value)

    def set_fade(self, value: int) -> bool:
        """Set the fade in/out of LFO3."""
        return self.set_direct_parameter("FADE", value)

    def set_destination(self, value: int) -> bool:
        """Set the destination of LFO3."""
        return self.set_direct_parameter("DEST", value)

    def set_waveform(self, value: int) -> bool:
        """Set the waveform of LFO3."""
        return self.set_direct_parameter("WAVE", value)

    def set_start_phase(self, value: int) -> bool:
        """Set the start phase of LFO3."""
        return self.set_direct_parameter("SPH", value)

    def set_trigger_mode(self, value: int) -> bool:
        """Set the trigger mode of LFO3."""
        return self.set_direct_parameter("MODE", value)

    def set_depth(self, value: int) -> bool:
        """Set the depth of LFO3."""
        return self.set_direct_parameter("DEP", value)
