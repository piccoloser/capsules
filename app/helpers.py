"""Generic classes and functions."""

import tkinter as tk
from tkinter import ttk
from typing import Any, Callable


class LabeledEntry(tk.Frame):
    """Simple line-entry with label"""

    def __init__(self, root: tk.Frame, text: str = ""):
        super().__init__(root)

        self.label = tk.Label(self, text=text)
        self.entry = tk.Entry(self)

        self.grid_columnconfigure(0, weight=1)

        self.label.grid(row=0, column=0, sticky=tk.E)
        self.entry.grid(row=0, column=1)

    @property
    def value(self) -> str:
        return self.entry.get()


class LabeledSelector(tk.Frame):
    """Simple dropdown selector.

    Requires a root object, label text, and a list of options.

    `options` must be a list of strings. If the list contains some
    other type, `string_func` must be defined to convert each item.
    """

    def __init__(
        self,
        root: tk.Frame,
        text: str,
        options: list[Any],
        str_func: Callable = None,
    ):
        super().__init__(root)

        self._value = tk.StringVar()

        self.label = tk.Label(self, text=text)
        self.options = SelectorOptions(*options, str_func=str_func)

        self.menu = ttk.OptionMenu(
            self, self._value, self.options[0], *self.options.list()
        )

        self.label.grid(row=0, column=0)
        self.menu.grid(row=0, column=1)

    @property
    def value(self) -> str:
        return self._value.get()

    @value.setter
    def value(self, value: str) -> None:
        self._value.set(value)

    def value_index(self) -> int:
        return self.options.list().index(self.value)


class SelectorOptions:
    """List of options for a Selector object"""

    def __init__(self, *options, str_func: Callable = None):
        self._is_liststr = all([isinstance(i, str) for i in options])
        self._str_func = str_func

        if not self._is_liststr and self._str_func is None:
            raise TypeError("A function is required to convert non-string options.")

        self.items = [*options]

    def __getitem__(self, index: int) -> str:
        if self._is_liststr:
            return self.items[index]

        return self._str_func(self.items[index])

    def list(self) -> list[str]:
        """Return list of items as strings."""
        if self._is_liststr:
            return self.items

        return [self._str_func(i) for i in self.items]
