"""
Build System Module

Name: mpw make

Description:
A simple wrapper written to make the use of Python multiprocessing easy to use

Homepage:
https://github.com/lodder/python_mpwrapper
"""

import os
import subprocess

NAME = "mpw make"

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
