# pylint_nivels_git

`pylint_nivels_git` is a custom Python package designed to help you run pylint, a popular Python code linter, with different configurations. It's perfect for projects where different linting rules are needed for different parts of the codebase.

## Requirements

This package requires the following Python packages:

- `pylint`
- `pylint-odoo`

You can install these packages using pip:

```bash
pip install pylint pylint-odoo
```

## Install 
This package is hosted on private git repository and for installation use this command:
```bash
pip install git+https://github.com/msakac/pylint_nivels
```

## Configuration

`pylint_nivels_git` uses custom configuration files for pylint. These are stored in the `configurations` directory. The package comes with several predefined configurations:

- `pylintrc`: The default pylint configuration. (Will ignore files in `oca` directory)
- `pylintrc_easy_peasy`: A more lenient configuration. (Will ignore files in `oca` directory)
- `pylintrc_quality_nerd`: A stricter configuration for quality enthusiasts. (Will ignore files in `oca` directory)
- `pylintrc_oca`: A configuration specifically for the `oca` directory.

## Usage

You can run `pylint_nivels_git` using the `pylint-nivels` command. This command takes two arguments:

1. `git_diff`: This is the branch or commit you want to diff against.
2. `pylint_config_key`: This is the key for the pylint configuration you want to use.

Here's an example of how to use the command:

```bash
pylint-nivels main pylintrc_quality_nerd
```
This command will run pylint with the `pylintrc_quality_nerd` configuration on all Python files (except for OCA) that have changed compared to the `main` branch.

Please note that the `pylintrc_oca` configuration will only lint Python files in the `oca` directory, while all other configurations will lint all Python files except those in the `oca` directory.

## Contributing

Changes and improvements are more than welcome! Please make your changes in a specific branch and request to pull into `main`!

After making changes to the package, you need to build the package using the following command:

```bash
python setup.py sdist bdist_wheel
```
