import tkinter as tk

from .. import template


class Template(template.TemplateBase):
    """Empty Ffiller Template"""

    title = "Empty"
    width = 300
    height = 200
    x = 50
    y = 50

    def __init__(self, root: tk.Tk):
        super().__init__(root)

    def build_gui(self):
        self.frame.grid()

    def extend_menu(self):
        ...
