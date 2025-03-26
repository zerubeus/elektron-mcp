from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController


class FMToneController(BaseSynthController):
    """Controller for FM Tone parameters."""

    # Algorithm and operator parameters (page 1)
    def set_algorithm(self, value: int) -> bool:
        """Set the FM algorithm (1-8)."""
        return self.set_parameter("page_1", "ALGO", value)

    def set_operator_c_ratio(self, value: int) -> bool:
        """Set the ratio of operator C (0.25-16)."""
        return self.set_parameter("page_1", "C", value)

    def set_operator_a_ratio(self, value: int) -> bool:
        """Set the ratio of operator A (0.25-16)."""
        return self.set_parameter("page_1", "A", value)

    def set_operator_b_ratio(self, value: int) -> bool:
        """Set the ratio of operator B (0.25-16 for both B1 and B2)."""
        return self.set_parameter("page_1", "B", value)

    def set_harmony(self, value: int) -> bool:
        """Set the harmony offset (-26 to +26)."""
        return self.set_parameter("page_1", "HARM", value)

    def set_detune(self, value: int) -> bool:
        """Set the detune amount (0-127)."""
        return self.set_parameter("page_1", "DTUN", value)

    def set_feedback(self, value: int) -> bool:
        """Set the feedback amount (0-127)."""
        return self.set_parameter("page_1", "FDBK", value)

    def set_mix(self, value: int) -> bool:
        """Set the mix level between operators (-63 to +63)."""
        return self.set_parameter("page_1", "MIX", value)

    # Operator A envelope parameters (page 2)
    def set_operator_a_attack(self, value: int) -> bool:
        """Set the attack time of operator A."""
        return self.set_parameter("page_2", "A.atk", value)

    def set_operator_a_decay(self, value: int) -> bool:
        """Set the decay time of operator A."""
        return self.set_parameter("page_2", "A.dec", value)

    def set_operator_a_end_level(self, value: int) -> bool:
        """Set the end level of operator A."""
        return self.set_parameter("page_2", "A.end", value)

    def set_operator_a_level(self, value: int) -> bool:
        """Set the level of operator A."""
        return self.set_parameter("page_2", "A.lev", value)

    # Operator B envelope parameters (page 2)
    def set_operator_b_attack(self, value: int) -> bool:
        """Set the attack time of operator B."""
        return self.set_parameter("page_2", "B.atk", value)

    def set_operator_b_decay(self, value: int) -> bool:
        """Set the decay time of operator B."""
        return self.set_parameter("page_2", "B.dec", value)

    def set_operator_b_end_level(self, value: int) -> bool:
        """Set the end level of operator B."""
        return self.set_parameter("page_2", "B.end", value)

    def set_operator_b_level(self, value: int) -> bool:
        """Set the level of operator B."""
        return self.set_parameter("page_2", "B.lev", value)

    # Modulation parameters (page 3)
    def set_operator_a_delay(self, value: int) -> bool:
        """Set the delay time for operator A."""
        return self.set_parameter("page_3", "ADEL", value)

    def set_operator_a_trigger(self, value: int) -> bool:
        """Set the trigger mode for operator A (0=off, 1=on)."""
        return self.set_parameter("page_3", "ATRG", value)

    def set_operator_a_reset(self, value: int) -> bool:
        """Set the reset mode for operator A (0=off, 1=on)."""
        return self.set_parameter("page_3", "ARST", value)

    def set_phase_retrigger(self, value: int) -> bool:
        """
        Set the phase retrigger mode.
        0=off, 1=all, 2=c, 3=a+b, 4=a+b2
        """
        return self.set_parameter("page_3", "PHRT", value)

    def set_operator_b_delay(self, value: int) -> bool:
        """Set the delay time for operator B."""
        return self.set_parameter("page_3", "BDEL", value)

    def set_operator_b_trigger(self, value: int) -> bool:
        """Set the trigger mode for operator B (0=off, 1=on)."""
        return self.set_parameter("page_3", "BTRG", value)

    def set_operator_b_reset(self, value: int) -> bool:
        """Set the reset mode for operator B (0=off, 1=on)."""
        return self.set_parameter("page_3", "BRST", value)

    # Ratio offset and key tracking parameters (page 4)
    def set_operator_c_ratio_offset(self, value: int) -> bool:
        """Set the ratio offset for operator C (-1.00 to +0.999)."""
        return self.set_parameter("page_4", "Ratio_Offset.C", value)

    def set_operator_a_ratio_offset(self, value: int) -> bool:
        """Set the ratio offset for operator A (-1.00 to +0.999)."""
        return self.set_parameter("page_4", "Ratio_Offset.A", value)

    def set_operator_b1_ratio_offset(self, value: int) -> bool:
        """Set the ratio offset for operator B1 (-1.00 to +0.999)."""
        return self.set_parameter("page_4", "Ratio_Offset.B1", value)

    def set_operator_b2_ratio_offset(self, value: int) -> bool:
        """Set the ratio offset for operator B2 (-1.00 to +0.999)."""
        return self.set_parameter("page_4", "Ratio_Offset.B2", value)

    def set_operator_a_key_tracking(self, value: int) -> bool:
        """Set the key tracking for operator A (0-127)."""
        return self.set_parameter("page_4", "Key_Track.A", value)

    def set_operator_b1_key_tracking(self, value: int) -> bool:
        """Set the key tracking for operator B1 (0-127)."""
        return self.set_parameter("page_4", "Key_Track.B1", value)

    def set_operator_b2_key_tracking(self, value: int) -> bool:
        """Set the key tracking for operator B2 (0-127)."""
        return self.set_parameter("page_4", "Key_Track.B2", value)
