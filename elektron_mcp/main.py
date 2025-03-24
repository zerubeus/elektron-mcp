from .elektron_types import elektron_config


def main():
    print("Hello from elektron-mcp!")
    # Example usage of elektron_config
    print(f"Number of synth types: {len(elektron_config.__dict__)}")

    # Serialize config to JSON and print it
    config_json = elektron_config.model_dump_json(indent=2)
    print("\nElektron Config JSON:")
    print(config_json)


if __name__ == "__main__":
    main()
