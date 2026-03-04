"""
Build System Module

Name: ninja

Description:
a small build system with a focus on speed

Homepage:
https://github.com/ninja-build/ninja
"""

import os
import subprocess

NAME = "ninja"

INDICATORS = ['build.ninja']

DEFAULT_COMMAND = "ninja"


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
