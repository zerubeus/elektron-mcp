"""
Digitone MIDI Interface

This module handles MIDI communication with Elektron Digitone devices.
It provides functionality for connecting to Digitone over MIDI (USB),
selecting channels, and sending control change (CC) messages.
"""

import mido
from typing import Optional, List
import logging

logger = logging.getLogger(__name__)

# MIDI Standard Control Change (CC) numbers for NRPN
NRPN_MSB_CC = 99  # CC for Non-Registered Parameter Number MSB
NRPN_LSB_CC = 98  # CC for Non-Registered Parameter Number LSB
DATA_ENTRY_MSB_CC = 6  # CC for Data Entry MSB
DATA_ENTRY_LSB_CC = 38  # CC for Data Entry LSB (for 14-bit precision)


class DigitoneMIDI:
    """Interface for MIDI communication with Elektron Digitone."""

    def __init__(self, port_name: Optional[str] = None):
        """
        Initialize the Digitone MIDI interface.

        Args:
            port_name: Name of the MIDI port to use. If None, will attempt to auto-detect.
        """
        self.input_port = None
        self.output_port = None
        self.connected = False

        if port_name:
            self.connect(port_name)
        else:
            self.auto_connect()

    def list_ports(self) -> List[str]:
        """List available MIDI ports."""
        inputs = mido.get_input_names()
        outputs = mido.get_output_names()
        return list(set(inputs + outputs))

    def auto_connect(self) -> bool:
        """
        Automatically connect to the first available Digitone device.

        Returns:
            bool: True if connection successful, False otherwise.
        """
        ports = self.list_ports()
        digitone_ports = [port for port in ports if "digitone" in port.lower()]

        if digitone_ports:
            return self.connect(digitone_ports[0])
        else:
            logger.warning("No Digitone device found. Available ports: %s", ports)
            return False

    def connect(self, port_name: str) -> bool:
        """
        Connect to the specified MIDI port.

        Args:
            port_name: Name of the MIDI port to connect to

        Returns:
            bool: True if connection successful, False otherwise.
        """
        try:
            # Close existing connections if any
            self.disconnect()

            # Open new connections
            self.output_port = mido.open_output(port_name)
            try:
                self.input_port = mido.open_input(port_name)
            except (IOError, ValueError) as e:
                logger.warning(f"Could not open input port {port_name}: {e}")
                # Continue with just output port

            self.connected = True
            logger.info(f"Connected to MIDI port: {port_name}")
            return True
        except (IOError, ValueError) as e:
            logger.error(f"Failed to connect to MIDI port {port_name}: {e}")
            self.disconnect()
            return False

    def disconnect(self) -> None:
        """Close all MIDI connections."""
        if self.input_port:
            self.input_port.close()
            self.input_port = None

        if self.output_port:
            self.output_port.close()
            self.output_port = None

        self.connected = False

    def send_cc(self, channel: int, cc: int, value: int) -> bool:
        """
        Send a Control Change (CC) message.

        Args:
            channel: MIDI channel (1-16)
            cc: Control Change number (0-127)
            value: Control Change value (0-127)

        Returns:
            bool: True if message sent successfully, False otherwise.
        """
        if not self.connected or not self.output_port:
            logger.error("Not connected to any MIDI port")
            return False

        # Convert 1-indexed channel to 0-indexed
        if 1 <= channel <= 16:
            channel = channel - 1
        else:
            logger.error(f"Invalid channel: {channel}. Must be between 1-16.")
            return False

        try:
            # Create and send the CC message
            msg = mido.Message(
                "control_change", channel=channel, control=cc, value=value
            )
            self.output_port.send(msg)
            logger.debug(f"Sent CC: channel={channel+1}, cc={cc}, value={value}")
            return True
        except Exception as e:
            logger.error(f"Error sending CC message: {e}")
            return False

    def send_nrpn(self, channel: int, nrpn_msb: int, nrpn_lsb: int, value: int) -> bool:
        """
        Send a Non-Registered Parameter Number (NRPN) message sequence.

        This sends a complete NRPN sequence:
        1. CC 99 (NRPN MSB)
        2. CC 98 (NRPN LSB)
        3. CC 6 (Data Entry MSB)

        Args:
            channel: MIDI channel (1-16)
            nrpn_msb: NRPN Parameter MSB (0-127)
            nrpn_lsb: NRPN Parameter LSB (0-127)
            value: Parameter value (0-127)

        Returns:
            bool: True if all messages sent successfully, False otherwise.
        """
        if not self.connected or not self.output_port:
            logger.error("Not connected to any MIDI port")
            return False

        # Convert 1-indexed channel to 0-indexed
        if 1 <= channel <= 16:
            channel = channel - 1
        else:
            logger.error(f"Invalid channel: {channel}. Must be between 1-16.")
            return False

        try:
            # Send NRPN MSB (CC 99)
            self.output_port.send(
                mido.Message(
                    "control_change",
                    channel=channel,
                    control=NRPN_MSB_CC,
                    value=nrpn_msb,
                )
            )

            # Send NRPN LSB (CC 98)
            self.output_port.send(
                mido.Message(
                    "control_change",
                    channel=channel,
                    control=NRPN_LSB_CC,
                    value=nrpn_lsb,
                )
            )

            # Send Data Entry MSB (CC 6)
            self.output_port.send(
                mido.Message(
                    "control_change",
                    channel=channel,
                    control=DATA_ENTRY_MSB_CC,
                    value=value,
                )
            )

            logger.debug(
                f"Sent NRPN: channel={channel+1}, nrpn={nrpn_msb}/{nrpn_lsb}, value={value}"
            )
            return True
        except Exception as e:
            logger.error(f"Error sending NRPN message: {e}")
            return False
