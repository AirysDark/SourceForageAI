"""
Build System Module

Name: conform

Description:
Progressively enhance HTML forms with React. Build resilient, type-safe forms with no hassle using web standards.

Homepage:
https://github.com/edmundhung/conform
"""

import os
import subprocess

NAME = "conform"

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
