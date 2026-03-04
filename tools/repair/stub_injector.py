
from .utils import safe_read, write_repair

STUBS = {
    "call_llm": "def call_llm(prompt): return ''",
    "clone_repo": "def clone_repo(url): pass",
    "run_build": "def run_build(cmd): return 1",
    "detect_build_system": "def detect_build_system(path): return 'unknown'"
}

def inject_stubs(python_files, outdir, report, json_data):

    for file in python_files:

        text = safe_read(file)
        fixed = text
        injected = False

        for name, code in STUBS.items():

            if f"{name}(" in text and f"def {name}" not in text:

                fixed = code + "\n\n" + fixed
                injected = True
                report.append(f"Injected stub {name} into {file}")

        if injected:

            repaired = write_repair(outdir, file, fixed)
            report.append(f"Generated repaired file {repaired}")
            json_data["generated_files"].append(str(repaired))
