SourceForageAI

SourceForageAI is an autonomous system designed to discover, analyze, build, and repair open-source repositories automatically.

The project combines:

- automatic build system detection
- repository intelligence scanning
- modular build engines
- AI-generated build fixes
- self-learning memory from successful builds

The goal is to create a system capable of building most open-source repositories automatically (~95–98%) without manual configuration.

---

Core Idea

Open-source repositories use many different build systems:

- Make
- CMake
- Meson
- Ninja
- Gradle
- Maven
- Bazel
- Cargo
- PlatformIO
- Python (setup.py / pyproject)
- Node (npm / yarn)
- Go
- Rust
- Android
- custom scripts

SourceForageAI attempts to:

1. detect the build system
2. predict the correct build command
3. run the build
4. analyze failures
5. generate fixes
6. retry automatically
7. store successful builds as knowledge

Over time the system learns how different projects build and becomes better at handling new repositories.

---

Main Features

Universal Build Detection

The engine detects build systems using:

- repository structure
- known indicator files
- CI configurations
- README instructions
- modular build detectors
- heuristics

Indicator examples:

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

Your project already contains hundreds of generated modules.

---

Repository Intelligence Scanner

SourceForageAI analyzes repositories to predict how they should be built.

It scans:

- README files
- CI pipelines (.github/workflows)
- Dockerfiles
- language patterns
- dependency files
- build scripts

Files responsible for this:

tools/build/repo_intelligence.py
tools/build/repo_analyzer.py
tools/build/heuristics.py

This allows the system to determine build commands even when a module does not exist.

---

Modular Build System

Build systems are implemented as plugins.

Location:

tools/build/modules/

Each module contains:

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

Your current setup already contains hundreds of generated modules (~300+).

---

AI Build Repair

If a build fails, SourceForageAI:

1. extracts errors from build logs
2. searches knowledge and web hints
3. generates a patch using an LLM
4. applies the patch
5. retries the build

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

Stores only successful builds so the AI can reuse known working solutions.

This allows the system to improve over time.

---

AI Model Support

The AI system can use different model providers.

Examples:

OpenAI
Ollama
local LLMs

Configuration:

tools/ai_models/config.py
tools/ai_models/loader.py

Example local model:

deepseek-coder

---

GitHub Automation

SourceForageAI includes multiple GitHub workflows.

Location:

.github/workflows/

Current workflows:

AI Autobuilder

ai-autobuilder.yml

Runs automatic build repair on repository pushes.

---

AI Build Discovery

ai-build-discovery.yml

Discovers new build systems and generates modules.

---

AI Module Generator

ai-module-generator.yml

Creates additional build modules.

---

AI Remote Build Lab

ai-remote-build.yml

Allows building external GitHub repositories via manual input.

User can provide:

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

1. detect build system
2. predict build command
3. run build
4. analyze errors
5. attempt automated fixes
6. retry until success or attempts exhausted

---

Remote Repository Builds

Using the workflow:

AI Remote Build Lab

You can enter a repository such as:

owner/repo

or

https://github.com/owner/repo

The system will automatically:

- clone the repo
- analyze it
- detect the build system
- attempt to build it
- repair failures

---

Vision

SourceForageAI aims to become an autonomous open-source build explorer capable of:

- building unknown repositories automatically
- repairing broken builds
- learning from successful builds
- expanding build system knowledge continuously

Long-term goal:

Automatically build the majority of open-source software.

---

License

MIT License

---

Contributing

Contributions are welcome.

Areas of improvement:

- additional build modules
- better repository intelligence
- smarter patch generation
- improved build heuristics
- expanded AI memory learning