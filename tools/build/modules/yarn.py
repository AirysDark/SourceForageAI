"""
Build System Module

Name: yarn

Description:
The 1.x line is frozen - features and bugfixes now happen on https://github.com/yarnpkg/berry

Homepage:
https://github.com/yarnpkg/yarn
"""

import os
import subprocess

NAME = "yarn"

INDICATORS = ['yarn.lock']

DEFAULT_COMMAND = "yarn build"


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
