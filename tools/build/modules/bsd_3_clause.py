"""
Build System Module

Name: bsd 3-clause

Description:
Entropy Pooling in Python with a BSD 3-Clause license.

Homepage:
https://github.com/fortitudo-tech/entropy-pooling
"""

import os
import subprocess

NAME = "bsd 3-clause"

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
