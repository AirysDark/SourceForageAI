"""
Build System Module

Name: 7z-build-nsis

Description:
7-zip build and package script with nsis script decompiling using ms visual studio

Homepage:
https://github.com/myfreeer/7z-build-nsis
"""

import os
import subprocess

NAME = "7z-build-nsis"

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
