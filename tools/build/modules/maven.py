"""
Build System Module

Name: maven

Description:
Apache Maven core

Homepage:
https://github.com/apache/maven
"""

import os
import subprocess

NAME = "maven"

INDICATORS = ['pom.xml']

DEFAULT_COMMAND = "mvn package"


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
