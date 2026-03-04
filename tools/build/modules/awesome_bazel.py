"""
Build System Module

Name: awesome-bazel

Description:
A curated list of Bazel rules, tooling and resources.

Homepage:
https://github.com/jin/awesome-bazel
"""

import os
import subprocess

NAME = "awesome-bazel"

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
