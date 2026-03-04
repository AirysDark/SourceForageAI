"""
Build System Module

Name: scons

Description:
SCons - a software construction tool

Homepage:
https://github.com/SCons/scons
"""

import os
import subprocess

NAME = "scons"

INDICATORS = ['SConstruct']

DEFAULT_COMMAND = "scons"


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
