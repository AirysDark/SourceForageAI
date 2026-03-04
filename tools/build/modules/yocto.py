"""
Build System Module

Name: yocto

Description:
Yocto/GL: Tiny C++ Libraries for Data-Driven Physically-based Graphics

Homepage:
https://github.com/xelatihy/yocto-gl
"""

import os
import subprocess

NAME = "yocto"

INDICATORS = ['bitbake.conf']

DEFAULT_COMMAND = "bitbake"


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
