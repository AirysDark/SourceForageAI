"""
Build System Module

Name: modern.js

Description:
Cheatsheet for the JavaScript knowledge you will frequently encounter in modern projects.

Homepage:
https://github.com/mbeaudru/modern-js-cheatsheet
"""

import os
import subprocess

NAME = "modern.js"

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
