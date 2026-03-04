import os
import re
from pathlib import Path

REPO_ROOT = Path(".")


# ---------------------------------------
# Scan repository files
# ---------------------------------------

def scan_repo():

    files = []
    extensions = set()

    for root, dirs, fs in os.walk(REPO_ROOT):

        for f in fs:

            files.append(f)

            ext = Path(f).suffix

            if ext:
                extensions.add(ext)

    return files, list(extensions)


# ---------------------------------------
# Parse README for build instructions
# ---------------------------------------

def scan_readme():

    readme_files = [
        "README.md",
        "README",
        "readme.md"
    ]

    patterns = [
        r"make\s+-j",
        r"cmake\s+.+",
        r"cargo\s+build",
        r"npm\s+install",
        r"npm\s+run\s+build",
        r"pip\s+install",
        r"go\s+build",
        r"gradle\s+build",
        r"mvn\s+package"
    ]

    for r in readme_files:

        p = REPO_ROOT / r

        if not p.exists():
            continue

        text = p.read_text(errors="ignore")

        for pat in patterns:

            m = re.search(pat, text, re.IGNORECASE)

            if m:
                return m.group(0)

    return None


# ---------------------------------------
# Inspect CI workflows
# ---------------------------------------

def scan_ci():

    ci_dirs = [
        ".github/workflows",
        ".gitlab-ci.yml",
        ".circleci"
    ]

    commands = []

    for d in ci_dirs:

        p = REPO_ROOT / d

        if not p.exists():
            continue

        if p.is_file():

            text = p.read_text(errors="ignore")

            commands += extract_commands(text)

        else:

            for f in p.rglob("*"):

                try:

                    text = f.read_text(errors="ignore")

                    commands += extract_commands(text)

                except:
                    pass

    return commands


def extract_commands(text):

    patterns = [
        r"make\s+-j",
        r"cmake\s+.+",
        r"cargo\s+build",
        r"npm\s+install",
        r"npm\s+run\s+build",
        r"pip\s+install",
        r"go\s+build",
        r"gradle\s+build",
        r"mvn\s+package"
    ]

    found = []

    for p in patterns:

        for m in re.findall(p, text, re.IGNORECASE):

            found.append(m)

    return found


# ---------------------------------------
# Dockerfile build detection
# ---------------------------------------

def scan_dockerfile():

    docker = REPO_ROOT / "Dockerfile"

    if not docker.exists():
        return None

    text = docker.read_text(errors="ignore")

    cmds = re.findall(r"RUN\s+(.+)", text)

    return cmds


# ---------------------------------------
# Predict build command
# ---------------------------------------

def predict_build():

    files, extensions = scan_repo()

    # direct indicators

    if "Cargo.toml" in files:
        return "cargo build"

    if "go.mod" in files:
        return "go build ./..."

    if "package.json" in files:
        return "npm install && npm run build"

    if "pyproject.toml" in files or "setup.py" in files:
        return "pip install -e ."

    if "pom.xml" in files:
        return "mvn package"

    if "build.gradle" in files:
        return "./grad