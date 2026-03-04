Aimport os
from pathlib import Path


def scan_repo(repo_root="."):

    repo_root = Path(repo_root)

    summary = {
        "files": set(),
        "extensions": set(),
        "languages": set(),
        "build_files": set(),
        "dependency_files": set(),
        "ci_files": set(),
        "docker_files": set(),
        "python_imports": set(),
        "entrypoints": set(),
        "stats": {
            "total_files": 0,
            "python_files": 0
        }
    }

    BUILD_FILES = {
        "CMakeLists.txt": "cmake",
        "Makefile": "make",
        "build.gradle": "gradle",
        "pom.xml": "maven",
        "Cargo.toml": "cargo",
        "package.json": "npm",
        "pyproject.toml": "python",
        "setup.py": "python",
        "meson.build": "meson"
    }

    DEP_FILES = {
        "requirements.txt",
        "poetry.lock",
        "Pipfile",
        "environment.yml",
        "package-lock.json",
        "yarn.lock"
    }

    CI_KEYWORDS = [
        ".github/workflows",
        ".gitlab-ci.yml",
        "azure-pipelines.yml"
    ]

    for root, dirs, files in os.walk(repo_root):

        for f in files:

            summary["stats"]["total_files"] += 1

            summary["files"].add(f)

            ext = os.path.splitext(f)[1]

            if ext:
                summary["extensions"].add(ext)

            path = Path(root) / f

            # language detection
            if ext == ".py":
                summary["languages"].add("python")
                summary["stats"]["python_files"] += 1

                try:
                    with open(path, "r", errors="ignore") as file:

                        for line in file:

                            if line.startswith("import ") or line.startswith("from "):

                                summary["python_imports"].add(line.strip())

                            if "__main__" in line:
                                summary["entrypoints"].add(str(path))

                except:
                    pass

            if ext in [".cpp", ".cc", ".cxx", ".c"]:
                summary["languages"].add("cpp")

            if ext == ".rs":
                summary["languages"].add("rust")

            if ext == ".js":
                summary["languages"].add("javascript")

            if ext == ".go":
                summary["languages"].add("go")

            # build system detection
            if f in BUILD_FILES:
                summary["build_files"].add(BUILD_FILES[f])

            # dependency files
            if f in DEP_FILES:
                summary["dependency_files"].add(f)

            # docker detection
            if f == "Dockerfile":
                summary["docker_files"].add(str(path))

            # CI detection
            for ci in CI_KEYWORDS:
                if ci in str(path):
                    summary["ci_files"].add(ci)

    # convert sets → lists for JSON compatibility
    for key in summary:
        if isinstance(summary[key], set):
            summary[key] = list(summary[key])

    return summaryimport os


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