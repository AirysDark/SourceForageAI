"""
Build System Module

Name: buildactions

Description:
BuildActions for use with the SuperUnityBuild build automation tool.

Homepage:
https://github.com/superunitybuild/buildactions
"""

import os
import subprocess

NAME = "buildactions"

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
