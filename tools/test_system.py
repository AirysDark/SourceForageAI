import sys
import json
import yaml
import importlib.util
from pathlib import Path
from time import time


ROOT = Path(__file__).resolve().parents[1]

sys.path.insert(0, str(ROOT))


REPORT = {
    "summary": {},
    "python_modules": [],
    "module_failures": [],
    "build_modules": [],
    "build_module_failures": [],
    "yaml_files": [],
    "yaml_failures": [],
}


SKIP_DIRS = {
    "__pycache__",
    ".git",
    "venv",
    ".venv",
    "node_modules",
    "dist",
    "build"
}


# --------------------------------
# Safe module loader
# --------------------------------

def load_module(path: Path):

    try:

        spec = importlib.util.spec_from_file_location(path.stem, path)

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        return module, None

    except Exception as e:

        return None, str(e)


# --------------------------------
# Python module tests
# --------------------------------

def test_python_modules():

    for file in ROOT.rglob("*.py"):

        if any(x in file.parts for x in SKIP_DIRS):
            continue

        module, error = load_module(file)

        if error:

            REPORT["module_failures"].append({
                "file": str(file),
                "error": error
            })

        else:

            REPORT["python_modules"].append(str(file))


# --------------------------------
# Build module validation
# --------------------------------

def test_build_modules():

    module_dir = ROOT / "tools" / "build" / "modules"

    if not module_dir.exists():
        return

    for file in module_dir.glob("*.py"):

        module, error = load_module(file)

        if error:

            REPORT["build_module_failures"].append({
                "file": str(file),
                "error": error
            })

            continue

        required = [
            "NAME",
            "INDICATORS",
            "DEFAULT_COMMAND",
            "detect"
        ]

        missing = [x for x in required if not hasattr(module, x)]

        if missing:

            REPORT["build_module_failures"].append({
                "file": str(file),
                "error": f"missing attributes {missing}"
            })

        else:

            REPORT["build_modules"].append(module.NAME)


# --------------------------------
# YAML workflow validation
# --------------------------------

def test_yaml():

    workflow_dir = ROOT / ".github" / "workflows"

    if not workflow_dir.exists():
        return

    for file in workflow_dir.glob("*.yml"):

        try:

            data = yaml.safe_load(file.read_text())

            if not isinstance(data, dict):
                raise Exception("invalid root structure")

            required = ["name", "on", "jobs"]

            for r in required:
                if r not in data:
                    raise Exception(f"missing key: {r}")

            REPORT["yaml_files"].append(str(file))

        except Exception as e:

            REPORT["yaml_failures"].append({
                "file": str(file),
                "error": str(e)
            })


# --------------------------------
# Build summary
# --------------------------------

def build_summary(start):

    REPORT["summary"] = {

        "python_modules_loaded":
            len(REPORT["python_modules"]),

        "python_module_failures":
            len(REPORT["module_failures"]),

        "build_modules_detected":
            len(REPORT["build_modules"]),

        "build_module_failures":
            len(REPORT["build_module_failures"]),

        "yaml_files_valid":
            len(REPORT["yaml_files"]),

        "yaml_failures":
            len(REPORT["yaml_failures"]),

        "runtime_seconds":
            round(time() - start, 2)
    }


# --------------------------------
# Run tests
# --------------------------------

def run():

    print("\nRunning SourceForageAI system tests\n")

    start = time()

    test_python_modules()
    test_build_modules()
    test_yaml()

    build_summary(start)

    report_file = ROOT / "system_test_report.json"

    report_file.write_text(json.dumps(REPORT, indent=2))

    print("Report saved:", report_file)

    print("\nSummary\n")

    for k, v in REPORT["summary"].items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    run()