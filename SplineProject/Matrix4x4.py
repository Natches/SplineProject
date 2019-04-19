from __future__ import annotations
import numpy as np
from Vector4D import Vector4D
import Utils

class Matrix4x4(object):
	__value = np.zeros((4, 4))

	def __init__(self, array=[[1.0, 0, 0, 0], [0.0, 1, 0, 0], [0.0, 0, 1, 0], [0.0, 0, 0, 1]]):
		assert(array.__len__() == 4 and array[0].__len__() == 4 and array[1].__len__() == 4 and array[2].__len__() == 4 and array[3].__len__() == 4)
		self.__value = array

	def transpose(self) -> Matrix4x4:
		self.__value = np.transpose(self.__value)
		return self

	def inverse(self) -> Matrix4x4:
		self.__value = np.inv(self.__value)
		return self

	@Utils.operatorDecorator
	def __mul__(self, other) -> Matrix4x4:
		return Matrix4x4(np.matmul(self.__value, other))

	@Utils.operatorDecorator
	def __imul__(self, other) -> Matrix4x4:
		self.__value = np.matmul(self.__value, other)
		return self

	def __getitem__(self, key) -> []:
		assert(key < 4)
		return self.__value[key]

	@property
	def value(self) -> np.ndarray:
		return self.__value

def Transpose(matrice=Matrix4x4) -> Matrix4x4:
	return Matrix4x4(np.transpose(matrice.value))

def Inverse(matrice=Matrix4x4) -> Matrix4x4:
	return Matrix4x4(np.inv(matrice.value))