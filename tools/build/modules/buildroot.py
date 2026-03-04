"""
Build System Module

Name: buildroot

Description:
Buildroot, making embedded Linux easy. Note that this is not the official repository, but only a mirror. The official Git repository is at https://gitlab.com/buildroot.org/buildroot/. Do not open issues or file pull requests here.

Homepage:
https://github.com/buildroot/buildroot
"""

import os
import subprocess

NAME = "buildroot"

INDICATORS = ['Config.in']

DEFAULT_COMMAND = "make"


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
