import json
from pathlib import Path

DB = Path("tools/build/build_patterns.json")


def store_pattern(files, command):

    if DB.exists():
        data = json.loads(DB.read_text())
    else:
        data = []

    data.append({
        "files": files,
        "cmd": command
    })

    DB.write_text(json.dumps(data, indent=2))