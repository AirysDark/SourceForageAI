"""
Build System Module

Name: openssl-cmake

Description:
Build OpenSSL with CMake on MacOS, Win32, Win64 and cross compile for Android, IOS

Homepage:
https://github.com/janbar/openssl-cmake
"""

import os
import subprocess

NAME = "openssl-cmake"

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
