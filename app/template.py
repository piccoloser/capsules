"""Template for PDF and corresponding forms."""

import importlib
import pathlib
import tkinter as tk
from abc import ABC, abstractmethod
from dataclasses import dataclass

from app.constants import TEMPLATE_PATH
from app.core import App


@dataclass
class TemplateBase(ABC):
    title: str
    width: int
    height: int
    x: int
    y: int

    def __init__(self, root: tk.Tk):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.menu = tk.Menu(self.root)
        self.menu_options: tk.Menu = None

    @abstractmethod
    def build_gui(self):
        """Construct the GUI."""
        ...

    @abstractmethod
    def extend_menu(self):
        """Add items to the menu bar."""
        ...

    @property
    def geometry(self) -> str:
        return f"{self.width}x{self.height}+{self.x}+{self.y}"

    def build_menu(self, app: App):
        """Build the default menu bar."""
        self.menu_options = tk.Menu(self.menu, tearoff=0)
        self.menu_options.add_command(
            label="Select Template", command=lambda: app.restart(True)
        )

        self.menu_options.add_command(label="Import Template", command=import_template)

        self.menu.add_cascade(label="Options", menu=self.menu_options)


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


def import_template() -> None:
    """Unpack a template for use in the program."""
    # get zip file
    # validate contents
    # unpack template and resources
    # notify user of success


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
