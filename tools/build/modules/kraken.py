"""
Build System Module

Name: kraken

Description:
Kraken CI is a continuous integration and testing system.

Homepage:
https://github.com/Kraken-CI/kraken
"""

import os
import subprocess

NAME = "kraken"

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
