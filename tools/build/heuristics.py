import subprocess
import os


FALLBACK_COMMANDS = [

    "make -j",
    "./configure && make -j",
    "cmake . && make -j",
    "pip install -e .",
    "cargo build",
    "go build ./...",
]


def heuristic_build(repo_root="."):

    print("Running heuristic build detection")

    for cmd in FALLBACK_COMMANDS:

        print("Trying:", cmd)

        r = subprocess.call(cmd, shell=True)

        if r == 0:
            print("Heuristic build succeeded")
            return 0

    print("Heuristic build failed")

    return 1