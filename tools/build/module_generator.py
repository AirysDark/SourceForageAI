import re
from pathlib import Path

# directory where modules are stored
MODULE_DIR = Path(__file__).parent / "modules"
MODULE_DIR.mkdir(parents=True, exist_ok=True)


TEMPLATE = """
\"\"\"
Auto-generated build module
\"\"\"

NAME = "{name}"

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

    if DEFAULT_COMMAND:
        subprocess.run(DEFAULT_COMMAND, shell=True)
    else:
        print("No build command defined for {name}")
"""


def sanitize(name):
    """Make safe python filename"""
    name = name.lower()
    name = re.sub(r"[^a-z0-9_]+", "_", name)
    return name


def create_module(name, indicators, cmd):

    name = sanitize(name)

    filename = MODULE_DIR / f"{name}.py"

    if filename.exists():
        print(f"Module already exists: {name}")
        return

    code = TEMPLATE.format(
        name=name,
        indicators=indicators,
        cmd=cmd
    )

    filename.write_text(code)

    print(f"Created module: {filename}")