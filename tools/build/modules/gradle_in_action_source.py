"""
Build System Module

Name: gradle-in-action-source

Description:
Source code for the Manning book "Gradle in Action"

Homepage:
https://github.com/bmuschko/gradle-in-action-source
"""

import os
import subprocess

NAME = "gradle-in-action-source"

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
