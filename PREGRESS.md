This app is a Model Context Protocol server that allows Claude and other MCP-compatible LLMs to interact with Elektron machines via MIDI.

## Features

- [x] use uv for dependency/project management
- [x] use pydantic for config validation
- [x] use pytest for testing
- [x] map all Digitone config params to MIDI values and display values in `elektron_mcp/digitone/digitone_config.py`
- [x] structure Digitone config into models, constants, and utils
- [x] add tests for all Digitone config params (amp, fx, lfo, filters, swarmer, wavetone, fmtone, fmdrum)
- [x] add a new utility in elektron_mpc/midi/ to handle MIDI communication with Digitone, should include channel selection, CC messages, midi value, etc.
- [x] create a base controller class (BaseSynthController) for common functionality across all controllers
- [x] implement WavetoneController for controlling all Wavetone synth engine parameters
- [x] implement FMDrumController for controlling all FM Drum synth engine parameters
- [x] implement FMToneController for controlling all FM Tone synth engine parameters
- [x] implement SwarmerController for controlling all Swarmer synth engine parameters
- [x] implement filter controllers for all filter types (MultiMode, Lowpass4, Equalizer, LegacyLpHp, CombMinus, CombPlus, BaseWidth)
- [x] implement AmpController for controlling amplitude/volume parameters
- [x] implement FXController for controlling effects parameters
