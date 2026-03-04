"""
Auto-generated build module
Build system: perforce jam

Description:
JamPlus is a very fast code and data build system derived from the original Perforce version of Jam

Homepage:
https://github.com/jamplus/jamplus
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

    print("Running build system: perforce jam")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
