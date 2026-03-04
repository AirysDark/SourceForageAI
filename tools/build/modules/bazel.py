"""
Build System Module

Name: bazel

Description:
a fast, scalable, multi-language and extensible build system

Homepage:
https://github.com/bazelbuild/bazel
"""

import os
import subprocess

NAME = "bazel"

INDICATORS = ['WORKSPACE', 'BUILD']

DEFAULT_COMMAND = "bazel build //..."


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
