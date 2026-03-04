"""
Build System Module

Name: python-cmake-buildsystem

Description:
A cmake buildsystem for compiling Python

Homepage:
https://github.com/python-cmake-buildsystem/python-cmake-buildsystem
"""

import os
import subprocess

NAME = "python-cmake-buildsystem"

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
