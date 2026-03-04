import subprocess
from pathlib import Path

MAX_ATTEMPTS = 200


COMMON_COMMANDS = [

    # make
    "make -j$(nproc)",
    "make",

    # cmake
    "cmake -B build && cmake --build build",
    "cmake . && make",

    # meson
    "meson setup build && ninja -C build",

    # ninja
    "ninja",

    # rust
    "cargo build",
    "cargo build --release",

    # go
    "go build ./...",

    # python
    "pip install -r requirements.txt",
    "pip install -e .",
    "python setup.py build",

    # node
    "npm install",
    "npm install && npm run build",

    # java
    "gradle build",
    "mvn package",

    # autotools
    "./configure && make",
]


# ---------------------------------------------------
# Detect languages used in repo
# ---------------------------------------------------

def detect_languages(repo):

    repo = Path(repo)

    langs = set()

    if list(repo.rglob("*.rs")):
        langs.add("rust")

    if list(repo.rglob("*.go")):
        langs.add("go")

    if list(repo.rglob("*.py")):
        langs.add("python")

    if list(repo.rglob("*.c")) or list(repo.rglob("*.cpp")):
        langs.add("c")

    if (repo / "package.json").exists():
        langs.add("node")

    if (repo / "pom.xml").exists():
        langs.add("java")

    return langs


# ---------------------------------------------------
# Language specific commands
# ---------------------------------------------------

def language_commands(lang):

    mapping = {

        "rust": [
            "cargo build",
            "cargo build --release"
        ],

        "go": [
            "go build ./..."
        ],

        "python": [
            "pip install -e .",
            "pip install -r requirements.txt",
            "python setup.py build"
        ],

        "node": [
            "npm install",
            "npm install && npm run build"
        ],

        "c": [
            "gcc *.c -o program",
            "clang *.c -o program",
            "make"
        ],

        "java": [
            "mvn package",
            "gradle build"
        ]
    }

    return mapping.get(lang, [])


# ---------------------------------------------------
# Discover shell scripts
# ---------------------------------------------------

def discover_scripts(repo):

    repo = Path(repo)

    scripts = []

    for file in repo.rglob("*.sh"):

        scripts.append(f"bash {file}")

    # build scripts
    for name in ["build.sh", "compile.sh", "run_build.sh"]:

        path = repo / name

        if path.exists():
            scripts.append(f"bash {name}")

    return scripts


# ---------------------------------------------------
# Extract commands from README
# ---------------------------------------------------

def discover_readme_commands(repo):

    repo = Path(repo)

    commands = []

    readme_files = list(repo.glob("README*"))

    for readme in readme_files:

        try:

            text = readme.read_text(errors="ignore")

            if "make" in text:
                commands.append("make")

            if "cmake" in text:
                commands.append("cmake -B build && cmake --build build")

            if "cargo build" in text:
                commands.append("cargo build")

            if "npm install" in text:
                commands.append("npm install && npm run build")

        except Exception:
            pass

    return commands


# ---------------------------------------------------
# Extract commands from CI pipelines
# ---------------------------------------------------

def discover_ci_commands(repo):

    repo = Path(repo)

    commands = []

    ci_dir = repo / ".github" / "workflows"

    if not ci_dir.exists():
        return commands

    for file in ci_dir.glob("*.yml"):

        try:

            text = file.read_text()

            for line in text.splitlines():

                if "run:" in line:

                    cmd = line.split("run:")[-1].strip()

                    commands.append(cmd)

        except Exception:
            pass

    return commands


# ---------------------------------------------------
# Generate build command list
# ---------------------------------------------------

def synthesize_commands(repo):

    repo = Path(repo)

    commands = []

    commands.extend(COMMON_COMMANDS)

    # language commands
    langs = detect_languages(repo)

    for lang in langs:

        commands.extend(language_commands(lang))

    # scripts
    commands.extend(discover_scripts(repo))

    # README hints
    commands.extend(discover_readme_commands(repo))

    # CI hints
    commands.extend(discover_ci_commands(repo))

    # remove duplicates
    seen = set()
    unique = []

    for cmd in commands:

        cmd = cmd.strip()

        if cmd and cmd not in seen:

            unique.append(cmd)

            seen.add(cmd)

    return unique


# ---------------------------------------------------
# Try commands until one works
# ---------------------------------------------------

def try_commands(repo):

    repo = Path(repo)

    commands = synthesize_commands(repo)

    attempts = 0

    for cmd in commands:

        if attempts >= MAX_ATTEMPTS:
            break

        attempts += 1

        print(f"[Synthesizer] Trying: {cmd}")

        try:

            result = subprocess.run(
                cmd,
                shell=True,
                cwd=repo
            )

            if result.returncode == 0:

                print(f"[Synthesizer] SUCCESS: {cmd}")

                return cmd

        except Exception as e:

            print("[Synthesizer] Error:", e)

    print("[Synthesizer] No command succeeded")

    return None