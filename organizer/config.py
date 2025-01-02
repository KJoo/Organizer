import os
import yaml
from pathlib import Path
from typing import Dict, Any

DEFAULT_CONFIG = {
    "base_dir": "~/Downloads",
    "simulate": False,
    "extract": False,
    "integrity": False,
    "password": None,
    "file_filter": ".*",
    "exclude_filter": None,
    "time_based": False,
    "max_threads": 4,
    "log_level": "INFO",
    "schedule": {
        "daily": [],
        "weekly": [],
        "custom": [],
    },
}

def get_config_dir() -> Path:
    if os.name == "nt":
        return Path(os.getenv("APPDATA", "~")) / "organizer"
    else:
        return Path.home() / ".config" / "organizer"

def load_config(file_path: str = None) -> Dict[str, Any]:
    config_dir = get_config_dir()
    config_path = file_path or config_dir / "config.yaml"

    if not config_path.exists():
        create_default_config(config_path)

    try:
        with open(config_path, "r") as file:
            user_config = yaml.safe_load(file) or {}
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML configuration: {e}")

    # Merge user config with defaults
    config = {**DEFAULT_CONFIG, **user_config}
    return config


def create_default_config(config_path: Path) -> None:
    config_dir = config_path.parent
    if not config_dir.exists():
        config_dir.mkdir(parents=True, exist_ok=True)

    with open(config_path, "w") as file:
        yaml.dump(DEFAULT_CONFIG, file)
    print(f"Default configuration created at {config_path}")

def list_schedules(config: Dict[str, Any]) -> None:
    schedules = config.get("schedule", {})
    daily = schedules.get("daily", [])
    weekly = schedules.get("weekly", [])
    custom = schedules.get("custom", [])

    print("Scheduled Tasks:")
    if not daily and not weekly and not custom:
        print("  No schedules found.")
        return

    if daily:
        print("  Daily:")
        for folder in daily:
            print(f"    - {folder}")

    if weekly:
        print("  Weekly:")
        for folder in weekly:
            print(f"    - {folder}")

    if custom:
        print("  Custom:")
        for entry in custom:
            print(f"    - {entry['folder']} at {entry['time']} every {entry['interval']}")

def remove_schedule(config_path: Path, folder: str) -> None:
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    schedules = config.get("schedule", {})
    schedules["daily"] = [f for f in schedules.get("daily", []) if f != folder]
    schedules["weekly"] = [f for f in schedules.get("weekly", []) if f != folder]
    schedules["custom"] = [
        entry for entry in schedules.get("custom", []) if entry.get("folder") != folder
    ]

    with open(config_path, "w") as file:
        yaml.dump(config, file)

    print(f"Removed schedule for folder: {folder}")

