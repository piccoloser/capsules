"""Entry point for program."""

from app import config, constants, core, version
from tkinter import messagebox


def show_help() -> None:
    """Displays a help message."""
    ...


def check_for_updates() -> None:
    update_available = version.update_available()

    if update_available:
        messagebox.showinfo(
            "Update Available",
            "There is a new version available!\nPlease go to About > Update.",
        )


def main():
    match constants.SETTINGS_PATH.is_file():
        case True:
            cfg = config.read(constants.SETTINGS_PATH)

        case False:
            cfg = config.first_run()

    root = core.App(cfg)
    root.mainloop()

    return


if __name__ == "__main__":
    main()
