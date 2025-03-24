from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController


class BasePageController(BaseSynthController):
    """Base controller for single-page parameter sets."""

    def set_page_parameter(self, param_name: str, value: int) -> bool:
        """
        Set a parameter value on a single page.

        Args:
            param_name: The parameter name
            value: The value to set (0-127)

        Returns:
            bool: True if successful, False if failed

        Raises:
            ValueError: If the parameter doesn't exist
        """
        if param_name not in self.config:
            raise ValueError(f"Invalid parameter: {param_name}")

        param = self.config[param_name]

        result = self.digitone_midi.send_cc(
            self.midi_channel,
            int(param.midi.cc_msb),
            value,
        )

        if result is None:
            raise Exception(f"Failed to set {param_name}")

        return result


class AmpController(BasePageController):
    """Controller for Amplitude/Volume parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the amplitude envelope."""
        return self.set_page_parameter("ATK", value)

    def set_hold(self, value: int) -> bool:
        """Set the hold time of the amplitude envelope."""
        return self.set_page_parameter("HOLD", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the amplitude envelope."""
        return self.set_page_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the amplitude envelope."""
        return self.set_page_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the amplitude envelope."""
        return self.set_page_parameter("REL", value)

    def set_envelope_reset(self, value: int) -> bool:
        """Set envelope reset mode (0=off, 1=on)."""
        return self.set_page_parameter("Env. RSET", value)

    def set_envelope_mode(self, value: int) -> bool:
        """Set envelope mode (0=AHD, 1=ADSR)."""
        return self.set_page_parameter("MODE", value)

    def set_pan(self, value: int) -> bool:
        """Set the stereo panning position (-64 to +64)."""
        return self.set_page_parameter("PAN", value)

    def set_volume(self, value: int) -> bool:
        """Set the overall volume level (0-127)."""
        return self.set_page_parameter("VOL", value)


class FXController(BasePageController):
    """Controller for Effects parameters."""

    def set_bit_reduction(self, value: int) -> bool:
        """Set the bit reduction amount (0-127)."""
        return self.set_page_parameter("BR", value)

    def set_overdrive(self, value: int) -> bool:
        """Set the overdrive amount (0-127)."""
        return self.set_page_parameter("OVER", value)

    def set_sample_rate_reduction(self, value: int) -> bool:
        """Set the sample rate reduction amount (0-127)."""
        return self.set_page_parameter("SRR", value)

    def set_sample_rate_routing(self, value: int) -> bool:
        """Set sample rate reduction routing (0=pre, 1=post)."""
        return self.set_page_parameter("SR.RT(pre/post)", value)

    def set_overdrive_routing(self, value: int) -> bool:
        """Set overdrive routing (0=pre, 1=post)."""
        return self.set_page_parameter("OD.RT(pre/post)", value)

    def set_delay(self, value: int) -> bool:
        """Set the delay send amount (0-127)."""
        return self.set_page_parameter("DEL", value)

    def set_reverb(self, value: int) -> bool:
        """Set the reverb send amount (0-127)."""
        return self.set_page_parameter("REV", value)

    def set_chorus(self, value: int) -> bool:
        """Set the chorus send amount (0-127)."""
        return self.set_page_parameter("CHR", value)
