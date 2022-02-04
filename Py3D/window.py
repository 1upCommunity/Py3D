from .general_imports import *

class Py3dWindow:
    def __init__(self, title=None, width=800, height=600,):
        self.title = title
        self.window = None
        self.width = width
        self.height = height
        self.meshes = []
    
        self.projection_matrix = np.matrix([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]
        ])

        self.camera = [
            [0, 0, 0],
            [0, 0, 0],
        ]

    def add_mesh(self, mesh):
        self.meshes.append(mesh)

    def rotate_matrix(self):
        angle_x = self.camera[1][0]
        angle_y = self.camera[1][1]
        angle_z = self.camera[1][2]

        rotation_z = np.matrix([
            [np.cos(angle_z), -np.sin(angle_z), 0],
            [np.sin(angle_z), np.cos(angle_z), 0],
            [0, 0, 1],
        ])

        rotation_y = np.matrix([
            [np.cos(angle_y), 0, np.sin(angle_y)],
            [0, 1, 0],
            [-np.sin(angle_y), 0, np.cos(angle_y)],
        ])

        rotation_x = np.matrix([
            [1, 0, 0],
            [0, np.cos(angle_x), -np.sin(angle_x)],
            [0, np.sin(angle_x), np.cos(angle_x)],
        ])

        self.projection_matrix = np.dot(rotation_z, np.dot(rotation_y, rotation_x))

    def move_matrix(self):
        self.projection_matrix = np.dot(np.matrix([
            [self.camera[0][0], self.camera[0][1], self.camera[0][2]],
            [self.camera[0][0], self.camera[0][1], self.camera[0][2]],
            [self.camera[0][0], self.camera[0][1], self.camera[0][2]]
        ]), self.projection_matrix)

    def init_window(self):
        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption(self.title)
        self.running = False

    def run(self,):
        self.running = True
        while self.running:
            self.draw()
            self.events()
            self.update()
            self.move_matrix()
            self.rotate_matrix()
        pygame.quit()

    def events(self,):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self,):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def draw(self,):
        self.window.fill((0, 0, 0))
        for mesh in self.meshes:
            mesh.draw(self.window)
        pygame.display.update()
        time.sleep(0.001)

    def on_events(self, func):
        self.events = lambda: func()
    
    def on_update(self, func):
        self.update = lambda: func()

    def on_draw(self, func):
        self.draw = lambda: func()
