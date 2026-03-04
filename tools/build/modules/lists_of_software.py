"""
Build System Module

Name: lists of software

Description:
A collective list of free APIs

Homepage:
https://github.com/public-apis/public-apis
"""

import os
import subprocess

NAME = "lists of software"

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
