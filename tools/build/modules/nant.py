"""
Build System Module

Name: nant

Description:
NAnt is a free .NET build tool. In theory it is kind of like make without make's wrinkles.

Homepage:
https://github.com/nant/nant
"""

import os
import subprocess

NAME = "nant"

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
