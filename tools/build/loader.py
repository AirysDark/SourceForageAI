import importlib.util
from pathlib import Path


MODULE_DIR = Path(__file__).parent / "modules"


def load_module(path):
    """Load a single module file"""

    spec = importlib.util.spec_from_file_location(path.stem, path)

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    return module


def load_all_modules():

    modules = []

    if not MODULE_DIR.exists():
        return modules

    for file in MODULE_DIR.glob("*.py"):

        try:
            module = load_module(file)
            modules.append(module)

        except Exception as e:

            print("Module load failed:", file, e)

    return modules


def detect_build_system(repo_root="."):

    modules = load_all_modules()

    detected = []

    for module in modules:

        if hasattr(module, "detect"):

            try:
                if module.detect(repo_root):
                    detected.append(module)

            except Exception as e:
                print("Detection error:", module.__name__, e)

    return detected