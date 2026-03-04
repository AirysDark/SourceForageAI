"""
Build System Module

Name: buck2

Description:
Build system, successor to Buck

Homepage:
https://github.com/facebook/buck2
"""

import os
import subprocess

NAME = "buck2"

INDICATORS = ['BUCK']

DEFAULT_COMMAND = "buck2 build"


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
