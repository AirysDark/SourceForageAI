"""
Build System Module

Name: openwrt

Description:
This repository is a mirror of https://git.openwrt.org/openwrt/openwrt.git It is for reference only and is not active for check-ins.  We will continue to accept Pull Requests here. They will be merged via staging trees then into openwrt.git.

Homepage:
https://github.com/openwrt/openwrt
"""

import os
import subprocess

NAME = "openwrt"

INDICATORS = ['rules.mk']

DEFAULT_COMMAND = "make"


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
