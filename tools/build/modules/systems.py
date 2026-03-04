"""
Build System Module

Name: systems

Description:
A curated list to learn about distributed systems

Homepage:
https://github.com/theanalyst/awesome-distributed-systems
"""

import os
import subprocess

NAME = "systems"

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
