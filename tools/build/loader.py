import os
import re
from pathlib import Path

BUILD_DIR = Path(__file__).parent


# -------------------------
# Logging helper
# -------------------------

def log(msg):
    print(f"[module-generator] {msg}", flush=True)


# -------------------------
# Safe module name
# -------------------------

def safe_name(name):

    name = name.lower()

    # replace invalid characters
    name = re.sub(r"[^a-z0-9_]+", "_", name)

    return name.strip("_")


# -------------------------
# Module template
# -------------------------

TEMPLATE = """
\"\"\"
Auto-generated build module

Name: {name}

Indicators:
{indicators}

Default command:
{cmd}
\"\"\"

import os
import subprocess

NAME = "{name}"

INDICATORS = {indicators}

DEFAULT_COMMAND = "{cmd}"


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

        print("No default command defined")
"""


# -------------------------
# Module creation
# -------------------------

def create_module(name, indicators, cmd):

    if not name:
        log("Invalid module name")
        return None

    module_name = safe_name(name)

    filename = BUILD_DIR / f"{module_name}.py"

    if filename.exists():

        log(f"Module already exists: {module_name}.py")

        return module_name

    if not isinstance(indicators, list):
        indicators = []

    indicators = list(set(indicators))

    code = TEMPLATE.format(
        name=module_name,
        indicators=indicators,
        cmd=cmd or ""
    )

    try:

        filename.write_text(code)

        log(f"Created module: {filename}")

        return module_name

    except Exception as e:

        log(f"Failed to create module: {e}")

        return None