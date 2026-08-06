"""Entry point for the PySide6 Qt GUI application."""

from __future__ import annotations

import sys
from PySide6.QtWidgets import QApplication

from gui.src.windows.main_window import MainWindow


def main() -> int:
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
