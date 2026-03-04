"""
Build System Module

Name: flubucore

Description:
A cross platform build and deployment automation system for building projects and executing deployment scripts using C# code.

Homepage:
https://github.com/dotnetcore/FlubuCore
"""

import os
import subprocess

NAME = "flubucore"

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
