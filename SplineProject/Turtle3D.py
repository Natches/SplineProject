import turtle 

class Turtle3D(turtle.Turtle):
	def __init__(self, shape=_CFG ['shape' ], undobuffersize=_CFG ['undobuffersize' ], visible=_CFG ['visible' ]):
		return super().__init__(shape=shape, undobuffersize=undobuffersize, visible=visible)


