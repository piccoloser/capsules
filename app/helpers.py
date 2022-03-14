"""Generic classes and functions."""

import tkinter as tk
from typing import Any, Callable


class LabeledEntry(tk.Frame):
    """Simple line-entry with label"""

    def __init__(self, root: tk.Frame, text: str):
        super().__init__(root)

        self.label = tk.Label(self, text=text)
        self.entry = tk.Entry(self)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)


class Selector(tk.Frame):
    """Simple dropdown selector"""

    def __init__(
        self,
        root: tk.Frame,
        text: str,
        options: list[Any] = None,
        str_func: Callable = None,
    ):
        super().__init__(root)

        self._value = tk.StringVar()

        self.label = tk.Label(self, text=text)
        self.options = SelectorOptions(*options, str_func=str_func)
        self.menu = tk.OptionMenu(self, self._value, *self.options.list())

        self.label.grid(row=0, column=0)
        self.menu.grid(row=0, column=1)

    @property
    def value(self) -> str:
        return self._value.get()


class SelectorOptions:
    """List of options for a Selector object"""

    def __init__(self, *options, str_func: Callable = None):
        self._is_liststr = all([isinstance(i, str) for i in options])
        self._str_func = str_func

        self.items = [*options]

    def list(self) -> list[str]:
        """Return list of items as strings."""
        if self._is_liststr:
            return self.items

        if self._str_func is None:
            raise TypeError("A function is required to convert non-string options.")

        return [self._str_func(i) for i in self.items]
