"""Main Window implementation using PySide6 for Desktop-App-Template."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from gui.src.components.status_bar import CustomStatusBar
from gui.src.controllers.backend_bridge import BackendBridge


class MainWindow(QMainWindow):
    """PySide6 Qt GUI Main Window for Desktop-App-Template."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Desktop-App-Template — PySide6 GUI")
        self.resize(800, 500)

        self.bridge = BackendBridge()
        self.bridge.status_changed.connect(self._on_status_changed)

        self._init_ui()

    def _init_ui(self) -> None:
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_label = QLabel("Desktop Application Template", self)
        title_label.setStyleSheet("font-size: 22px; font-weight: bold; color: #1e1e2e;")
        layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignCenter)

        desc_label = QLabel(
            "C++ High-Performance Backend + Python Middleware + PySide6 Qt GUI",
            self,
        )
        desc_label.setStyleSheet("font-size: 13px; color: #555555;")
        layout.addWidget(desc_label, alignment=Qt.AlignmentFlag.AlignCenter)

        input_layout = QHBoxLayout()
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Enter payload or task name...")
        self.input_field.setFixedWidth(300)

        self.action_button = QPushButton("Execute Task", self)
        self.action_button.clicked.connect(self._on_execute_clicked)

        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.action_button)
        layout.addLayout(input_layout)

        self.output_label = QLabel("", self)
        self.output_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #2e7d32;")
        layout.addWidget(self.output_label, alignment=Qt.AlignmentFlag.AlignCenter)

        self.status_bar = CustomStatusBar(self)
        self.setStatusBar(self.status_bar)

    def _on_execute_clicked(self) -> None:
        text = self.input_field.text() or "Sample Payload"
        result = self.bridge.process_request(text)
        self.output_label.setText(result)

    def _on_status_changed(self, status: str) -> None:
        self.status_bar.set_status(f"Backend Status: {status}")
