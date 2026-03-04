"""
Build System Module

Name: android-make

Description:
Contains a script that assembles FFmpeg library for Android 

Homepage:
https://github.com/Javernaut/ffmpeg-android-maker
"""

import os
import subprocess

NAME = "android-make"

INDICATORS = ['Android.mk']

DEFAULT_COMMAND = "make"


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
