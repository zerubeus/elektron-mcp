from elektron_mcp.digitone.services.base_synth_controller import BaseSynthController


class AmpController(BaseSynthController):
    """Controller for Amplitude/Volume parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the amplitude envelope."""
        return self.set_direct_parameter("ATK", value)

    def set_hold(self, value: int) -> bool:
        """Set the hold time of the amplitude envelope."""
        return self.set_direct_parameter("HOLD", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the amplitude envelope."""
        return self.set_direct_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the amplitude envelope."""
        return self.set_direct_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the amplitude envelope."""
        return self.set_direct_parameter("REL", value)

    def set_envelope_reset(self, value: int) -> bool:
        """Set envelope reset mode (0=off, 1=on)."""
        return self.set_direct_parameter("Env. RSET", value)

    def set_envelope_mode(self, value: int) -> bool:
        """Set envelope mode (0=AHD, 1=ADSR)."""
        return self.set_direct_parameter("MODE", value)

    def set_pan(self, value: int) -> bool:
        """Set the stereo panning position (-64 to +64)."""
        return self.set_direct_parameter("PAN", value)

    def set_volume(self, value: int) -> bool:
        """Set the overall volume level (0-127)."""
        return self.set_direct_parameter("VOL", value)


class FXController(BaseSynthController):
    """Controller for Effects parameters."""

    def set_bit_reduction(self, value: int) -> bool:
        """Set the bit reduction amount (0-127)."""
        return self.set_direct_parameter("BR", value)

    def set_overdrive(self, value: int) -> bool:
        """Set the overdrive amount (0-127)."""
        return self.set_direct_parameter("OVER", value)

    def set_sample_rate_reduction(self, value: int) -> bool:
        """Set the sample rate reduction amount (0-127)."""
        return self.set_direct_parameter("SRR", value)

    def set_sample_rate_routing(self, value: int) -> bool:
        """Set sample rate reduction routing (0=pre, 1=post)."""
        return self.set_direct_parameter("SR.RT(pre/post)", value)

    def set_overdrive_routing(self, value: int) -> bool:
        """Set overdrive routing (0=pre, 1=post)."""
        return self.set_direct_parameter("OD.RT(pre/post)", value)

    def set_delay(self, value: int) -> bool:
        """Set the delay send amount (0-127)."""
        return self.set_direct_parameter("DEL", value)

    def set_reverb(self, value: int) -> bool:
        """Set the reverb send amount (0-127)."""
        return self.set_direct_parameter("REV", value)

    def set_chorus(self, value: int) -> bool:
        """Set the chorus send amount (0-127)."""
        return self.set_direct_parameter("CHR", value)
