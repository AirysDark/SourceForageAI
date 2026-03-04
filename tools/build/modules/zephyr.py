"""
Build System Module

Name: zephyr

Description:
Primary Git Repository for the Zephyr Project. Zephyr is a new generation, scalable, optimized, secure RTOS for multiple hardware architectures.

Homepage:
https://github.com/zephyrproject-rtos/zephyr
"""

import os
import subprocess

NAME = "zephyr"

INDICATORS = ['west.yml']

DEFAULT_COMMAND = "west build"


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
