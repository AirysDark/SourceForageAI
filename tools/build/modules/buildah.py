"""
Build System Module

Name: buildah

Description:
A tool that facilitates building OCI images.

Homepage:
https://github.com/containers/buildah
"""

import os
import subprocess

NAME = "buildah"

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
