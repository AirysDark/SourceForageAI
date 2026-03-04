#!/usr/bin/env python3

import json
import os
import requests
import re
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
BUILD_DIR = SCRIPT_DIR / "build"
BUILD_DIR.mkdir(exist_ok=True)

JSON_FILE = BUILD_DIR / "build_systems.json"

HEADERS = {
    "User-Agent": "AI-Autobuilder"
}


# -------------------------
# Logging helper
# -------------------------

def log(msg):
    print(msg, flush=True)


# -------------------------
# Safe filename
# -------------------------

def safe_name(name):
    name = name.lower()
    name = re.sub(r"[^a-z0-9_]+", "_", name)
    return name.strip("_")


# -------------------------
# Load JSON
# -------------------------

def load_local():

    if JSON_FILE.exists():

        log("Loading existing build_systems.json")

        try:
            with open(JSON_FILE) as f:
                return json.load(f)
        except Exception:
            log("JSON corrupted, resetting")

    return {"build_systems": []}


# -------------------------
# Wikipedia discovery
# -------------------------

def fetch_wikipedia():

    log("Fetching Wikipedia build systems")

    url = "https://en.wikipedia.org/wiki/List_of_build_automation_software"

    systems = []

    try:

        r = requests.get(url, headers=HEADERS, timeout=20)

        names = re.findall(r'>([A-Za-z0-9\-\+ ]+)</a>', r.text)

        for name in names:

            name = name.strip()

            if len(name) < 3:
                continue

            systems.append({
                "name": name.lower(),
                "category": "build-system",
                "source": "wikipedia",
                "description": "",
                "homepage": "",
                "repo": "",
                "language": "",
                "stars": 0,
                "topics": [],
                "indicator_files": [],
                "default_command": "",
                "confidence_weight": 0.3
            })

        log(f"Wikipedia systems found: {len(systems)}")

    except Exception as e:

        log(f"Wikipedia fetch failed: {e}")

    return systems


# -------------------------
# GitHub discovery
# -------------------------

def fetch_github():

    log("Searching GitHub")

    systems = []

    queries = [
        "topic:build-system",
        "topic:build-tool",
        "topic:build-automation"
    ]

    for q in queries:

        log(f"GitHub query: {q}")

        url = f"https://api.github.com/search/repositories?q={q}&per_page=50"

        try:

            r = requests.get(url, headers=HEADERS, timeout=20)

            data = r.json()

            items = data.get("items", [])

            log(f"Repositories found: {len(items)}")

            for repo in items:

                name = repo["name"].lower()

                systems.append({
                    "name": name,
                    "category": "build-system",
                    "source": "github",
                    "description": repo.get("description", ""),
                    "homepage": repo.get("html_url", ""),
                    "repo": repo.get("html_url", ""),
                    "language": repo.get("language", ""),
                    "stars": repo.get("stargazers_count", 0),
                    "topics": repo.get("topics", []),
                    "indicator_files": [],
                    "default_command": "",
                    "confidence_weight": 0.2
                })

        except Exception as e:

            log(f"GitHub query failed: {e}")

    log(f"GitHub systems collected: {len(systems)}")

    return systems


# -------------------------
# Guess commands
# -------------------------

def guess_commands(name):

    mapping = {
        "make": "make -j",
        "cmake": "cmake -B build && cmake --build build",
        "cargo": "cargo build",
        "gradle": "./gradlew build",
        "maven": "mvn package",
        "bazel": "bazel build //...",
        "meson": "meson setup build && ninja -C build",
        "ninja": "ninja",
        "scons": "scons"
    }

    return mapping.get(name.lower(), "")


# -------------------------
# Guess indicator files
# -------------------------

def guess_indicators(name):

    mapping = {
        "make": ["Makefile"],
        "cmake": ["CMakeLists.txt"],
        "cargo": ["Cargo.toml"],
        "gradle": ["build.gradle"],
        "maven": ["pom.xml"],
        "bazel": ["WORKSPACE"],
        "meson": ["meson.build"],
        "ninja": ["build.ninja"],
        "scons": ["SConstruct"]
    }

    return mapping.get(name.lower(), [])


# -------------------------
# Enrich metadata
# -------------------------

def enrich_system_information(systems):

    log("Enriching metadata from GitHub")

    total = len(systems)

    for i, sys in enumerate(systems):

        name = sys.get("name")

        log(f"[{i+1}/{total}] Enriching: {name}")

        try:

            url = f"https://api.github.com/search/repositories?q={name}&per_page=1"

            r = requests.get(url, headers=HEADERS, timeout=20)

            if r.status_code == 403:
                log("GitHub rate limit reached. Sleeping 60s.")
                time.sleep(60)
                continue

            data = r.json()

            items = data.get("items", [])

            if not items:
                continue

            repo = items[0]

            sys["description"] = repo.get("description", "")
            sys["homepage"] = repo.get("html_url", "")
            sys["repo"] = repo.get("html_url", "")
            sys["language"] = repo.get("language", "")
            sys["stars"] = repo.get("stargazers_count", 0)
            sys["topics"] = repo.get("topics", [])

        except Exception as e:

            log(f"Metadata fetch failed for {name}: {e}")

    return systems


# -------------------------
# Merge systems
# -------------------------

def merge(local, new):

    log("Merging system lists")

    seen = {x["name"] for x in local}

    added = 0

    for sys in new:

        if sys["name"] not in seen:

            sys["default_command"] = guess_commands(sys["name"])
            sys["indicator_files"] = guess_indicators(sys["name"])

            local.append(sys)

            seen.add(sys["name"])

            added += 1

    log(f"New systems added: {added}")

    return local


# -------------------------
# Generate modules
# -------------------------

def generate_modules(systems):

    log("Generating build modules")

    total = len(systems)

    for i, system in enumerate(systems):

        raw_name = system.get("name", "unknown")

        name = safe_name(raw_name)

        log(f"[{i+1}/{total}] Generating module: {name}.py")

        indicators = system.get("indicator_files", [])
        command = system.get("default_command", "")
        desc = system.get("description", "")
        homepage = system.get("homepage", "")

        module_file = BUILD_DIR / f"{name}.py"

        code = f'''"""
Build System Module

Name: {raw_name}

Description:
{desc}

Homepage:
{homepage}
"""

import os
import subprocess

NAME = "{raw_name}"

INDICATORS = {indicators}

DEFAULT_COMMAND = "{command}"


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
'''

        module_file.write_text(code)

    return total


# -------------------------
# Main
# -------------------------

def main():

    log("AI Autobuilder Generator Started")

    data = load_local()

    systems = data.get("build_systems", [])

    log(f"Existing systems: {len(systems)}")

    wiki = fetch_wikipedia()
    gh = fetch_github()

    systems = merge(systems, wiki)
    systems = merge(systems, gh)

    systems = enrich_system_information(systems)

    data["build_systems"] = systems

    log("Saving build_systems.json")

    with open(JSON_FILE, "w") as f:
        json.dump(data, f, indent=2)

    log(f"Total systems stored: {len(systems)}")

    created = generate_modules(systems)

    log(f"Modules generated: {created}")

    log(f"Output directory: {BUILD_DIR}")

    log("AI Autobuilder Generator Finished")


if __name__ == "__main__":
    main()