"""
Auto-generated build module
Build system: git-commit-id-maven-plugin

Description:
Maven plugin which includes build-time git repository information into an POJO / *.properties). Make your apps tell you which version exactly they were built from! Priceless in large distributed deployments... :-)

Homepage:
https://github.com/git-commit-id/git-commit-id-maven-plugin
"""

import os
import subprocess

INDICATORS = []

DEFAULT_COMMAND = ""


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: git-commit-id-maven-plugin")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
