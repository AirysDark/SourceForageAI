"""
Build System Module

Name: bundler

Description:
Manage your Ruby application's gem dependencies

Homepage:
https://github.com/rubygems/bundler
"""

import os
import subprocess

NAME = "bundler"

INDICATORS = ['Gemfile']

DEFAULT_COMMAND = "bundle install"


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
