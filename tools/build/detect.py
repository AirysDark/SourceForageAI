import importlib.util
from pathlib import Path

# directory containing build modules
MODULE_DIR = Path(__file__).parent / "modules"


def detect_build_type(repo):

    repo = Path(repo)

    if not MODULE_DIR.exists():
        return "unknown"

    for module_file in MODULE_DIR.glob("*.py"):

        name = module_file.stem

        try:

            spec = importlib.util.spec_from_file_location(name, module_file)

            module = importlib.util.module_from_spec(spec)

            spec.loader.exec_module(module)

            if hasattr(module, "detect"):

                if module.detect(repo):

                    return name

        except Exception:
            continue

    return "unknown"