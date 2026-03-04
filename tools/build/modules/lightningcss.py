"""
Build System Module

Name: lightningcss

Description:
An extremely fast CSS parser, transformer, bundler, and minifier written in Rust.

Homepage:
https://github.com/parcel-bundler/lightningcss
"""

import os
import subprocess

NAME = "lightningcss"

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
