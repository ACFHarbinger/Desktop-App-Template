# gui/

PySide6 Qt GUI module template for Desktop-App-Template. Managed with [uv](https://github.com/astral-sh/uv).

```bash
uv sync --all-extras --dev
uv run pytest test -v
```

## Directory Structure

| Directory | Purpose |
| --- | --- |
| `src/` | Python Qt / PySide6 source code (windows, components, controllers) |
| `qml/` | QML declarative UI files and custom components |
| `resources/` | Qt resource definition (`.qrc`) and build scripts |
| `test/` | Unit and UI integration tests (pytest, pytest-qt) |
