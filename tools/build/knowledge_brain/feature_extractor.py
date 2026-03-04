from pathlib import Path

def extract_features(repo):

    repo = Path(repo)

    features = {
        "languages": [],
        "build_files": []
    }

    if list(repo.rglob("*.rs")):
        features["languages"].append("rust")

    if list(repo.rglob("*.go")):
        features["languages"].append("go")

    if list(repo.rglob("*.py")):
        features["languages"].append("python")

    if list(repo.rglob("*.c")) or list(repo.rglob("*.cpp")):
        features["languages"].append("c")

    if (repo / "Cargo.toml").exists():
        features["build_files"].append("cargo")

    if (repo / "CMakeLists.txt").exists():
        features["build_files"].append("cmake")

    if (repo / "Makefile").exists():
        features["build_files"].append("make")

    if (repo / "package.json").exists():
        features["build_files"].append("npm")

    if (repo / "pom.xml").exists():
        features["build_files"].append("maven")

    return features