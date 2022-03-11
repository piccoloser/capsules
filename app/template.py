"""Template for PDF and corresponding forms."""

from abc import ABC, abstractmethod
from app.constants import TEMPLATE_PATH
from dataclasses import dataclass

import importlib
import pathlib


@dataclass
class TemplateBase(ABC):
    title: str
    width: int
    height: int
    x: int
    y: int

    @abstractmethod
    def build_gui(self):
        """Construct the GUI."""
        ...

    @abstractmethod
    def build_menu(self):
        """Construct the menu bar."""
        ...

    @property
    def geometry(self) -> str:
        return f"{self.width}x{self.height}+{self.x}+{self.y}"


def load(filename: str) -> TemplateBase or None:
    filename = pathlib.Path(TEMPLATE_PATH.replace("{}", filename))

    if filename.is_file():
        import_path = filename.as_posix().replace("/", ".").replace(".py", "")
        source = importlib.import_module(import_path)

        return source.template
