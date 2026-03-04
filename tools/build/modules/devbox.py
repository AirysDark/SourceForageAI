"""
Build System Module

Name: devbox

Description:
Instant, easy, and predictable development environments

Homepage:
https://github.com/jetify-com/devbox
"""

import os
import subprocess

NAME = "devbox"

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
