from __future__ import annotations
import numpy as np
from Vector4D import Vector4D

class Matrix4x4(object):
	__value = np.zeros((4, 4))

	def __init__(self, array=[[1.0, 0, 0, 0], [0.0, 1, 0, 0], [0.0, 0, 1, 0], [0.0, 0, 0, 1]]):
		assert(array.__len__() == 4 and array[0].__len__() == 4 and array[1].__len__() == 4 and array[2].__len__() == 4 and array[3].__len__() == 4)
		self.__value = array
		return super().__init__()

	def transpose(self) -> Matrix4x4:
		return Matrix4x4(np.transpose(self.__value))

	def inverse(self) -> Matrix4x4:
		return Matrix4x4(np.inv(self.__value))

	def __mul__(self, other='Matrix4x4') -> Matrix4x4:
		return Matrix4x4(np.matmul(self.__value, other.__value))

	def __imul__(self, other='Matrix4x4') -> Matrix4x4:
		self.__value = np.matmul(self.__value, other.__value)
		return self

	def mulVec4(self, other=Vector4D) -> Vector4D:
		return Vector4D.fromArray(np.matmul(self.__value, other.value()))

	def __getitem__(self, key):
		assert(key < 4)
		return self.__value[key]

	def value(self):
		return self.__value