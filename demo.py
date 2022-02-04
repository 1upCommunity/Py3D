# Py3D demo

from Py3D.__init__ import *
import random

win = Py3dWindow(title="Py3D")
win.init_window()

mesh_ = Mesh(win)

for i in range(-10, 10):
    for j in range(-10, 10):
        mesh_.add_point((i, random.randint(-1, 1) / 10, j))

win.add_mesh(mesh_)

# key movement
def move():
    win.camera[1][0] += 0.001
    win.camera[1][1] += 0.003
    win.camera[1][2] += 0.002
    win.camera[0][0] += 1

win.on_update(lambda: move())
win.run()
