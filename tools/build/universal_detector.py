import os

SIGNATURES = {
    "cmake": ["CMakeLists.txt"],
    "make": ["Makefile", "makefile"],
    "meson": ["meson.build"],
    "ninja": ["build.ninja"],
    "cargo": ["Cargo.toml"],
    "gradle": ["build.gradle", "settings.gradle"],
    "maven": ["pom.xml"],
    "bazel": ["WORKSPACE", "BUILD"],
    "scons": ["SConstruct"],
    "go": ["go.mod"],
    "node": ["package.json"],
    "python": ["setup.py", "pyproject.toml"],
}

def detect(repo_root="."):

    detected = []

    for root, dirs, files in os.walk(repo_root):

        for system, indicators in SIGNATURES.items():

            for f in indicators:

                if f in files:
                    detected.append(system)

    if detected:
        return list(set(detected))

    return ["unknown"]