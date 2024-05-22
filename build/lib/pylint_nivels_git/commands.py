import argparse
import os
import logging

# Dictionary mapping keys to configuration file paths
CONFIGURATION_PATHS = {
    'pylintrc': 'configurations/.pylintrc',
    'pylintrc_easy_peasy': 'configurations/.pylintrc_easy_peasy',
    'pylintrc_quality_nerd': 'configurations/.pylintrc_quality_nerd',
    'pylintrc_oca': 'configurations/.pylintrc_oca'
}

def get_git_diff_cmd(git_diff, pylint_config_key):
    ''' Get the git diff command based on the configuration key. If linting oca then only lint files in oca directory
    Else lint all python files in the diff excluding oca directory'''
    if pylint_config_key == 'pylintrc_oca':
        return f"$(git diff --name-only --diff-filter=ACMRTUXB {git_diff} | grep -E '(.py$)' | grep -E '^oca/')"
    return f"$(git diff --name-only --diff-filter=ACMRTUXB {git_diff} | grep -E '(.py$)' | grep -vE '^oca/')"

def run_pylint_nivels(git_diff, pylint_config_key):
    ''' Get the configuration file path from the key and run pylint with it '''
    if pylint_config_key not in CONFIGURATION_PATHS:
        logging.error("Error: Configuration key '%s' not found.", pylint_config_key)
        return

    pylint_configuration = CONFIGURATION_PATHS[pylint_config_key]
    current_directory = os.path.dirname(__file__)
    configuration_path = os.path.join(current_directory, pylint_configuration)

    if not os.path.exists(configuration_path):
        logging.error("Error: Configuration file %s not found.", configuration_path)
        return

    git_diff_command = get_git_diff_cmd(git_diff, pylint_config_key)

    pylint_command = f"pylint --load-plugins=pylint_odoo --rcfile={configuration_path} {git_diff_command} --output-format=colorized"
    os.system(pylint_command)


def main():
    ''' Parse command line arguments call method which runs pylint '''
    parser = argparse.ArgumentParser(description="Run pylint with custom configuration")
    parser.add_argument("git_diff", help="Branch or commit to diff against")
    parser.add_argument("pylint_config_key", help="Key to retrieve the pylint configuration file path")
    args = parser.parse_args()
    run_pylint_nivels(args.git_diff, args.pylint_config_key)

if __name__ == "__main__":
    main()
