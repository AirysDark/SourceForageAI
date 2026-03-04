"""
Build System Module

Name: redo

Description:
📘  OpenAPI/Swagger-generated API Reference Documentation

Homepage:
https://github.com/Redocly/redoc
"""

import os
import subprocess

NAME = "redo"

INDICATORS = ['redo.do']

DEFAULT_COMMAND = "redo"


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
