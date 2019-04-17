from __future__ import annotations
import numpy as np
from Vector3D import Vector3D
from Vector4D import Vector4D
from Matrix4x4 import Matrix4x4

class Quaternion(object):
	__value = Vector4D()

	def __init__(self, quat=Vector4D):
		self.__value = quat

	@classmethod
	def fromVec3(cls, vecPart=Vector3D, scalar=float):
		return cls(Vector4D.fromVector3(vecPart, scalar))

	@classmethod
	def fromEuler(cls, angle=Vector3D):
		return cls(cls.__fromEuler(cls, angle))

	def __fromEuler(self, angle=Vector3D) -> Vector4D:
		theta = angle.floatMul((3.14159265 / 180.0) * 0.5);
		cosV = Vector3D(np.cos(theta.x()), np.cos(theta.y()), np.cos(theta.z()));
		sinV = Vector3D(np.sin(theta.x()), np.sin(theta.y()), np.sin(theta.z()));
		 
		return Vector4D(sinV.x() * cosV.y() * cosV.z() + cosV.x() * sinV.y() * sinV.z(),
					cosV.x() * sinV.y() * cosV.z() - sinV.x() * cosV.y() * sinV.z(),
					sinV.x() * sinV.y() * cosV.z() + cosV.x() * cosV.y() * sinV.z(),
					cosV.x() * cosV.y() * cosV.z() - sinV.x() * sinV.y() * sinV.z());

	def invert(self) -> Quaternion:
		norm = self.norm();
		if (norm == 1.0):
			return self.conjugate()
		else:
			return Quaternion(Vector4D.fromArray((self.conjugate().__value).value() / (norm * norm)))

	def conjugate(self) -> Quaternion:
		return Quaternion.fromVec3(-self.__value.xyz(), self.__value.w())

	def rotate(self, other=Vector3D) -> Vector3D:
		vecPart = self.__value.xyz()
		scalar = self.__value.w()
		quatTemp = Quaternion.fromVec3(other.floatMul(scalar) + vecPart.cross(other), -(vecPart.dot(other)))
		return (Quaternion.fromVec3(other.floatMul(scalar) + vecPart.cross(other), -(vecPart.dot(other))) * self.invert()).__value.xyz()

	def rotate4D(self, other=Vector4D) -> Vector4D:
		return Vector4D(self.rotate(other.xyz()))

	def norm(self):
		return self.__value.norm()

	def normalize(self):
		return Quaternion(self.__value.normalize())

	def __add__(self, other='Quaternion') -> Quaternion:
		return self.__value + other.__value

	def __sub__(self, other='Quaternion') -> Quaternion:
		return self.__value - other.__value

	def __mul__(self, other='Quaternion') -> Quaternion:
		vecPartA =self.__value.xyz()
		scalarA = self.__value.w()
		vecPartB = other.__value.xyz()
		scalarB = other.__value.w()
		return Quaternion.fromVec3(vecPartA.floatMul(scalarB) + vecPartB.floatMul(scalarA) + vecPartA.cross(vecPartB),
							scalarA * scalarB - vecPartA.dot(vecPartB))

	def __iadd__(self, other='Quaternion') -> Quaternion:
		self.__value += other.__value
		return self.__value

	def __isub__(self, other='Quaternion') -> Quaternion:
		self.__value -= other.__value
		return self.__value

	def __imul__(self, other='Quaternion') -> Quaternion:
		self.__value = self * other
		return self.__value

	def matrix(self) -> Matrix4x4:
		self = self.normalize()
		vecPart = self.__value.xyz()
		scalar = self.__value.w()
		vecA = Vector4D.fromVector3(vecPart, vecPart.x())
		vecB = Vector4D.fromVector3(vecPart, vecPart.y())
		vecC = Vector4D(scalar, scalar, scalar, vecPart.z())
		
		vecB = vecA * vecB
		vecC = vecA * vecC
		
		vYZ = (vecPart.y() *  vecPart.z())

		return Matrix4x4([[0.5 - (vecB.y() + vecB.z()), (vecB.w() - vecC.z()), (vecC.w() + vecC.y()), 0],
					[(vecB.w() + vecC.z()), 0.5 - (vecB.x() + vecB.z()), (vYZ - vecC.x()), 0],
					[(vecC.w() - vecC.y()), (vYZ + vecC.x()), 0.5 - (vecB.x() + vecB.y()), 0],
					[0, 0, 0, 1]])



