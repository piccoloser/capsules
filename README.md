# Python Project Template

### This project template includes the following files and folders:
#### `/.vscode`
* `launch.json`
    * Forces `main.py` when the program is run, assuming you use VS Code

#### `/app`
* `constants.py`
    * Includes constant `APP_VERSION`, a `str` set to "v0.0.1" by default
* `core.py`
* `helpers.py`

#### `/tests`
* `test_main.py`
    * Includes two default tests that should always pass:
        * `test_int()`
        * `test_imports()`

#### `/`
* `main.py`
    * Includes boilerplate `main()` function
* `README.md`
    * This file
* `requirements.txt`
    * Required imports for this workflow

### This project uses the following modules by default:
* `pretty_errors`
* `pytest`

*When you push to your repository or create a pull request, GitHub Actions will automatically format your code using `Black`, sort imports using `isort`, and runs tests using `pytest` (required).*