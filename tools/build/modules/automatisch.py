"""
Build System Module

Name: automatisch

Description:
The open source Zapier alternative. Build workflow automation without spending time and money.

Homepage:
https://github.com/automatisch/automatisch
"""

import os
import subprocess

NAME = "automatisch"

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
