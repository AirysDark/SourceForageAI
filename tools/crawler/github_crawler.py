import requests
import subprocess
import json
from pathlib import Path
import time

API = "https://api.github.com/search/repositories"

WORKDIR = Path("crawler_workspace")
WORKDIR.mkdir(exist_ok=True)

DB = Path("crawler_db.json")

HEADERS = {
    "User-Agent": "SourceForageAI"
}


QUERIES = [
    "language:C stars:>20",
    "language:Python stars:>20",
    "language:Rust stars:>20",
    "language:Go stars:>20",
    "topic:cli",
    "topic:library"
]


def load_db():

    if DB.exists():
        return json.loads(DB.read_text())

    return []


def save_db(data):

    DB.write_text(json.dumps(data, indent=2))


def discover_repositories():

    repos = []

    for q in QUERIES:

        r = requests.get(
            API,
            params={"q": q, "per_page": 20},
            headers=HEADERS
        )

        data = r.json()

        for item in data.get("items", []):

            repos.append(item["full_name"])

    return repos


def clone_repo(repo):

    path = WORKDIR / repo.replace("/", "_")

    if path.exists():
        return path

    subprocess.run([
        "git",
        "clone",
        "--depth",
        "1",
        f"https://github.com/{repo}.git",
        str(path)
    ])

    return path


def run_autobuilder(repo_path):

    subprocess.run([
        "python",
        "tools/ai_autobuilder.py"
    ], cwd=repo_path)


def main():

    db = load_db()

    repos = discover_repositories()

    for repo in repos:

        if repo in db:
            continue

        print("Building:", repo)

        path = clone_repo(repo)

        run_autobuilder(path)

        db.append(repo)

        save_db(db)

        time.sleep(3)


if __name__ == "__main__":
    main()