"""
Build System Module

Name: rspack

Description:
The fast Rust-based JavaScript bundler with a modernized webpack API 🦀

Homepage:
https://github.com/web-infra-dev/rspack
"""

import os
import subprocess

NAME = "rspack"

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
