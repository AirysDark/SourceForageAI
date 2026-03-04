
from pathlib import Path
import sys

ROOT = Path(".")
OUTDIR = ROOT / "repaired_files"
REPORT = ROOT / "repair_report.txt"
JSON_REPORT = ROOT / "repair_report.json"

IGNORE_DIRS = {
    "__pycache__", ".git", ".github",
    "venv", ".venv", "env",
    "node_modules", "dist", "build",
    "repaired_files"
}

STDLIB = set(sys.builtin_module_names)

COMMON_STDLIB = {
    "json","os","sys","pathlib","subprocess","tempfile","signal",
    "random","sqlite3","ast","collections","datetime","time",
    "uuid","http","math","itertools","functools","threading"
}

STDLIB.update(COMMON_STDLIB)

SAFE_PIP = {
    "requests","psutil","pyyaml","networkx"
}
