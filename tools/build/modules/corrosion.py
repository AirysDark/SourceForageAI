"""
Build System Module

Name: corrosion

Description:
Marrying Rust and CMake - Easy Rust and C/C++ Integration!

Homepage:
https://github.com/corrosion-rs/corrosion
"""

import os
import subprocess

NAME = "corrosion"

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
