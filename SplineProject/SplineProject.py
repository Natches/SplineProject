import numpy as np
from tkinter import Tk
from Camera import Camera
from Scene import Scene
from Renderer import Renderer
from Mesh import Mesh
from math3d import Vector4D, Vector3D, Quaternion
import math3d
import datetime as time

def InitCamera() -> Camera:
	cam = Camera()
	cam.update_perspective(60, 16/9, 1, 100)
	cam.update_view(Vector3D([0, 5, -10]), Vector3D([0, 0.0, 0]), Vector3D([0.0, 1, 0.0]))
	return cam

if __name__ == "__main__":
	mesh = Mesh([Vector4D([1, 1, 1, 1]),
			  Vector4D([-1, 1, 1, 1]),
			  Vector4D([-1, 1, -1, 1]),
			  Vector4D([1, 1, -1, 1]),
			  Vector4D([1, -1, 1, 1]),
			  Vector4D([-1, -1, 1, 1]),
			  Vector4D([-1, -1, -1, 1]),
			  Vector4D([1, -1, -1, 1]),], [0, 1, 2, 3, 0, 4, 5, 1, 5, 6, 2, 6, 7, 3, 7, 4])
	scene = Scene()
	camera = InitCamera()
	scene.camera = camera
	scene += mesh
	renderer = Renderer(640, 360, 0)

	def renderScene():
		timeNow = time.datetime.now()
		renderer.clear()
		renderer.render(scene)
		renderer.swap_buffer()
		deltatime = (time.datetime.now() - timeNow).microseconds / 1000000
		renderer.pen.screen.ontimer(render, 0)
	renderer.pen.screen.ontimer(render, 0)
	renderer.pen.screen.listen()

renderer.pen.screen.mainloop()
	
