from __future__ import annotations
import numpy as np
import Utils


class Vector2D(object):
	__value = np.zeros(2)

	def __init__(self, array=[0, 0]):
		np.copyto(self.__value, array)

	@Utils.operatorDecorator
	def __add__(self, other) -> Vector2D:
		return self.__value + other

	@Utils.operatorDecorator
	def __sub__(self, other) -> Vector2D:
		return self.__value - other

	@Utils.operatorDecorator
	def __mul__(self, other) -> Vector2D:
		return self.__value * other

	@Utils.operatorDecorator
	def __div__(self, other) -> Vector2D:
		return self.__value / other

	@Utils.operatorDecorator
	def __iadd__(self, other) -> Vector2D:
		self.__value += other
		return self.__value

	@Utils.operatorDecorator
	def __isub__(self, other) -> Vector2D:
		self.__value -= other
		return self.__value

	@Utils.operatorDecorator
	def __imul__(self, other) -> Vector2D:
		self.__value *= other
		return self.__value

	@Utils.operatorDecorator
	def __idiv__(self, other) -> Vector2D:
		self.__value /= other
		return self.__value

	def __neg__(self, other='Vector2D') -> Vector2D:
		return -other.__value

	def dot(self, other='Vector2D') -> float:
		return np.dot(self.__value, other.__value)

	def norm(self) -> float:
		return np.linalg.norm(self.__value)

	def normalize(self) -> Vector2D:
		self /= self.norm()	
		return self

	@property
	def x(self) -> float:
		return self.__value[0]

	@property
	def y(self) -> float:
		return self.__value[1]

	@x.setter
	def x(self, value) -> None:
		self.__value[0] = value

	@y.setter
	def y(self, value) -> None:
		self.__value[1] = value

	@property
	def value(self) -> np.ndarray:
		return self.__value
