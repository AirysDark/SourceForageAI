"""
Build System Module

Name: parcel

Description:
The zero configuration build tool for the web. 📦🚀

Homepage:
https://github.com/parcel-bundler/parcel
"""

import os
import subprocess

NAME = "parcel"

INDICATORS = ['package.json']

DEFAULT_COMMAND = "parcel build"


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
