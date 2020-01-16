
import numpy as np
from PyQt5 import QtCore
from PyQt5.Qt import *

from PyQt5.Qt import pyqtSignal, pyqtSlot
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
        #self.timer.start(1)
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
        self.figure = Figures().tesseract
        self.coordinate_w: float = 0
        self.distance = 3
        self.angle = 0.01
        self.scale = 1.0
        self.angles = {
            'X': .0,
            'Y': .0,
            'Z': .0,
            'XY': .0,
            'XZ': .0,
            'ZY': .0,
            'XW': .0,
            'YW': .0,
            'ZW': .0
        }

    def set_scale_figure(self, value: float = 0):
        self.scale = value
        self.draw()

    def set_coordinate_w(self, value: float = 0):
        self.coordinate_w = value
        self.draw()

    def scale_figure(self, figure: dict = (), value=1.0):
        array = np.array(figure['points'])
        array = array.dot(value)
        figure['points'] = array.tolist()
        return figure

    def connect(self, figure2D: dict = (), pen: QPen = QPen()):
        for edge in figure2D['edges']:
            self.scene.addLine(figure2D['points'][edge[0]][0], figure2D['points'][edge[0]][1],
                               figure2D['points'][edge[1]][0], figure2D['points'][edge[1]][1], pen)

    def draw(self):
        self.scene.clear()

        figure4D = self.transform4D.rotate_xy(self.figure.copy(), self.angles['XY'])  # поворот
        figure4D = self.transform4D.rotate_xz(figure4D, self.angles['XZ'])  # поворот
        figure4D = self.transform4D.rotate_yz(figure4D, self.angles['ZY'])  # поворот
        figure4D = self.transform4D.rotate_xw(figure4D, self.angles['XW'])  # поворот
        figure4D = self.transform4D.rotate_yw(figure4D, self.angles['YW'])  # поворот
        figure4D = self.transform4D.rotate_zw(figure4D, self.angles['ZW'])  # поворот

        figure3D = self.transform4D.projection_3D(figure4D, self.distance, self.coordinate_w)  # проекция
        figure3D = self.transform3D.rotate_x(figure3D, self.angles['X'])  # поворот
        figure3D = self.transform3D.rotate_y(figure3D, self.angles['Y'])  # поворот
        figure3D = self.transform3D.rotate_z(figure3D, self.angles['Z'])  # поворот

        figure2D = self.transform3D.projection_2D(figure3D, self.distance)  # проекция

        figure2D = self.scale_figure(figure2D, self.scale)

        self.connect(figure2D, self.pen)

        diameter = 10
        for point in figure2D['points']:
            self.scene.addEllipse(point[0] - diameter/2, point[1] - diameter/2, diameter, diameter, QPen(Qt.NoPen), QBrush(Qt.black))

    def timeout(self):
        self.draw()

    def rotate_x(self, value: float):
        self.angles['X'] = value
        self.draw()

    def rotate(self, type: str = 'X', value: float = 0):
        self.angles[type] = value
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
