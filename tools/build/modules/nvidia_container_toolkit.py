"""
Build System Module

Name: nvidia-container-toolkit

Description:
Build and run containers leveraging NVIDIA GPUs

Homepage:
https://github.com/NVIDIA/nvidia-container-toolkit
"""

import os
import subprocess

NAME = "nvidia-container-toolkit"

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
