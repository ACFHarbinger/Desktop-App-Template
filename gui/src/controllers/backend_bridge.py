"""Bridge between PySide6 GUI and C++ / PyTorch backend operations."""

from __future__ import annotations

from PySide6.QtCore import QObject, Signal, Slot


class BackendBridge(QObject):
    """QObject bridge for marshaling signals between GUI and Python/C++ backends."""

    status_changed = Signal(str)
    result_ready = Signal(str)

    def __init__(self) -> None:
        super().__init__()
        self._status = "Idle"

    @Slot(str, result=str)
    def process_request(self, payload: str) -> str:
        """Process a request payload by delegating to backend components."""
        self._status = "Processing"
        self.status_changed.emit(self._status)
        result = f"Backend processed: '{payload}'"
        self._status = "Completed"
        self.status_changed.emit(self._status)
        self.result_ready.emit(result)
        return result
