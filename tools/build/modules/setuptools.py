"""
Build System Module

Name: setuptools

Description:
Official project repository for the Setuptools build system

Homepage:
https://github.com/pypa/setuptools
"""

import os
import subprocess

NAME = "setuptools"

INDICATORS = ['setup.py']

DEFAULT_COMMAND = "python setup.py build"


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
