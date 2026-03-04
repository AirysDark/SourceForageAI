"""
Build System Module

Name: swift-llbuild

Description:
A low-level build system, used by Xcode and the Swift Package Manager

Homepage:
https://github.com/swiftlang/swift-llbuild
"""

import os
import subprocess

NAME = "swift-llbuild"

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
