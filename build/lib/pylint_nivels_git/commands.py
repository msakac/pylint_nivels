import argparse
import os
import subprocess

# Dictionary mapping keys to configuration file paths
CONFIGURATION_PATHS = {
    'path_to_pylintrc': 'configurations/.pylintrc',
    'path_to_easy_peasy': 'configurations/.pylintrc_easy_peasy',
    'path_to_quality_nerd': 'configurations/.pylintrc_quality_nerd'
}

def run_pylint_nivels(git_diff, pylint_configuration_key):
    # Check if the provided key exists in the configuration paths dictionary
    if pylint_configuration_key not in CONFIGURATION_PATHS:
        print(f"Error: Configuration key '{pylint_configuration_key}' not found.")
        return

    # Get the corresponding configuration file path
    pylint_configuration = CONFIGURATION_PATHS[pylint_configuration_key]

    # Get the current directory of the script
    current_directory = os.path.dirname(__file__)

    # Form the absolute path to the configuration file
    configuration_path = os.path.join(current_directory, pylint_configuration)

    # Check if the configuration file exists
    if not os.path.exists(configuration_path):
        print(f"Error: Configuration file '{configuration_path}' not found.")
        return

    # Get the list of Python files changed in the diff
    git_diff_command = f"$(git diff --name-only --diff-filter=ACMRTUXB {git_diff} | grep -E '(.py$)')"
    # git_files = subprocess.run(git_diff_command, shell=True, capture_output=True, text=True).stdout.strip()

    # if not git_files:
    #     print("No Python files to lint.")
    #     exit(0)

    # Use the retrieved configuration file path in the pylint command
    pylint_executable = os.path.join(os.environ.get('VIRTUAL_ENV', ''), 'bin', 'pylint')
    pylint_command = f"{pylint_executable} --load-plugins=pylint_odoo --rcfile={configuration_path} {git_diff_command} --output-format=colorized"

    # Print the command for debugging
    print(f"Running command: {pylint_command}")

    # Execute the command
    subprocess.run(pylint_command, shell=True, capture_output=True, text=True)


def main():
    parser = argparse.ArgumentParser(description="Run pylint with custom configuration")
    parser.add_argument("git_diff", help="Branch or commit to diff against")
    parser.add_argument("pylint_configuration_key", help="Key to retrieve the pylint configuration file path")
    args = parser.parse_args()

    run_pylint_nivels(args.git_diff, args.pylint_configuration_key)

if __name__ == "__main__":
    main()
