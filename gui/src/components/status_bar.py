"""Status bar widget component for PySide6 MainWindow."""

from __future__ import annotations

from PySide6.QtWidgets import QLabel, QStatusBar, QWidget


class CustomStatusBar(QStatusBar):
    """Custom status bar component for displaying app state and backend notifications."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._label = QLabel("Ready")
        self.addWidget(self._label)

    def set_status(self, message: str) -> None:
        """Update status message."""
        self._label.setText(message)
