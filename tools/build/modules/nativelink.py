"""
Build System Module

Name: nativelink

Description:
NativeLink is an open source high-performance build cache and remote execution server, compatible with Bazel, Soong, Pants, Buck2, Reclient, and other RE-compatible build systems. It offers drastically faster builds, reduced test flakiness, and support for specialized hardware.

Homepage:
https://github.com/TraceMachina/nativelink
"""

import os
import subprocess

NAME = "nativelink"

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
