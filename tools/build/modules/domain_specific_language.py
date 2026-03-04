"""
Build System Module

Name: domain specific language

Description:
An MLIR-based compiler framework bridges DSLs (domain-specific languages) to DSAs (domain-specific architectures).

Homepage:
https://github.com/buddy-compiler/buddy-mlir
"""

import os
import subprocess

NAME = "domain specific language"

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
