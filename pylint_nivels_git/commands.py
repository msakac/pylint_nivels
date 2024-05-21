import argparse
import os

def run_pylint_nivels(pylint_configuration):
    git_files = os.popen("git diff --name-only --diff-filter=ACMRTUXB | grep  -E '.py$'").read()
    if not git_files:
        exit(0)

    pylint_command = f"pylint --load-plugins=pylint_odoo --rcfile={pylint_configuration} {git_files} --output-format=colorized"
    os.system(pylint_command)

def main():
    parser = argparse.ArgumentParser(description="Run pylint with custom configuration")
    parser.add_argument("pylint_configuration", help="Path to the pylint configuration file")
    args = parser.parse_args()
    run_pylint_nivels(args.pylint_configuration)

if __name__ == "__main__":
    main()
