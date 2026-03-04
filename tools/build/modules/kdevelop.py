"""
Build System Module

Name: kdevelop

Description:
Cross-platform IDE for C, C++, Python, QML/JavaScript and PHP

Homepage:
https://github.com/KDE/kdevelop
"""

import os
import subprocess

NAME = "kdevelop"

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
