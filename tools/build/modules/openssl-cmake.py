"""
Auto-generated build module
Build system: openssl-cmake

Description:
CMake wrapper for OpenSSL supporting cross-compilation

Homepage:
https://github.com/viaduck/openssl-cmake
"""

import os
import subprocess

INDICATORS = []

DEFAULT_COMMAND = ""


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: openssl-cmake")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
