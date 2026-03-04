"""
Build System Module

Name: npm

Description:
This repository is moving to: https://github.com/npm/cli

Homepage:
https://github.com/npm/npm
"""

import os
import subprocess

NAME = "npm"

INDICATORS = ['package.json']

DEFAULT_COMMAND = "npm install && npm run build"


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
