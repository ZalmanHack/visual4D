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

    def rotate_x(self, points3D: list = (), angle=1.0):
        matrix = [
            [1, 0, 0],
            [0, cos(radians(angle)), -sin(radians(angle))],
            [0, sin(radians(angle)), cos(radians(angle))]
        ]
        return self._dot(points3D, matrix)

    def rotate_y(self, points3D: list = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, -sin(radians(angle))],
            [0, 1, 0],
            [sin(radians(angle)), 0, cos(radians(angle))]
        ]
        return self._dot(points3D, matrix)

    def rotate_z(self, points3D: list = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), -sin(radians(angle)), 0],
            [sin(radians(angle)), cos(radians(angle)), 0],
            [0, 0, 1]
        ]
        return self._dot(points3D, matrix)

    def projection_2D(self, points3D: list = (), distance=1.0):
        projection = np.array([
            [0., 0., 0.],
            [0., 0., 0.]
        ], float)
        array = np.array(points3D)
        if array is not None:
            result: list = []
            if len(array.shape) == 2 and array.shape[1] == 3:
                for row_XYZ in array:
                    projection[0][0] = 1.0 / (distance - row_XYZ[2])
                    projection[1][1] = 1.0 / (distance - row_XYZ[2])
                    result.append(projection.dot(row_XYZ.reshape(3, 1)).reshape(1, 2)[0])
            return result

    def scale(self, points: list = (), value = 1.0):
        array = np.array(points)
        array = array.dot(value)
        return array.tolist()

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

    def rotate_xw(self, points4D: list = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, cos(radians(angle)), -sin(radians(angle)), 0],
            [0, sin(radians(angle)), cos(radians(angle)), 0],
            [0, 0, 0, 1]
        ]
        return self._dot(points4D, matrix)

    def rotate_yw(self, points4D: list = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, -sin(radians(angle)), 0],
            [0, 1, 0, 0],
            [sin(radians(angle)), 0, cos(radians(angle)), 0],
            [0, 0, 0, 1]
        ]
        return self._dot(points4D, matrix)

    def rotate_zw(self, points4D: list = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), -sin(radians(angle)), 0, 0],
            [sin(radians(angle)), cos(radians(angle)), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ]
        return self._dot(points4D, matrix)

    def rotate_xy(self, points4D: list = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, cos(radians(angle)), -sin(radians(angle))],
            [0, 0, sin(radians(angle)), cos(radians(angle))],
        ]
        return self._dot(points4D, matrix)

    def rotate_xz(self, points4D: list = (), angle=1.0):
        matrix = [
            [1, 0, 0, 0],
            [0, cos(radians(angle)), 0, sin(radians(angle))],
            [0, 0, 1, 0],
            [0, -sin(radians(angle)), 0, cos(radians(angle))],
        ]
        return self._dot(points4D, matrix)

    def rotate_yz(self, points4D: list = (), angle=1.0):
        matrix = [
            [cos(radians(angle)), 0, 0, sin(radians(angle))],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [-sin(radians(angle)), 0, 0, cos(radians(angle))],
        ]
        return self._dot(points4D, matrix)

    def projection_3D(self, points4D: list = (), distance=1.0):
        projection = np.array([
            [0., 0., 0., 0],
            [0., 0., 0., 0],
            [0., 0., 0., 0]
        ], float)
        array = np.array(points4D)
        if array is not None:
            result: list = []
            if len(array.shape) == 2 and array.shape[1] == 4:
                for row_XYZW in array:
                    projection[0][0] = 1.0 / (distance - row_XYZW[3])
                    projection[1][1] = 1.0 / (distance - row_XYZW[3])
                    projection[2][2] = 1.0 / (distance - row_XYZW[3])
                    result.append(projection.dot(row_XYZW.reshape(4, 1)).reshape(1, 3)[0])
            return result

    def scale(self, points: list = (), value = 1.0):
        array = np.array(points)
        array = array.dot(value)
        return array.tolist()