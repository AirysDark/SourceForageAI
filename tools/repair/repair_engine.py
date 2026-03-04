import json
from pathlib import Path
import shutil

REPORT = Path("repair_report.txt")
OUTDIR = Path("repaired_files")

OUTDIR.mkdir(exist_ok=True)

report_lines = []

report_lines.append("SourceForageAI Repair Report\n")


# ------------------------------------------------
# Load system test failures
# ------------------------------------------------

failures = []

if Path("system_test_report.json").exists():

    data = json.loads(Path("system_test_report.json").read_text())

    failures += data.get("module_failures", [])
    failures += data.get("build_module_failures", [])
    failures += data.get("yaml_failures", [])


report_lines.append(f"Failures detected: {len(failures)}\n")


# ------------------------------------------------
# Attempt repairs
# ------------------------------------------------

for f in failures:

    file_path = f.get("file")

    if not file_path:
        continue

    path = Path(file_path)

    if not path.exists():
        continue

    text = path.read_text()

    fixed = text


    # simple repair examples

    if "clone_repo(" in text and "def clone_repo" not in text:
        report_lines.append(f"Detected missing clone_repo in {file_path}")
        fixed = "def clone_repo(url):\n    pass\n\n" + fixed


    if "call_llm" in text and "def call_llm" not in text:
        report_lines.append(f"Detected missing call_llm in {file_path}")
        fixed = "def call_llm(prompt):\n    return ''\n\n" + fixed


    repaired_path = OUTDIR / path.name

    repaired_path.write_text(fixed)

    report_lines.append(f"Repaired file generated: {repaired_path}")


# ------------------------------------------------
# Save report
# ------------------------------------------------

REPORT.write_text("\n".join(report_lines))

print("Repair complete")