
def analyze_imports(imports, root, stdlib, report, json_data):

    missing = set()

    for file, imps in imports.items():

        for imp in imps:

            mod = imp.split(".")[0]

            if mod in stdlib:
                continue

            if not (root / f"{mod}.py").exists():
                missing.add(mod)
                report.append(f"Missing import {mod} in {file}")

    json_data["missing_imports"] = list(missing)
    return missing
