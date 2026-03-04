"""
Build System Module

Name: earthly

Description:
Super simple build framework with fast, repeatable builds and an instantly familiar syntax – like Dockerfile and Makefile had a baby.

Homepage:
https://github.com/earthly/earthly
"""

import os
import subprocess

NAME = "earthly"

INDICATORS = ['Earthfile']

DEFAULT_COMMAND = "earthly build"


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
