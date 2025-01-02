"""
Organizer Package

This package provides functionality for file organization, configuration management,
task scheduling, and CLI parsing.
"""

# Expose key functions and classes for external imports
from .core import main
from .config import load_config, list_schedules, remove_schedule
from .tasks import schedule_tasks
from .cli import parse_arguments

__all__ = ["main", "load_config", "list_schedules", "remove_schedule", "schedule_tasks", "parse_arguments"]

