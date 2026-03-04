"""
Build System Module

Name: bitbake

Description:
The official bitbake Git is at https://git.openembedded.org/bitbake/. Do not open issues or file pull requests here.

Homepage:
https://github.com/openembedded/bitbake
"""

import os
import subprocess

NAME = "bitbake"

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
