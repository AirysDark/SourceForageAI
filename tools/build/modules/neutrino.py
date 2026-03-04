"""
Build System Module

Name: neutrino

Description:
Create and build modern JavaScript projects with zero initial configuration.

Homepage:
https://github.com/neutrinojs/neutrino
"""

import os
import subprocess

NAME = "neutrino"

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
