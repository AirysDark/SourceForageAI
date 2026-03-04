"""
Build System Module

Name: rsbuild

Description:
Simple, fast, extensible build tool. Powered by Rspack 🦀

Homepage:
https://github.com/web-infra-dev/rsbuild
"""

import os
import subprocess

NAME = "rsbuild"

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
