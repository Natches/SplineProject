from turtle import Turtle
from Scene import Scene

class Renderer(object):
	__pen = Turtle()

	def __init__(self, width=int, height=int, speed=0):
		self.__pen.screen.setup(width, height, startx=0, starty=0)
		self.__pen.screen.screensize(width, height)
		self.__pen.speed(speed)
		self.__pen.hideturtle()
		self.__pen.pu()
		self.__pen.screen.tracer(0, 0)

	def Render(self, scene=Scene):
		for entity in scene:
			entity.Draw(self.__pen, scene.camera())

	def Clear(self):
		self.__pen.clear()

	def SwapBuffer(self):
		self.__pen.screen.update()

	def pen(self) -> Turtle:
		return self.__pen

