"""
Build System Module

Name: github-actions-react-native

Description:
📱 A template for your next React Native project: Expo, PNPM, TypeScript, TailwindCSS, Husky, EAS, GitHub Actions, Env Vars, expo-router, react-query, react-hook-form.

Homepage:
https://github.com/obytes/react-native-template-obytes
"""

import os
import subprocess

NAME = "github-actions-react-native"

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
