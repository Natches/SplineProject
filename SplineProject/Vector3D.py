from __future__ import annotations
import numpy as np
import Utils
from Vector2D import Vector2D

class Vector3D(object):
	__value = np.zeros(3)

	def __init__(self, array=[0, 0, 0]):
		self.__value = np.array(array)

	@Utils.OperatorDecorator
	def __add__(self, other) -> Vector3D:
		return Vector3D(self.__value + other)
	
	@Utils.OperatorDecorator
	def __sub__(self, other) -> Vector3D:
		return Vector3D(self.__value - other)
	
	@Utils.OperatorDecorator
	def __mul__(self, other) -> Vector3D:
		return Vector3D(self.__value * other)
	
	@Utils.OperatorDecorator
	def __div__(self, other) -> Vector3D:
		return Vector3D(self.__value / other)
	
	@Utils.OperatorDecorator
	def __iadd__(self, other) -> Vector3D:
		self.__value += other
		return self

	@Utils.OperatorDecorator
	def __isub__(self, other) -> Vector3D:
		self.__value -= other
		return self

	@Utils.OperatorDecorator
	def __imul__(self, other) -> Vector3D:
		self.__value *= other
		return self

	@Utils.OperatorDecorator
	def __idiv__(self, other) -> Vector3D:
		self.__value /= other
		return self

	def __neg__(self) -> Vector3D:
		return Vector3D(-self.__value)

	def dot(self, other='Vector3D') -> float:
		return np.dot(self.__value, other.__value)

	def norm(self) -> float:
		return np.linalg.norm(self.__value)

	def normalize(self) -> Vector3D:
		norm = self.norm()
		if(norm != 0):
			self = self.__div__(norm)
		return self

	@property
	def x(self) -> float:
		return self.__value[0]

	@property
	def y(self) -> float:
		return self.__value[1]

	@property
	def z(self) -> float:
		return self.__value[2]

	@property
	def xy(self) -> Vector2D:
		return Vector2D(self.__value[0:2])

	@property
	def yz(self) -> Vector2D:
		return Vector2D(self.__value[1:3])

	@x.setter
	def x(self, value) -> None:
		self.__value[0] = value

	@y.setter
	def y(self, value) -> None:
		self.__value[1] = value

	@z.setter
	def z(self, value) -> None:
		self.__value[2] = value

	@property
	def value(self) -> np.ndarray:
		return self.__value


