"""
Build System Module

Name: zeus

Description:
NOT MY CODE! Zeus trojan horse - leaked in 2011, I am not the author. This repository is for study purposes only, do not message me about your lame hacking attempts. 

Homepage:
https://github.com/zeustrojancode/Zeus
"""

import os
import subprocess

NAME = "zeus"

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
