from math3d import Quaternion, Vector3D, Vector4D, Matrix4x4, Vector2D
from turtle import Turtle
from Camera import Camera
import Camera as cam
import math
import copy
import Utils

class Mesh(object):
	__dirty = True
	__rotation = Quaternion(Vector4D([0, 0, 0, 1]))
	__position = Vector3D([0, 0, 0])
	__scale = Vector3D([1, 1, 1])

	__modelMx = Matrix4x4()
	__vertex = [Vector4D]
	__indices = [int]

	__futures = []
	def __init__(self, vertex=[Vector4D], indices=[int]):
		self.__vertex = vertex
		self.__indices = indices
		

	def __getitem__(self, key):
		return self.__vertex[key]

	@property
	def rotation(self) -> Quaternion:
		return self.__rotation

	@property
	def position(self) -> Vector3D:
		return self.__position

	@property
	def scale(self) -> Vector3D:
		return self.__scale

	@rotation.setter
	def rotation(self, rotation=Quaternion):
		self.__rotation = rotation
		self.__dirty = True

	@position.setter
	def position(self, position=Vector3D):
		self.__position = position
		self.__dirty = True

	@scale.setter
	def scale(self, scale=Vector3D):
		self.__scale = scale
		self.__dirty = True

	@property
	def model_matrix(self):
		if(self.__dirty):
			self.__BuildModelMatrix()
			self.__dirty = False
		return self.__modelMx

	def __BuildModelMatrix(self):
		scale = Matrix4x4([[self.__scale.x, 0, 0, 0],[0, self.__scale.y, 0, 0],[0, 0, self.__scale.z, 0],[0,0,0,1]])
		rot = self.__rotation.matrix()
		translate = Matrix4x4([[1, 0, 0, self.__position.x],
								[0, 1, 0, self.__position.y],
								[0, 0, 1, self.__position.z],
								[0, 0, 0, 1]])
		self.__modelMx = translate * rot * scale
		return self.__modelMx

	def draw(self, pen=Turtle, camera=Camera):
		mvp = camera.view_perspective * self.model_matrix
		height = pen.getscreen().canvheight - 1
		width = pen.getscreen().canvwidth - 1
		transformedPoints = copy.deepcopy(self.__vertex)
		transformedPoints[:] = [self.__transform_point(vertex, mvp, width, height) for vertex in transformedPoints]

		lastPoint = transformedPoints[self.__indices[0]]
		pen.setpos(lastPoint.x, lastPoint.y)
		for idx in self.__indices:
			position =Utils.FindIntersection(lastPoint, transformedPoints[idx], width, height)
			if(position.__len__() > 0):
				pen.pd()
				pen.setpos(position[1].x, position[1].y)
				pen.pu()
				lastPoint = position[1]
			else:
				lastPoint = transformedPoints[idx]
			pen.setpos(lastPoint.x, lastPoint.y)
		pen.pu()

	def __transform_point(self, vertex=Vector4D, mvp=Matrix4x4, width=int, height=int) -> Vector2D:
		vertex = (mvp * vertex)
		vertex = vertex.xyz.__div__(vertex.w)
		vertex = cam.From3DSpaceToScreen(vertex, width, height)
		return vertex

