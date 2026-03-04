"""
Build System Module

Name: meson

Description:
The Meson Build System

Homepage:
https://github.com/mesonbuild/meson
"""

import os
import subprocess

NAME = "meson"

INDICATORS = ['meson.build']

DEFAULT_COMMAND = "meson setup build && meson compile -C build"


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
