from math import ceil

import cv2
import numpy as np
from PySide2 import QtGui
from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QLabel, QFrame, QSizePolicy


class ImageWidget(QLabel):

    def __init__(self, parent, frame=None):
        super(ImageWidget, self).__init__(parent=parent)
        self.setFrameStyle(QFrame.StyledPanel)
        self.setSizePolicy(QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed))
        if frame is not None:
            self.set_frame(frame)

    def set_frame(self, frame=None):
        t_w, t_h = self.width(), self.height()
        template = np.zeros((t_h, t_w, 3)).astype(np.uint8)
        if frame is not None:
            h, w = frame.shape[:2]
            if len(frame.shape) == 2:
                frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
            if w * h > 0:
                if w / h > t_w / t_h:
                    new_h = h * t_w // w
                    r_frame = cv2.resize(frame, (t_w, new_h))
                    template[ceil((t_h - new_h) / 2): t_h - (t_h - new_h) // 2, :] = r_frame
                else:
                    new_w = w * t_h // h
                    r_frame = cv2.resize(frame, (new_w, t_h))
                    template[:, ceil((t_w - new_w) / 2): t_w - (t_w - new_w) // 2] = r_frame
        template = cv2.cvtColor(template, cv2.COLOR_BGR2RGB)
        img = QtGui.QImage(template, template.shape[1], template.shape[0], QtGui.QImage.Format_RGB888)
        self.setPixmap(QPixmap.fromImage(img))
