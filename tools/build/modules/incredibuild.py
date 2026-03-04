"""
Build System Module

Name: incredibuild

Description:
Incredibuild 无限试用

Homepage:
https://github.com/mafagan/pojie
"""

import os
import subprocess

NAME = "incredibuild"

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
