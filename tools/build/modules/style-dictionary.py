"""
Auto-generated build module
Build system: style-dictionary

Description:
A build system for creating cross-platform styles.

Homepage:
https://github.com/style-dictionary/style-dictionary
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

    print("Running build system: style-dictionary")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
