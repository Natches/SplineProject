import numpy as np
from tkinter import Tk
from Camera import Camera
from Scene import Scene
from Renderer import Renderer
from Mesh import Mesh
from math3d import Vector4D, Vector3D, Quaternion

import datetime as time

def InitCamera() -> Camera:
	cam = Camera()
	cam.UpdatePerspective(60, 16/9, 1, 100)
	cam.UpdateView(Vector3D([0, 0, -10]), Vector3D([0, 0.0, -11]), Vector3D([0.0, 1, 0.0]))
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
	scene.setCamera(camera)
	mesh.UpdatePosition(Vector3D(0,0,-20))
	scene += mesh
	renderer = Renderer(640, 360, 0)
	deltatime = 0.001
	speed = 500	

	def MoveCameraUp(event):
		up = Vector3D(0,1,0).floatMul(deltatime).floatMul(speed)
		camera.UpdateView((camera.eye() + up), camera.at() + up, camera.up())

	def MoveCameraDown(event):
		up = Vector3D(0,1,0).floatMul(deltatime).floatMul(speed)
		camera.UpdateView((camera.eye() - up), camera.at() - up, camera.up())

	def MoveCameraForward(event):
		dir = (camera.at() - camera.eye()).normalize().floatMul(deltatime).floatMul(speed)
		camera.UpdateView(camera.eye() + dir, camera.at() + dir, camera.up())
		print(dir._Vector3D__value.__str__())
		print(camera.eye()._Vector3D__value.__str__())
		print(camera.at()._Vector3D__value.__str__())

	def MoveCameraBackward(event):
		dir = (camera.at() - camera.eye()).normalize().floatMul(deltatime).floatMul(speed)
		camera.UpdateView(camera.eye() - dir, camera.at() - dir, camera.up())

	def MoveCameraRight(event):
		dir = (camera.at() - camera.eye())
		right = dir.normalize().cross(camera.up()).floatMul(deltatime).floatMul(speed)
		camera.UpdateView(camera.eye() + right, camera.at() + right, camera.up())

	def MoveCameraLeft(event):
		dir = (camera.at() - camera.eye())
		right = dir.normalize().cross(camera.up()).floatMul(deltatime).floatMul(speed)
		camera.UpdateView(camera.eye() - right, camera.at() - right, camera.up())

	renderer.pen().screen.getcanvas().bind("w", MoveCameraForward)
	renderer.pen().screen.getcanvas().bind("s", MoveCameraBackward)
	renderer.pen().screen.getcanvas().bind("q", MoveCameraUp)
	renderer.pen().screen.getcanvas().bind("e", MoveCameraDown)
	renderer.pen().screen.getcanvas().bind("a", MoveCameraLeft)
	renderer.pen().screen.getcanvas().bind("d", MoveCameraRight)

	def render():
		timeNow = time.datetime.now()
		renderer.Clear()
		renderer.Render(scene)
		renderer.pen().pd()
		renderer.pen().setpos(0, 0)
		renderer.pen().setpos(0, 10)
		renderer.SwapBuffer()
		deltatime = (time.datetime.now() - timeNow).microseconds / 1000000
		renderer.pen().screen.ontimer(render, 16)
	renderer.pen().screen.ontimer(render, 16)
	renderer.pen().screen.listen()

renderer.pen().screen.mainloop()
	
