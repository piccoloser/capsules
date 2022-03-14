"""Functions to handle user settings."""

import pathlib
from configparser import ConfigParser

from app.constants import (
    DEFAULT,
    DEFAULT_SETTINGS,
    DEFAULT_USER_SETTINGS,
    ONCE,
    ONCE_SETTINGS,
    SETTINGS_PATH,
    USER,
)

DEFAULT_CONFIG = ConfigParser(allow_no_value=True)
DEFAULT_CONFIG[DEFAULT] = DEFAULT_SETTINGS
DEFAULT_CONFIG[ONCE] = ONCE_SETTINGS
DEFAULT_CONFIG[USER] = DEFAULT_USER_SETTINGS


def clear_once(parser: ConfigParser):
    """Clear ONCE settings."""
    parser[ONCE].clear()
    with open(SETTINGS_PATH, "w") as settings:
        parser.write(settings)


def first_run() -> ConfigParser:
    """Initial setup, return default ConfigParser."""
    with open(SETTINGS_PATH, "w") as settings:
        DEFAULT_CONFIG.write(settings)

    return DEFAULT_CONFIG


def get(parser: ConfigParser, section: str, key: str) -> str or None:
    """Get value from a ConfigParser or None if value is default."""
    value = parser[section].get(key)

    if value == "default" and section != DEFAULT:
        return None

    return value


def once(parser: ConfigParser, **once_settings) -> None:
    """Settings that reset when the application is closed."""
    parser[ONCE] = once_settings

    with open(SETTINGS_PATH, "w") as settings:
        parser.write(settings)


def read(path: pathlib.Path) -> ConfigParser:
    """Read a settings file and return a ConfigParser."""
    config = ConfigParser(allow_no_value=True)
    config.read(path)

    return config


def write(parser: ConfigParser, **user_settings) -> None:
    """Write one or more user settings to a ConfigParser."""
    parser[USER] = user_settings
    with open(SETTINGS_PATH, "w") as settings:
        parser.write(settings)
