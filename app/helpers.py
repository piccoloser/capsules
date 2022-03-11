"""Generic classes and functions."""

import tkinter as tk


class LabeledEntry(tk.Frame):
    def __init__(self, root: tk.Frame, text: str):
        super().__init__(root)

        self.label = tk.Label(self, text=text)
        self.entry = tk.Entry(self)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)
