"""
Build System Module

Name: gn

Description:
Must-read papers on graph neural networks (GNN)

Homepage:
https://github.com/thunlp/GNNPapers
"""

import os
import subprocess

NAME = "gn"

INDICATORS = ['BUILD.gn']

DEFAULT_COMMAND = "gn gen out && ninja -C out"


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
