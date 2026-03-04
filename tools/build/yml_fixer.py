#!/usr/bin/env python3

import yaml
import json
import requests
from pathlib import Path

WORKFLOW_DIR = Path(".github/workflows")
SCHEMA_FILE = Path("tools/build/yml_schema_db.json")

GITHUB_API = "https://api.github.com"

--------------------------------------------------

Load YAML safely

--------------------------------------------------

def load_yaml(file):

try:
    with open(file, "r") as f:
        return yaml.safe_load(f)

except Exception:
    return None

--------------------------------------------------

Save YAML

--------------------------------------------------

def save_yaml(file, data):

with open(file, "w") as f:
    yaml.dump(data, f, sort_keys=False)

--------------------------------------------------

Load schema database

--------------------------------------------------

def load_schema():

if SCHEMA_FILE.exists():

    try:
        return json.loads(SCHEMA_FILE.read_text())
    except Exception:
        pass

return {
    "top_keys": {},
    "job_keys": {},
    "step_keys": {}
}

--------------------------------------------------

Save schema database

--------------------------------------------------

def save_schema(schema):

SCHEMA_FILE.parent.mkdir(parents=True, exist_ok=True)

SCHEMA_FILE.write_text(
    json.dumps(schema, indent=2)
)

--------------------------------------------------

Learn structure from workflow

--------------------------------------------------

def learn_structure(schema, data):

if not isinstance(data, dict):
    return

for k in data.keys():
    schema["top_keys"][k] = schema["top_keys"].get(k, 0) + 1

jobs = data.get("jobs")

if isinstance(jobs, dict):

    for job in jobs.values():

        if not isinstance(job, dict):
            continue

        for k in job.keys():
            schema["job_keys"][k] = schema["job_keys"].get(k, 0) + 1

        steps = job.get("steps")

        if isinstance(steps, list):

            for step in steps:

                if not isinstance(step, dict):
                    continue

                for k in step.keys():
                    schema["step_keys"][k] = schema["step_keys"].get(k, 0) + 1

--------------------------------------------------

Scrape GitHub workflows

--------------------------------------------------

def scrape_github(schema, repo):

print("Learning from repo:", repo)

url = f"{GITHUB_API}/repos/{repo}/contents/.github/workflows"

r = requests.get(url)

if r.status_code != 200:
    return

files = r.json()

for f in files:

    if not f["name"].endswith((".yml", ".yaml")):
        continue

    raw = requests.get(f["download_url"])

    try:
        data = yaml.safe_load(raw.text)
        learn_structure(schema, data)
    except Exception:
        pass

--------------------------------------------------

Validate workflow

--------------------------------------------------

def validate_structure(data):

if not isinstance(data, dict):
    return False

required = ["name", "on", "jobs"]

for r in required:

    if r not in data:
        return False

return True

--------------------------------------------------

Fix common problems

--------------------------------------------------

def fix_common_issues(data):

if not isinstance(data, dict):
    data = {}

if "name" not in data:
    data["name"] = "AI Generated Workflow"

if "on" not in data:
    data["on"] = {"workflow_dispatch": None}

if "jobs" not in data:
    data["jobs"] = {}

return data

--------------------------------------------------

Process local workflows

--------------------------------------------------

def process_file(schema, file):

print("Checking", file)

data = load_yaml(file)

if data is None:
    print("Invalid YAML")
    return

learn_structure(schema, data)

if validate_structure(data):
    print("Valid workflow")
    return

print("Repairing workflow")

fixed = fix_common_issues(data)

save_yaml(file, fixed)

print("Repaired", file)

--------------------------------------------------

Main

--------------------------------------------------

def main():

schema = load_schema()

# Learn from popular repositories

popular = [
    "actions/runner",
    "actions/checkout",
    "microsoft/vscode",
    "tensorflow/tensorflow",
    "pytorch/pytorch"
]

for repo in popular:
    scrape_github(schema, repo)

if WORKFLOW_DIR.exists():

    for file in WORKFLOW_DIR.glob("*.yml"):
        process_file(schema, file)

save_schema(schema)

print("Schema database updated")

if name == "main":
main()