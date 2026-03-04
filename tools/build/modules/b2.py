"""
Build System Module

Name: b2

Description:
B2 makes it easy to build C++ projects, everywhere.

Homepage:
https://github.com/bfgroup/b2
"""

import os
import subprocess

NAME = "b2"

INDICATORS = ['Jamroot']

DEFAULT_COMMAND = "b2"


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
