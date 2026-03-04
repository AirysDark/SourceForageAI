"""
Build System Module

Name: android_build

Description:
A useful tool for building android artifacts via Github Action

Homepage:
https://github.com/Wsine/android_builder
"""

import os
import subprocess

NAME = "android_build"

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
