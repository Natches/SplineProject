import numpy as np
from tkinter import Tk
from Camera import Camera
from Scene import Scene
from Renderer import Renderer
from Mesh import Mesh
from math3d import Vector4D, Vector3D, Quaternion
import math3d
import datetime as time
import Spline as sp

def InitCamera() -> Camera:
	cam = Camera()
	cam.update_perspective(60, 16/9, 1, 100)
	cam.update_view(Vector3D([0, 0.00000000001, -10]), Vector3D([0, 0.0, 0]), Vector3D([0.0, 1, 0.0]))
	return cam

if __name__ == "__main__":
	curve = sp.HermitienneCurve()
	curve.p1 = Vector3D([-1,0,0])
	curve.p2 = Vector3D([1,0,0])
	curve.r1 = Vector3D([1,-10,0])
	curve.r2 = Vector3D([-1,10,0])
	vertex = []
	indices = []
	i = 0
	t = 0
	while t < 1:
		vertex.append(curve.compute(t))
		indices.append(i)
		i += 1
		t += curve._Curve__precision

	mesh = Mesh(vertex, indices)
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
		renderer.pen.screen.ontimer(renderScene, 0)
	renderer.pen.screen.ontimer(renderScene, 0)
	renderer.pen.screen.listen()

renderer.pen.screen.mainloop()
	
