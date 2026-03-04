"""
Build System Module

Name: make

Description:
git://git.savannah.gnu.org/make

Homepage:
https://github.com/mirror/make
"""

import os
import subprocess

NAME = "make"

INDICATORS = ['Makefile', 'makefile']

DEFAULT_COMMAND = "make -j"


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
