"""
Build System Module

Name: nx

Description:
The Monorepo Platform that amplifies both developers and AI agents. Nx optimizes your builds, scales your CI, and fixes failed PRs automatically. Ship in half the time.

Homepage:
https://github.com/nrwl/nx
"""

import os
import subprocess

NAME = "nx"

INDICATORS = ['nx.json']

DEFAULT_COMMAND = "nx build"


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
