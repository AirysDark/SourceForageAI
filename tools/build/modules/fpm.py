"""
Build System Module

Name: fpm

Description:
Effing package management! Build packages for multiple platforms (deb, rpm, etc) with great ease and sanity.

Homepage:
https://github.com/jordansissel/fpm
"""

import os
import subprocess

NAME = "fpm"

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
