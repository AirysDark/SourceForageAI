"""
Build System Module

Name: harness

Description:
Harness Open Source is an end-to-end developer platform with Source Control Management, CI/CD Pipelines, Hosted Developer Environments, and Artifact Registries.

Homepage:
https://github.com/harness/harness
"""

import os
import subprocess

NAME = "harness"

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
