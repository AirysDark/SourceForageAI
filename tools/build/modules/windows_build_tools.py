"""
Build System Module

Name: windows-build-tools

Description:
:package: Install C++ Build Tools for Windows using npm

Homepage:
https://github.com/felixrieseberg/windows-build-tools
"""

import os
import subprocess

NAME = "windows-build-tools"

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
