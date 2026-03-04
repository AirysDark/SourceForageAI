"""
Build System Module

Name: mill

Description:
A better build tool for Java, Scala and Kotlin: Simpler than Maven, easier than Gradle, with 3-7x faster dev workflows than other JVM build tools

Homepage:
https://github.com/com-lihaoyi/mill
"""

import os
import subprocess

NAME = "mill"

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
