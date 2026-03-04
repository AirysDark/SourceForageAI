"""
Build System Module

Name: gnome builder

Description:
Read-only mirror of https://gitlab.gnome.org/GNOME/gnome-builder

Homepage:
https://github.com/GNOME/gnome-builder
"""

import os
import subprocess

NAME = "gnome builder"

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
