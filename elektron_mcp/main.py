import sys
from elektron_mcp.mcp_server.server import mcp
from elektron_mcp.midi.digitone_midi import DigitoneMIDI


def check_midi_connection():
    """Verify MIDI connection before starting the server"""
    try:
        midi = DigitoneMIDI()
        if not midi.connected:
            print(
                "ERROR: Could not connect to Digitone. Please check your USB connection.",
                file=sys.stderr,
            )
            print(f"Available MIDI ports: {midi.list_ports()}", file=sys.stderr)
            return False
        print(
            f"Successfully connected to MIDI device: {midi.output_port}",
            file=sys.stderr,
        )
        return True
    except Exception as e:
        print(f"ERROR connecting to MIDI: {str(e)}", file=sys.stderr)
        return False


def main():
    """Entry point for the elektron-mcp command"""
    print("Starting Elektron MCP server...", file=sys.stderr)

    # Verify MIDI connection before starting server
    if not check_midi_connection():
        print(
            "MIDI connection failed. Server will start but may not function correctly.",
            file=sys.stderr,
        )

    try:
        mcp.run()
    except Exception as e:
        print(f"ERROR running MCP server: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
