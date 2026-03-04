"""
Build System Module

Name: mingw-builds

Description:
MinGW-W64 compiler binaries

Homepage:
https://github.com/niXman/mingw-builds-binaries
"""

import os
import subprocess

NAME = "mingw-builds"

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
