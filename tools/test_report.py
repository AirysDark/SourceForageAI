import json
from pathlib import Path

report = json.loads(Path("system_test_report.json").read_text())

print("\n===== SourceForageAI TEST REPORT =====\n")

print("Python modules loaded:", len(report["python_modules"]))
print("Build modules detected:", len(report["build_modules"]))
print("Workflow files valid:", len(report["yaml_files"]))

if report["module_failures"]:
    print("\nPython module failures:")
    for f in report["module_failures"]:
        print(f)

if report["build_module_failures"]:
    print("\nBuild module failures:")
    for f in report["build_module_failures"]:
        print(f)

if report["yaml_failures"]:
    print("\nYAML failures:")
    for f in report["yaml_failures"]:
        print(f)

print("\n======================================")