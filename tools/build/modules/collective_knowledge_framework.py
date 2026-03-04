"""
Build System Module

Name: collective knowledge framework

Description:
Android application to participate in experiment crowdsourcing (such as workload crowd-benchmarking and crowd-tuning) using Collective Knowledge Framework and open repositories of knowledge: 

Homepage:
https://github.com/ctuning/crowdsource-experiments-using-android-devices
"""

import os
import subprocess

NAME = "collective knowledge framework"

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
