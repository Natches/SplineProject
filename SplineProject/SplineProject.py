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
	renderer = Renderer(1280, 720, 0)

	scene = Scene()
	camera = InitCamera()
	curve = sp.HermitienneCurve(renderer.pen.screen.getcanvas(), camera)
	curve.p1 = Vector3D([-1,0,0])
	curve.p2 = Vector3D([1,0,0])
	curve.r1 = Vector3D([-1,10,0])
	curve.r2 = Vector3D([0,10,0])
	curve.precision = 100
	scene.camera = camera
	scene += curve

	def renderScene():
		timeNow = time.datetime.now()
		renderer.clear()
		renderer.render(scene)
		renderer.swap_buffer()
		deltatime = (time.datetime.now() - timeNow).microseconds / 1000
		#print(((int)(1000 / deltatime)).__str__())
		renderer.pen.screen.ontimer(renderScene, 0)
	renderer.pen.screen.ontimer(renderScene, 0)

renderer.pen.screen.mainloop()
	
