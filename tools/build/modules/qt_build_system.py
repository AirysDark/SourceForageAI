"""
Build System Module

Name: qt build system

Description:
Build Library Management System With Python & PyQt5 & MySQL , Generating Excel Reports , Users , App Themes

Homepage:
https://github.com/Pythondeveloper6/Build-Library-Management-System-Python-PyQt5
"""

import os
import subprocess

NAME = "qt build system"

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
