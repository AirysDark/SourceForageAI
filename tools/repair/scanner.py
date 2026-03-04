
import ast
from collections import defaultdict
from .utils import safe_read, is_ignored

def scan_repo(root, ignore_dirs):

    python_files = [
        f for f in root.rglob("*.py")
        if not is_ignored(f, ignore_dirs)
    ]

    imports = defaultdict(list)
    definitions = defaultdict(list)
    references = defaultdict(list)

    for file in python_files:

        src = safe_read(file)

        try:
            tree = ast.parse(src)
        except Exception:
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

    return python_files, imports, definitions, references
