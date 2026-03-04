"""
Build System Module

Name: jump to content

Description:
Code and other content related to Jumping Rivers blogs (https://www.jumpingrivers.com/blog/)

Homepage:
https://github.com/jumpingrivers/blog
"""

import os
import subprocess

NAME = "jump to content"

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
