"""
Build System Module

Name: xrm-ci-framework

Description:
xRM CI Framework provides you with the tools automate the build and deployment of your CRM Solution. Using the framework to implement a fully automated DevOps pipeline will allow you to deploy more frequently with added consistency and quality.

Homepage:
https://github.com/WaelHamze/xrm-ci-framework
"""

import os
import subprocess

NAME = "xrm-ci-framework"

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
