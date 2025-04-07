import pytest
from unittest.mock import patch
import logging

from elektron_mcp.digitone.services.wavetone_controller import WavetoneController
from elektron_mcp.digitone.config.config import digitone_config
from elektron_mcp.midi.digitone_midi import DigitoneMIDI

logger = logging.getLogger(__name__)


def test_set_osc1_pitch():
    """Test that the set_osc1_pitch method correctly sends the MIDI CC message."""
    # Create a DigitoneMIDI instance
    # Note: This requires a real Digitone device connected
    digitone_midi = DigitoneMIDI()

    # Skip the test if no Digitone is connected
    if not digitone_midi.connected:
        pytest.skip("No Digitone device connected. Skipping test.")

    # Configure a wavetone services for MIDI channel 1
    midi_channel = 1
    wavetone_controller = WavetoneController(
        digitone_config.wavetone.pages, digitone_midi, midi_channel
    )

    # Get the expected CC number for OSC1 pitch from the config
    osc1_pitch_param = digitone_config.wavetone.pages["page_1"].parameters["TUN1"]
    expected_cc = int(osc1_pitch_param.midi.cc_msb)

    # Set a test value for pitch
    test_value = 10  # Middle value (0 in actual pitch)

    # Use a mocked send_cc method to verify the correct parameters are sent
    with patch.object(
        digitone_midi, "send_cc", wraps=digitone_midi.send_cc
    ) as mock_send_cc:
        # Call the method we're testing
        result = wavetone_controller.set_osc1_pitch(test_value)

        # Assert that send_cc was called with the correct parameters
        mock_send_cc.assert_called_once_with(midi_channel, expected_cc, test_value)

        # Assert that the method returned True (successful)
        assert result is True, "set_osc1_pitch should return True on success"

    # Log the action for visibility
    logger.info(
        f"Successfully sent CC {expected_cc} with value {test_value} to Digitone on channel {midi_channel}"
    )
