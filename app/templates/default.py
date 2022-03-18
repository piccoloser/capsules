import tkinter as tk

from .. import config, template
from ..helpers import LabeledSelector


class Template(template.TemplateBase):
    """Ffiller Template Selector"""

    title = "Ffiller"
    width = 400
    height = 250
    x = 50
    y = 50

    def __init__(self, root: tk.Tk):
        super().__init__(root)
        self.root = root

    def build_gui(self):
        template_names = template.get_all_except(["default", "empty"])
        templates = template.load_multiple(template_names)

        lbl_inst = tk.Label(self.frame, text="Select an application template!")

        sel_template = LabeledSelector(
            self.frame, "Template", templates, lambda i: i.title
        )

        var_default = tk.IntVar()
        chk_default = tk.Checkbutton(
            self.frame, text="Make Default", variable=var_default
        )

        btn_launch = tk.Button(
            self.frame,
            text="Launch Template",
            command=lambda: self.launch(
                template_names[sel_template.value_index()], var_default.get()
            ),
        )

        for widget in (lbl_inst, sel_template, chk_default, btn_launch):
            widget.grid(pady=5)

        self.frame.grid()

    def extend_menu(self):
        ...

    def launch(self, selection, default):
        if not default:
            config.once(self.root.cfg, template=selection)

        else:
            self.root.set_prefs(confirm=False, template=selection)

        self.root.restart()
