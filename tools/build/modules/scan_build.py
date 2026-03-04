"""
Build System Module

Name: scan-build

Description:
An example project to experience the Build Scan® service of Develocity with Gradle builds.

Homepage:
https://github.com/gradle/gradle-build-scan-quickstart
"""

import os
import subprocess

NAME = "scan-build"

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
