"""
Build System Module

Name: flit

Description:
Simplified packaging of Python modules

Homepage:
https://github.com/pypa/flit
"""

import os
import subprocess

NAME = "flit"

INDICATORS = ['pyproject.toml']

DEFAULT_COMMAND = "flit build"


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
