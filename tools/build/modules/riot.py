"""
Build System Module

Name: riot

Description:
RIOT -  The friendly OS for IoT

Homepage:
https://github.com/RIOT-OS/RIOT
"""

import os
import subprocess

NAME = "riot"

INDICATORS = ['Makefile']

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
