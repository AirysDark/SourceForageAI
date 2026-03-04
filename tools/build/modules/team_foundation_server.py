"""
Build System Module

Name: team foundation server

Description:
Cross-platform CLI for Microsoft Team Foundation Server and Visual Studio Team Services

Homepage:
https://github.com/microsoft/tfs-cli
"""

import os
import subprocess

NAME = "team foundation server"

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
