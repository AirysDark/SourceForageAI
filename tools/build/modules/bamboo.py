"""
Build System Module

Name: bamboo

Description:
Testable, composable, and adapter based Elixir email library for devs that love piping.

Homepage:
https://github.com/beam-community/bamboo
"""

import os
import subprocess

NAME = "bamboo"

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
