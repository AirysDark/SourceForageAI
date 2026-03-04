"""
Build System Module

Name: terms of use

Description:
Current and prior versions of the terms that apply to your use of the Unity Editor software.

Homepage:
https://github.com/Unity-Technologies/TermsOfService
"""

import os
import subprocess

NAME = "terms of use"

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
