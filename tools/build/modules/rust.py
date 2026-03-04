"""
Build System Module

Name: rust

Description:
Empowering everyone to build reliable and efficient software.

Homepage:
https://github.com/rust-lang/rust
"""

import os
import subprocess

NAME = "rust"

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
