from turtle import Turtle
from Scene import Scene

class Renderer(object):
	__pen = Turtle()

	def __init__(self, width=int, height=int, speed=0):
		self.__pen.screen.setup(width, height, startx=0, starty=0)
		self.__pen.screen.screensize(width, height)
		self.__pen.screen.setworldcoordinates(0, height, width, 0)
		self.__pen.speed(speed)
		self.__pen.hideturtle()
		self.__pen.home()
		self.__pen.pu()
		self.__pen.screen.tracer(0, 0)
		self.__pen.resizemode("noresize")

	def render(self, scene=Scene):
		for entity in scene:
			entity.draw(self.__pen, scene.camera)

	def clear(self):
		self.__pen.clear()

	def swap_buffer(self):
		self.__pen.screen.update()

	@property
	def pen(self) -> Turtle:
		return self.__pen

