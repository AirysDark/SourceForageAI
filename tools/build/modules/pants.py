"""
Build System Module

Name: pants

Description:
The Pants Build System

Homepage:
https://github.com/pantsbuild/pants
"""

import os
import subprocess

NAME = "pants"

INDICATORS = ['pants.toml']

DEFAULT_COMMAND = "pants build"


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
