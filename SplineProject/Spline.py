import numpy as np
from math3d import Vector4D, Vector3D, Matrix4x4, Matrix4x3


class Curve(object):
	__control_points = [Vector3D]
	__constant_matrix = Matrix4x4()
	__geometric_matrix = Matrix4x3()
	__precision = 0.01

	def __init__(self, *args, **kwargs):
		return super().__init__(*args, **kwargs)

	def __build_geometric_matrix(self):
		assert(False)

	def compute(self, value):
		assert(False)

class HermitienneCurve(Curve):
	__dirty = True
	__tan_line = [Vector3D(), Vector3D()]

	def __init__(self, *args, **kwargs):
		self._Curve__control_points = [Vector3D(), Vector3D()]
		self._Curve__constant_matrix = Matrix4x4([[2, -2, 1, 1], [-3, 3, -2, -1], [0, 0, 1, 0], [1, 0, 0, 0]])
		return super().__init__(*args, **kwargs)

	def __build_geometric_matrix(self):
		if(self.__dirty):
			self._Curve__geometric_matrix = Matrix4x3([self._Curve__control_points[0].value, self._Curve__control_points[1].value,
				 self.__tan_line[0].value,  self.__tan_line[1].value])
		return self._Curve__geometric_matrix

	def compute(self, value) -> Vector4D:
		assert(value <= 1)
		self.__build_geometric_matrix()
		value_vec = Vector4D([value**3, value**2, value, 1])
		return Vector4D.fromVector3(value_vec * self._Curve__constant_matrix * self._Curve__geometric_matrix, 1)

	@property
	def p1(self) -> Vector3D:
		return self._Curve__control_points[0]

	@property
	def p2(self) -> Vector3D:
		return self._Curve__control_points[1]

	@property
	def r1(self) -> Vector3D:
		return self.__tan_line[0]

	@property
	def r2(self) -> Vector3D:
		return self.__tan_line[1]

	@p1.setter
	def p1(self, value=Vector3D) -> Vector3D:
		self.__dirty = True
		self._Curve__control_points[0] = value

	@p2.setter
	def p2(self, value=Vector3D) -> Vector3D:
		self.__dirty = True
		self._Curve__control_points[1] = value

	@r1.setter
	def r1(self, value=Vector3D) -> Vector3D:
		self.__dirty = True
		self.__tan_line[0] = value

	@r2.setter
	def r2(self, value=Vector3D) -> Vector3D:
		self.__dirty = True
		self.__tan_line[1] = value




class BezierCurve(Curve):
	def __init__(self, *args, **kwargs):
		__control_point = [Vector3D(), Vector3D(), Vector3D(), Vector3D()]
		__constant_matrix = Matrix4x4([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
		return super().__init__(*args, **kwargs)

