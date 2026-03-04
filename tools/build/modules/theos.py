"""
Build System Module

Name: theos

Description:
A cross-platform suite of tools for building and deploying software for iOS and other platforms.

Homepage:
https://github.com/theos/theos
"""

import os
import subprocess

NAME = "theos"

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
