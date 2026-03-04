import os


def scan_repo(repo_root="."):

    summary = {
        "files": set(),
        "extensions": set()
    }

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            summary["files"].add(f)

            ext = os.path.splitext(f)[1]

            if ext:
                summary["extensions"].add(ext)

    return summary