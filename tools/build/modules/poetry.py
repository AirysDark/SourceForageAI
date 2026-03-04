"""
Build System Module

Name: poetry

Description:
Python packaging and dependency management made easy

Homepage:
https://github.com/python-poetry/poetry
"""

import os
import subprocess

NAME = "poetry"

INDICATORS = ['pyproject.toml']

DEFAULT_COMMAND = "poetry build"


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system:", NAME)

    if DEFAULT_COMMAND:

        subprocess.run(DEFAULT_COMMAND, shell=True)

    else:

        print("No default build command known")
