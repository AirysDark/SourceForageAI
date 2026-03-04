#!/usr/bin/env python3

import json
import requests
import re
import time
from pathlib import Path
from html.parser import HTMLParser


SCRIPT_DIR = Path(__file__).resolve().parent
BUILD_DIR = SCRIPT_DIR / "modules"
BUILD_DIR.mkdir(parents=True, exist_ok=True)

DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

JSON_FILE = DATA_DIR / "build_systems.json"

HEADERS = {
    "User-Agent": "SourceForageAI"
}


# -------------------------
# Logging
# -------------------------

def log(msg):
    print(msg, flush=True)


# -------------------------
# Safe module name
# -------------------------

def safe_name(name):

    name = name.lower()

    name = re.sub(r"[^a-z0-9]+", "_", name)

    name = re.sub(r"_+", "_", name)

    return name.strip("_")


# -------------------------
# Filter garbage names
# -------------------------

BAD_WORDS = {
    "wikipedia",
    "privacy",
    "terms",
    "developers",
    "articles",
    "categories",
    "about",
    "policy"
}


def valid_name(name):

    n = name.lower()

    if any(b in n for b in BAD_WORDS):
        return False

    if len(n) < 3:
        return False

    return True


# -------------------------
# Load existing data
# -------------------------

def load_local():

    if JSON_FILE.exists():

        try:

            log("Loading existing build_systems.json")

            return json.loads(JSON_FILE.read_text())

        except Exception:

            log("Corrupted JSON reset")

    return {"build_systems": []}


# -------------------------
# Wikipedia parser
# -------------------------

class LinkParser(HTMLParser):

    def __init__(self):

        super().__init__()

        self.links = []

    def handle_starttag(self, tag, attrs):

        if tag == "a":

            for a in attrs:

                if a[0] == "title":

                    self.links.append(a[1])


def fetch_wikipedia():

    log("Fetching Wikipedia build systems")

    url = "https://en.wikipedia.org/wiki/List_of_build_automation_software"

    systems = []

    try:

        r = requests.get(url, headers=HEADERS, timeout=20)

        parser = LinkParser()

        parser.feed(r.text)

        for name in parser.links:

            if not valid_name(name):
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

        log(f"Wikipedia systems discovered: {len(systems)}")

    except Exception as e:

        log(f"Wikipedia fetch failed: {e}")

    return systems


# -------------------------
# GitHub discovery
# -------------------------

def fetch_github():

    log("Searching GitHub")

    queries = [
        "topic:build-system",
        "topic:build-tool",
        "topic:build-automation"
    ]

    systems = []

    for q in queries:

        url = f"https://api.github.com/search/repositories?q={q}&per_page=50"

        try:

            r = requests.get(url, headers=HEADERS, timeout=20)

            if r.status_code == 403:

                log("GitHub rate limit hit ? sleeping 60s")

                time.sleep(60)

                continue

            data = r.json()

            items = data.get("items", [])

            for repo in items:

                name = repo["name"].lower()

                if not valid_name(name):
                    continue

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

            log(f"GitHub search failed: {e}")

    log(f"GitHub systems discovered: {len(systems)}")

    return systems


# -------------------------
# Guess commands
# -------------------------

COMMAND_MAP = {
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


def guess_commands(name):

    return COMMAND_MAP.get(name.lower(), "")


# -------------------------
# Guess indicator files
# -------------------------

INDICATOR_MAP = {
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


def guess_indicators(name):

    return INDICATOR_MAP.get(name.lower(), [])


# -------------------------
# Merge lists
# -------------------------

def merge(existing, new):

    seen = {x["name"] for x in existing}

    added = 0

    for sys in new:

        if sys["name"] in seen:
            continue

        sys["default_command"] = guess_commands(sys["name"])
        sys["indicator_files"] = guess_indicators(sys["name"])

        existing.append(sys)

        seen.add(sys["name"])

        added += 1

    log(f"New systems added: {added}")

    return existing


# -------------------------
# Generate modules
# -------------------------

def generate_modules(systems):

    created = 0

    for sys in systems:

        raw_name = sys["name"]

        module_name = safe_name(raw_name)

        file = BUILD_DIR / f"{module_name}.py"

        if file.exists():
            continue

        indicators = sys.get("indicator_files", [])
        cmd = sys.get("default_command", "")

        code = f'''
"""
Auto generated build module
"""

NAME = "{raw_name}"

INDICATORS = {indicators}

DEFAULT_COMMAND = "{cmd}"


def detect(repo_root="."):

    import os

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            if f in INDICATORS:
                return True

    return False


def build():

    import subprocess

    if not DEFAULT_COMMAND:
        print("No build command defined for", NAME)
        return 1

    result = subprocess.run(DEFAULT_COMMAND, shell=True)

    return result.returncode
'''

        file.write_text(code)

        created += 1

    log(f"Modules generated: {created}")


# -------------------------
# Main
# -------------------------

def main():

    log("SourceForageAI Autobuilder started")

    data = load_local()

    systems = data["build_systems"]

    log(f"Existing systems: {len(systems)}")

    wiki = fetch_wikipedia()

    gh = fetch_github()

    systems = merge(systems, wiki)

    systems = merge(systems, gh)

    data["build_systems"] = systems

    JSON_FILE.write_text(json.dumps(data, indent=2))

    log(f"Total systems stored: {len(systems)}")

    generate_modules(systems)

    log("Autobuilder finished")


if __name__ == "__main__":
    main()