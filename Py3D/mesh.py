from .general_imports import *

class Mesh:
    def __init__(self, parnet):
        self.points = []
        self.parent = parnet

    def add_point(self, position):
        self.points.append(np.matrix(position))

    def draw(self, window):
        for point in self.points:
            p = np.reshape(point, (3, 1))
            projection = np.dot(self.parent.projection_matrix, p)
            projection = projection.tolist()
            x = projection[0][0]
            y = projection[1][0]
            pygame.draw.circle(window, (255, 255, 255), (int(x) + window.get_width() / 2, int(y) + window.get_width() / 2), 1)
