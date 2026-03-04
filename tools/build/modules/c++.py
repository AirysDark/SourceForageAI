"""
Auto-generated build module
Build system: c++

Description:
Collection of various algorithms in mathematics, machine learning, computer science, physics, etc implemented in C for educational purposes.

Homepage:
https://github.com/TheAlgorithms/C
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

    print("Running build system: c++")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
