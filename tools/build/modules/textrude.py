"""
Build System Module

Name: textrude

Description:
Code generation from YAML/JSON/CSV models  via SCRIBAN templates

Homepage:
https://github.com/NeilMacMullen/Textrude
"""

import os
import subprocess

NAME = "textrude"

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
