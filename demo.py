# Py3D demo

from Py3D.__init__ import *

win = Py3dWindow(title="Py3D")
win.init_window()

mesh_ = Mesh(win)
mesh_.add_point((0, 0, 0))
mesh_.add_point((0, 0, 100))
mesh_.add_point((0, 100, 0))
mesh_.add_point((0, 100, 100))
mesh_.add_point((100, 0, 0))
mesh_.add_point((100, 0, 100))
mesh_.add_point((100, 100, 0))
mesh_.add_point((100, 100, 100))

win.add_mesh(mesh_)

win.run()
