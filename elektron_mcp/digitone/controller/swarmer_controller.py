from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController


class SwarmerController(BaseSynthController):
    """Controller for Swarmer parameters."""

    def set_tune(self, value: int) -> bool:
        """Set the tuning of the swarmer."""
        return self.set_parameter("page_1", "TUNE", value)

    def set_swarm(self, value: int) -> bool:
        """Set the swarm amount (number of unison voices)."""
        return self.set_parameter("page_1", "SWRM", value)

    def set_detune(self, value: int) -> bool:
        """Set the detune amount between voices."""
        return self.set_parameter("page_1", "DET", value)

    def set_mix(self, value: int) -> bool:
        """Set the mix level between dry and swarmed signal."""
        return self.set_parameter("page_1", "MIX", value)

    def set_main_octave(self, value: int) -> bool:
        """Set the main octave transposition (0=normal, 1=+1 octave, 2=+2 octaves)."""
        return self.set_parameter("page_1", "M.OCT", value)

    def set_main_waveform(self, value: int) -> bool:
        """Set the main oscillator waveform."""
        return self.set_parameter("page_1", "MAIN", value)

    def set_animation(self, value: int) -> bool:
        """Set the animation/movement amount of the swarm."""
        return self.set_parameter("page_1", "ANIM", value)

    def set_noise_modulation(self, value: int) -> bool:
        """Set the amount of noise modulation applied to the swarm."""
        return self.set_parameter("page_1", "N.MOD", value)
