from setuptools import setup, find_packages

setup(
    name="pylint_nivels_git",
    version='1.0',
    packages=find_packages(),
    package_data={'': ['configurations/*']},
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "pylint_nivels=pylint_nivels_git.commands:main",
        ]
    },
)
