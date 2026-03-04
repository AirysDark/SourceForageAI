"""
Build System Module

Name: dotnet

Description:
This repo is the official home of .NET on GitHub. It's a great starting point to find many .NET OSS projects from Microsoft and the community, including many that are part of the .NET Foundation.

Homepage:
https://github.com/microsoft/dotnet
"""

import os
import subprocess

NAME = "dotnet"

INDICATORS = ['*.csproj']

DEFAULT_COMMAND = "dotnet build"


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
