import numpy as np
from tkinter import Tk
from Camera import Camera
from Scene import Scene
from Renderer import Renderer
from Mesh import Mesh
from math3d import Vector4D, Vector3D, Quaternion

def InitCamera() -> Camera:
	cam = Camera()
	cam.UpdatePerspective(60, 16/9, 1, 100)
	cam.UpdateView(Vector3D(0, 5, 10), Vector3D(0.0, 0.0, 0.0), Vector3D(0.0, 1, 0.0))
	return cam



if __name__ == "__main__":
	mesh = Mesh([Vector4D(1, 1, 1, 1),
			  Vector4D(-1, 1, 1, 1),
			  Vector4D(-1, 1, -1, 1),
			  Vector4D(1, 1, -1, 1),
			  Vector4D(1, -1, 1, 1),
			  Vector4D(-1, -1, 1, 1),
			  Vector4D(-1, -1, -1, 1),
			  Vector4D(1, -1, -1, 1),], [0, 1, 2, 3, 0, 4, 5, 1, 5, 6, 2, 6, 7, 3, 7, 4])
	scene = Scene()
	camera = InitCamera()
	scene.setCamera(camera)
	scene += mesh
	mesh.UpdatePosition(Vector3D(1, 0, 0))
	scene += mesh
	mesh.UpdatePosition(Vector3D(-1, 0, 0))
	scene += mesh
	renderer = Renderer(640, 360, 0)
	#renderer.pen().screen.onkey(lmd, "q")
	#renderer.pen().screen.listen()
	while(True):
		renderer.Clear()
		renderer.Render(scene)
		renderer.SwapBuffer()

turtle.mainloop()
	
