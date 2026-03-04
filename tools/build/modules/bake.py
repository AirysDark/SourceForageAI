"""
Build System Module

Name: bake

Description:
The Pokemon Go Bot, baking with community.

Homepage:
https://github.com/PokemonGoF/PokemonGo-Bot
"""

import os
import subprocess

NAME = "bake"

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
