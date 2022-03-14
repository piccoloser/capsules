"""Entry point for program."""

from tkinter import messagebox

from app import config, constants, core, version


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
    if constants.SETTINGS_PATH.is_file():
        cfg = config.read(constants.SETTINGS_PATH)

    else:
        cfg = config.first_run()

    root = core.App(cfg)
    root.mainloop()


if __name__ == "__main__":
    main()
