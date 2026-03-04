"""
Build System Module

Name: aria2-build-msys2

Description:
aria2 build scripts on msys2 with custom patches.

Homepage:
https://github.com/myfreeer/aria2-build-msys2
"""

import os
import subprocess

NAME = "aria2-build-msys2"

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
