from PySide2.QtCore import QObject, QPoint, Signal, QEvent


class TouchObserver(QObject):
    pressed = Signal(QPoint)
    released = Signal(QPoint)
    moved = Signal(QPoint)

    def __init__(self, window):
        super().__init__(window)
        self._window = window
        self.window.installEventFilter(self)

    @property
    def window(self):
        return self._window

    def eventFilter(self, obj, event):
        if self.window is obj:
            if event.type() == QEvent.MouseButtonPress:
                self.pressed.emit(event.pos())
            elif event.type() == QEvent.MouseMove:
                self.moved.emit(event.pos())
            elif event.type() == QEvent.MouseButtonRelease:
                self.released.emit(event.pos())
        return super().eventFilter(obj, event)
