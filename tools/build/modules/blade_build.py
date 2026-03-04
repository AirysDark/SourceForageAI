"""
Build System Module

Name: blade-build

Description:
Blade is a powerful build system from Tencent, supports many mainstream programming languages, such as C/C++, java, scala, python, protobuf...

Homepage:
https://github.com/blade-build/blade-build
"""

import os
import subprocess

NAME = "blade-build"

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
