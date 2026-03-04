"""
Auto-generated build module
Build system: nginx-builder

Description:
A tool to build deb or rpm package of required Nginx version from the source code, with the ability to connect third-party modules. Nginx parameters are set in the yaml configuration file.

Homepage:
https://github.com/Tinkoff/Nginx-builder
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

    print("Running build system: nginx-builder")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
