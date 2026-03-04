"""
Build System Module

Name: blade

Description:
:rocket: Lightning fast and elegant mvc framework for Java8

Homepage:
https://github.com/lets-blade/blade
"""

import os
import subprocess

NAME = "blade"

INDICATORS = ['BLADE_ROOT']

DEFAULT_COMMAND = "blade build"


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
