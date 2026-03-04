"""
Auto-generated build module
Build system: build-harness

Description:
Collection of Makefiles to facilitate building Golang projects, Dockerfiles, Helm charts, and more

Homepage:
https://github.com/cloudposse/build-harness
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

    print("Running build system: build-harness")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
