import importlib
import json
import yaml
from pathlib import Path

ROOT = Path(".")
REPORT = {
    "python_modules": [],
    "module_failures": [],
    "build_modules": [],
    "build_module_failures": [],
    "yaml_files": [],
    "yaml_failures": [],
}


# --------------------------------
# Test Python modules
# --------------------------------

def test_python_modules():

    for file in ROOT.rglob("*.py"):

        if "__pycache__" in str(file):
            continue

        module = str(file).replace("/", ".").replace("\\", ".").replace(".py", "")

        try:
            importlib.import_module(module)
            REPORT["python_modules"].append(module)

        except Exception as e:
            REPORT["module_failures"].append({
                "module": module,
                "error": str(e)
            })


# --------------------------------
# Test build modules
# --------------------------------

def test_build_modules():

    module_dir = ROOT / "tools" / "build" / "modules"

    if not module_dir.exists():
        return

    for file in module_dir.glob("*.py"):

        module = f"tools.build.modules.{file.stem}"

        try:

            m = importlib.import_module(module)

            if hasattr(m, "detect"):
                REPORT["build_modules"].append(module)

        except Exception as e:

            REPORT["build_module_failures"].append({
                "module": module,
                "error": str(e)
            })


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
# Run all tests
# --------------------------------

def run():

    print("Running SourceForageAI system tests")

    test_python_modules()
    test_build_modules()
    test_yaml()

    out = ROOT / "system_test_report.json"

    out.write_text(json.dumps(REPORT, indent=2))

    print("Report saved:", out)


if __name__ == "__main__":
    run()