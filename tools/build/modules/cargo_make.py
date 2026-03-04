"""
Build System Module

Name: cargo-make

Description:
Rust task runner and build tool.

Homepage:
https://github.com/sagiegurari/cargo-make
"""

import os
import subprocess

NAME = "cargo-make"

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
