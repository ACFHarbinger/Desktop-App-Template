"""Tests for PySide6 MainWindow component."""

from __future__ import annotations

from gui.src.windows.main_window import MainWindow


def test_main_window_initialization(qapp) -> None:
    window = MainWindow()
    assert window.windowTitle() == "Desktop-App-Template — PySide6 GUI"
    assert window.input_field is not None
    assert window.action_button is not None


def test_main_window_execute_action(qapp) -> None:
    window = MainWindow()
    window.input_field.setText("Test Payload")
    window.action_button.click()
    assert "Backend processed: 'Test Payload'" in window.output_label.text()
