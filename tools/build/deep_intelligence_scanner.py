#!/usr/bin/env python3

import ast
import json
from pathlib import Path

ROOT = Path(".")

REPORT = {
    "python_files": [],
    "imports": {},
    "classes": {},
    "functions": {},
    "entrypoints": [],
    "build_indicators": [],
    "scripts": []
}


# -----------------------------------------
# Detect build systems
# -----------------------------------------

BUILD_FILES = [
    "Makefile",
    "CMakeLists.txt",
    "Cargo.toml",
    "package.json",
    "pyproject.toml",
    "setup.py",
    "build.gradle",
    "pom.xml",
    "meson.build",
    "WORKSPACE",
]


def detect_build_indicators():

    for file in ROOT.rglob("*"):

        if file.name in BUILD_FILES:
            REPORT["build_indicators"].append(str(file))


# -----------------------------------------
# Python code analyzer
# -----------------------------------------

def analyze_python_file(path):

    try:
        tree = ast.parse(path.read_text())
    except Exception:
        return

    REPORT["python_files"].append(str(path))

    imports = []
    classes = []
    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

            if node.name == "main":
                REPORT["entrypoints"].append(str(path))


    REPORT["imports"][str(path)] = imports
    REPORT["classes"][str(path)] = classes
    REPORT["functions"][str(path)] = functions


# -----------------------------------------
# Script discovery
# -----------------------------------------

def detect_scripts():

    for file in ROOT.rglob("*"):

        if file.suffix in [".sh", ".bash"]:
            REPORT["scripts"].append(str(file))


# -----------------------------------------
# Scan repository
# -----------------------------------------

def scan_repo():

    print("Running Deep Intelligence Scan...\n")

    detect_build_indicators()
    detect_scripts()

    for py in ROOT.rglob("*.py"):
        analyze_python_file(py)


# -----------------------------------------
# Generate architecture map
# -----------------------------------------

def generate_architecture():

    print("\n=== MODULE RELATIONSHIPS ===\n")

    for file, imports in REPORT["imports"].items():

        if not imports:
            continue

        print(file)

        for i in imports:
            print("   ->", i)

        print()


# -----------------------------------------
# Print report
# -----------------------------------------

def print_report():

    print("\n=== BUILD INDICATORS ===")
    for f in REPORT["build_indicators"]:
        print(f)

    print("\n=== PYTHON FILES ===")
    for f in REPORT["python_files"]:
        print(f)

    print("\n=== ENTRYPOINTS ===")
    for e in REPORT["entrypoints"]:
        print(e)

    print("\n=== SCRIPTS ===")
    for s in REPORT["scripts"]:
        print(s)

    generate_architecture()


# -----------------------------------------
# Save JSON intelligence
# -----------------------------------------

def save_json():

    out = Path("repo_intelligence.json")

    out.write_text(json.dumps(REPORT, indent=2))

    print("\nSaved intelligence to repo_intelligence.json")


# -----------------------------------------
# Main
# -----------------------------------------

def main():

    scan_repo()

    print_report()

    save_json()


if __name__ == "__main__":
    main()