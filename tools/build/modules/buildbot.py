"""
Build System Module

Name: buildbot

Description:
Python-based continuous integration testing framework; your pull requests are more than welcome!

Homepage:
https://github.com/buildbot/buildbot
"""

import os
import subprocess

NAME = "buildbot"

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
