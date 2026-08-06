"""Pytest configuration and fixtures for GUI module tests."""

from __future__ import annotations

import pytest
from PySide6.QtWidgets import QApplication


@pytest.fixture(scope="session")
def qapp() -> QApplication:
    """Fixture providing singleton QApplication instance for UI tests."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    return app
