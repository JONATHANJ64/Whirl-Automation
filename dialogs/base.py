import threading

from PySide2.QtCore import Signal, QTimer
from PySide2.QtWidgets import QDialog


class WhirlDialogBase(QDialog):

    closed = Signal()

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self._b_stop = threading.Event()
        self._b_stop.clear()
        QTimer.singleShot(500, self.initialize)

    def initialize(self):
        pass

    def closeEvent(self, event):
        self._b_stop.set()
        getattr(self, "closed").emit()
