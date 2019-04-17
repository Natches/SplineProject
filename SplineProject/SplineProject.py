import numpy as np
from tkinter import Tk
from Camera import Camera
import turtle
from turtle import Turtle
from Mesh import Mesh
from math3d import Vector4D, Vector3D, Quaternion

if __name__ == "__main__":
	mesh = Mesh([Vector4D(1, 1, 1, 1),
			  Vector4D(-1, 1, 1, 1),
			  Vector4D(-1, 1, -1, 1),
			  Vector4D(1, 1, -1, 1)], [0, 1, 2, 3, 0])
	cam = Camera()
	cam.UpdatePerspective(60, 16/9, 1, 100)
	cam.UpdateView(Vector3D(0, 5, 10), Vector3D(0.0, 0.0, 0.0), Vector3D(0.0, 1, 0.0))
	pen = Turtle()
	pen.speed(0)
	pen.hideturtle()
	pen.pu()
	yangle = 10
	mesh.UpdatePosition(Vector3D(0, 0, 0))
	pen.screen.tracer(0, 0)
	while(True):
		pen.clear()
		mesh.UpdateRotation(Quaternion.fromEuler(Vector3D( 0, 0, yangle)))
		mesh.Draw(pen, cam)
		pen.screen.update()
		yangle += 0.1

turtle.mainloop()
	
