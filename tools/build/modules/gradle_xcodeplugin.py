"""
Build System Module

Name: gradle-xcodeplugin

Description:
gradle plugin for building Xcode Projects for iOS, watchOS, macOS or tvOS

Homepage:
https://github.com/openbakery/gradle-xcodePlugin
"""

import os
import subprocess

NAME = "gradle-xcodeplugin"

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
