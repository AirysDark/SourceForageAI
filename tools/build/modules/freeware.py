"""
Build System Module

Name: freeware

Description:
cc65 - a freeware C compiler for 6502 based systems

Homepage:
https://github.com/cc65/cc65
"""

import os
import subprocess

NAME = "freeware"

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
