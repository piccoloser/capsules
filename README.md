# Capsules

A simple, modular GUI-application launcher.

## The Basics
### No templates installed:
![No Templates](../media/no_template.jpg)

### With a template installed:
![Template Available](../media/with_templates.jpg)

### Example Template:
![Example Template](../media/example_template.jpg)

### Default Options Menu:
![Default Options Menu](../media/example_options.jpg)

## Creating a Template
First, you'll need a `.py` file with the same basic layout as [empty.py](./app/templates/empty.py), saved in `/app/templates`. You can declare your program's GUI within `Template.build_gui()` and program-specific menu options under `Template.extend_menu()`. Your program's necessary functions can be added as needed, and resources should be kept in `/app/resources/YOUR_TEMPLATE`.

To remove a template, delete the `.py` file and all associated resources. A method of adding and removing templates from within the program is under development.
