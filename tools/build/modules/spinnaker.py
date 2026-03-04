"""
Build System Module

Name: spinnaker

Description:
Spinnaker is an open source, multi-cloud continuous delivery platform for releasing software changes with high velocity and confidence.

Homepage:
https://github.com/spinnaker/spinnaker
"""

import os
import subprocess

NAME = "spinnaker"

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
