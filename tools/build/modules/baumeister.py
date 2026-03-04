"""
Build System Module

Name: baumeister

Description:
Unmaintained – :construction_worker: The aim of this project is to help you to build your things. From Bootstrap themes over static websites to single page applications.

Homepage:
https://github.com/micromata/Baumeister
"""

import os
import subprocess

NAME = "baumeister"

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
