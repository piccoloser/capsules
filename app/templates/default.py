from ..template import TemplateBase


class DefaultTemplate(TemplateBase):
    def __init__(self):
        self.title = "Ffiller"
        self.width = 500
        self.height = 500
        self.x = 50
        self.y = 50

    def build_gui(self):
        ...

    def build_menu(self):
        ...


template = DefaultTemplate()
