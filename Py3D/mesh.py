from turtle import position
from .general_imports import *

class Mesh:
    def __init__(self, parnet):
        self.points = []
        self.lines = []
        self.rotation = [0, 0, 0]
        self.position = [0, 0, 0]
        self.parent = parnet

    def add_point(self, position):
        position = [position[0] * 100, position[1] * 100, position[2] * 100, 1]
        self.points.append(np.matrix(position))

    def add_line(self, point1, point2):
        point1 = [point1[0] * 100, point1[1] * 100, point1[2] * 100, 1]
        point2 = [point2[0] * 100, point2[1] * 100, point2[2] * 100, 1]
        self.lines.append([point1, point2])

    def get_rotated_matrix(self):
        angle_x = math.radians(self.rotation[0])
        angle_y = math.radians(self.rotation[1])
        angle_z = math.radians(self.rotation[2])

        pos_x = self.position[0]
        pos_y = self.position[1]
        pos_z = self.position[2]

        rotation_z = np.matrix([
            [np.cos(angle_z), -np.sin(angle_z), 0, 0],
            [np.sin(angle_z), np.cos(angle_z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ],)

        rotation_y = np.matrix([
            [np.cos(angle_y), 0, np.sin(angle_y), 0],
            [0, 1, 0, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y), 0],
            [0, 0, 0, 1]
        ])

        rotation_x = np.matrix([
            [1, 0, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x), 0],
            [0, np.sin(angle_x), np.cos(angle_x), 0],
            [0, 0, 0, 1],
        ])

        return rotation_x * rotation_y * rotation_z

    def draw(self, window):
        translation = [self.position[0] * 100, self.position[1] * 100, self.position[2] * 100, 0]

        for point in self.points:
            p = np.reshape(point, (4, 1))
            rot = self.get_rotated_matrix()
            projection = np.dot(self.parent.projection_matrix, p)
            projection = rot * projection + translation
            projection = projection.tolist()
            x = projection[0][0]
            y = projection[1][0]
            pygame.draw.circle(window, (255, 255, 255), (int(x) + window.get_width() / 2 - 100, int(y) + window.get_width() / 2- 100) , 3)

        for line in self.lines:
            p1 = np.reshape(line[0], (4, 1))
            p2 = np.reshape(line[1], (4, 1))
            rot = self.get_rotated_matrix()
            projection1 = np.dot(self.parent.projection_matrix, p1)
            projection2 = np.dot(self.parent.projection_matrix, p2)
            projection1 = rot * projection1 + translation
            projection2 = rot * projection2 + translation
            projection1 = projection1.tolist()
            projection2 = projection2.tolist()
            x1 = projection1[0][0]
            y1 = projection1[1][0]
            x2 = projection2[0][0]
            y2 = projection2[1][0]
            pygame.draw.line(window, (255, 255, 255), (int(x1) + window.get_width() / 2 - 100, int(y1) + window.get_width() / 2- 100), (int(x2) + window.get_width() / 2 - 100, int(y2) + window.get_width() / 2- 100), 1)