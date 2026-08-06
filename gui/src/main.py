"""Entry point for the PySide6 Qt GUI application."""

from __future__ import annotations

import sys

from gui.src.windows.main_window import MainWindow
from PySide6.QtWidgets import QApplication


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
