
import numpy as np
from PyQt5 import QtCore
from PyQt5.Qt import *

from transformations import *
from figures import *

class MyGraphicView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        self.initFunctions()

    def initUI(self):
        self.setFrameShape(QFrame.NoFrame)
        self.setAlignment(QtCore.Qt.AlignCenter)
        # сцена --------------------------------------------------------------------------------------------------------
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.scene.setBackgroundBrush(QBrush(Qt.white))
        # таймер отрисовки ---------------------------------------------------------------------------------------------
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)
        self.timer.start(1)
        # шрифт --------------------------------------------------------------------------------------------------------
        self.font = QFont()
        self.font.setPixelSize(25)
        self.font.setBold(False)
        self.font.setFamily("Arial")
        # кисти --------------------------------------------------------------------------------------------------------
        self.pen = QPen(Qt.black)
        self.pen.setWidth(3)
        self.brush = QBrush(Qt.NoBrush)
        # --------------------------------------------------------------------------------------------------------------
        self.transform3D = Transformations3D()
        self.transform4D = Transformations4D()

    def initFunctions(self):
        self.figure = Figures.tesseract

        self.points2D: list = []
        self.points3D: list = []
        self.points4D: list = self.figure['points']
        self.distance = 3
        self.angle = 0.01

    def connect3D(self, i = 0, j = 0, points: list = ()):
        self.scene.addLine(points[i][0], points[i][1],
                           points[j][0], points[j][1], self.pen)

    def connect4D(self, i = 0, j = 0, points: list = ()):
        self.scene.addLine(points[i][0], points[i][1],
                           points[j][0], points[j][1], self.pen)

    def draw(self):
        self.scene.clear()
        self.points3D = self.transform4D.projection_3D(self.points4D, self.distance)
        self.points3D = self.transform3D.rotate_x(self.points3D, 90)
        self.points2D = self.transform3D.projection_2D(self.points3D, self.distance)
        self.points2D = self.transform3D.scale(self.points2D, 500)

        self.pen = QPen(Qt.black)
        self.pen.setWidth(3)
        for item in self.figure['edges']:
            self.connect4D(item[0], item[1], self.points2D)
        diameter = 10
        self.pen.setWidth(3)
        for point in self.points2D:
            self.scene.addEllipse(point[0] - diameter/2, point[1] - diameter/2, diameter, diameter, QPen(Qt.NoPen), QBrush(Qt.red))

    def timeout(self):
        #self.points4D = self.transform4D.rotate_zw(self.points4D, 0.1)
        #self.points4D = self.transform4D.rotate_xy(self.points4D, 0.1)
        self.points4D = self.transform4D.rotate_zw(self.points4D, 0.1)
        self.points4D = self.transform4D.rotate_xy(self.points4D, 0.1)
        self.draw()



if __name__ == "__main__":
    angle = 0.5
    arr = np.array([
        [0, 0, 0],
        [0, 100, 0],
        [100, 100, 0],
        [100, 0, 0]
    ])
    print(arr)
    print(arr.size)
    print(type(arr.shape))

    transform = Transformations3D()
    distance = 0.5
    for i in range(0, 1):
        arr = transform.rotate_x(arr, 0.03)
    arr = transform.projection_2D(arr, distance)
    print(arr)
