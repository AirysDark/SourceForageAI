"""
Auto-generated build module
Build system: mingw-builds

Description:
Scripts for building the 32 and 64-bit MinGW-W64 compilers for Windows

Homepage:
https://github.com/niXman/mingw-builds
"""

import os
import subprocess

INDICATORS = []

DEFAULT_COMMAND = ""


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: mingw-builds")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
