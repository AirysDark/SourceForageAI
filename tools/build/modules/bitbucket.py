"""
Build System Module

Name: bitbucket

Description:
BitBucket API gem - bitbucket_rest_api

Homepage:
https://github.com/bitbucket-rest-api/bitbucket
"""

import os
import subprocess

NAME = "bitbucket"

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
