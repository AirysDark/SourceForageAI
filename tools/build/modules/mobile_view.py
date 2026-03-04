"""
Build System Module

Name: mobile view

Description:
Enhanced WebView component for Android that works as intended out of the box

Homepage:
https://github.com/delight-im/Android-AdvancedWebView
"""

import os
import subprocess

NAME = "mobile view"

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
