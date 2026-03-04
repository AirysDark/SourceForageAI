"""
Auto-generated build module
Build system: android-make

Description:


Homepage:

"""

import os
import subprocess

INDICATORS = ['Android.mk']

DEFAULT_COMMAND = "make"


def detect(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    print("Running build system: android-make")

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No default build command known")
