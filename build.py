from __future__ import annotations

import subprocess
from typing import Collection, Generator


class Spec:
    """Details for a PyInstaller spec file."""

    def __init__(
        self,
        filename: str = "main.py",
        path_separator: str = ";",
        name: str = "",
        console: bool = False,
    ):
        self.filename = filename
        self.path_separator = path_separator

        self._datas = []
        self._hidden_imports = []
        self._name = name
        self._console = console

    def flag_items(
        self,
        flag: str,
        items: Collection,
        join_values: bool = False,
    ) -> Generator:
        """Get generator that yields each item in a collection after a flag."""
        for item in items:
            yield flag

            if join_values:
                yield self.path_separator.join(item)

            else:
                yield item

    @property
    def console(self) -> str:
        if self._console:
            return "--console"

        return "--windowed"

    @property
    def datas(self) -> Generator:
        return self.flag_items("--add-data", self._datas, True)

    @property
    def hidden_imports(self) -> Generator:
        return self.flag_items("--hidden-import", self._hidden_imports)

    @property
    def name(self) -> tuple[str, str]:
        return ("--name", self._name)

    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    def add_data(self, *args: tuple[str, str]) -> None:
        """Add files and directories to the spec.

        Format: (INPUT_PATH, OUTPUT_PATH)
        """
        self._datas.extend(args)

    def add_hidden_imports(self, *args: str) -> None:
        """Add hidden imports to the spec."""
        self._hidden_imports.extend(args)

    def makespec(self) -> None:
        """Generate a spec file."""
        subprocess.run(
            [
                "pyi-makespec",
                self.filename,
                self.console,
                *self.name,
                *self.datas,
                *self.hidden_imports,
            ],
            shell=True,
        )

        return f"./{self._name}.spec"


s = Spec(name="Ffiller")

s.add_data(
    ("app", "app"),
    ("output", "output"),
    ("README.md", "."),
)

s.add_hidden_imports(
    "openpyxl",
    "PIL.ImageDraw",
    "tkinter",
    "tkinter.filedialog",
    "tkinter.ttk",
)

subprocess.call(["pyinstaller", s.makespec(), "-y"])
