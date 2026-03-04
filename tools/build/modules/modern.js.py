"""
Auto-generated build module
Build system: modern.js

Description:
A progressive web framework based on React and Rsbuild.

Homepage:
https://github.com/web-infra-dev/modern.js
"""

import os
import subprocess

INDICATORS = []

DEFAULT_COMMAND = ""


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: modern.js")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
