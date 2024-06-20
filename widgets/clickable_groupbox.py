from PySide2.QtCore import Signal, Qt
from PySide2.QtWidgets import QGroupBox


class ClickableGroupBox(QGroupBox):

    sig_clicked = Signal()

    def __init__(self, parent):
        super().__init__(parent)
        self.setCursor(Qt.PointingHandCursor)

    def mouseReleaseEvent(self, event) -> None:
        getattr(self, 'sig_clicked').emit()
        return super().mouseReleaseEvent(event)
