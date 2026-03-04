"""
Build System Module

Name: ci pipelines

Description:
Train Schedule sample app for Jenkins Pipelines exercises

Homepage:
https://github.com/linuxacademy/cicd-pipeline-train-schedule-pipelines
"""

import os
import subprocess

NAME = "ci pipelines"

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
