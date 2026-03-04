
from .config import *
from .scanner import scan_repo
from .import_analyzer import analyze_imports
from .symbol_analyzer import analyze_symbols
from .dependency_manager import install_dependencies
from .stub_injector import inject_stubs
from .brain_generator import generate_brain
from .router_generator import generate_router
from .orchestrator_generator import generate_orchestrator
from .worker_generator import generate_worker_pool
from .scheduler_generator import generate_scheduler
from .report_writer import write_reports

OUTDIR.mkdir(exist_ok=True)

report = ["SourceForageAI Advanced Repair Report\n"]

json_data = {
    "missing_imports": [],
    "undefined_symbols": [],
    "orphan_modules": [],
    "circular_imports": [],
    "unused_imports": [],
    "generated_files": []
}

python_files, imports, definitions, references = scan_repo(ROOT, IGNORE_DIRS)

missing = analyze_imports(imports, ROOT, STDLIB, report, json_data)

analyze_symbols(definitions, references, report, json_data)

inject_stubs(python_files, OUTDIR, report, json_data)

install_dependencies(missing, SAFE_PIP, report)

generate_brain(ROOT, report)
generate_router(ROOT, report)
generate_orchestrator(ROOT, report)
generate_worker_pool(ROOT, report)
generate_scheduler(ROOT, report)

write_reports(REPORT, JSON_REPORT, report, json_data)

print("SourceForageAI repair scan complete")
