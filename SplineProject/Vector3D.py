import numpy as np
from Vector2D import Vector2D

class Vector3D(object):
	__value = np.zeros(3)

	def __init__(self, x=float, y=float, z=float):
		self.__value[0] = x
		self.__value[1] = y
		self.__value[2] = z
		return super().__init__()

	def __add__(self, other=Vector3D):
		return self.__value + other.__value

	def __sub__(self, other=Vector3D):
		return self.__value - other.__value

	def __mul__(self, other=Vector3D):
		return self.__value * other.__value

	def __div__(self, other=Vector3D):
		return self.__value / other.__value

	def __iadd__(self, other=Vector3D):
		self.__value += other.__value
		return self.__value

	def __isub__(self, other=Vector3D):
		self.__value -= other.__value
		return self.__value

	def __imul__(self, other=Vector3D):
		self.__value *= other.__value
		return self.__value

	def __idiv__(self, other=Vector3D):
		self.__value /= other.__value
		return self.__value

	def dot(self, other=Vector3D):
		return np.dot(self.__value, other.__value)

	def cross(self, other=Vector3D):
		return np.cross(self.__value, other.__value)

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

	def z(self):
		return self.__value[2]

	def xy(self):
		return Vector2D(self.x(), self.y())

	def xz(self):
		return Vector2D(self.x(), self.z())

	def yz(self):
		return Vector2D(self.y(), self.z())


