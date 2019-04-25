import numpy as np
import sympy as sp
from math3d import Vector3D, Matrix4x4
from abc import ABC, abstractmethod


class Curve(ABC):
	__control_Points = [Vector3D]
	__constant_Matrix = Matrix4x4()
	__precision = 0.01

	def __init__(self, *args, **kwargs):
		return super().__init__(*args, **kwargs)

	@abstractmethod
	def build_geometric_matrix(self):
		pass

class HermitienneCurve(Curve):
	__t = sp.Symbol('t') 
	__x_equation = ""
	__y_equation = ""
	__z_equation = ""
	__x_derivative_equation 
	__y_derivative_equation
	__z_derivative_equation

	def __init__(self, *args, **kwargs):
		__control_point = [Vector3D(), Vector3D()]
		__constant_Matrix = Matrix4x4([[2, -2, 1, 1], [-3, 3, -2, -1], [0, 0, 1, 0], [1, 0, 0, 0]])
		return super().__init__(*args, **kwargs)

	def build_geometric_matrix(self):
		if(isinstance(x, str)):
			self.__computeFunctionFromString()

	@property
	def c1(self) -> Vector3D:
		return self._Curve__control_Points[0]

	@property
	def c2(self) -> Vector3D:
		return self._Curve__control_Points[2]

	@control_point1.setter
	def c1(self, value=Vector3D) -> Vector3D:
		self._Curve__control_Points[0] = value

	@control_point2.setter
	def c2(self, value=Vector3D) -> Vector3D:
		self._Curve__control_Points[2] = value

	@property
	def t(self):
		return __t

	def __computeFunctionFromString(self):
		x = eval(self.__x_equation)
		xprime = x.diff(self.t)
		self.__x_equation = sp.lambdify(t, x, 'numpy')
		self.__x_derivative_equation = sp.lambdify(t, xprime, 'numpy')
		y = eval(self.__y_equation)
		yprime = y.diff(self.t)
		self.__y_equation = sp.lambdify(t, y, 'numpy')
		self.__y_derivative_equation = sp.lambdify(t, yprime, 'numpy')
		z = eval(self.__z_equation)
		zprime = z.diff(self.t)
		self.__z_equation = sp.lambdify(t, z, 'numpy')
		self.__z_derivative_equation = sp.lambdify(t, zprime, 'numpy')
		


class BezierCurve(Curve):
	def __init__(self, *args, **kwargs):
		__control_point = [Vector3D(), Vector3D(), Vector3D(), Vector3D()]
		__constant_Matrix = Matrix4x4([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
		return super().__init__(*args, **kwargs)

