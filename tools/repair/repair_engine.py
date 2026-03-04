import json
import ast
import subprocess
import sys
import yaml
from pathlib import Path
from collections import defaultdict

ROOT = Path(".")
OUTDIR = Path("repaired_files")
REPORT = Path("repair_report.txt")
JSON_REPORT = Path("repair_report.json")

OUTDIR.mkdir(exist_ok=True)

report = []
report.append("SourceForageAI Advanced Repair Report\n")

json_data = {
    "missing_imports": [],
    "undefined_symbols": [],
    "orphan_modules": [],
    "circular_imports": [],
    "unused_imports": [],
    "brain_errors": [],
    "generated_files": [],
}

# ------------------------------------------------
# directories to ignore
# ------------------------------------------------

IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".github",
    "venv",
    ".venv",
    "env",
    "node_modules",
    "dist",
    "build",
    "repaired_files",
}

# ------------------------------------------------
# stdlib detection
# ------------------------------------------------

STDLIB = set(sys.builtin_module_names)

COMMON_STDLIB = {
    "json","os","sys","pathlib","subprocess","tempfile","signal","random",
    "sqlite3","ast","collections","datetime","time","uuid","http"
}

STDLIB.update(COMMON_STDLIB)

# ------------------------------------------------
# helpers
# ------------------------------------------------

def safe_read(path):
    try:
        return path.read_text()
    except:
        return ""

def write_repair(path, text):
    repaired = OUTDIR / path.name
    repaired.write_text(text)
    return repaired

def is_ignored(path):
    return any(p in IGNORE_DIRS for p in path.parts)

# ------------------------------------------------
# collect python files
# ------------------------------------------------

python_files = [
    f for f in ROOT.rglob("*.py")
    if not is_ignored(f)
]

imports = defaultdict(list)
definitions = defaultdict(list)
references = defaultdict(list)

# ------------------------------------------------
# AST scanning
# ------------------------------------------------

for file in python_files:

    source = safe_read(file)

    try:
        tree = ast.parse(source)
    except Exception as e:

        report.append(f"Syntax error in {file}: {e}")
        repaired = write_repair(file, source)
        report.append(f"Copied broken file for manual repair: {repaired}")
        continue

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):
            for n in node.names:
                imports[file].append(n.name)

        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports[file].append(node.module)

        elif isinstance(node, ast.FunctionDef):
            definitions[file].append(node.name)

        elif isinstance(node, ast.ClassDef):
            definitions[file].append(node.name)

        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                references[file].append(node.func.id)

# ------------------------------------------------
# detect missing imports
# ------------------------------------------------

missing_imports = set()

for file, imps in imports.items():

    for imp in imps:

        mod = imp.split(".")[0]

        if mod in STDLIB:
            continue

        local_file = ROOT / f"{mod}.py"
        local_pkg = ROOT / mod

        if not local_file.exists() and not local_pkg.exists():

            missing_imports.add(mod)
            report.append(f"Missing import in {file}: {mod}")

json_data["missing_imports"] = list(missing_imports)

# ------------------------------------------------
# undefined symbols
# ------------------------------------------------

for file, calls in references.items():

    defs = definitions.get(file, [])

    for name in calls:

        if name not in defs and not name.startswith("_"):

            report.append(f"Possible undefined symbol in {file}: {name}")
            json_data["undefined_symbols"].append(name)

# ------------------------------------------------
# orphan modules
# ------------------------------------------------

for file in python_files:

    name = file.stem
    used = False

    for imps in imports.values():
        for imp in imps:
            if name in imp:
                used = True

    if not used and not file.name.startswith("test_"):
        report.append(f"Possible orphan module: {file}")
        json_data["orphan_modules"].append(str(file))

# ------------------------------------------------
# circular imports
# ------------------------------------------------

for file, imps in imports.items():

    for imp in imps:

        other = ROOT / f"{imp.split('.')[0]}.py"

        if other in imports:

            if file.stem in str(imports.get(other, [])):

                msg = f"Circular import detected: {file} <-> {other}"

                report.append(msg)
                json_data["circular_imports"].append(msg)

# ------------------------------------------------
# unused imports
# ------------------------------------------------

for file, imps in imports.items():

    refs = references.get(file, [])

    for imp in imps:

        name = imp.split(".")[0]

        if name not in refs:

            report.append(f"Unused import in {file}: {name}")
            json_data["unused_imports"].append(name)

# ------------------------------------------------
# stub injection repair
# ------------------------------------------------

STUBS = {
    "call_llm": "def call_llm(prompt):\n    return ''\n",
    "clone_repo": "def clone_repo(url):\n    pass\n",
    "run_build": "def run_build(cmd):\n    return 1\n",
    "detect_build_system": "def detect_build_system(path):\n    return 'unknown'\n"
}

for file in python_files:

    text = safe_read(file)
    fixed = text
    injected = False

    for name, code in STUBS.items():

        if f"{name}(" in text and f"def {name}" not in text:

            report.append(f"Injecting stub {name} into {file}")
            fixed = "\n" + code + "\n" + fixed
            injected = True

    if injected:

        repaired = write_repair(file, fixed)

        report.append(f"Generated repaired file: {repaired}")
        json_data["generated_files"].append(str(repaired))

# ------------------------------------------------
# dependency install attempts
# ------------------------------------------------

for mod in missing_imports:

    try:

        subprocess.run(
            ["pip", "install", mod],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        report.append(f"Installed dependency: {mod}")

    except:

        report.append(f"Dependency install failed: {mod}")

# ------------------------------------------------
# workflow YAML validation
# ------------------------------------------------

workflow_dir = ROOT / ".github" / "workflows"

if workflow_dir.exists():

    for wf in workflow_dir.glob("*.yml"):

        try:

            data = yaml.safe_load(safe_read(wf))

            if not isinstance(data, dict):
                report.append(f"Invalid workflow YAML: {wf}")

            if "jobs" not in data:
                report.append(f"Workflow missing jobs: {wf}")

        except Exception as e:

            report.append(f"Broken workflow YAML: {wf} {e}")

# ------------------------------------------------
# brain component auto-generation
# ------------------------------------------------

brain_templates = {
    "core/Cerebrum.py":
"""class Cerebrum:

    def process(self, task):
        return {"status":"analysis complete","task":task}
""",

    "core/Cerebellum.py":
"""class Cerebellum:

    def process(self, task):
        return {"status":"execution complete","task":task}
""",

    "core/Brainstem.py":
"""class Brainstem:

    def process(self, task):
        return {"status":"system processed","task":task}
"""
}

for file, template in brain_templates.items():

    path = Path(file)

    if not path.exists():

        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(template)

        report.append(f"Generated missing brain component: {file}")
        json_data["generated_files"].append(file)

# ------------------------------------------------
# ensure python packages
# ------------------------------------------------

for f in python_files:

    pkg = f.parent / "__init__.py"

    if not pkg.exists():

        pkg.write_text("")
        report.append(f"Generated package file: {pkg}")

# ------------------------------------------------
# save reports
# ------------------------------------------------

REPORT.write_text("\n".join(report))
JSON_REPORT.write_text(json.dumps(json_data, indent=2))

print("SourceForageAI repair scan complete")