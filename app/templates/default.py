import tkinter as tk

from .. import template
from ..helpers import LabeledEntry, Selector


class Template(template.TemplateBase):
    """Ffiller Template Selector"""

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

        sel1 = Selector(
            self.frame, "Select an Option", [*range(1, 21)], lambda x: str(x)
        )
        sel1.grid()

        tk.Button(
            self.frame, text="Test Entry", command=lambda: print(entry1.entry.get())
        ).grid()
        tk.Button(
            self.frame, text="Test Selector", command=lambda: print(sel1.value)
        ).grid()

        self.frame.grid()

    def build_menu(self):
        ...
