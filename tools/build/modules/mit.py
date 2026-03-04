"""
Build System Module

Name: mit

Description:
An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.

Homepage:
https://github.com/mitmproxy/mitmproxy
"""

import os
import subprocess

NAME = "mit"

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
