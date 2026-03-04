"""
Auto-generated build module
Build system: flow-core-x

Description:
Powerful and user-friendly CI/CD server with high availability, parallel processing, runner auto-scaling 

Homepage:
https://github.com/FlowCI/flow-core-x
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

    print("Running build system: flow-core-x")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
