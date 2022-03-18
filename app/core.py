"""Program-specific classes and functions."""

import configparser
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

from app import config, template
from app.constants import DEFAULT, ONCE, USER


class App(tk.Tk):
    """Main Application."""

    def __init__(self, cfg: configparser.ConfigParser):
        super().__init__()
        super().protocol("WM_DELETE_WINDOW", self.teardown)

        self.cfg = cfg

        # load user-defined template or default
        self._template_class = template.load(
            config.get(self.cfg, ONCE, "template")
            or config.get(self.cfg, USER, "template")
            or config.get(self.cfg, DEFAULT, "template")
        )

        try:
            self.template = self._template_class(self)

        # if template doesn't exist for any reason, load default
        except TypeError:
            self._template_class = template.load("default")
            self.template = self._template_class(self)

        self.title(self.template.title)
        self.geometry(self.template.geometry)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.build_menu()
        self.template.extend_menu()

        super().config(menu=self.template.menu)

        self.template.build_gui()

    def build_menu(self):
        """Build the default menu bar."""
        menu = self.template.menu

        self.menu_about = tk.Menu(menu, tearoff=0)
        self.menu_about.add_command(
            label="Select Template", command=lambda: self.restart(True)
        )

        menu.add_cascade(label="About", menu=self.menu_about)

    def restart(self, select_template: bool = False) -> None:
        """Restart the program."""
        try:
            self.destroy()

        except tk.TclError:
            quit()

        if select_template:
            config.once(self.cfg, template="default")

        subprocess.call([sys.executable, *sys.argv])

    def set_prefs(self, confirm: bool = True, **user_settings) -> None:
        """Change user preferences."""
        config.write(self.cfg, **user_settings)

        if confirm:
            if not messagebox.askokcancel(
                "Restart Required",
                "Your changes will not take effect until you restart the program. "
                "Would you like to do so now?",
            ):
                return

        self.restart()

    def teardown(self):
        config.clear_once(self.cfg)
        self.destroy()
