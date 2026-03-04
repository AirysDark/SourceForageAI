"""
Build System Module

Name: qmake

Description:
A Simple & Strong Tool for TCP&UDP Debug

Homepage:
https://github.com/rangaofei/SSokit-qmake
"""

import os
import subprocess

NAME = "qmake"

INDICATORS = ['*.pro']

DEFAULT_COMMAND = "qmake && make"


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
