import numpy as np
from tkinter import Tk
from Camera import Camera
import turtle
from turtle import Turtle
from Vector2D import Vector2D
from Matrix4x4 import Matrix4x4

if __name__ == "__main__":
	cam = Camera()
	cam.UpdatePerspective(60, 16/9, 1, 100)
	cam.UpdateView(np.array([-5.0, 5, 10]), np.array([0.0, 0.0, 0.0]), np.array([0.0, 1, 0.0]))
	pen = Turtle()
	pen.speed(0)
	pen.hideturtle()
	pen.pu()
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([1, 1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pen.pd()
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([-1, 1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([-1, 1, -5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([1, 1, -5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([1, 1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)

	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([1, -1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([-1, -1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)
	pos = cam.From3DSpaceToScreen(cam.TransformPoint(np.array([-1, 1, 5, 1])))
	pen.setpos(pos[0] * pen.getscreen().canvwidth, pos[1] * pen.getscreen().canvheight)

turtle.mainloop()
	
