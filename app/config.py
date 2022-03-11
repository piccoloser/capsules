"""Functions to handle user settings."""

from app.constants import (
    DEFAULT,
    DEFAULT_SETTINGS,
    DEFAULT_USER_SETTINGS,
    SETTINGS_PATH,
    USER,
)
from configparser import ConfigParser

import pathlib


DEFAULT_CONFIG = ConfigParser()
DEFAULT_CONFIG[DEFAULT] = DEFAULT_SETTINGS
DEFAULT_CONFIG[USER] = DEFAULT_USER_SETTINGS


def first_run() -> ConfigParser:
    """Initial setup, return default ConfigParser."""
    with open(SETTINGS_PATH, "w") as settings:
        DEFAULT_CONFIG.write(settings)

    return DEFAULT_CONFIG


def read(path: pathlib.Path) -> ConfigParser:
    """Read a settings file and return a ConfigParser."""
    config = ConfigParser()
    config.read(path)

    return config


def write(parser: ConfigParser, **user_settings) -> None:
    """Write one or more user settings to a ConfigParser."""
    parser[USER] = user_settings

    with open(SETTINGS_PATH, "w") as settings:
        parser.write(settings)
