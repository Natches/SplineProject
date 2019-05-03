from turtle import RawTurtle, Screen
from Scene import Scene
import turtle
import tkinter as TK

class Screen(turtle._Screen):

	def onEvent(self,event):
		self.getcanvas().hscroll.grid_forget()
		self.getcanvas().vscroll.grid_forget()

	def __init__(self):
		super().__init__()
		self._root.resizable(False, False)
		self._root.bind( '<Configure>', self.onEvent)

	def setup(self, width, height, startx, starty):
		super().setup(width=width, height=height, startx=startx, starty=starty)
		self.getcanvas().hscroll.grid_forget()
		self.getcanvas().vscroll.grid_forget()

	def setworldcoordinates(self, llx, lly, urx, ury):
		if self.mode() != "world":
			self.mode("world")
		xspan = float(urx - llx)
		yspan = float(ury - lly)
		wx, wy = self._window_size()
		self.screensize(wx, wy)
		oldxscale, oldyscale = self.xscale, self.yscale
		self.xscale = self.canvwidth / xspan
		self.yscale = self.canvheight / yspan
		self._setscrollregion(0, 0, wx, wy)
		self.getcanvas().hscroll.grid_forget()
		self.getcanvas().vscroll.grid_forget()



class Renderer(object):
	__screen = Screen()
	__pen = RawTurtle

	def __init__(self, width=int, height=int, speed=0):
		self.__screen.setup(width, height, startx=0, starty=0)
		self.__screen.setworldcoordinates(0, height, width, 0)
		self.__screen.tracer(0, 0)
		self.__screen.listen()
		self.__pen = RawTurtle(self.__screen, undobuffersize=0)
		self.__pen.pu()
		self.__pen.speed(speed)
		self.__pen.hideturtle()
		self.__pen.resizemode("noresize")
		self.__pen.setundobuffer(None)

	def render(self, scene=Scene):
		for entity in scene:
			entity.draw(self.__pen, scene.camera)

	def clear(self):
		self.__pen.clear()

	def swap_buffer(self):
		self.__screen.update()

	@property
	def pen(self) -> RawTurtle:
		return self.__pen

