"""
Build System Module

Name: esp-idf

Description:
Espressif IoT Development Framework. Official development framework for Espressif SoCs.

Homepage:
https://github.com/espressif/esp-idf
"""

import os
import subprocess

NAME = "esp-idf"

INDICATORS = ['idf.py']

DEFAULT_COMMAND = "idf.py build"


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
