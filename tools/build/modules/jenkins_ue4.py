"""
Build System Module

Name: jenkins-ue4

Description:
Automated Unreal Engine 4 Project Builds

Homepage:
https://github.com/skymapgames/jenkins-ue4
"""

import os
import subprocess

NAME = "jenkins-ue4"

INDICATORS = []

DEFAULT_COMMAND = ""


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
