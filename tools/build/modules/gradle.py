"""
Build System Module

Name: gradle

Description:
Adaptable, fast automation for all

Homepage:
https://github.com/gradle/gradle
"""

import os
import subprocess

NAME = "gradle"

INDICATORS = ['build.gradle', 'settings.gradle']

DEFAULT_COMMAND = "./gradlew build"


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
