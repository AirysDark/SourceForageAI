import json
from pathlib import Path


REPORT_FILE = Path("system_test_report.json")

if not REPORT_FILE.exists():

    print("Report file not found")
    exit(1)


report = json.loads(REPORT_FILE.read_text())


print("\n===== SourceForageAI SYSTEM TEST REPORT =====\n")

summary = report["summary"]

for k, v in summary.items():
    print(f"{k}: {v}")


def print_section(title, items):

    if not items:
        return

    print(f"\n{title}\n")

    for item in items:
        print(item)


print_section("Python module failures", report["module_failures"])
print_section("Build module failures", report["build_module_failures"])
print_section("Workflow YAML failures", report["yaml_failures"])


print("\n=============================================\n")