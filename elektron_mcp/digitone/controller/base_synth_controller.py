from elektron_mcp.digitone.models.models import ParameterGroup
from elektron_mcp.midi.digitone_midi import DigitoneMIDI
import logging

logger = logging.getLogger(__name__)


class BaseSynthController:
    """Base controller for Digitone parameters."""

    def __init__(
        self,
        config: dict[str, ParameterGroup],
        digitone_midi: DigitoneMIDI,
        midi_channel: int,
    ):
        """
        Initialize the controller.

        Args:
            config: A dictionary mapping parameter names/pages to ParameterGroup objects.
            digitone_midi: The DigitoneMIDI interface for sending MIDI messages.
            midi_channel: The MIDI channel to use (1-16).
        """
        self.config = config
        self.digitone_midi = digitone_midi
        self.midi_channel = midi_channel

    def set_parameter(self, page: str, param_name: str, value: int) -> bool:
        """
        Set a page-based parameter via CC (original method for backward compatibility).

        Args:
            page: Parameter page key in config (e.g. 'page_1', 'page_2').
            param_name: The name of the parameter to set.
            value: The CC value to send (0-127).

        Returns:
            True if successful, False otherwise.

        Raises:
            ValueError: If page or param_name is invalid.
            Exception: If sending CC fails.
        """
        if page not in self.config:
            raise ValueError(f"Invalid page: {page}")
        if param_name not in self.config[page].parameters:
            raise ValueError(f"Invalid parameter: {param_name} on {page}")

        param = self.config[page].parameters[param_name]
        cc_msb = int(param.midi.cc_msb)

        result = self.digitone_midi.send_cc(self.midi_channel, cc_msb, value)

        if result is None:
            raise Exception(f"Failed to set {param_name} on {page}")
        return result

    def set_parameter_nrpn(self, page: str, param_name: str, value: int) -> bool:
        """
        Set a page-based parameter using NRPN first, then fall back to CC if NRPN fails.

        Args:
            page: Parameter page key in config (e.g. 'page_1', 'page_2').
            param_name: The name of the parameter to set.
            value: The value to send (0-127).

        Returns:
            True if successful, False otherwise.

        Raises:
            ValueError: If page or param_name is invalid.
            Exception: If neither NRPN nor CC succeeds.
        """
        if page not in self.config:
            raise ValueError(f"Invalid page: {page}")
        if param_name not in self.config[page].parameters:
            raise ValueError(f"Invalid parameter: {param_name} on {page}")

        param = self.config[page].parameters[param_name]

        # Attempt NRPN if mappings exist
        try:
            if hasattr(param.midi, "nrpn_msb") and hasattr(param.midi, "nrpn_lsb"):
                result = self.digitone_midi.send_nrpn(
                    self.midi_channel,
                    param.midi.nrpn_msb,
                    param.midi.nrpn_lsb,
                    value,
                )
                if result:
                    logger.debug(f"Set {param_name} on {page} to {value} using NRPN")
                    return result
            logger.debug(
                f"No NRPN mapping for {param_name} on {page}, or NRPN failed. Trying CC..."
            )
        except Exception as e:
            logger.warning(f"NRPN failed for {param_name} on {page}: {e}. Trying CC...")

        # Fall back to CC
        try:
            if not param.midi.cc_msb:
                logger.error(f"No CC MSB defined for {param_name} on {page}")
                return False

            cc_msb = int(param.midi.cc_msb)
            result = self.digitone_midi.send_cc(self.midi_channel, cc_msb, value)
            if result:
                logger.debug(f"Set {param_name} on {page} to {value} using CC")
                return True

            logger.error(f"Failed to set {param_name} on {page} using CC")
            return False

        except Exception as e:
            logger.error(f"Failed to set {param_name} on {page}: {e}")
            raise Exception(f"Failed to set {param_name} on {page}") from e

    def set_direct_parameter_nrpn(self, param_name: str, value: int) -> bool:
        """
        Directly set a non-page-based parameter using NRPN.

        Args:
            param_name: Parameter name in config.
            value: The value to send (0-127).

        Returns:
            True if successful, False otherwise.

        Raises:
            ValueError: If the parameter is not in config.
            Exception: If sending NRPN fails.
        """
        if param_name not in self.config:
            raise ValueError(f"Invalid parameter: {param_name}")

        param = self.config[param_name]
        result = self.digitone_midi.send_nrpn(
            self.midi_channel,
            param.midi.nrpn_msb,
            param.midi.nrpn_lsb,
            value,
        )
        if result is None:
            raise Exception(f"Failed to set {param_name}")
        return result

    def set_direct_parameter(self, param_name: str, value: int) -> bool:
        """
        Directly set a non-page-based parameter using CC.

        Args:
            param_name: Parameter name in config.
            value: The value to send (0-127).

        Returns:
            True if successful, False otherwise.

        Raises:
            ValueError: If the parameter is not in config.
            Exception: If sending CC fails.
        """
        if param_name not in self.config:
            raise ValueError(f"Invalid parameter: {param_name}")

        param = self.config[param_name]
        try:
            if not param.midi.cc_msb:
                logger.error(f"No CC MSB defined for {param_name}")
                return False

            cc_msb = int(param.midi.cc_msb)
            result = self.digitone_midi.send_cc(self.midi_channel, cc_msb, value)
            if result:
                logger.debug(f"Set {param_name} to {value} using CC")
                return True

            logger.error(f"Failed to set {param_name} using CC")
            return False

        except Exception as e:
            logger.error(f"Failed to set {param_name}: {e}")
            raise Exception(f"Failed to set {param_name}") from e
