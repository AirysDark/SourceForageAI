"""
Build System Module

Name: turborepo

Description:
Build system optimized for JavaScript and TypeScript, written in Rust

Homepage:
https://github.com/vercel/turborepo
"""

import os
import subprocess

NAME = "turborepo"

INDICATORS = ['turbo.json']

DEFAULT_COMMAND = "turbo run build"


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
