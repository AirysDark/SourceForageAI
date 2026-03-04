import json
import os
from pathlib import Path

workflow = os.getenv("GITHUB_WORKFLOW", "SourceForageAI Workflow")
run_id = os.getenv("GITHUB_RUN_ID", "")
repo = os.getenv("GITHUB_REPOSITORY", "")

body = [
    f"{workflow} Report",
    "",
    f"Repository: {repo}",
    f"Run ID: {run_id}",
    ""
]

# ------------------------------------------------
# System Test Report
# ------------------------------------------------

if Path("system_test_report.json").exists():

    try:
        r = json.load(open("system_test_report.json"))

        errors = []
        errors += r.get("module_failures", [])
        errors += r.get("build_module_failures", [])
        errors += r.get("yaml_failures", [])

        body.append("Key Errors:\n")

        if errors:
            for e in errors[:20]:
                body.append(str(e))
        else:
            body.append("No errors detected")

    except Exception as e:
        body.append("Report parsing failed")
        body.append(str(e))

# ------------------------------------------------
# Recon Report
# ------------------------------------------------

elif Path("ultra_recon.txt").exists():

    body.append("Repository Tree Snapshot:\n")

    try:
        lines = open("ultra_recon.txt").read().splitlines()

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

# ------------------------------------------------
# Intelligence JSON
# ------------------------------------------------

elif Path("repo_intelligence.json").exists():

    body.append("Repository Intelligence JSON detected")

else:

    body.append("No report files detected")

open("release_body.txt", "w").write("\n".join(body))