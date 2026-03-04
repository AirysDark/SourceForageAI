"""
Build System Module

Name: buck

Description:
A fast build system that encourages the creation of small, reusable modules over a variety of platforms and languages.

Homepage:
https://github.com/facebook/buck
"""

import os
import subprocess

NAME = "buck"

INDICATORS = ['BUCK']

DEFAULT_COMMAND = "buck build"


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
