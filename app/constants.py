import pathlib
from PIL import ImageFont

# app information
APP_VERSION: str = "v0.0.1"
GITHUB_RELEASES_URL: str = "https://github.com/piccoloser/ffiller/releases"
GITHUB_API_URL: str = "https://api.github.com/repos/piccoloser/ffiller/releases"

OUTPUT_PATH: pathlib.Path = pathlib.Path("./output/")
RESOURCES_PATH: pathlib.Path = pathlib.Path("./app/resources/")
SETTINGS_PATH: pathlib.Path = pathlib.Path("settings.ini")
TEMPLATE_PATH: str = "./app/templates/"

FONT_PATH: pathlib.Path = RESOURCES_PATH / "RobotoMono-Regular.ttf"

DEFAULT: str = "DEFAULT"
DEFAULT_SETTINGS: dict = {"template": "default"}
DEFAULT_USER_SETTINGS: dict = {}
ONCE: str = "ONCE"
ONCE_SETTINGS: dict = {}
USER: str = "USER"
