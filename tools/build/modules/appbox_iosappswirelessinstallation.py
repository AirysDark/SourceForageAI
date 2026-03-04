"""
Build System Module

Name: appbox-iosappswirelessinstallation

Description:
AppBox is a tool for iOS developers to deploy Development, Ad-Hoc, and In-house (Enterprise) applications directly to the devices from your Dropbox account. Check WebServices Status - https://status.getappbox.com

Homepage:
https://github.com/getappbox/AppBox-iOSAppsWirelessInstallation
"""

import os
import subprocess

NAME = "appbox-iosappswirelessinstallation"

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
