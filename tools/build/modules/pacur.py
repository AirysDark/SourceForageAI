"""
Build System Module

Name: pacur

Description:
Automated deb, rpm and pkgbuild build system

Homepage:
https://github.com/pacur/pacur
"""

import os
import subprocess

NAME = "pacur"

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
