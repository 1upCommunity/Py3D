# Taken from: https://github.com/Josephbakulikira/3D-engine-from-scraph--pygame/blob/master/engine/utils/camera.py

from math import tan, pi
from .general_imports import *

class Camera:
    def __init__(self, position, near, far, fov):
        self.position = position
        self.near = near
        self.far = far
        self.fov = fov
        self.yaw = 0
        self.tangent = 1.0 / tan(self.fov * 0.5 / 180 * pi)
        self.direction = []

    def projection(self):
        """Compute the projection Matrix corresponding to the current camera position
        and orientation.
        Returns:
            Matrix - the projection matrix
        """
        matrix = np.matrix([
            [75 * self.tangent, 0.0, 0.0],
            [0.0, self.tangent, 0.0],
            [0.0, 0.0, self.far / (self.far - self.near)],
            [0.0, 0.0, (-self.far * self.near) / (self.far - self.near)],
        ])
        return matrix

    def set_pos(self, pos):
        """Set the camera position
        Args:
            pos (list) - the new position
        """
        self.transform = pos
