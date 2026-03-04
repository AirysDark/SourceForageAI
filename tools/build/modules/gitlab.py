"""
Build System Module

Name: gitlab

Description:
GitLab CE Mirror | Please open new issues in our issue tracker on GitLab.com

Homepage:
https://github.com/gitlabhq/gitlabhq
"""

import os
import subprocess

NAME = "gitlab"

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
