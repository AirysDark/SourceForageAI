"""
Build System Module

Name: asdf

Description:
Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more

Homepage:
https://github.com/asdf-vm/asdf
"""

import os
import subprocess

NAME = "asdf"

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
