from __future__ import annotations
import numpy as np
from Vector3D import Vector3D

class Vector4D(object):
	__value = np.zeros(4)

	def __init__(self, x=0.0, y=0.0, z=0.0, w=0.0):
		self.__value = np.array([x, y, z, w])
	
	@classmethod
	def fromVector3(cls, vec3=Vector3D, w=1.0):
		return cls(vec3.x(), vec3.y(), vec3.z(), w)

	@classmethod
	def fromArray(cls, array=[0, 0, 0, 0]):
		return cls(array[0], array[1], array[2], array[3])

	def __add__(self, other='Vector4D') -> Vector4D:
		return Vector4D.fromArray(self.__value + other.__value)

	def __sub__(self, other='Vector4D') -> Vector4D:
		return Vector4D.fromArray(self.__value - other.__value)

	def __mul__(self, other='Vector4D') -> Vector4D:
		return Vector4D.fromArray(self.__value * other.__value)

	def floatMul(self, other=float) -> Vector4D:
		return Vector4D.fromArray(self.__value * other)

	def __div__(self, other='Vector4D') -> Vector4D:
		return Vector4D.fromArray(self.__value / other.__value)

	def __iadd__(self, other='Vector4D') -> Vector4D:
		self.__value += other.__value
		return self

	def __isub__(self, other='Vector4D') -> Vector4D:
		self.__value -= other.__value
		return self

	def __imul__(self, other='Vector4D') -> Vector4D:
		self.__value *= other.__value
		return self

	def __idiv__(self, other='Vector4D') -> Vector4D:
		self.__value /= other.__value
		return self

	def __neg__(self):
		return Vector4D.fromArray(-self.__value)

	def dot(self, other='Vector4D') -> float:
		return np.dot(self.__value, other.__value)

	def norm(self) -> float:
		return np.linalg.norm(self.__value)

	def normalize(self) -> Vector4D:
		return Vector4D.fromArray(self.__value / self.norm())

	def inormalize(self) -> Vector4D:
		self.__value /= self.norm()
		return self

	def x(self) -> float:
		return self.__value[0]

	def y(self) -> float:
		return self.__value[1]

	def z(self) -> float:
		return self.__value[2]

	def w(self) -> float:
		return self.__value[3]

	def xyz(self) -> Vector3D:
		return Vector3D(self.x(), self.y(), self.z())

	def value(self):
		return self.__value


