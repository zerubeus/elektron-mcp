# Elektron MCP

A Model Context Protocol (MCP) server that allows Claude and other MCP-compatible LLMs to interact with and control Elektron synthesizers via MIDI.

## Features

- Complete MIDI control interface for the Elektron Digitone synthesizer
- Structured controllers for all Digitone sound engines:
  - Wavetone (waveshaping synthesis)
  - FM Tone (FM synthesis)
  - FM Drum (percussive FM synthesis)
  - Swarmer (unison/swarm synthesis)
- Comprehensive parameter control for:
  - All filter types (Multi-Mode, Lowpass4, Equalizer, etc.)
  - Amplitude and envelope settings
  - Effects processing (delay, reverb, chorus, bit reduction, etc.)
- MCP server exposing all synth parameters as tools for LLMs
- Type-safe parameter validation using Pydantic
- Modular architecture for easy extension to other Elektron devices

## Installation and Usage

### Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) for package management
- An Elektron Digitone connected via USB
- Claude Desktop app (for full integration)

### Installing Dependencies

```bash
# Clone the repository
git clone https://github.com/yourusername/elektron-mcp.git
cd elektron-mcp

# Install dependencies with uv
uv pip install -e .

# For development, install with dev dependencies
uv pip install -e ".[dev]"
```

### Running the Server

There are three ways to run the server:

#### 1. Development Mode (for testing)

This launches the FastMCP Inspector web interface where you can test tools interactively:

```bash
# Run the server in development mode
fastmcp dev elektron_mcp/main.py
```

#### 2. Direct Execution

Run the server directly from the command line:

```bash
# Using Python directly
python -m elektron_mcp.main

# Using uv
uv run python -m elektron_mcp.main

# Using the FastMCP CLI
fastmcp run elektron_mcp/main.py
```

#### 3. Installing with Claude Desktop

To use with Claude AI, install the server in Claude Desktop:

```bash
# Install the server for use with Claude
fastmcp install elektron_mcp/main.py

# With a custom name (optional)
fastmcp install elektron_mcp/main.py --name "Elektron Digitone Controller"

# With environment variables (if needed)
fastmcp install elektron_mcp/main.py -e MIDI_PORT=Digitone
```

### MIDI Configuration

Ensure your Digitone is connected via USB before starting the server. The server will attempt to auto-detect the device. If you have multiple MIDI devices connected, you may need to specify the port name using an environment variable:

```bash
# Set the MIDI port environment variable
export MIDI_PORT="Digitone"

# Then run the server
python -m elektron_mcp.main
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
- **Object-oriented design**: For maintainable, extensible code

## Use Cases

- Allow Claude and other LLMs to create and modify sounds on the Digitone
- Programmatically control Digitone parameters for automated sound design
- Bridge between AI-generated music and hardware synthesis

## Future Extensions

- Support for additional Elektron devices (Analog Four, Octatrack, etc.)
- Pattern sequencing and automation
- Sound preset management
- Additional synthesis parameters
