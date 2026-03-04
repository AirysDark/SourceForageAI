"""
Auto-generated build module
Build system: pip-build

Description:


Homepage:

"""

import os
import subprocess

INDICATORS = ['pyproject.toml']

DEFAULT_COMMAND = "python -m build"


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: pip-build")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
