"""
Build System Module

Name: lure

Description:
Lure - User Recon Automation for GoPhish

Homepage:
https://github.com/highmeh/lure
"""

import os
import subprocess

NAME = "lure"

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
