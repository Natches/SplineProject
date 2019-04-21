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
		height = pen.getscreen().canvheight * 0.5
		width = pen.getscreen().canvwidth * 0.5
		transformedPoints = copy.deepcopy(self.__vertex)
		for idx in range(0, self.__vertex.__len__()):
			transformedPoints[idx] = cam.From3DSpaceToScreen((mvp * transformedPoints[idx]).xyz, width, height)

		lastPoint = transformedPoints[self.__indices[0]]
		pen.setpos(lastPoint.x, lastPoint.y)
		for idx in self.__indices:
			if((math.fabs(transformedPoints[idx].x) < width and math.fabs(transformedPoints[idx].y) < height) or 
				(math.fabs(lastPoint.x) < width  and math.fabs(lastPoint.y) < height)):
				position = Utils.FindIntersection(transformedPoints[idx], lastPoint, width, height)
				pen.setpos(position[0].x, position[0].y)
				pen.pd()
				pen.setpos(position[1].x, position[1].y)
				pen.pu()
			lastPoint = transformedPoints[idx]
		pen.pu()

