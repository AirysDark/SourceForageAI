"""
Build System Module

Name: shake

Description:
Shake build system

Homepage:
https://github.com/ndmitchell/shake
"""

import os
import subprocess

NAME = "shake"

INDICATORS = ['Shakefile.hs']

DEFAULT_COMMAND = "shake"


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
