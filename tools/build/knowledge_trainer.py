#!/usr/bin/env python3

import json
from pathlib import Path
from collections import defaultdict

ROOT = Path(file).resolve().parents[2]

MEMORY_DIR = ROOT / "tools" / "ai_memory"
SUCCESS_DB = MEMORY_DIR / "success_db.json"

OUTPUT_DIR = ROOT / "tools" / "build"
KNOWLEDGE_FILE = OUTPUT_DIR / "knowledge_db.json"

def load_success_memory():

if not SUCCESS_DB.exists():
    print("No success memory found")
    return []

try:
    data = json.loads(SUCCESS_DB.read_text())
    return data
except Exception:
    return []

def extract_features(entry):

repo_tree = entry.get("repo_tree", "")
build_cmd = entry.get("build_command", "")
build_type = entry.get("build_type", "unknown")

indicators = []

files = repo_tree.split("\n")

for f in files:

    name = Path(f).name

    if name in [
        "Makefile",
        "CMakeLists.txt",
        "Cargo.toml",
        "package.json",
        "setup.py",
        "pyproject.toml",
        "meson.build",
        "WORKSPACE",
        "build.gradle",
        "pom.xml",
        "platformio.ini",
    ]:
        indicators.append(name)

return {
    "indicators": indicators,
    "command": build_cmd,
    "type": build_type,
}

def train_knowledge(data):

knowledge = defaultdict(lambda: defaultdict(int))

for entry in data:

    features = extract_features(entry)

    for indicator in features["indicators"]:

        cmd = features["command"]

        if cmd:
            knowledge[indicator][cmd] += 1

result = {}

for indicator, cmds in knowledge.items():

    best_cmd = max(cmds, key=cmds.get)

    result[indicator] = {
        "command": best_cmd,
        "count": cmds[best_cmd],
    }

return result

def save_knowledge(knowledge):

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

KNOWLEDGE_FILE.write_text(
    json.dumps(knowledge, indent=2)
)

print(f"Knowledge saved to {KNOWLEDGE_FILE}")

def main():

print("=== SourceForageAI Knowledge Trainer ===")

data = load_success_memory()

if not data:
    print("No training data available")
    return

print(f"Training from {len(data)} successful builds")

knowledge = train_knowledge(data)

save_knowledge(knowledge)

print("Training complete")

if name == "main":
main()