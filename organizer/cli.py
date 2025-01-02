import argparse
from typing import Dict

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Organize and process archive files.")
    parser.add_argument("directory", help="Base directory containing files to organize. Must exist.")
    parser.add_argument("-e", "--extract", action="store_true", help="Extract archive files in the directory.")
    parser.add_argument("-s", "--simulate", action="store_true", help="Simulate actions without making changes.")
    parser.add_argument("-i", "--integrity", action="store_true", help="Check file integrity during processing.")
    parser.add_argument("-x", "--exclude", help="Regex pattern to exclude specific files or folders.")
    parser.add_argument("-sd", "--schedule-daily", action="store_true", help="Schedule the script to run daily.")
    parser.add_argument("-sw", "--schedule-weekly", action="store_true", help="Schedule the script to run weekly.")
    parser.add_argument("--list-schedules", action="store_true", help="Display all scheduled tasks.")
    parser.add_argument("--remove-schedule", help="Remove a folder from its schedule by providing the folder path.")
    return parser.parse_args()

