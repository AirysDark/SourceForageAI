"""
Build System Module

Name: buildxl

Description:
Microsoft Build Accelerator

Homepage:
https://github.com/microsoft/BuildXL
"""

import os
import subprocess

NAME = "buildxl"

INDICATORS = ['config.dsc']

DEFAULT_COMMAND = "bxl build"


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
