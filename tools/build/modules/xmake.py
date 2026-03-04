"""
Build System Module

Name: xmake

Description:
🔥 A cross-platform build utility based on Lua

Homepage:
https://github.com/xmake-io/xmake
"""

import os
import subprocess

NAME = "xmake"

INDICATORS = ['xmake.lua']

DEFAULT_COMMAND = "xmake"


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
