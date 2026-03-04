"""
Build System Module

Name: task

Description:
A fast, cross-platform build tool inspired by Make, designed for modern workflows.

Homepage:
https://github.com/go-task/task
"""

import os
import subprocess

NAME = "task"

INDICATORS = ['Taskfile.yml']

DEFAULT_COMMAND = "task"


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
