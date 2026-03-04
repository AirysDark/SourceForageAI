"""
Build System Module

Name: realize

Description:
Realize is the #1 Golang Task Runner which enhance your workflow by automating the most common tasks and using the best performing Golang live reloading.

Homepage:
https://github.com/oxequa/realize
"""

import os
import subprocess

NAME = "realize"

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
