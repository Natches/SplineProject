from turtle import Turtle, Screen
from Scene import Scene
import turtle

class Renderer(object):
	__screen = Screen()
	__pen = Turtle()

	def __init__(self, width=int, height=int, speed=0):
		self.__screen.setup(width, height, startx=0, starty=0)
		self.__screen.screensize(width, height)
		self.__screen.setworldcoordinates(0, 0, width, height)
		self.__screen.tracer(0, 0)
		self.__screen.listen()
		self.__pen.speed(speed)
		self.__pen.hideturtle()
		self.__pen.home()
		self.__pen.pu()
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

