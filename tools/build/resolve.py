from build.loader import load_modules
from build.universal_detector import detect

def resolve(repo_root="."):

    detected = detect(repo_root)

    modules = load_modules()

    for m in modules:

        if m.NAME in detected:

            return m

    return None