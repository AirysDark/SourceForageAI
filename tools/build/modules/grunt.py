"""
Build System Module

Name: grunt

Description:
Grunt: The JavaScript Task Runner

Homepage:
https://github.com/gruntjs/grunt
"""

import os
import subprocess

NAME = "grunt"

INDICATORS = ['Gruntfile.js']

DEFAULT_COMMAND = "grunt"


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
