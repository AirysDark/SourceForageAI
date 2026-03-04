"""
Build System Module

Name: waf

Description:
使用Nginx+Lua实现的WAF（版本v1.0）

Homepage:
https://github.com/unixhot/waf
"""

import os
import subprocess

NAME = "waf"

INDICATORS = ['wscript']

DEFAULT_COMMAND = "./waf build"


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
