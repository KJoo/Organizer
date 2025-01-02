#!/usr/bin/env python3
from organizer.config import load_config, list_schedules, remove_schedule
from organizer.cli import parse_arguments
from pathlib import Path

def main():
    try:
        args = parse_arguments()

        # Validate directory argument
        directory = args.directory
        if not Path(directory).exists():
            raise FileNotFoundError(f"Directory '{directory}' does not exist.")

        config_path = Path.home() / ".config" / "organizer" / "config.yaml"
        config = load_config(config_path)

        if args.list_schedules:
            list_schedules(config)
        elif args.remove_schedule:
            remove_schedule(config_path, args.remove_schedule)
        else:
            print("No specific action was requested.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

