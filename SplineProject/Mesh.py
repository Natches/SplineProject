from math3d import Quaternion, Vector3D, Vector4D, Matrix4x4, Vector2D
from turtle import Turtle
from Camera import Camera
import Camera as cam
import math
import copy
import Utils
import numpy as np

class Mesh(object):
	__dirty = True
	__rotation = Quaternion(Vector4D([0, 0, 0, 1]))
	__position = Vector3D([0, 0, 0])
	__scale = Vector3D([1, 1, 1])

	__modelMx = Matrix4x4()
	__vertex = []
	__indices = []

	__transformed_points = []


	def __init__(self, vertex=[], indices=[]):
		self.__vertex = vertex
		self.__transformed_points = [Vector2D()] * vertex.__len__()
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
		dirty = self.__dirty
		mvp = camera.view_perspective * self.model_matrix
		height = pen.getscreen().canvheight
		width = pen.getscreen().canvwidth
		if(self.__transformed_points.__len__() != self.__vertex.__len__()):
			self.__transformed_points = [Vector2D()] * self.__vertex.__len__()
		
		if(dirty):
			array = np.transpose(np.dot(mvp.value, np.transpose(np.array([vertex.value for vertex in self.__vertex]))))
			self.__transformed_points[:] = [self.__transform_point(Vector4D(vertex), width, height) for vertex in array]
		
		lastPoint = copy.deepcopy(self.__transformed_points[self.__indices[0]])
		pen.setpos(lastPoint.x, lastPoint.y)
		lastPointOutside = lastPoint.x > width or lastPoint.y > height or lastPoint.y < 0.0 or lastPoint.x < 0.0
		transformedPointOutside = False
		for idx in self.__indices:
			position = copy.deepcopy(self.__transformed_points[idx])
			transformedPointOutside = position.x > width or position.y > height or position.y < 0.0 or position.x < 0.0
			if(not lastPointOutside or not transformedPointOutside):
				if(lastPointOutside or transformedPointOutside):
					position = Utils.FindIntersection(lastPoint, position, width, height)
					if(position.__len__() > 0):
						position = position[1]
				pen.pd()
				pen.setpos(position.x, position.y)
				pen.pu()
			lastPoint = position
			pen.setpos(lastPoint.x, lastPoint.y)
			lastPointOutside = transformedPointOutside
		pen.pu()

	def __transform_point(self, vertex=Vector4D, width=int, height=int) -> Vector2D:
		vertex = vertex.xyz.__div__(vertex.w)
		return Utils.From3DSpaceToScreen(vertex, width, height)

