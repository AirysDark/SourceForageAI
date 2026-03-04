"""
Build System Module

Name: ci-detector

Description:
Detect continuous integration environment and get information of current build

Homepage:
https://github.com/OndraM/ci-detector
"""

import os
import subprocess

NAME = "ci-detector"

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
