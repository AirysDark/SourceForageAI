"""
Build System Module

Name: pnpm

Description:


Homepage:

"""

import os
import subprocess

NAME = "pnpm"

INDICATORS = ['pnpm-lock.yaml']

DEFAULT_COMMAND = "pnpm build"


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
