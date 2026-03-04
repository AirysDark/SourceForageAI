"""
Build System Module

Name: pip-build

Description:
Advanced tutorial building a multibranch Pipeline project with selectively executed stages

Homepage:
https://github.com/jenkins-docs/building-a-multibranch-pipeline-project
"""

import os
import subprocess

NAME = "pip-build"

INDICATORS = ['pyproject.toml']

DEFAULT_COMMAND = "python -m build"


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
