"""
Build System Module

Name: bob

Description:
Bob is a high-level build tool for multi-language projects.

Homepage:
https://github.com/benchkram/bob
"""

import os
import subprocess

NAME = "bob"

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
