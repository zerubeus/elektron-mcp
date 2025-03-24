from .digitone_config import digitone_config


def main():
    print("Hello from elektron-mcp!")
    # Example usage of digitone_config
    print(f"Number of synth types: {len(digitone_config.__dict__)}")

    # Serialize config to JSON and print it
    config_json = digitone_config.model_dump_json(indent=2)
    print("\nElektron Config JSON:")
    print(config_json)


if __name__ == "__main__":
    main()
