"""
Build System Module

Name: tundra

Description:
Tundra is a code build system that tries to be accurate and fast for incremental builds

Homepage:
https://github.com/deplinenoise/tundra
"""

import os
import subprocess

NAME = "tundra"

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
