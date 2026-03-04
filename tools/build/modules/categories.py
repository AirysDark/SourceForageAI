"""
Build System Module

Name: categories

Description:
Side menu with some categories to choose.

Homepage:
https://github.com/Yalantis/Side-Menu.Android
"""

import os
import subprocess

NAME = "categories"

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
