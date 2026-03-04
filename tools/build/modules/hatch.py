"""
Build System Module

Name: hatch

Description:
Modern, extensible Python project management

Homepage:
https://github.com/pypa/hatch
"""

import os
import subprocess

NAME = "hatch"

INDICATORS = ['pyproject.toml']

DEFAULT_COMMAND = "hatch build"


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
