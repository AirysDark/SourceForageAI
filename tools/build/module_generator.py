import re
import json
from pathlib import Path

# directory where modules are stored
MODULE_DIR = Path(__file__).parent / "modules"
MODULE_DIR.mkdir(parents=True, exist_ok=True)


TEMPLATE = '''
"""
Auto-generated build module
"""

NAME = {display_name}

INDICATORS = {indicators}

DEFAULT_COMMAND = {cmd}


def detect(repo_root="."):
    import os

    indicators = set(INDICATORS)

    for root, dirs, files in os.walk(repo_root):

        # check files
        for f in files:
            if f in indicators:
                return True

        # check directories
        for d in dirs:
            if d in indicators:
                return True

    return False


def build():
    import subprocess

    if not DEFAULT_COMMAND:
        print("No build command defined for", NAME)
        return 1

    try:
        result = subprocess.run(
            DEFAULT_COMMAND,
            shell=True,
            check=False
        )

        return result.returncode

    except Exception as e:
        print("Build failed:", e)
        return 1
'''


# ---------------------------------------------------
# Name sanitizer
# ---------------------------------------------------

def sanitize(name: str) -> str:
    """Convert arbitrary name into valid python module name"""

    name = name.lower()

    name = re.sub(r"[^a-z0-9]+", "_", name)

    name = re.sub(r"_+", "_", name)

    name = name.strip("_")

    if not name:
        name = "module"

    if name[0].isdigit():
        name = f"build_{name}"

    return name


# ---------------------------------------------------
# Module creator
# ---------------------------------------------------

def create_module(name, indicators=None, cmd=None, overwrite=False):
    """
    Create a build module file
    """

    indicators = indicators or []
    cmd = cmd or ""

    module_name = sanitize(name)

    filename = MODULE_DIR / f"{module_name}.py"

    if filename.exists() and not overwrite:
        print(f"Module already exists: {module_name}")
        return filename

    code = TEMPLATE.format(
        display_name=json.dumps(name),
        indicators=json.dumps(list(indicators)),
        cmd=json.dumps(cmd)
    )

    filename.write_text(code, encoding="utf-8")

    print(f"Created module: {filename}")

    return filename