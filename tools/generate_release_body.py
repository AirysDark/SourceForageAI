import json
import os
from pathlib import Path
from datetime import datetime

workflow = os.getenv("GITHUB_WORKFLOW", "SourceForageAI Workflow")
run_id = os.getenv("GITHUB_RUN_ID", "")
repo = os.getenv("GITHUB_REPOSITORY", "")

body = []

body.append(f"{workflow} Report")
body.append("")
body.append(f"Repository: {repo}")
body.append(f"Run ID: {run_id}")
body.append(f"Generated: {datetime.utcnow().isoformat()} UTC")
body.append("")


def read_lines(file, limit=50):
    try:
        lines = Path(file).read_text().splitlines()
        if len(lines) > limit:
            return lines[:limit] + ["... truncated ..."]
        return lines
    except Exception as e:
        return [f"Failed to read {file}: {e}"]


# ------------------------------------------------
# System Test Report
# ------------------------------------------------

if Path("system_test_report.json").exists():

    body.append("System Test Results\n")

    try:

        r = json.load(open("system_test_report.json"))

        summary = r.get("summary", {})

        for k, v in summary.items():
            body.append(f"{k}: {v}")

        errors = []
        errors += r.get("module_failures", [])
        errors += r.get("build_module_failures", [])
        errors += r.get("yaml_failures", [])

        body.append("")
        body.append("Key Errors:\n")

        if errors:
            for e in errors[:20]:
                body.append(str(e))
        else:
            body.append("No errors detected")

    except Exception as e:

        body.append("System test parsing failed")
        body.append(str(e))

    body.append("")


# ------------------------------------------------
# Recon Report
# ------------------------------------------------

if Path("ultra_recon.txt").exists():

    body.append("Repository Tree Snapshot\n")

    try:

        lines = Path("ultra_recon.txt").read_text().splitlines()

        tree_section = False
        count = 0

        for line in lines:

            if "=== FULL FILE TREE ===" in line:
                tree_section = True
                continue

            if tree_section:

                body.append(line)

                count += 1

                if count > 50:
                    body.append("... truncated ...")
                    break

    except Exception as e:

        body.append("Recon report parsing failed")
        body.append(str(e))

    body.append("")


# ------------------------------------------------
# Repair Report
# ------------------------------------------------

if Path("repair_report.txt").exists():

    body.append("Repair Engine Summary\n")

    lines = read_lines("repair_report.txt", 40)

    body.extend(lines)

    body.append("")


# ------------------------------------------------
# Repo Intelligence
# ------------------------------------------------

if Path("repo_intelligence.json").exists():

    body.append("Repository Intelligence Summary\n")

    try:

        data = json.load(open("repo_intelligence.json"))

        for k, v in list(data.items())[:20]:

            body.append(f"{k}: {v}")

    except Exception as e:

        body.append("Failed to parse intelligence JSON")
        body.append(str(e))

    body.append("")


# ------------------------------------------------
# Fallback
# ------------------------------------------------

if len(body) < 6:

    body.append("No report files detected.")


# ------------------------------------------------
# Write release body
# ------------------------------------------------

Path("release_body.txt").write_text("\n".join(body))

print("Release body generated")