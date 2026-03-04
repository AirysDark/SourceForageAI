"""
Build System Module

Name: ant

Description:
An enterprise-class UI design language and React UI library

Homepage:
https://github.com/ant-design/ant-design
"""

import os
import subprocess

NAME = "ant"

INDICATORS = ['build.xml']

DEFAULT_COMMAND = "ant"


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
