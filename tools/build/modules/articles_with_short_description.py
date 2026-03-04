"""
Build System Module

Name: articles with short description

Description:
CSV file containing the article id, title, lat/lng coordinate, and short description for all English language Wikipedia articles with location data.

Homepage:
https://github.com/placemarkt/wiki_coordinates
"""

import os
import subprocess

NAME = "articles with short description"

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
