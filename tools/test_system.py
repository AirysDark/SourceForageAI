import sys
import json
import yaml
import importlib
import importlib.util
from pathlib import Path
from time import time


ROOT = Path(__file__).resolve().parents[1]

# ensure project root is importable
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


# --------------------------------
# Utility: safe module loader
# --------------------------------

def load_module_from_path(path: Path):
    """Safely load module regardless of filename"""

    try:
        spec = importlib.util.spec_from_file_location(path.stem, path)

        module = importlib.util.module_from_spec(spec)

        spec.loader.exec_module(module)

        return module, None

    except Exception as e:
        return None, str(e)


# --------------------------------
# Test Python modules
# --------------------------------

def test_python_modules():

    for file in ROOT.rglob("*.py"):

        if "__pycache__" in str(file):
            continue

        if ".github" in str(file):
            continue

        module, error = load_module_from_path(file)

        if error:

            REPORT["module_failures"].append({
                "file": str(file),
                "error": error
            })

        else:

            REPORT["python_modules"].append(str(file))


# --------------------------------
# Test build modules
# --------------------------------

def test_build_modules():

    module_dir = ROOT / "tools" / "build" / "modules"

    if not module_dir.exists():
        return

    for file in module_dir.glob("*.py"):

        module, error = load_module_from_path(file)

        if error:

            REPORT["build_module_failures"].append({
                "file": str(file),
                "error": error
            })

            continue

        if hasattr(module, "detect"):
            REPORT["build_modules"].append(file.stem)


# --------------------------------
# Validate YAML workflows
# --------------------------------

def test_yaml():

    workflow_dir = ROOT / ".github" / "workflows"

    if not workflow_dir.exists():
        return

    for file in workflow_dir.glob("*.yml"):

        try:

            yaml.safe_load(file.read_text())

            REPORT["yaml_files"].append(str(file))

        except Exception as e:

            REPORT["yaml_failures"].append({
                "file": str(file),
                "error": str(e)
            })


# --------------------------------
# Summary
# --------------------------------

def build_summary(start_time):

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
            round(time() - start_time, 2)
    }


# --------------------------------
# Run all tests
# --------------------------------

def run():

    print("Running SourceForageAI system tests")

    start = time()

    test_python_modules()

    test_build_modules()

    test_yaml()

    build_summary(start)

    out = ROOT / "system_test_report.json"

    out.write_text(json.dumps(REPORT, indent=2))

    print("Report saved:", out)

    print("\nSummary:")

    for k, v in REPORT["summary"].items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    run()