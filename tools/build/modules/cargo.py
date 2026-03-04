"""
Build System Module

Name: cargo

Description:
The Rust package manager

Homepage:
https://github.com/rust-lang/cargo
"""

import os
import subprocess

NAME = "cargo"

INDICATORS = ['Cargo.toml']

DEFAULT_COMMAND = "cargo build"


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
