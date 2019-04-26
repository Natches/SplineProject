from __future__ import annotations
import numpy as np
import Utils

class Matrix4x3(object):
	__value = np.zeros((4, 3))

	def __init__(self, array=[[1.0, 0, 0], [0.0, 1, 0], [0.0, 0, 1], [0.0, 0, 0]]):
		assert(array.__len__() == 4 and array[0].__len__() == 3 and array[1].__len__() == 3 and array[2].__len__() == 3 and array[3].__len__() == 3)
		self.__value = array

	def inverse(self) -> Matrix4x3:
		self.__value = np.inv(self.__value)
		return self

	def __getitem__(self, key) -> []:
		assert(key < 4)
		return self.__value[key]

	@property
	def value(self) -> np.ndarray:
		return self.__value

def Inverse(matrice=Matrix4x3) -> Matrix4x3:
	return Matrix4x3(np.inv(matrice.value))