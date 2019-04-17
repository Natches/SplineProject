import numpy as np

class Vector2D(object):
	__value = np.zeros(2)

	def __init__(self, x=float, y=float):
		self.__value[0] = x
		self.__value[1] = y
		return super().__init__()

	def __add__(self, other=Vector2D):
		return self.__value + other.__value

	def __sub__(self, other=Vector2D):
		return self.__value - other.__value

	def __mul__(self, other=Vector2D):
		return self.__value * other.__value

	def __div__(self, other=Vector2D):
		return self.__value / other.__value

	def __iadd__(self, other=Vector2D):
		self.__value += other.__value
		return self.__value

	def __isub__(self, other=Vector2D):
		self.__value -= other.__value
		return self.__value

	def __imul__(self, other=Vector2D):
		self.__value *= other.__value
		return self.__value

	def __idiv__(self, other=Vector2D):
		self.__value /= other.__value
		return self.__value

	def dot(self, other=Vector2D):
		return np.dot(self.__value, other.__value)

	def norm(self):
		return np.linalg.norm(self.__value, ord=1)

	def normalize(self):
		return self.__value / self.norm()

	def inormalize(self):
		self.__value /= self.norm()
		return self.__value

	def x(self):
		return self.__value[0]

	def y(self):
		return self.__value[1]
