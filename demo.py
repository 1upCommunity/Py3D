# Py3D demo

from Py3D.__init__ import *

win = Py3dWindow(title="Py3D")
win.init_window()

mesh_ = Mesh(win)
mesh_.add_point((0, 0, 0))

# floor
for i in range(0, 100):
    for j in range(0, 100):
        mesh_.add_point((i, 0, j ))

win.add_mesh(mesh_)

# key movement
def keyboard():
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            win.running = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_ESCAPE:
                win.running = False
            if i.key == pygame.K_LEFT:
                win.camera[1][1] -= 0.01
            if i.key == pygame.K_RIGHT:
                win.camera[1][1] += 0.01
            if i.key == pygame.K_UP:
                win.camera[1][0] -= 0.01
            if i.key == pygame.K_DOWN:
                win.camera[1][0] += 0.01

win.on_events(lambda: keyboard())

win.run()
