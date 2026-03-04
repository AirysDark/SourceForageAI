"""
Build System Module

Name: about wikipedia

Description:
tweet about anonymous Wikipedia edits from particular IP address ranges

Homepage:
https://github.com/edsu/anon
"""

import os
import subprocess

NAME = "about wikipedia"

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
