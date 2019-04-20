from math3d import Quaternion, Vector3D, Vector4D, Matrix4x4
from turtle import Turtle
from Camera import Camera
import Camera as cam
import math

class Mesh(object):
	__dirty = True
	__rotation = Quaternion(Vector4D([0, 0, 0, 1]))
	__position = Vector3D([0, 0, 0])
	__scale = Vector3D([1, 1, 1])

	__modelMx = Matrix4x4()
	__vertex = [Vector4D]
	__indices = [int]

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
			return self.__BuildModelMatrix()
		else:
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
		height = pen.getscreen().canvheight
		width = pen.getscreen().canvwidth
		pen.pu()
		point = cam.From3DSpaceToScreen((mvp * self.__vertex[self.__indices[0]]).xyz, width, height)
		pen.setpos(point.x, point.y)
		pen.pd()
		for idx in self.__indices:
			position = (mvp * self.__vertex[idx]).xyz
			if((position - camera.eye).normalize().dot(camera.at) > 0):
				point = cam.From3DSpaceToScreen(position, width, height)
				pen.setpos(point.x, point.y)
		pen.pu()
