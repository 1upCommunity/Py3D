from .general_imports import *

class Py3dWindow:
    def __init__(self, title=None, width=800, height=600,):
        self.title = title
        self.window = None
        self.width = width
        self.height = height
        self.meshes = []
    
        self.projection_matrix = np.matrix([
            [1, 0, 1],
            [0, 1, 1]
        ])

    def add_mesh(self, mesh):
        self.meshes.append(mesh)
    
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
