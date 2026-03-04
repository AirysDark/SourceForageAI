"""
Build System Module

Name: integrated development environments

Description:
RStudio is an integrated development environment (IDE) for R

Homepage:
https://github.com/rstudio/rstudio
"""

import os
import subprocess

NAME = "integrated development environments"

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
