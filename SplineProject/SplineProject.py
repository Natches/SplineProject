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
	cam = Camera('ortho')
	cam.update_ortho(20, 20, 1, 100)
	cam.update_perspective(60, 16/9, 1, 100)
	cam.update_view(Vector3D([0, 0.00000000001, -10]), Vector3D([0, 0.0, 0]), Vector3D([0.0, 1, 0.0]))
	return cam

if __name__ == "__main__":
	renderer = Renderer(640, 360, 0)
	scene = Scene()
	scene.camera = InitCamera()
	curve = sp.HermitienneCurve(renderer.pen.screen, scene.camera,
							[Vector3D([-1,0,0]), Vector3D([1,0,0])],
							[Vector3D([0,100,0]), Vector3D([0,100,0])])
	scene += curve

	def renderScene():
		sp.canDrag = True
		timeNow = time.datetime.now()
		renderer.clear()
		renderer.render(scene)
		renderer.swap_buffer()
		deltatime = (time.datetime.now() - timeNow).microseconds / 1000
		#print(((int)(1000 / deltatime)).__str__())
		renderer.pen.screen.ontimer(renderScene, 0)
	renderer.pen.screen.ontimer(renderScene, 0)

renderer.pen.screen.mainloop()
	
