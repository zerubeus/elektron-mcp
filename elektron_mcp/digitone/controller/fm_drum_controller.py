from elektron_mcp.digitone.models.models import ParameterGroup
from elektron_mcp.midi.digitone_midi import DigitoneMIDI
from elektron_mcp.digitone.controller.base_synth_controller import BaseSynthController


class FMDrumController(BaseSynthController):
    """Controller for FM Drum parameters."""

    def __init__(
        self,
        fmdrum_config: dict[str, ParameterGroup],
        digitone_midi: DigitoneMIDI,
        midi_channel: int,
    ):
        super().__init__(fmdrum_config, digitone_midi, midi_channel)

    # Basic FM Parameters
    def set_tune(self, value: int) -> bool:
        """Set the tune/pitch of the drum."""
        return self.set_parameter("page_1", "tune", value)

    def set_stimulus(self, value: int) -> bool:
        """Set the stimulus amount."""
        return self.set_parameter("page_1", "stim", value)

    def set_stimulus_depth(self, value: int) -> bool:
        """Set the stimulus depth."""
        return self.set_parameter("page_1", "sdep", value)

    def set_algorithm(self, value: int) -> bool:
        """Set the FM algorithm (1-7)."""
        return self.set_parameter("page_1", "algo", value)

    def set_operator_c(self, value: int) -> bool:
        """Set the level of operator C."""
        return self.set_parameter("page_1", "OP.C", value)

    def set_operator_ab(self, value: int) -> bool:
        """Set the level of operators A and B."""
        return self.set_parameter("page_1", "OP.AB", value)

    def set_feedback(self, value: int) -> bool:
        """Set the feedback amount."""
        return self.set_parameter("page_1", "FDBK", value)

    def set_fold(self, value: int) -> bool:
        """Set the fold amount."""
        return self.set_parameter("page_1", "FOLD", value)

    # Operator 1 Parameters
    def set_ratio1(self, value: int) -> bool:
        """Set the frequency ratio of operator 1."""
        return self.set_parameter("page_2", "RATIO1", value)

    def set_decay1(self, value: int) -> bool:
        """Set the decay of operator 1."""
        return self.set_parameter("page_2", "DEC1", value)

    def set_end_level1(self, value: int) -> bool:
        """Set the end level of operator 1."""
        return self.set_parameter("page_2", "END1", value)

    def set_modulation1(self, value: int) -> bool:
        """Set the modulation amount of operator 1."""
        return self.set_parameter("page_2", "MOD1", value)

    # Operator 2 Parameters
    def set_ratio2(self, value: int) -> bool:
        """Set the frequency ratio of operator 2."""
        return self.set_parameter("page_2", "RATIO2", value)

    def set_decay2(self, value: int) -> bool:
        """Set the decay of operator 2."""
        return self.set_parameter("page_2", "DEC2", value)

    def set_end_level2(self, value: int) -> bool:
        """Set the end level of operator 2."""
        return self.set_parameter("page_2", "END2", value)

    def set_modulation2(self, value: int) -> bool:
        """Set the modulation amount of operator 2."""
        return self.set_parameter("page_2", "MOD2", value)

    # Envelope Parameters
    def set_hold(self, value: int) -> bool:
        """Set the hold time of the envelope."""
        return self.set_parameter("page_3", "HOLD", value)

    def set_decay(self, value: int) -> bool:
        """Set the decay time of the envelope."""
        return self.set_parameter("page_3", "DEC", value)

    def set_phase_c(self, value: int) -> bool:
        """Set the phase of operator C."""
        return self.set_parameter("page_3", "PH.C", value)

    def set_level(self, value: int) -> bool:
        """Set the output level."""
        return self.set_parameter("page_3", "LEV", value)

    def set_noise_reset(self, value: int) -> bool:
        """Set the noise reset mode (0=off, 1=on)."""
        return self.set_parameter("page_3", "NRST", value)

    def set_noise_mode(self, value: int) -> bool:
        """Set the noise mode (0=off, 1=on)."""
        return self.set_parameter("page_3", "NRM", value)

    # Noise Parameters
    def set_noise_hold(self, value: int) -> bool:
        """Set the noise hold time."""
        return self.set_parameter("page_4", "NHLD", value)

    def set_noise_decay(self, value: int) -> bool:
        """Set the noise decay time."""
        return self.set_parameter("page_4", "NDEC", value)

    def set_transient(self, value: int) -> bool:
        """Set the transient amount."""
        return self.set_parameter("page_4", "TRAN", value)

    def set_transient_level(self, value: int) -> bool:
        """Set the transient level."""
        return self.set_parameter("page_4", "TLEV", value)

    def set_noise_base(self, value: int) -> bool:
        """Set the noise base frequency."""
        return self.set_parameter("page_4", "BASE", value)

    def set_noise_width(self, value: int) -> bool:
        """Set the noise width."""
        return self.set_parameter("page_4", "WDTH", value)

    def set_granularity(self, value: int) -> bool:
        """Set the noise granularity."""
        return self.set_parameter("page_4", "GRAN", value)

    def set_noise_level(self, value: int) -> bool:
        """Set the noise level."""
        return self.set_parameter("page_4", "NLEV", value)
