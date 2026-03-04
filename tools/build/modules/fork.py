"""
Build System Module

Name: fork

Description:
a c# utility library. C#工具包，C#工具类，常用方法，系统API，文件处理、加密解密、Winform美化（C# Tools）

Homepage:
https://github.com/yuzhengyang/Fork
"""

import os
import subprocess

NAME = "fork"

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
