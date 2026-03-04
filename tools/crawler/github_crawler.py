import requests
import subprocess
import json
from pathlib import Path
import time
import os

API = "https://api.github.com/search/repositories"

WORKDIR = Path("crawler_workspace")
WORKDIR.mkdir(exist_ok=True)

DB = Path("crawler_db.json")

TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "User-Agent": "SourceForageAI"
}

if TOKEN:
    HEADERS["Authorization"] = f"Bearer {TOKEN}"


QUERIES = [
    "language:C stars:>20",
    "language:Python stars:>20",
    "language:Rust stars:>20",
    "language:Go stars:>20",
    "topic:cli",
    "topic:library"
]


MAX_REPOS = 50
PAGES = 3


# -----------------------------
# Database
# -----------------------------

def load_db():

    if DB.exists():
        return set(json.loads(DB.read_text()))

    return set()


def save_db(data):

    DB.write_text(json.dumps(list(data), indent=2))


# -----------------------------
# Discover repos
# -----------------------------

def discover_repositories():

    repos = []

    for q in QUERIES:

        print("Query:", q)

        for page in range(1, PAGES + 1):

            r = requests.get(
                API,
                params={
                    "q": q,
                    "per_page": 30,
                    "page": page
                },
                headers=HEADERS
            )

            if r.status_code != 200:

                print("GitHub API error:", r.text)
                return repos

            data = r.json()

            items = data.get("items", [])

            if not items:
                break

            for item in items:

                repos.append(item["full_name"])

                if len(repos) >= MAX_REPOS:
                    return repos

            time.sleep(1)

    return repos


# -----------------------------
# Clone repo
# -----------------------------

def clone_repo(repo):

    path = WORKDIR / repo.replace("/", "_")

    if path.exists():
        return path

    print("Cloning:", repo)

    subprocess.run([
        "git",
        "clone",
        "--depth",
        "1",
        f"https://github.com/{repo}.git",
        str(path)
    ])

    return path


# -----------------------------
# Run autobuilder
# -----------------------------

def run_autobuilder(repo_path):

    autobuilder = Path(__file__).resolve().parents[2] / "tools" / "ai_autobuilder.py"

    if not autobuilder.exists():
        print("Autobuilder not found")
        return

    print("Running autobuilder on", repo_path)

    subprocess.run([
        "python",
        str(autobuilder)
    ], cwd=repo_path)


# -----------------------------
# Main
# -----------------------------

def main():

    db = load_db()

    repos = discover_repositories()

    print("Discovered repos:", len(repos))

    for repo in repos:

        if repo in db:
            continue

        print("Processing:", repo)

        path = clone_repo(repo)

        run_autobuilder(path)

        db.add(repo)

        save_db(db)

        time.sleep(2)


if __name__ == "__main__":
    main()