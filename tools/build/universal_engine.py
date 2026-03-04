import os
import subprocess

SIGNATURES = {
    "cmake": {
        "files": ["CMakeLists.txt"],
        "cmd": "cmake -B build && cmake --build build"
    },
    "make": {
        "files": ["Makefile", "makefile"],
        "cmd": "make -j"
    },
    "meson": {
        "files": ["meson.build"],
        "cmd": "meson setup build && ninja -C build"
    },
    "cargo": {
        "files": ["Cargo.toml"],
        "cmd": "cargo build"
    },
    "gradle": {
        "files": ["build.gradle", "settings.gradle"],
        "cmd": "./gradlew build"
    },
    "maven": {
        "files": ["pom.xml"],
        "cmd": "mvn package"
    },
    "bazel": {
        "files": ["WORKSPACE", "BUILD"],
        "cmd": "bazel build //..."
    },
    "node": {
        "files": ["package.json"],
        "cmd": "npm install && npm run build"
    },
    "python": {
        "files": ["setup.py", "pyproject.toml"],
        "cmd": "pip install -e ."
    },
    "go": {
        "files": ["go.mod"],
        "cmd": "go build ./..."
    }
}


def detect_build_system(repo_root="."):

    for root, dirs, files in os.walk(repo_root):

        for system, sig in SIGNATURES.items():

            for indicator in sig["files"]:

                if indicator in files:
                    return system

    return "unknown"


def run_build(repo_root="."):

    system = detect_build_system(repo_root)

    if system in SIGNATURES:

        cmd = SIGNATURES[system]["cmd"]

        print("Detected:", system)
        print("Running:", cmd)

        return subprocess.call(cmd, shell=True)

    return heuristic_build(repo_root)