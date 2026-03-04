import os
import subprocess
from pathlib import Path


SIGNATURES = {
    "cmake": {
        "files": ["CMakeLists.txt"],
        "cmd": "cmake -B build && cmake --build build"
    },
    "make": {
        "files": ["Makefile", "makefile"],
        "cmd": "make -j$(nproc)"
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
        "cmd": "./gradlew build || gradle build"
    },
    "maven": {
        "files": ["pom.xml"],
        "cmd": "mvn -B package"
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


# -------------------------------
# Detect build systems
# -------------------------------

def detect_build_system(repo_root="."):

    repo_root = Path(repo_root)

    detected = set()

    for root, dirs, files in os.walk(repo_root):

        for system, sig in SIGNATURES.items():

            for indicator in sig["files"]:

                if indicator in files:
                    detected.add(system)

    if not detected:
        return ["unknown"]

    return list(detected)


# -------------------------------
# Execute command safely
# -------------------------------

def run_command(cmd, cwd):

    try:

        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=1800
        )

        return {
            "returncode": result.returncode,
            "stdout": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:

        return {
            "returncode": -1,
            "stderr": "build timeout"
        }


# -------------------------------
# Build runner
# -------------------------------

def run_build(repo_root="."):

    systems = detect_build_system(repo_root)

    print("Detected build systems:", systems)

    for system in systems:

        if system in SIGNATURES:

            cmd = SIGNATURES[system]["cmd"]

            print(f"Running build for {system}")
            print("Command:", cmd)

            result = run_command(cmd, repo_root)

            if result["returncode"] == 0:

                print("Build succeeded")
                return result

            else:

                print("Build failed")
                print(result["stderr"])

    return heuristic_build(repo_root)


# -------------------------------
# Heuristic fallback
# -------------------------------

def heuristic_build(repo_root):

    print("Running heuristic build")

    heuristics = [
        "pip install -r requirements.txt",
        "python setup.py install",
        "npm install",
        "make",
        "go build ./..."
    ]

    for cmd in heuristics:

        result = run_command(cmd, repo_root)

        if result["returncode"] == 0:

            print("Heuristic succeeded:", cmd)
            return result

    return {
        "returncode": 1,
        "stderr": "No build method succeeded"
    }