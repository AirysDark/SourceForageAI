"""
Build System Module

Name: awesome-test-automation

Description:
A curated list of awesome test automation frameworks, tools, libraries, and software for different programming languages. Sponsored by https://zapple.tech and https://automated-testing.info

Homepage:
https://github.com/atinfo/awesome-test-automation
"""

import os
import subprocess

NAME = "awesome-test-automation"

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
