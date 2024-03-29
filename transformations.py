from math import *
import numpy as np


class Transformations3D():
    def _dot(self, points3D: list = (), matrix3D: list = ()):
        points = np.array(points3D)
        matrix = np.array(matrix3D)
        result = []
        if points.size != 0:
            if len(points.shape) == 2 and points.shape[1] == 3:
                for row_XYZ in points:
                    result.append(matrix.dot(row_XYZ.reshape(3, 1)).reshape(1, 3)[0])
            return result

    def rotate_x(self, figure3D: dict = (), angle=1.0):
        matrix = [
            [1, 0, 0],
            [0, cos(radians(angle)), -sin(radians(angle))],
            [0, sin(radians(angle)), cos(radians(angle))]
        ]
        figure3D['points'] = self._dot(figure3D['points'], matrix)
        return figure3D

    def rotate_y(self, figure3D: dict = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, -sin(radians(angle))],
            [0, 1, 0],
            [sin(radians(angle)), 0, cos(radians(angle))]
        ]
        figure3D['points'] = self._dot(figure3D['points'], matrix)
        return figure3D

    def rotate_z(self, figure3D: dict = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), -sin(radians(angle)), 0],
            [sin(radians(angle)), cos(radians(angle)), 0],
            [0, 0, 1]
        ]
        figure3D['points'] = self._dot(figure3D['points'], matrix)
        return figure3D

    def projection_2D(self, figure3D: dict = (), distance=1.0):
        projection = np.array([
            [0., 0., 0.],
            [0., 0., 0.]
        ], float)
        array = np.array(figure3D['points'])
        if array is not None:
            result: list = []
            if len(array.shape) == 2 and array.shape[1] == 3:
                for row_XYZ in array:
                    projection[0][0] = 1.0 / (distance - row_XYZ[2])
                    projection[1][1] = 1.0 / (distance - row_XYZ[2])
                    result.append(projection.dot(row_XYZ.reshape(3, 1)).reshape(1, 2)[0])
            figure3D['points'] = result
            return figure3D

    def scale(self, figure: dict = (), value=1.0):
        array = np.array(figure['points'])
        array = array.dot(value)
        figure['points'] = array.tolist()
        return figure


class Transformations4D():
    def _dot(self, points4D: list = (), matrix4D: list = ()):
        points = np.array(points4D)
        matrix = np.array(matrix4D)
        result = []
        if points.size != 0:
            if len(points.shape) == 2 and points.shape[1] == 4:
                for row_XYZ in points:
                    result.append(matrix.dot(row_XYZ.reshape(4, 1)).reshape(1, 4)[0])
            return result

    def rotate_xw(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, cos(radians(angle)), -sin(radians(angle)), 0],
            [0, sin(radians(angle)), cos(radians(angle)), 0],
            [0, 0, 0, 1]
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def rotate_yw(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, -sin(radians(angle)), 0],
            [0, 1, 0, 0],
            [sin(radians(angle)), 0, cos(radians(angle)), 0],
            [0, 0, 0, 1]
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def rotate_zw(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), -sin(radians(angle)), 0, 0],
            [sin(radians(angle)), cos(radians(angle)), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def rotate_xy(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, cos(radians(angle)), -sin(radians(angle))],
            [0, 0, sin(radians(angle)), cos(radians(angle))],
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def rotate_xz(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, cos(radians(angle)), 0, sin(radians(angle))],
            [0, 0, 1, 0],
            [0, -sin(radians(angle)), 0, cos(radians(angle))],
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def rotate_yz(self, figure4D: dict = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, 0, sin(radians(angle))],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-sin(radians(angle)), 0, 0, cos(radians(angle))],
        ]
        figure4D['points'] = self._dot(figure4D['points'], matrix)
        return figure4D

    def intersection_4D(self, figure4D: dict = (), coordinate_w: float =1.0):
        points3D = []
        polygons3D = []  # НЕ РЕАЛИЗОВАНО !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        edges3D = []  # КОСТЫЛЬ (пока что)
        points4D = figure4D['points']
        polygons4D = figure4D['polygons']
        # перебор полигонов и поиск тех, которые находятся на искомой координате
        for polygon in polygons4D:
            # перебор точек полигона (в контексте линий)
            if len(polygon) > 2:
                index = 0
                edge = []  # грань
                while index < len(polygon):
                    # запоминаем W'ки точек отрезка
                    poly1 = points4D[polygon[index]]
                    if index + 1 == len(polygon):
                        poly2 = points4D[polygon[0]]
                    else:
                        poly2 = points4D[polygon[index + 1]]
                    # если первый > второго, то меняем местами, (для правильного диапазона)
                    if poly1[3] > poly2[3]:
                        poly1, poly2 = poly2, poly1
                    # проверяем, входит ли искомая координата в искомый диапазон
                    if coordinate_w >= poly1[3] and coordinate_w <= poly2[3]:
                        # вычисляем координаты новой точки, которая лежит на данном отрезке
                        # получем отношение получившихся 2х отрезков (по W координате, потому что знаем только ее)
                        # получаем альфу отношения
                        if coordinate_w - poly2[3] != 0:
                            alfa = fabs(coordinate_w - poly1[3]) / fabs(coordinate_w - poly2[3])
                            # получаем координаты новой точки
                            x = (poly1[0] + alfa * poly2[0]) / (1 + alfa)
                            y = (poly1[1] + alfa * poly2[1]) / (1 + alfa)
                            z = (poly1[2] + alfa * poly2[2]) / (1 + alfa)
                            # добавляем новую точку в 3Д массив
                            if [x, y, z] not in points3D:
                                points3D.append([x, y, z, coordinate_w])
                            edge.append(points3D.index([x, y, z, coordinate_w]))
                    index += 1
                # костыльный метод соединения граней !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                if edge != [] and edge not in edges3D:
                    edges3D.append(edge)
        print(coordinate_w)
        return {'points': points3D, 'edges': edges3D, 'polygons': polygons3D}

    def projection_3D(self, figure4D: dict = (), distance: float = 1.0):
        projection = np.array([
            [0., 0., 0., 0],
            [0., 0., 0., 0],
            [0., 0., 0., 0]
        ], float)
        array = np.array(figure4D['points'])
        if array is not None:
            result: list = []
            if len(array.shape) == 2 and array.shape[1] == 4:
                for row_XYZW in array:
                    projection[0][0] = 1.0 / (distance - row_XYZW[3])
                    projection[1][1] = 1.0 / (distance - row_XYZW[3])
                    projection[2][2] = 1.0 / (distance - row_XYZW[3])
                    result.append(projection.dot(row_XYZW.reshape(4, 1)).reshape(1, 3)[0])
            figure4D['points'] = result
            return figure4D


    def scale(self, figure: dict = (), value=1.0):
        array = np.array(figure['points'])
        array = array.dot(value)
        figure['points'] = array.tolist()
        return figure
