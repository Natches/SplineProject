import numpy as np
from math3d import Vector4D, Vector3D, Matrix4x4, Matrix4x3
from turtle import RawTurtle, Canvas, Turtle
from Mesh import Mesh
from Camera import Camera
from Matrix4x4 import Inverse

class DragableTurtle(RawTurtle):
	__drag_function
	
	def __init__(self, dragfunction=None, canvas=None, shape=_CFG ['shape' ], undobuffersize=_CFG ['undobuffersize' ], visible=_CFG ['visible' ]):
		self.__drag_function = dragfunction
		return super().__init__(canvas=canvas, shape=shape, undobuffersize=undobuffersize, visible=visible)

class Curve(Mesh):
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

	@property
	def control_points(self):
		return self.__control_points

	@control_points.setter
	def control_points(self, points=[]):
		self.__dirty = True
		self.__control_points = points

	@property
	def precision(self):
		return self.__precision

	@precision.setter
	def precision(self, value):
		self.__precision = 1 / value

	def draw(self, pen=Turtle, camera=Camera):
		super(Curve, self).draw(pen, camera)


class HermitienneCurve(Curve):
	__dirty = True
	__turtle_dirty = True
	__tan_line = [Vector3D(), Vector3D()]
	__point_controller = [RawTurtle]

	def __init__(self, canvas=Canvas, camera=Camera):
		self._Curve__control_points = [Vector3D(), Vector3D()]
		self.__point_controller = [RawTurtle(canvas, shape='circle'), RawTurtle(canvas, shape='circle')]
		self.__point_controller[0].pu()
		self.__point_controller[0].speed(0)
		lmd = lambda x, y: self.on_drag(self.__point_controller[0], camera, x, y)
		self.__point_controller[0].ondrag(lmd)
		self.__point_controller[1].pu()
		self.__point_controller[1].speed(0)
		lmd = lambda x, y: self.on_drag(self.__point_controller[1], camera, x, y)
		self.__point_controller[1].ondrag(lmd)
		self._Curve__constant_matrix = Matrix4x4([[2, -2, 1, 1], [-3, 3, -2, -1], [0, 0, 1, 0], [1, 0, 0, 0]])
		return super().__init__()

	def on_drag(self, turtle, camera, x, y):
		i = -1
		if(turtle == self.__point_controller[0]):
			i = 0
		else:
			i = 1
		x = (2.0 * x) / turtle.screen.canvwidth - 1.0;
		y = 1.0 - (2.0 * y) / turtle.screen.canvheight;
		clip = Vector4D([x, y, -1, 1])
		eye = Inverse(camera.view_perspective) * clip
		self._Curve__control_points[i] = Vector3D([eye.x * eye.z, eye.y * eye.z, 0])
		self.__dirty = True
		self.__turtle_dirty = True
		

	def __build_geometric_matrix(self):
		if(self.__dirty):
			self._Curve__geometric_matrix = self._Curve__constant_matrix * Matrix4x3([self._Curve__control_points[0].value, self._Curve__control_points[1].value,
				 self.__tan_line[0].value,  self.__tan_line[1].value])
			self.__dirty = False
		return self._Curve__geometric_matrix

	def compute(self, value) -> Vector4D:
		assert(value <= 1)
		self.__build_geometric_matrix()
		value_vec = Vector4D([value**3, value**2, value, 1])
		return Vector4D.fromVector3(value_vec * self._Curve__geometric_matrix, 1)

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



	def init_mesh(self):
		self._Mesh__vertex.clear()
		self._Mesh__indices.clear()
		i = 0
		t = 0
		while t < 1:
			self._Mesh__vertex.append(self.compute(t))
			self._Mesh__indices.append(i)
			i += 1
			t += self._Curve__precision

	def draw(self, pen=Turtle, camera=Camera):
		if(self.__turtle_dirty):
			self.init_mesh()
			mvp = camera.view_perspective * self.model_matrix
			height = pen.getscreen().canvheight - 1
			width = pen.getscreen().canvwidth - 1
			position = self._Mesh__transform_point(self._Mesh__vertex[0], mvp, width, height)
			self.__point_controller[0].setpos(position.x - 8, position.y - 8)
			position = self._Mesh__transform_point(self._Mesh__vertex[self._Mesh__vertex.__len__() - 1], mvp, width, height)
			self.__point_controller[1].setpos(position.x - 8, position.y - 8)
			self.__turtle_dirty = False
		self._Mesh__dirty = True
		super(HermitienneCurve, self).draw(pen, camera)





class BezierCurve(Curve):
	def __init__(self, *args, **kwargs):
		__control_point = [Vector3D(), Vector3D(), Vector3D(), Vector3D()]
		__constant_matrix = Matrix4x4([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])
		return super().__init__(*args, **kwargs)

