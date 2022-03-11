"""Program-specific classes and functions."""

import configparser
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

from app import config, template
from app.constants import DEFAULT, USER


class App(tk.Tk):
    """Main Application."""

    def __init__(self, cfg: configparser.ConfigParser):
        super().__init__()

        self.cfg = cfg

        # load user-defined template or default
        self._template_class = template.load(
            self.cfg[USER].get("template") or self.cfg[DEFAULT].get("template")
        )
        self.template = self._template_class(self)

        self.title(self.template.title)
        self.geometry(self.template.geometry)

        self.template.build_menu()
        self.template.build_gui()

    def restart(self) -> None:
        """Restart the program."""
        self.destroy()
        subprocess.call([sys.executable, *sys.argv])

    def set_prefs(self, **user_settings) -> None:
        """Change user preferences."""
        config.write(self.cfg, **user_settings)

        if messagebox.askokcancel(
            "Restart Required",
            "Your changes will not take effect until you restart the program. "
            "Would you like to do so now?",
        ):
            self.restart()
