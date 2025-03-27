# Elektron MCP

A Model Context Protocol (MCP) server that allows Claude and other MCP-compatible LLMs to interact with and control Elektron synthesizers via MIDI.

# Prompt examples

```
“Use Digitone MCP to design an evolving dark pad using the Wavetone machine on track 1.”
"Use Digitone MPC to design a Dark thick pad using Wavetone machine on track 1."
```

Only Wavetone machine is supported for now, other machines will be added soon, stay tuned!

## Features

- [x] Complete MIDI control interface for the Elektron Digitone synthesizer
- [x] Structured controllers for all Digitone sound engines:
  - [x] Wavetone (waveshaping synthesis)
  - [ ] FM Tone (FM synthesis)
  - [ ] FM Drum (percussive FM synthesis)
  - [ ] Swarmer (unison/swarm synthesis)
- [x] Comprehensive parameter control for:
  - [x] All filter types
    - [x] MultiMode
    - [ ] Lowpass4
    - [ ] Equalizer
    - [ ] LegacyLpHp
    - [ ] CombMinus
    - [ ] CombPlus
    - [ ] BaseWidth
  - [x] Amplitude and envelope settings
  - [x] Effects processing (delay, reverb, chorus, bit reduction, etc.)
  - [x] LFOs control
- [x] MCP server exposing all synth parameters as tools for LLMs
- [x] Type-safe parameter validation using Pydantic
- [x] Modular architecture for easy extension to other Elektron devices

## Demo

Watch Claude control the Elektron Digitone synthesizer in real-time:

[![Claude controlling Elektron Digitone](https://img.youtube.com/vi/EXf6lOTjla8/0.jpg)](https://www.youtube.com/watch?v=EXf6lOTjla8)

## Installation and Usage

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) for package management
- An Elektron Digitone connected via USB
- Claude Desktop app (for full integration)

### Installing Dependencies

uv is mandatory for this project so start by installing it:

#### For macOS:

```bash
brew install uv
```

#### For Windows:

Follow the instructions [here](https://docs.astral.sh/uv/getting-started/installation/)

### 3. Installing with Claude Desktop

To use with Claude AI, add the MCP server configuration in Claude Desktop:

Go to Claude > Settings > Developer > Edit Config > claude_desktop_config.json to include the following:

```json
{
  "mcpServers": {
    "Digitone 2": {
      "command": "uvx",
      "args": ["elektron-mcp"]
    }
  }
}
```

## Architecture

The library is designed with a clean, object-oriented architecture:

- **Base Controllers**: Common functionality abstracted into base classes
- **Specialized Controllers**: Dedicated controllers for each synth engine and module
- **MCP Tools**: Direct interface between LLMs and the synth's parameters
- **MIDI Interface**: Reliable communication with Digitone hardware

## Implementation Details

This library uses:

- **FastMCP**: For exposing synth controls to LLMs
- **Pydantic models**: For data validation, serialization, and type safety
- **mido**: For MIDI communication

## Use Cases

- Allow Claude and other LLMs to create and modify sounds on the Digitone
- Programmatically control Digitone parameters for automated sound design
- Bridge between AI-generated music and hardware synthesis

## Future Extensions

- Support for additional Elektron devices (Analog Four, Octatrack, etc.)
- Pattern sequencing and automation
- Sound preset management
- Additional synthesis parameters
