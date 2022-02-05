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

def move(events):
    for i in events:
        if i.type == 771:
            if i.text == 'w':
                win.camera[0][2] -= 1
            if i.text == 's':
                win.camera[0][2] += 1
            if i.text == 'a':
                win.camera[0][0] -= 1
            if i.text == 'd':
                win.camera[0][0] += 1

win.on_events(move)
win.run()
