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
        """Initialize the controller.

        Args:
            config: Dictionary of parameter configurations
            digitone_midi: The MIDI interface
            midi_channel: MIDI channel to use (1-16)
        """
        self.config = config
        self.digitone_midi = digitone_midi
        self.midi_channel = midi_channel

    def set_parameter(self, page: str, param_name: str, value: int) -> bool:
        """
        Set a parameter value for page-based parameters.
        This is the original method to maintain backward compatibility.

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

        # Convert cc_msb to int before sending - use CC by default for backward compatibility
        cc_msb = int(param.midi.cc_msb)

        result = self.digitone_midi.send_cc(
            self.midi_channel,
            cc_msb,
            value,
        )

        if result is None:
            raise Exception(f"Failed to set {param_name} on {page}")

        return result

    def set_parameter_nrpn(self, page: str, param_name: str, value: int) -> bool:
        """
        Set a parameter value using NRPN with fallback to CC.
        This is a new method that tries NRPN first, then falls back to CC.

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

        # Try NRPN first
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
            else:
                logger.debug(f"No NRPN mapping for {param_name} on {page}, trying CC")

        except Exception as e:
            logger.warning(
                f"NRPN method failed for {param_name} on {page}: {e}. Trying CC method."
            )

        # Fall back to CC
        try:
            if not param.midi.cc_msb:
                logger.error(f"No CC MSB defined for {param_name} on {page}")
                return False

            # Convert cc_msb to int before sending
            cc_msb = int(param.midi.cc_msb)

            result = self.digitone_midi.send_cc(
                self.midi_channel,
                cc_msb,
                value,
            )

            if result:
                logger.debug(f"Set {param_name} on {page} to {value} using CC")
                return result
            else:
                logger.error(f"Failed to set {param_name} on {page} using CC")
                return False

        except Exception as e:
            logger.error(f"Failed to set {param_name} on {page}: {e}")
            raise Exception(f"Failed to set {param_name} on {page}") from e

    def set_direct_parameter(self, param_name: str, value: int) -> bool:
        """
        Set a parameter value directly (non-page-based) using NRPN with fallback to CC.

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

        # Try NRPN first
        try:
            if hasattr(param.midi, "nrpn_msb") and hasattr(param.midi, "nrpn_lsb"):
                result = self.digitone_midi.send_nrpn(
                    self.midi_channel,
                    param.midi.nrpn_msb,
                    param.midi.nrpn_lsb,
                    value,
                )

                if result:
                    logger.debug(f"Set {param_name} to {value} using NRPN")
                    return result
            else:
                logger.debug(f"No NRPN mapping for {param_name}, trying CC")

        except Exception as e:
            logger.warning(
                f"NRPN method failed for {param_name}: {e}. Trying CC method."
            )

        # Fall back to CC
        try:
            if not param.midi.cc_msb:
                logger.error(f"No CC MSB defined for {param_name}")
                return False

            result = self.digitone_midi.send_cc(
                self.midi_channel,
                int(param.midi.cc_msb),
                value,
            )

            if result:
                logger.debug(f"Set {param_name} to {value} using CC")
                return result
            else:
                logger.error(f"Failed to set {param_name} using CC")
                return False

        except Exception as e:
            logger.error(f"Failed to set {param_name}: {e}")
            raise Exception(f"Failed to set {param_name}") from e
