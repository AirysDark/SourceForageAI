"""
Build System Module

Name: build

Description:
The official build framework for the Armbian Linux distribution. This repository contains the complete toolchain and scripts required to compile custom OS images from source, including kernel configuration, U-Boot handling, and board-specific tweaks for various ARM and ARM64 single-board computers.

Homepage:
https://github.com/armbian/build
"""

import os
import subprocess

NAME = "build"

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
