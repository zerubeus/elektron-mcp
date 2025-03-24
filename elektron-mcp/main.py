from elektron_types import elektron_config


def main():
    print("Hello from elektron-mcp!")
    # Example usage of elektron_config
    print(f"Number of synth types: {len(elektron_config.__dict__)}")


if __name__ == "__main__":
    main()
