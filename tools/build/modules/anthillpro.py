"""
Build System Module

Name: anthillpro

Description:
The missing command-line utility for AnthillPro, a deploy, test, and release automation framework.

Homepage:
https://github.com/dylanmei/hilltop
"""

import os
import subprocess

NAME = "anthillpro"

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
