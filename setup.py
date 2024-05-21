from setuptools import setup, find_packages

setup(
    name="pylint_nivels_git",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pylint_nivels=pylint_nivels_git.commands:main",
        ]
    },
)
