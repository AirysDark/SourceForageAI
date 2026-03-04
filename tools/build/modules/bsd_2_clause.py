"""
Build System Module

Name: bsd 2-clause

Description:
not mine!, BSD-2-clauses

Homepage:
https://github.com/prepare/opendiagram
"""

import os
import subprocess

NAME = "bsd 2-clause"

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
