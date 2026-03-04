"""
Build System Module

Name: continuum

Description:
Continuous saving of tmux environment. Automatic restore when tmux is started. Automatic tmux start when computer is turned on.

Homepage:
https://github.com/tmux-plugins/tmux-continuum
"""

import os
import subprocess

NAME = "continuum"

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
