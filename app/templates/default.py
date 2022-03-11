import tkinter as tk

from .. import template
from ..helpers import LabeledEntry


class Template(template.TemplateBase):
    title = "Ffiller (Select a Template)"
    width = 500
    height = 500
    x = 50
    y = 50

    def __init__(self, root: tk.Tk):
        super().__init__(root)

    def build_gui(self):
        entry1 = LabeledEntry(self.frame, "MyEntry")
        entry1.grid()

        tk.Button(
            self.frame, text="Test Entry", command=lambda: print(entry1.entry.get())
        ).grid()

        self.frame.grid()

    def build_menu(self):
        ...
