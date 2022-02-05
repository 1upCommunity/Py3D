from .general_imports import *

class Mesh:
    def __init__(self, parnet):
        self.points = []
        self.parent = parnet

    def add_point(self, position):
        position = [position[0] * 100, position[1] * 100, position[2] * 100]
        self.points.append(np.matrix(position))

    def draw(self, window):
        p = (self.points[0] - self.parent.camera[0])
        print(self.points[0], p)
        for point in self.points:
            p = (point - self.parent.camera[0])
            p = np.reshape(p, (3, 1))
            projection = np.dot(self.parent.projection_matrix, p)
            projection = projection.tolist()
            x = projection[0][0]
            y = projection[1][0]
            pygame.draw.circle(window, (255, 255, 255), (int(x) + window.get_width() / 2 - 100, int(y) + window.get_width() / 2- 100) , 1)
