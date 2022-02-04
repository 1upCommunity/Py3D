# Py3D demo

from Py3D.__init__ import *
import random

win = Py3dWindow(title="Py3D")
win.init_window()

mesh_ = Mesh(win)

side = 10

for i in range(-side, side):
    for j in range(-side, side):
        for k in range(-side, side):
            mesh_.add_point((i + random.random(), j + random.random(), k + random.random()))

win.add_mesh(mesh_)

def move():
    win.camera[1][0] += 0.01
    win.camera[1][1] += 0.01
    win.camera[1][2] += 0.01

win.on_update(lambda: move())
win.run()
