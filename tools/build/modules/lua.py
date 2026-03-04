"""
Build System Module

Name: lua

Description:
A copy of the Lua development repository, as seen by the Lua team. Mirrored irregularly. Please DO NOT send pull requests or any other stuff. All communication should be through the Lua mailing list https://www.lua.org/lua-l.html

Homepage:
https://github.com/lua/lua
"""

import os
import subprocess

NAME = "lua"

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
