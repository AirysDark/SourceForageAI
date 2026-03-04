"""
Build System Module

Name: fake

Description:
FAKE - F# Make

Homepage:
https://github.com/fsprojects/FAKE
"""

import os
import subprocess

NAME = "fake"

INDICATORS = ['build.fsx']

DEFAULT_COMMAND = "fake run build.fsx"


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
