import numpy as np
from Vector3D import Vector3D

class Vector4D(object):
	__value = np.zeros(4)

	def __init__(self, x=float, y=float, z=float, w=float):
		self.__value[0] = x
		self.__value[1] = y
		self.__value[2] = z
		self.__value[3] = w
		return super().__init__()
	
	def __init__(self, vec3=Vector3D, w=1.0):
		self.__value[0] = vec3.x
		self.__value[1] = vec3.y
		self.__value[2] = vec3.z
		self.__value[3] = w
		return super().__init__()

	def __add__(self, other=Vector4D):
		return self.__value + other.__value

	def __sub__(self, other=Vector4D):
		return self.__value - other.__value

	def __mul__(self, other=Vector4D):
		return self.__value * other.__value

	def __div__(self, other=Vector4D):
		return self.__value / other.__value

	def __iadd__(self, other=Vector4D):
		self.__value += other.__value
		return self.__value

	def __isub__(self, other=Vector4D):
		self.__value -= other.__value
		return self.__value

	def __imul__(self, other=Vector4D):
		self.__value *= other.__value
		return self.__value

	def __idiv__(self, other=Vector4D):
		self.__value /= other.__value
		return self.__value

	def dot(self, other=Vector4D):
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

	def z(self):
		return self.__value[2]

	def w(self):
		return self.__value[3]

	def xyz(self):
		return Vector3D(self.x(), self.y(), self.z())


