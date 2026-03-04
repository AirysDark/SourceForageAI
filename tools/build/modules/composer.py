"""
Build System Module

Name: composer

Description:
Dependency Manager for PHP

Homepage:
https://github.com/composer/composer
"""

import os
import subprocess

NAME = "composer"

INDICATORS = ['composer.json']

DEFAULT_COMMAND = "composer install"


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
