"""
Build System Module

Name: continuous integration

Description:
continuous integration and continuous delivery

Homepage:
https://github.com/cicdops/awesome-ciandcd
"""

import os
import subprocess

NAME = "continuous integration"

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
