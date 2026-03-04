"""
Build System Module

Name: arduino

Description:
ESP8266 core for Arduino

Homepage:
https://github.com/esp8266/Arduino
"""

import os
import subprocess

NAME = "arduino"

INDICATORS = ['*.ino']

DEFAULT_COMMAND = "arduino-cli compile"


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
