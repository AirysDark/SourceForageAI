"""
Build System Module

Name: cmake_examples

Description:
Useful CMake Examples

Homepage:
https://github.com/ttroy50/cmake-examples
"""

import os
import subprocess

NAME = "cmake_examples"

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
