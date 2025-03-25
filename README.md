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
git https://github.com/zerubeus/elektron-mcp.git
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

To use with Claude AI, add the MCP server configuration in Claude Desktop:

```json
{
  "mcpServers": {
    "Digitone 2": {
      "command": "uv",
      "args": [
        "run",
        "--with-editable",
        "/Users/yourusername/elektron-mcp",
        "python",
        "-m",
        "elektron_mcp.main"
      ],
      "cwd": "/Users/yourusername/elektron-mcp"
    }
  }
}
```

The `--with-editable` flag is key as it adds the project directory to Python's path, solving module import issues.

You can also install the server using the FastMCP CLI:

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

### Troubleshooting

If you encounter issues running the server, here are some common problems and their solutions:

#### Server Crashes on Startup

If you see an error like "Server transport closed unexpectedly," check for these issues:

1. **MIDI Device Connection**: Ensure your Digitone is connected via USB and turned on. The server requires a connected Digitone to function properly.

2. **Check MIDI Port Names**: You can run this command to see available MIDI ports:

   ```python
   python -c "import mido; print(mido.get_input_names(), mido.get_output_names())"
   ```

3. **Run with Debug Output**: For more verbose logging:

   ```bash
   python -m elektron_mcp.main
   ```

   This will show detailed error messages on stderr, which is helpful for diagnosing issues.

4. **Specify MIDI Port**: If auto-detection fails, specify your MIDI port:

   ```bash
   # For direct execution
   MIDI_PORT="Your Digitone Port Name" python -m elektron_mcp.main

   # For Claude Desktop installation
   fastmcp install elektron_mcp/main.py -e MIDI_PORT="Your Digitone Port Name"
   ```

#### Missing Dependencies

If you see import errors, ensure all dependencies are installed:

```bash
# Reinstall with all dependencies
uv pip install -e .
```

#### Permission Issues

On some systems, you might need permission to access MIDI devices:

```bash
# Linux
sudo usermod -a -G audio $USER
# Then log out and log back in
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
