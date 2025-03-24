# Elektron MCP

A Python library for working with Elektron synthesizers via MIDI Control Protocol (MCP).

## Features

- Type-safe parameter definitions for various Elektron synths
- Data validation using Pydantic
- JSON serialization/deserialization for saving and loading configurations
- Comprehensive test suite

## Implementation Details

This library uses Pydantic models for data validation, serialization, and type safety:

- Parameter values are validated against their acceptable ranges
- Enum-based parameters validate against their allowed options
- Complex nested synth configurations can be easily serialized to JSON
- Type hints provide editor auto-completion and documentation

## Testing

The test suite includes validations for:

- Parameter ranges
- Enum option validation
- JSON serialization/deserialization
- Nested parameter structures
