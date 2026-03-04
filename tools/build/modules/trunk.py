"""
Build System Module

Name: trunk

Description:
Build, bundle & ship your Rust WASM application to the web.

Homepage:
https://github.com/trunk-rs/trunk
"""

import os
import subprocess

NAME = "trunk"

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
