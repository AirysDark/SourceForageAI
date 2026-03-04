"""
Build System Module

Name: padavan-builder-workflow

Description:
Automatic Padavan firmware builds using GitHub servers

Homepage:
https://github.com/shvchk/padavan-builder-workflow
"""

import os
import subprocess

NAME = "padavan-builder-workflow"

INDICATORS = []

DEFAULT_COMMAND = ""


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
