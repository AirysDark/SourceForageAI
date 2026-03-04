"""
Build System Module

Name: aseprite-macos-buildsh

Description:
Automated script to create latest release app (either beta, or release whichever is newer) of Aseprite for macOS

Homepage:
https://github.com/haxpor/aseprite-macos-buildsh
"""

import os
import subprocess

NAME = "aseprite-macos-buildsh"

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
