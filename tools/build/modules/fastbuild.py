"""
Build System Module

Name: fastbuild

Description:
High performance build system for Windows, OSX and Linux. Supporting caching, network distribution and more.

Homepage:
https://github.com/fastbuild/fastbuild
"""

import os
import subprocess

NAME = "fastbuild"

INDICATORS = ['fbuild.bff']

DEFAULT_COMMAND = "fbuild"


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
