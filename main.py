from math import *
import numpy as np
import sys
from PyQt5.Qt import QApplication, QMessageBox

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
