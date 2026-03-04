"""
Build System Module

Name: dependencycheck

Description:
OWASP dependency-check is a software composition analysis utility that detects publicly disclosed vulnerabilities in application dependencies.

Homepage:
https://github.com/dependency-check/DependencyCheck
"""

import os
import subprocess

NAME = "dependencycheck"

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
