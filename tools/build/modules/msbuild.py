"""
Build System Module

Name: msbuild

Description:
The Microsoft Build Engine (MSBuild) is the build platform for .NET and Visual Studio.

Homepage:
https://github.com/dotnet/msbuild
"""

import os
import subprocess

NAME = "msbuild"

INDICATORS = ['*.sln']

DEFAULT_COMMAND = "msbuild"


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
