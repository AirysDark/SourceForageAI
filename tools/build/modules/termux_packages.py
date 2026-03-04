"""
Build System Module

Name: termux-packages

Description:
A package build system for Termux.

Homepage:
https://github.com/termux/termux-packages
"""

import os
import subprocess

NAME = "termux-packages"

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
