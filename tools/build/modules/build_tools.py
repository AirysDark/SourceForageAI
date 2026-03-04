"""
Build System Module

Name: build_tools

Description:
Used to build ONLYOFFICE DocumentServer-related products

Homepage:
https://github.com/ONLYOFFICE/build_tools
"""

import os
import subprocess

NAME = "build_tools"

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
