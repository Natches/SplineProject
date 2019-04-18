from __future__ import annotations
import numpy as np
from Vector2D import Vector2D

class Vector3D(object):
	__value = np.zeros(3)

	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.__value = np.array([x, y, z])

	@classmethod
	def fromArray(cls, array=[0, 0, 0]) -> Vector3D:
		return cls(array[0], array[1], array[2])

	def __add__(self, other='Vector3D') -> Vector3D:
		return Vector3D.fromArray(self.__value + other.__value)

	def __sub__(self, other='Vector3D') -> Vector3D:
		return Vector3D.fromArray(self.__value - other.__value)

	def __mul__(self, other='Vector3D') -> Vector3D:
		return Vector3D.fromArray(self.__value * other.__value)

	def floatMul(self, other=float) -> Vector3D:
		return Vector3D.fromArray(self.__value * other)

	def __div__(self, other='Vector3D') -> Vector3D:
		return Vector3D.fromArray(self.__value / other.__value)

	def __iadd__(self, other='Vector3D') -> Vector3D:
		self.__value += other.__value
		return self

	def __isub__(self, other='Vector3D') -> Vector3D:
		self.__value -= other.__value
		return self

	def __imul__(self, other='Vector3D') -> Vector3D:
		self.__value *= other.__value
		return self

	def __idiv__(self, other='Vector3D') -> Vector3D:
		self.__value /= other.__value
		return self

	def __neg__(self):
		return Vector3D.fromArray(-self.__value)

	def dot(self, other='Vector3D') -> float:
		return np.dot(self.__value, other.__value)

	def cross(self, other='Vector3D') -> Vector3D:
		return Vector3D.fromArray(np.cross(self.__value, other.__value))

	def norm(self) -> float:
		return np.linalg.norm(self.__value)

	def normalize(self) -> Vector3D:
		return Vector3D.fromArray(self.__value / self.norm())

	def inormalize(self) -> Vector3D:
		self.__value /= self.norm()
		return self

	def x(self) -> float:
		return self.__value[0]

	def y(self) -> float:
		return self.__value[1]

	def z(self) -> float:
		return self.__value[2]

	def xy(self) -> Vector2D:
		return Vector2D(self.x(), self.y())

	def xz(self) -> Vector2D:
		return Vector2D(self.x(), self.z())

	def yz(self) -> Vector2D:
		return Vector2D(self.y(), self.z())

	def value(self):
		return self.__value


