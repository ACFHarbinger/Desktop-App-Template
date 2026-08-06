<div align="center">

# Desktop-App-Template

**A production-ready GitHub template repository for desktop applications — combining a high-performance C++ backend base, Python middleware & deep learning engine (PyTorch/TensorFlow), and PySide6 Qt GUI modules.**

<a href="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/ci.yml"><img alt="CI" src="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/ci.yml/badge.svg"></a>
<a href="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/docs.yml"><img alt="Docs" src="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/docs.yml/badge.svg"></a>
<a href="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/security.yml"><img alt="Security Audit" src="https://github.com/ACFHarbinger/Desktop-App-Template/actions/workflows/security.yml/badge.svg"></a>
<img alt="PRs Welcome" src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg">
<a href="https://github.com/astral-sh/ruff"><img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json"></a>
<a href="https://mypy-lang.org/"><img alt="MyPy" src="https://img.shields.io/badge/MyPy-checked-2f4f4f.svg"></a>

</br>

<a href="https://github.com/ACFHarbinger/Desktop-App-Template/releases"><img alt="Release" src="https://img.shields.io/github/v/release/ACFHarbinger/Desktop-App-Template?include_prereleases&logo=github&color=blue"></a>
<a href="LICENSE.md"><img alt="License" src="https://img.shields.io/badge/License-AGPL_v3-blue.svg"></a>
<a href="https://github.com/ACFHarbinger/Desktop-App-Template/issues"><img alt="Open Issues" src="https://img.shields.io/github/issues/ACFHarbinger/Desktop-App-Template?color=yellow"></a>
<a href="https://github.com/ACFHarbinger/Desktop-App-Template/commits/main"><img alt="Last Commit" src="https://img.shields.io/github/last-commit/ACFHarbinger/Desktop-App-Template?color=blueviolet"></a>

</br>

<a href="https://isocpp.org/"><img alt="C++" src="https://img.shields.io/badge/C%2B%2B-17-00599C?logo=cplusplus&logoColor=white"></a>
<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/Python-3.11+-3776ab?logo=python&logoColor=white"></a>
<a href="https://qt.io/"><img alt="PySide6 / Qt" src="https://img.shields.io/badge/Qt-PySide6-41CD52?logo=qt&logoColor=white"></a>
<a href="https://pytorch.org/"><img alt="PyTorch" src="https://img.shields.io/badge/PyTorch-Deep_Learning-EE4C2C?logo=pytorch&logoColor=white"></a>
<a href="https://cmake.org/"><img alt="CMake" src="https://img.shields.io/badge/CMake-Build-064F8C?logo=cmake&logoColor=white"></a>
<a href="https://github.com/astral-sh/uv"><img alt="uv" src="https://img.shields.io/badge/managed%20by-uv-261230.svg"></a>

</div>

## About

`Desktop-App-Template` is a modern, modular template repository designed for high-performance desktop applications. It provides a clean hybrid architecture:
- **C++ Base Engine** (`src/`, `include/`): For resource-intensive, performance-critical backend computations.
- **Python Backend & Middleware** (`backend/`): Connects C++ native modules to the frontend, manages business logic, and orchestrates PyTorch/TensorFlow deep learning models.
- **PySide6 Qt GUI Module** (`gui/`): Rich Qt Widgets & QML user interfaces, custom components, resources, and UI test suites.

## Architecture

```
Desktop-App-Template/
├── CMakeLists.txt              # C++ base build system
├── src/, include/, test/       # C++ high-performance engine source, headers, tests
├── backend/                    # Python middleware & PyTorch/TensorFlow deep learning engine
│   ├── pyproject.toml
│   ├── src/                    # Backend source (flow, jinja, torch integrations)
│   ├── test/                   # Backend tests
│   └── benchmark/              # Backend benchmarks
├── gui/                        # PySide6 / QML Desktop GUI module
│   ├── pyproject.toml
│   ├── qml/                    # Declarative QML views, components, singletons
│   ├── resources/              # Qt resources (.qrc) and generator scripts
│   ├── src/                    # PySide6 windows, status bars, controllers, and backend bridges
│   └── test/                   # Qt UI integration and unit tests
├── desktop/                    # OS desktop packaging (.desktop, macOS, Windows scripts)
├── docs/                       # Project documentation
└── justfile                    # Root task runner recipes (just build, just test, etc.)
```

## Quick Start

```bash
# Clone the repository template
git clone https://github.com/ACFHarbinger/Desktop-App-Template.git
cd Desktop-App-Template

# Set up development environment
just setup

# Build C++, backend, and GUI modules
just build

# Run unit tests across all modules
just test
```

## License

Dual-licensed under GNU AGPL-3.0 and Commercial terms. See [`LICENSE.md`](LICENSE.md) and [`LICENSE.txt`](LICENSE.txt) for details.
