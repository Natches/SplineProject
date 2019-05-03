from Vector2D import Vector2D
from Vector3D import Vector3D
from Vector4D import Vector4D
from Matrix4x4 import Matrix4x4
from Quaternion import Quaternion
from Matrix4x3 import Matrix4x3
import numpy as np
import copy

def Normalize(vector):
	norm = vector.norm()
	if(norm != 0):
		return vector.__div__(norm)
	return copy.deepcopy(vector)

def Cross(a, b):
	temp = np.cross(a.value, b.value)
	return Vector3D(np.cross(a.value, b.value))


def Transpose(matrice=Matrix4x4) -> Matrix4x4:
	return Matrix4x4(np.transpose(matrice.value))

def Inverse(matrice=Matrix4x4) -> Matrix4x4:
	return Matrix4x4(np.linalg.inv(matrice.value))

