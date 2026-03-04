"""
Build System Module

Name: developers

Description:
Curated list of design and UI resources from stock photos, web templates, CSS frameworks, UI libraries, tools and much more

Homepage:
https://github.com/bradtraversy/design-resources-for-developers
"""

import os
import subprocess

NAME = "developers"

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
