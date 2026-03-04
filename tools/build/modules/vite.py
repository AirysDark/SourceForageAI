"""
Build System Module

Name: vite

Description:
Next generation frontend tooling. It's fast!

Homepage:
https://github.com/vitejs/vite
"""

import os
import subprocess

NAME = "vite"

INDICATORS = ['vite.config.js']

DEFAULT_COMMAND = "vite build"


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
