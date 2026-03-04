"""
Build System Module

Name: phing

Description:
PHing Is Not GNU make; it's a PHP project build system or build tool based on  Apache Ant.

Homepage:
https://github.com/phingofficial/phing
"""

import os
import subprocess

NAME = "phing"

INDICATORS = ['build.xml']

DEFAULT_COMMAND = "phing"


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
