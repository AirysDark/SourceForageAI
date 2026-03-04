"""
Build System Module

Name: bsd

Description:
bsdiff and bspatch are libraries for building and applying patches to binary files.

Homepage:
https://github.com/mendsley/bsdiff
"""

import os
import subprocess

NAME = "bsd"

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
