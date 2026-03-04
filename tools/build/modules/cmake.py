"""
Build System Module

Name: cmake

Description:
Mirror of CMake upstream repository

Homepage:
https://github.com/Kitware/CMake
"""

import os
import subprocess

NAME = "cmake"

INDICATORS = ['CMakeLists.txt']

DEFAULT_COMMAND = "cmake -B build && cmake --build build"


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
