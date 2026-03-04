"""
Build System Module

Name: rake

Description:
A make-like build utility for Ruby.

Homepage:
https://github.com/ruby/rake
"""

import os
import subprocess

NAME = "rake"

INDICATORS = ['Rakefile']

DEFAULT_COMMAND = "rake"


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
