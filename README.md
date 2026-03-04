SourceForageAI

SourceForageAI is an autonomous system designed to discover, analyze, build, and repair open-source repositories automatically.

The project combines:

- automatic build system detection
- repository intelligence scanning
- modular build engines
- AI-generated build fixes
- self-learning knowledge from successful builds

The goal is to create a system capable of building most open-source repositories automatically (~95–98%) without manual configuration.

---

Core Idea

Open-source repositories use many different build systems, such as:

- Make
- CMake
- Meson
- Ninja
- Gradle
- Maven
- Bazel
- Cargo
- PlatformIO
- Python ("setup.py", "pyproject")
- Node ("npm", "yarn")
- Go
- Rust
- Android
- custom build scripts

SourceForageAI attempts to automatically:

1. Detect the build system
2. Predict the correct build command
3. Execute the build
4. Analyze failures
5. Generate fixes using AI
6. Retry the build
7. Store successful builds as reusable knowledge

Over time the system learns how projects build and becomes better at handling new repositories.

---

Main Features

Universal Build Detection

SourceForageAI detects build systems using multiple signals:

- repository structure
- known indicator files
- CI configurations
- README instructions
- modular build detectors
- heuristics

Example indicator files:

Makefile
CMakeLists.txt
Cargo.toml
build.gradle
pom.xml
meson.build
WORKSPACE
platformio.ini
package.json
setup.py
pyproject.toml

Detection modules live inside:

tools/build/modules/

The project already contains hundreds of generated modules.

---

Repository Intelligence Scanner

SourceForageAI analyzes repositories to predict how they should be built.

It scans:

- README files
- CI pipelines (".github/workflows")
- Dockerfiles
- language patterns
- dependency files
- build scripts

Key components:

tools/build/repo_intelligence.py
tools/build/repo_analyzer.py
tools/build/heuristics.py

This allows SourceForageAI to determine build commands even when a dedicated module does not exist.

---

Modular Build System

Build systems are implemented as plugins.

Location:

tools/build/modules/

Each module defines:

NAME
INDICATORS
DEFAULT_COMMAND
detect()
build()

Example module:

NAME = "cmake"

INDICATORS = ["CMakeLists.txt"]

DEFAULT_COMMAND = "cmake -B build && cmake --build build"

Because modules are isolated, new build systems can be added without modifying core code.

Your current setup already contains 300+ generated modules.

---

AI Build Repair

If a build fails, SourceForageAI automatically attempts to repair it.

Process:

1. Extract errors from build logs
2. Search internal knowledge and web hints
3. Generate a patch using an LLM
4. Apply the patch
5. Retry the build

The AI must return a unified diff patch, which is automatically applied.

Core file:

tools/ai_autobuilder.py

Supporting modules:

tools/ai_build.py
tools/ai_patch.py
tools/ai_repo.py
tools/ai_llm.py

---

Self-Learning Memory

The system stores build knowledge in:

tools/ai_memory/

Files:

memory.py
success_db.json

Two types of memory exist:

Failure Memory

Stores build errors and attempted fixes.

Success Memory

Stores successful builds so the AI can reuse working commands.

This allows the system to continuously improve over time.

---

AI Model Support

SourceForageAI supports multiple AI model providers.

Examples:

- OpenAI
- Ollama
- local LLMs

Configuration files:

tools/ai_models/config.py
tools/ai_models/loader.py

Example local model:

deepseek-coder

---

GitHub Automation

SourceForageAI includes several automated workflows.

Location:

.github/workflows/

---

AI Autobuilder

ai-autobuilder.yml

Runs automatic build repair when repository changes occur.

---

AI Build Discovery

ai-build-discovery.yml

Discovers new build systems and generates additional modules.

---

AI Module Generator

ai-module-generator.yml

Creates new modular build system plugins.

---

AI Remote Build Lab

ai-remote-build.yml

Allows building external GitHub repositories via manual input.

Users can provide:

- repository
- branch
- build hints
- custom commands
- workflow options

---

AI Training

ai-training.yml

Improves build knowledge and heuristics.

---

AI Maintenance

ai-maintenance.yml

Cleans logs and temporary files.

---

Project Structure

SourceForageAI
│
├── .github
│   └── workflows
│       ├── ai-autobuilder.yml
│       ├── ai-build-discovery.yml
│       ├── ai-maintenance.yml
│       ├── ai-module-generator.yml
│       ├── ai-remote-build.yml
│       └── ai-training.yml
│
├── tools
│   │
│   ├── ai_autobuilder.py
│   ├── ai_build.py
│   ├── ai_config.py
│   ├── ai_llm.py
│   ├── ai_patch.py
│   ├── ai_repo.py
│   │
│   ├── ai_memory
│   │   ├── memory.py
│   │   └── success_db.json
│   │
│   ├── ai_models
│   │   ├── config.py
│   │   └── loader.py
│   │
│   └── build
│       │
│       ├── modules
│       │   └── (hundreds of build system modules)
│       │
│       ├── detect.py
│       ├── heuristics.py
│       ├── knowledge.py
│       ├── module_generator.py
│       ├── module_learning.py
│       ├── repo_analyzer.py
│       ├── repo_intelligence.py
│       ├── resolve.py
│       ├── universal_detector.py
│       ├── universal_engine.py
│       └── websearch.py
│
└── README.md

---

Running Locally

Run the autobuilder:

python tools/ai_autobuilder.py

The system will:

1. Detect the build system
2. Predict the build command
3. Run the build
4. Analyze errors
5. Attempt automated fixes
6. Retry until success or attempt limits are reached

---

Remote Repository Builds

Using the workflow:

AI Remote Build Lab

You can enter a repository such as:

owner/repo

or

https://github.com/owner/repo

SourceForageAI will automatically:

- clone the repository
- analyze its structure
- detect the build system
- attempt the build
- repair failures

---

Vision

SourceForageAI aims to become an autonomous open-source build explorer capable of:

- building unknown repositories automatically
- repairing broken builds
- learning from successful builds
- expanding build system knowledge continuously

Long-term goal

Automatically build the majority of open-source software.

---

License

MIT License

---

Contributing

Contributions are welcome.

Areas for improvement include:

- additional build modules
- improved repository intelligence
- smarter patch generation
- better build heuristics
- expanded AI memory learning

Pull requests and ideas are welcome.