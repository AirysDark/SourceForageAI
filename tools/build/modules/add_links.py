"""
Build System Module

Name: add links

Description:
Generate add to calendar links for Google, iCal and other calendar systems

Homepage:
https://github.com/spatie/calendar-links
"""

import os
import subprocess

NAME = "add links"

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
