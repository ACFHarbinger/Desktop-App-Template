"""Script to generate or compile Qt QRC resources into Python modules."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def generate_resources() -> None:
    resources_dir = Path(__file__).parent
    qrc_file = resources_dir / "resources.qrc"
    output_py = resources_dir.parent / "src" / "resources_rc.py"

    if not qrc_file.exists():
        print(f"Error: {qrc_file} not found.")
        sys.exit(1)

    cmd = ["pyside6-rcc", str(qrc_file), "-o", str(output_py)]
    print(f"Compiling {qrc_file} -> {output_py}...")
    try:
        subprocess.run(cmd, check=True)
        print("Resources compiled successfully.")
    except Exception as e:
        print(f"Resource compilation skipped or failed: {e}")


if __name__ == "__main__":
    generate_resources()
