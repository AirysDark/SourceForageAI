"""
Build System Module

Name: mage

Description:
Prior to making any Submission(s), you must sign an Adobe Contributor License Agreement, available here at: https://opensource.adobe.com/cla.html. All Submissions you make to Adobe Inc. and its affiliates, assigns and subsidiaries (collectively “Adobe”) are subject to the terms of the Adobe Contributor License Agreement.

Homepage:
https://github.com/magento/magento2
"""

import os
import subprocess

NAME = "mage"

INDICATORS = ['magefile.go']

DEFAULT_COMMAND = "mage"


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
