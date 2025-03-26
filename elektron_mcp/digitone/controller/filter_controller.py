from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController
import logging

logger = logging.getLogger(__name__)


class BaseFilterController(BaseSynthController):
    """Base controller for filter parameters."""

    def set_filter_parameter(self, param_name: str, value: int) -> bool:
        """
        Set a filter parameter value using the improved base controller method.

        Args:
            param_name: The filter parameter name
            value: The value to set (0-127)

        Returns:
            bool: True if successful, False if failed

        Raises:
            ValueError: If the parameter doesn't exist
        """
        # Use the direct parameter access in the base class
        return self.set_direct_parameter(param_name, value)


class MultiModeFilterController(BaseFilterController):
    """Controller for Multi-Mode Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the cutoff frequency of the filter."""
        return self.set_filter_parameter("FREQ", value)

    def set_resonance(self, value: int) -> bool:
        """Set the resonance of the filter."""
        return self.set_filter_parameter("RESO", value)

    def set_type(self, value: int) -> bool:
        """Set the filter type."""
        return self.set_filter_parameter("TYPE", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)


class Lowpass4FilterController(BaseFilterController):
    """Controller for Lowpass 4 Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the cutoff frequency of the filter."""
        return self.set_filter_parameter("FREQ", value)

    def set_resonance(self, value: int) -> bool:
        """Set the resonance of the filter."""
        return self.set_filter_parameter("RESO", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)


class EqualizerFilterController(BaseFilterController):
    """Controller for Equalizer Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the center frequency of the equalizer."""
        return self.set_filter_parameter("FREQ", value)

    def set_gain(self, value: int) -> bool:
        """Set the gain of the equalizer."""
        return self.set_filter_parameter("GAIN", value)

    def set_q(self, value: int) -> bool:
        """Set the Q factor (bandwidth) of the equalizer."""
        return self.set_filter_parameter("Q", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the center frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)


class BaseWidthFilterController(BaseFilterController):
    """Controller for Base-Width Filter parameters."""

    def set_envelope_delay(self, value: int) -> bool:
        """Set the envelope delay."""
        return self.set_filter_parameter("ENV.Delay", value)

    def set_key_tracking(self, value: int) -> bool:
        """Set the key tracking amount."""
        return self.set_filter_parameter("KEY.Tracking", value)

    def set_base(self, value: int) -> bool:
        """Set the base frequency."""
        return self.set_filter_parameter("BASE", value)

    def set_width(self, value: int) -> bool:
        """Set the width."""
        return self.set_filter_parameter("WDTH", value)

    def set_envelope_reset(self, value: int) -> bool:
        """Set the envelope reset mode (0=off, 1=on)."""
        return self.set_filter_parameter("Env Reset", value)


class LegacyLpHpFilterController(BaseFilterController):
    """Controller for Legacy LP/HP Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the cutoff frequency of the filter."""
        return self.set_filter_parameter("FREQ", value)

    def set_resonance(self, value: int) -> bool:
        """Set the resonance of the filter."""
        return self.set_filter_parameter("RESO", value)

    def set_type(self, value: int) -> bool:
        """Set the filter type (0=lowpass, 1=highpass, 2=off)."""
        return self.set_filter_parameter("TYPE(lowpass/highpass)", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the cutoff frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)


class CombMinusFilterController(BaseFilterController):
    """Controller for Comb- Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the frequency of the comb filter."""
        return self.set_filter_parameter("FREQ", value)

    def set_feedback(self, value: int) -> bool:
        """Set the feedback amount of the comb filter."""
        return self.set_filter_parameter("FDBK", value)

    def set_lowpass(self, value: int) -> bool:
        """Set the lowpass filter amount in the feedback path."""
        return self.set_filter_parameter("LPF", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)


class CombPlusFilterController(BaseFilterController):
    """Controller for Comb+ Filter parameters."""

    def set_attack(self, value: int) -> bool:
        """Set the attack time of the filter envelope."""
        return self.set_filter_parameter("ATK", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the filter envelope."""
        return self.set_filter_parameter("DEC", value)

    def set_sustain(self, value: int) -> bool:
        """Set the sustain level of the filter envelope."""
        return self.set_filter_parameter("SUS", value)

    def set_release(self, value: int) -> bool:
        """Set the release time of the filter envelope."""
        return self.set_filter_parameter("REL", value)

    def set_frequency(self, value: int) -> bool:
        """Set the frequency of the comb filter."""
        return self.set_filter_parameter("FREQ", value)

    def set_feedback(self, value: int) -> bool:
        """Set the feedback amount of the comb filter."""
        return self.set_filter_parameter("FDBK", value)

    def set_lowpass(self, value: int) -> bool:
        """Set the lowpass filter amount in the feedback path."""
        return self.set_filter_parameter("LPF", value)

    def set_envelope_depth(self, value: int) -> bool:
        """Set the envelope depth (how much the envelope affects the frequency)."""
        return self.set_filter_parameter("ENV.Depth", value)
