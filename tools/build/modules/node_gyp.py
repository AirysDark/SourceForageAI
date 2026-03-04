"""
Build System Module

Name: node-gyp

Description:
Node.js native addon build tool

Homepage:
https://github.com/nodejs/node-gyp
"""

import os
import subprocess

NAME = "node-gyp"

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
