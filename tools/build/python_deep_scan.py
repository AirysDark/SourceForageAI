import ast
from pathlib import Path

def analyze_python_file(path):
    try:
        tree = ast.parse(path.read_text())
    except:
        return None

    imports = []
    classes = []
    functions = []

    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for n in node.names:
                imports.append(n.name)

        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module)

        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(node, ast.FunctionDef):
            functions.append(node.name)

    return {
        "imports": imports,
        "classes": classes,
        "functions": functions
    }


def scan_repo(root="."):
    root = Path(root)

    for py in root.rglob("*.py"):
        data = analyze_python_file(py)

        if not data:
            continue

        print("\nFILE:", py)

        if data["imports"]:
            print("  Imports:")
            for i in data["imports"]:
                print("   -", i)

        if data["classes"]:
            print("  Classes:")
            for c in data["classes"]:
                print("   -", c)

        if data["functions"]:
            print("  Functions:")
            for f in data["functions"]:
                print("   -", f)


if __name__ == "__main__":
    scan_repo()