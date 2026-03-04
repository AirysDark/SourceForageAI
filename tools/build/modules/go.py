"""
Build System Module

Name: go

Description:
The Go programming language

Homepage:
https://github.com/golang/go
"""

import os
import subprocess

NAME = "go"

INDICATORS = ['go.mod']

DEFAULT_COMMAND = "go build ./..."


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
