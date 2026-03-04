"""
Build System Module

Name: just

Description:
🤖 Just a command runner

Homepage:
https://github.com/casey/just
"""

import os
import subprocess

NAME = "just"

INDICATORS = ['justfile']

DEFAULT_COMMAND = "just"


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
