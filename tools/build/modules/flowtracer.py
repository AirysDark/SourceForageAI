"""
Build System Module

Name: flowtracer

Description:
Trace information flow for inter-software comparisons in mass spectrometry-based bottom-up proteomics.

Homepage:
https://github.com/OKdll/flowTraceR
"""

import os
import subprocess

NAME = "flowtracer"

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
