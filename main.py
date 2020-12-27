from math import *
import numpy as np
import sys
from PyQt5.Qt import QApplication, QMessageBox
from PyQt5.Qt import pyqtSignal, pyqtSlot

import mainWindowUI
from myGraphicsView import MyGraphicView

from PyQt5.Qt import *

class MainWindow(QMainWindow, mainWindowUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.initUI()


    def initUI(self):
        # инициализация своей графической сцены ------------------------------------------------------------------------
        self.graphicView = MyGraphicView(self)
        self.gridLayout.addWidget(self.graphicView)
        self.graphicView.fps.connect(self.fps)
        self.count = 0
        self.counter = 10
        self.sum_fps = 0

    @pyqtSlot(int)
    def fps(self, value: int):
        print('time: ' + str(value))
        if self.count < self.counter:
            self.count += 1
            self.sum_fps += value
        else:
            self.count = 0
            self.sum_fps = int(self.sum_fps / self.counter)
            self.label_fps.setText('FPS: {}'.format(self.sum_fps))


    @pyqtSlot(float)
    def on_rotate_x_valueChanged(self, value):
        self.graphicView.rotate('X', value)

    @pyqtSlot(float)
    def on_rotate_y_valueChanged(self, value):
        self.graphicView.rotate('Y', value)

    @pyqtSlot(float)
    def on_rotate_z_valueChanged(self, value):
        self.graphicView.rotate('Z', value)

    @pyqtSlot(float)
    def on_rotate_xy_valueChanged(self, value):
        self.graphicView.rotate('XY', value)


    @pyqtSlot(float)
    def on_rotate_xz_valueChanged(self, value):
        self.graphicView.rotate('XZ', value)

    @pyqtSlot(float)
    def on_rotate_yz_valueChanged(self, value):
        self.graphicView.rotate('ZY', value)

    @pyqtSlot(float)
    def on_rotate_xw_valueChanged(self, value):
        self.graphicView.rotate('XW', value)

    @pyqtSlot(float)
    def on_rotate_yw_valueChanged(self, value):
        self.graphicView.rotate('YW', value)

    @pyqtSlot(float)
    def on_rotate_zw_valueChanged(self, value):
        self.graphicView.rotate('ZW', value)

    @pyqtSlot(float)
    def on_scale_valueChanged(self, value):
        self.coordinate_w.setMaximum(value)
        self.coordinate_w.setMinimum(-value)
        print(self.coordinate_w.minimum())
        self.graphicView.set_scale_figure(value)

    @pyqtSlot(float)
    def on_coordinate_w_valueChanged(self, value):
        # нормализация
        value = (value - self.coordinate_w.minimum())/(self.coordinate_w.maximum() - self.coordinate_w.minimum())
        value = value * 2 - 1
        self.graphicView.set_coordinate_w(value)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
