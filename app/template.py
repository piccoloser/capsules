"""Template for PDF and corresponding forms."""

import importlib
import pathlib
import tkinter as tk
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.constants import TEMPLATE_PATH


@dataclass
class TemplateBase(ABC):
    title: str
    width: int
    height: int
    x: int
    y: int

    def __init__(self, root: tk.Tk):
        self.frame = tk.Frame(root)

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


def get_all_except(ignored: list[str] = None) -> list[str]:
    """List available templates, with exceptions."""
    contents = pathlib.Path(TEMPLATE_PATH).glob("*.py")
    templates = [i.stem for i in contents if i.is_file()]

    if ignored is None:
        ignored = []

    ignored.append("__init__")

    templates = list(filter(lambda i: i not in ignored, templates))

    return templates


def get_import_path(filepath: pathlib.Path) -> str:
    """Convert a filepath to Python import format."""
    return filepath.as_posix().replace("/", ".").replace(".py", "")


def load(filename: str) -> TemplateBase:
    filename = pathlib.Path(TEMPLATE_PATH + f"{filename}.py")

    if filename.is_file():
        import_path = get_import_path(filename)
        source = importlib.import_module(import_path)

        return source.Template


def load_multiple(filenames: list[str]) -> list[TemplateBase]:
    filenames = [pathlib.Path(TEMPLATE_PATH + f"{i}.py") for i in filenames]

    templates: list[TemplateBase] = []
    for filename in filenames:
        if filename.is_file():
            import_path = get_import_path(filename)
            source = importlib.import_module(import_path)

        templates.append(source.Template)

    return templates
