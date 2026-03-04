import re
from pathlib import Path

# directory where modules are stored
MODULE_DIR = Path(__file__).parent / "modules"
MODULE_DIR.mkdir(parents=True, exist_ok=True)


TEMPLATE = """
\"\"\"
Auto-generated build module
\"\"\"

NAME = "{display_name}"

INDICATORS = {indicators}

DEFAULT_COMMAND = "{cmd}"


def detect(repo_root="."):
    import os

    for root, dirs, files in os.walk(repo_root):

        # check file indicators
        for f in files:
            if f in INDICATORS:
                return True

        # check directory indicators
        for d in dirs:
            if d in INDICATORS:
                return True

    return False


def build():
    import subprocess

    if not DEFAULT_COMMAND:
        print("No build command defined for {display_name}")
        return 1

    result = subprocess.run(DEFAULT_COMMAND, shell=True)

    return result.returncode
"""


def sanitize(name: str) -> str:
    """Convert a name into a safe python module filename"""

    name = name.lower()

    # replace invalid characters
    name = re.sub(r"[^a-z0-9_]+", "_", name)

    # remove duplicate underscores
    name = re.sub(r"_+", "_", name)

    # trim underscores
    name = name.strip("_")

    # prevent starting with number
    if name and name[0].isdigit():
        name = f"build_{name}"

    return name


def create_module(name, indicators, cmd, overwrite=False):
    """Create a build module"""

    module_name = sanitize(name)

    filename = MODULE_DIR / f"{module_name}.py"

    if filename.exists() and not overwrite:
        print(f"Module already exists: {module_name}")
        return

    code = TEMPLATE.format(
        display_name=name,
        indicators=indicators,
        cmd=cmd
    )

    filename.write_text(code)

    print(f"Created module: {filename}")
