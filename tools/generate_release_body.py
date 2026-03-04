import json

body = ["SourceForageAI System Test Report", ""]

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

except:
    body.append("Report parsing failed")

open("release_body.txt","w").write("\n".join(body))