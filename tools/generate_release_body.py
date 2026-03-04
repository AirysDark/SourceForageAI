import json
import os

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

open("release_body.txt","w").write("\n".join(body))
