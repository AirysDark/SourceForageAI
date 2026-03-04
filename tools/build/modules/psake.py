"""
Build System Module

Name: psake

Description:
A build automation tool written in PowerShell

Homepage:
https://github.com/psake/psake
"""

import os
import subprocess

NAME = "psake"

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
