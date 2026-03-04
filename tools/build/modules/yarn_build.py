"""
Build System Module

Name: yarn.build

Description:
Build 🛠 and Bundle 📦 your local workspaces. Like Bazel, Buck, Pants and Please but for Yarn Berry. Build any language, mix javascript, typescript, golang and more in one polyglot repo. Ship your bundles to AWS Lambda, Docker, or any nodejs runtime.

Homepage:
https://github.com/ojkelly/yarn.build
"""

import os
import subprocess

NAME = "yarn.build"

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
