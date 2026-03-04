"""
Build System Module

Name: gulp

Description:
A toolkit to automate & enhance your workflow

Homepage:
https://github.com/gulpjs/gulp
"""

import os
import subprocess

NAME = "gulp"

INDICATORS = ['gulpfile.js']

DEFAULT_COMMAND = "gulp"


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
