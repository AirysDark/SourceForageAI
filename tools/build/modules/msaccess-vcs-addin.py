"""
Auto-generated build module
Build system: msaccess-vcs-addin

Description:
Synchronize your Access Forms, Macros, Modules, Queries, Reports, and more with a version control system.

Homepage:
https://github.com/joyfullservice/msaccess-vcs-addin
"""

import os
import subprocess

INDICATORS = []

DEFAULT_COMMAND = ""


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: msaccess-vcs-addin")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
