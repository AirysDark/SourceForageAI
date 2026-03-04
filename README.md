SourceForageAI

SourceForageAI is an autonomous build discovery and repair system designed to automatically analyze, detect, build, and repair open-source repositories with minimal configuration.

The project combines repository structure analysis, modular build detection, AI-assisted patching, and self-learning memory to make building unfamiliar codebases dramatically easier.

SourceForageAI can automatically attempt to build most open-source repositories, diagnose failures, generate fixes, and learn from successful builds to improve future results.

---

Overview

Modern open-source projects use many different build systems:

- Make
- CMake
- Meson
- Ninja
- Gradle
- Maven
- Bazel
- Cargo
- PlatformIO
- Python
- Node
- Go
- and many more.

SourceForageAI attempts to identify the correct build system automatically, run the build, analyze failures, and repair issues using AI and learned build knowledge.

The system is designed to approach ~95–98% automatic build compatibility across public repositories.

---

Key Features

Universal Build Detection

Automatically detects build systems using:

- repository structure
- indicator files
- CI configuration
- README instructions
- modular build detectors

Example indicator files:

Makefile
CMakeLists.txt
Cargo.toml
build.gradle
pom.xml
meson.build
WORKSPACE
platformio.ini

---

Modular Build System Architecture

Build systems are implemented as plugins inside:

tools/build/modules/

Each module defines:

NAME
INDICATORS
DEFAULT_COMMAND
detect()
build()

Example:

NAME = "cmake"

INDICATORS = ["CMakeLists.txt"]

DEFAULT_COMMAND = "cmake -B build && cmake --build build"

This makes it easy to add support for new build systems.

---

Repository Intelligence Scanner

SourceForageAI scans repositories for build hints from:

- directory structure
- README instructions
- GitHub Actions / CI pipelines
- language detection
- dependency files

This allows the system to predict build commands even when no module exists.

---

AI-Driven Build Repair

If a build fails, SourceForageAI can:

1. analyze the build log
2. extract the error
3. search for solutions
4. generate a patch
5. apply the patch
6. retry the build

The AI returns a unified diff patch which is automatically applied.

---

Self-Learning Memory

SourceForageAI stores successful fixes in a local memory database:

tools/ai_memory/db.json

The system remembers:

- build failures
- generated fixes
- successful patches

Future builds can reuse these solutions automatically.

---

Successful Build Memory

A special memory store records only successful builds so they can be reused as references for similar repositories.

This allows the system to improve over time.

---

GitHub Automation

The project includes multiple GitHub workflows that allow the AI to operate automatically.

Examples:

Workflow| Purpose
AI Autobuilder| Builds and repairs repositories
AI Remote Build Lab| Builds external repositories
AI Build Discovery| Expands build system modules
AI Training| Improves build knowledge
AI Maintenance| Cleans logs and temporary files
AI Module Generator| Generates new build modules

---

Project Structure

SourceForageAI
│
├── tools
│   │
│   ├── ai_autobuilder.py
│   ├── ai_build.py
│   ├── ai_patch.py
│   ├── ai_repo.py
│   ├── ai_llm.py
│   │
│   ├── ai_memory
│   │   └── db.json
│   │
│   └── build
│       │
│       ├── detect.py
│       ├── universal_engine.py
│       ├── repo_intelligence.py
│       ├── websearch.py
│       ├── knowledge.py
│       │
│       └── modules
│           ├── make.py
│           ├── cmake.py
│           ├── gradle.py
│           ├── cargo.py
│           ├── bazel.py
│           └── ...
│
├── .github
│   └── workflows
│
└── README.md

---

Installation

Clone the repository:

git clone https://github.com/YOURNAME/SourceForageAI.git
cd SourceForageAI

Install dependencies:

pip install requests

Optional system dependencies:

sudo apt install build-essential cmake git

---

Running SourceForageAI

Run the AI autobuilder:

python tools/ai_autobuilder.py

The system will:

1. detect the build system
2. run the build
3. analyze failures
4. attempt automatic repairs
5. retry until successful or attempts exhausted

---

Remote Repository Builds

SourceForageAI can also attempt to build external repositories automatically using the GitHub workflow:

AI Remote Build Lab

Input fields allow specifying:

- repository
- branch
- optional build hints
- optional custom commands

---

Adding a New Build System

Create a new module inside:

tools/build/modules/

Example:

NAME = "meson"

INDICATORS = ["meson.build"]

DEFAULT_COMMAND = "meson setup build && ninja -C build"

The detector will automatically load it.

No core code changes required.

---

AI Model Support

SourceForageAI supports multiple providers:

OpenAI
Ollama
Local LLMs

Example local model:

deepseek-coder

---

Goals

SourceForageAI aims to create a fully autonomous build system explorer capable of:

- building unknown repositories
- repairing broken builds
- learning from successful builds
- expanding its own build knowledge

Long term vision:

Automatically build most of the open-source ecosystem.

---

Status

Current capabilities:

- modular build detection
- AI build repair
- GitHub automation
- repository intelligence scanning
- self-learning memory
- automatic module generation

Development continues to improve:

- build coverage
- repair accuracy
- knowledge reuse

---

License

MIT License

---

Contributing

Contributions are welcome.

You can help by:

- adding new build modules
- improving repository intelligence
- expanding repair strategies
- testing against more repositories

---

Name

SourceForageAI

The system forages through source code repositories, discovering how to build them automatically.