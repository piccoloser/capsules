"""Program-specific classes and functions."""

from app import config, template
from app.constants import DEFAULT, USER

import configparser
import tkinter as tk


class App(tk.Tk):
    """Main Application."""

    def __init__(self, cfg: configparser.ConfigParser):
        super().__init__()

        self.cfg = cfg

        # load user-defined template or default
        self.template = template.load(
            self.cfg[USER].get("template") or self.cfg[DEFAULT].get("template")
        )

        self.title(self.template.title)
        self.geometry(self.template.geometry)

    def set_prefs(self, **user_settings) -> None:
        """Change user preferences."""
        config.write(self.cfg, **user_settings)
