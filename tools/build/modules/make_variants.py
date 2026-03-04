"""
Build System Module

Name: make variants

Description:
Steamless is a DRM remover of the SteamStub variants.  The goal of Steamless is to make a single solution for unpacking all Steam DRM-packed files. Steamless aims to support as many games as possible. 

Homepage:
https://github.com/atom0s/Steamless
"""

import os
import subprocess

NAME = "make variants"

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
